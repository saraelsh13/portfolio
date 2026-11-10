"""Checks of scientific invariants rather than expected headline results."""
import unittest
import random
from experiment import (HYPOTHESES, POINTS, choose_query, evaluate,
                        run_trial, run_experiment)


class ExperimentTests(unittest.TestCase):
    def test_hypotheses_are_unique_and_binary(self):
        self.assertEqual(len(HYPOTHESES), len(set(HYPOTHESES)))
        self.assertTrue(all(len(h) == 16 and set(h) <= {0, 1} for h in HYPOTHESES))

    def test_query_never_leaves_pool(self):
        for strategy in ("fixed", "random", "disagreement"):
            self.assertIn(choose_query(strategy, {2, 7}, HYPOTHESES,
                                       random.Random(4)), {2, 7})

    def test_balanced_split_is_selected(self):
        # Query 0 splits 2:2; query 1 splits 3:1.
        candidates = [(0, 0), (0, 0), (1, 0), (1, 1)]
        self.assertEqual(choose_query("disagreement", {0, 1}, candidates,
                                      random.Random(0)), 0)

    def test_true_in_class_rule_cannot_be_eliminated(self):
        for target in HYPOTHESES:
            records = run_trial(target, list(range(12)), list(range(12, 16)),
                                "disagreement", 0)
            self.assertTrue(all(r["candidates"] >= 1 for r in records))

    def test_empty_model_is_not_counted_as_confident(self):
        result = evaluate([], (1,) * 16, [12, 13, 14, 15], [0])
        self.assertEqual(result["inconsistent"], 1)
        self.assertEqual(result["false_certainty_rate"], 0)
        self.assertEqual(result["accuracy"], 0)

    def test_determinism_and_equal_initial_accuracy(self):
        raw, summary = run_experiment(4)
        self.assertEqual((raw, summary), run_experiment(4))
        for seed in range(4):
            for condition in ("in_class", "omitted_rule"):
                starts = [r["accuracy"] for r in raw if r["seed"] == seed
                          and r["condition"] == condition and r["budget"] == 0]
                self.assertEqual(len(set(starts)), 1)

    def test_full_query_budget_and_invalid_input(self):
        raw, _ = run_experiment(2, 12)
        self.assertTrue(all(r["budget"] <= 12 for r in raw))
        with self.assertRaises(ValueError):
            run_experiment(2, 13)


if __name__ == "__main__":
    unittest.main()
