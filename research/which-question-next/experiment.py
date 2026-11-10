"""A small, inspectable active-learning experiment. Python standard library only.

Run: python experiment.py --seeds 100 --output results
An agent may query labels in a pool, never in the held-out evaluation set.
"""

import argparse
import csv
import itertools
import json
import random
import statistics
from pathlib import Path

POINTS = list(itertools.product((0, 1), repeat=4))
STRATEGIES = ("fixed", "random", "disagreement")


def make_hypotheses():
    """Return truth tables, so every candidate can be inspected directly.

    Eight literals and AND/OR/XOR of each pair of positive attributes.
    Deduplication prevents equivalent rules receiving extra prior weight.
    """
    tables = []
    for i in range(4):
        for invert in (False, True):
            tables.append(tuple(int(bool(x[i]) != invert) for x in POINTS))
    for i, j in itertools.combinations(range(4), 2):
        for op in (lambda a, b: a & b, lambda a, b: a | b, lambda a, b: a ^ b):
            tables.append(tuple(op(x[i], x[j]) for x in POINTS))
    return list(dict.fromkeys(tables))


HYPOTHESES = make_hypotheses()


def choose_query(strategy, available, candidates, rng):
    """Choose an index WITHOUT access to the true rule or evaluation labels.

    With a uniform distribution over consistent deterministic hypotheses,
    the most balanced binary vote also maximizes expected information gain.
    Empty candidate sets fall back to a random query, and are recorded.
    """
    if strategy == "fixed":
        return min(available)
    if strategy == "random" or not candidates:
        return rng.choice(sorted(available))
    if strategy != "disagreement":
        raise ValueError("Unknown strategy")
    scores = {i: abs(sum(h[i] for h in candidates) / len(candidates) - 0.5)
              for i in sorted(available)}
    best = min(scores.values())
    return rng.choice([i for i, score in scores.items() if score == best])


def evaluate(candidates, target, heldout, observed):
    """Confidence is vote agreement CONDITIONAL on the candidate rule set.

    An empty set is model inconsistency, not certainty. Prediction then
    falls back to the majority observed label (ties predict zero).
    """
    correct = 0
    false_certain = 0
    fallback = int(bool(observed) and sum(observed) > len(observed) / 2)
    for i in heldout:
        if candidates:
            p = sum(h[i] for h in candidates) / len(candidates)
            prediction = int(p > 0.5)
            false_certain += int(p in (0.0, 1.0) and prediction != target[i])
        else:
            prediction = fallback
        correct += int(prediction == target[i])
    return {"accuracy": correct / len(heldout),
            "false_certainty_rate": false_certain / len(heldout),
            "inconsistent": int(not candidates),
            "candidates": len(candidates)}


def run_trial(target, pool, heldout, strategy, seed, max_budget=6):
    candidates = HYPOTHESES.copy()
    available = set(pool)
    observed = []
    rng = random.Random(seed)
    records = []
    for budget in range(max_budget + 1):
        records.append({"budget": budget,
                        **evaluate(candidates, target, heldout, observed)})
        if budget < max_budget:
            query = choose_query(strategy, available, candidates, rng)
            label = target[query]  # The oracle is consulted only AFTER selection.
            observed.append(label)
            candidates = [h for h in candidates if h[query] == label]
            available.remove(query)
    return records


def run_experiment(seeds=100, max_budget=6):
    if seeds < 2:
        raise ValueError("Use at least two seeds")
    if not 0 <= max_budget <= 12:
        raise ValueError("Budget must be between 0 and the 12-point query pool size")
    raw = []
    for seed in range(seeds):
        rng = random.Random(seed)
        indices = list(range(len(POINTS)))
        rng.shuffle(indices)
        pool, heldout = indices[:12], indices[12:]
        # Paired strategies see identical target rules and held-out points.
        in_class = rng.choice(HYPOTHESES)
        triple = rng.sample(range(4), 3)
        omitted = tuple(x[triple[0]] ^ x[triple[1]] ^ x[triple[2]] for x in POINTS)
        assert omitted not in HYPOTHESES
        for condition, target in (("in_class", in_class), ("omitted_rule", omitted)):
            for strategy in STRATEGIES:
                for record in run_trial(target, pool, heldout, strategy, seed + 10000,
                                        max_budget):
                    raw.append({"seed": seed, "condition": condition,
                                "strategy": strategy, **record})
    summary = []
    for condition in ("in_class", "omitted_rule"):
        for strategy in STRATEGIES:
            for budget in range(max_budget + 1):
                group = [r for r in raw if r["condition"] == condition
                         and r["strategy"] == strategy and r["budget"] == budget]
                summary.append({"condition": condition, "strategy": strategy,
                                "budget": budget, "trials": seeds,
                                "accuracy": statistics.mean(r["accuracy"] for r in group),
                                "accuracy_sd": statistics.stdev(r["accuracy"] for r in group),
                                "false_certainty_rate": statistics.mean(
                                    r["false_certainty_rate"] for r in group),
                                "inconsistency_rate": statistics.mean(
                                    r["inconsistent"] for r in group)})
    return raw, summary


def write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", type=int, default=100)
    parser.add_argument("--max-budget", type=int, default=6)
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "results")
    args = parser.parse_args()
    raw, summary = run_experiment(args.seeds, args.max_budget)
    args.output.mkdir(parents=True, exist_ok=True)
    write_csv(args.output / "raw_trials.csv", raw)
    write_csv(args.output / "summary.csv", summary)
    config = {"seed_ids": [0, args.seeds - 1], "trials_per_condition": args.seeds,
              "max_budget": args.max_budget, "attributes": 4,
              "query_pool_size": 12, "heldout_size": 4,
              "hypothesis_count": len(HYPOTHESES),
              "strategies": STRATEGIES, "python_requirement": "3.10+"}
    (args.output / "config.json").write_text(json.dumps(config, indent=2) + "\n")
    print(json.dumps(config, indent=2))
    print("Wrote raw_trials.csv, summary.csv, and config.json")


if __name__ == "__main__":
    main()
