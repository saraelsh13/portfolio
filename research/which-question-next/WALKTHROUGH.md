# A beginner's walkthrough

Start with `experiment.py`. Run the tests before changing it. This is a guide for learning the implementation, not a record of completed personal study.

| Concept | Everyday meaning | Where to look |
| --- | --- | --- |
| Object | A list of four yes/no attributes | `POINTS` |
| Hypothesis | A possible rule for assigning labels | `make_hypotheses` |
| Version space | Rules that still agree with every observed answer | `candidates` in `run_trial` |
| Query | An object whose label the agent requests | `choose_query` |
| Oracle | The hidden rule returning a requested label | `target[query]` |
| Prediction | Majority label among remaining explanations | `evaluate` |
| Held-out set | Objects saved for evaluation, never queried | `heldout` |
| Seed | A number that makes random choices repeatable | `random.Random` |
| Model inconsistency | None of the available explanations fits the observations | Empty `candidates` |

## Follow one run

1. `run_experiment` chooses a hidden rule and separates query objects from test objects.
2. `run_trial` starts with every candidate rule.
3. `choose_query` receives only available indices, candidate rules, and a random generator. It cannot see hidden answers.
4. The selected object's label is revealed. Inconsistent rules are removed.
5. `evaluate` checks predictions on held-out objects. These scores are recorded but not sent to query selection.
6. This repeats up to the requested budget.

## First exercise

Run `python experiment.py --seeds 10 --output practice-results` to keep the published results intact. Open the CSV and compare budgets 0 and 6. Explain why results at those budgets share the same seed.

## Small changes to try

- Increase `--seeds` to 200 with a separate output folder. Does the qualitative contrast persist?
- Change the tie-breaking prediction from zero to one. Which conditions are affected?
- Add the three-attribute XOR rules to the candidate set. The omission assertion should fail. Before removing it, redesign the condition label and controls so the experiment still means what the README says.
- Record one query trajectory, including which rules remain after each observation. Can you explain one case where unanimous predictions are wrong?

## Questions to answer before presenting the project

- Why does disagreement sampling avoid needing the true label before choosing a query?
- What assumption makes a balanced vote informative?
- Why can a model be unanimous and wrong?
- Why is zero surviving hypotheses different from one surviving hypothesis?
- Why is the query budget not a computation budget?
- What would have to change to demonstrate learning across tasks?

Use AI to explain unfamiliar code and propose changes. Check the explanation against actual execution and write your own account in the research log. Passing tests does not establish that the scientific design is adequate.
