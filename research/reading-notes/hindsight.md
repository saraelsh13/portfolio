# Learning from unsuccessful proof attempts

**Source:** Aygün et al. (2022), [Proving Theorems using Incremental Learning and Hindsight Experience Replay](https://proceedings.mlr.press/v162/aygun22a.html), ICML 2022. Lei M. Zhang is a coauthor.

**Status:** Draft based on the published abstract. Full-paper and personal review pending.

## What the paper studies

The work adapts hindsight experience replay to use intermediate data from unsuccessful proof attempts. A neural clause-scoring function replaces the E prover's handcrafted scoring heuristics in an incremental learning setting. The authors report competitive benchmark performance and shorter proofs than E in most cases.

## Interpretation to investigate

An attempt that fails at its original goal can still produce useful intermediate experience. This raises a selection question: which intermediate outcomes support later learning? It does not imply that every failed attempt is useful.

## Connection to the portfolio

The current experiment retains observed labels and eliminates candidate explanations, but it does not learn a search policy or implement hindsight replay. A future experiment could compare retaining successes alone with retaining selected intermediate outcomes, evaluated on new tasks.

## Questions for full-paper review

- How are intermediate outcomes selected and relabelled?
- Which ablations separate hindsight replay from incremental training?
- What costs are included in comparison with the baseline prover?
- Does the method improve transfer, search efficiency, or both under the reported setup?
