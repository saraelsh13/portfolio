# Research and learning log

## Initial implementation

**Status:** Initial implementation record. Personal walkthrough, review, and further experiments are pending.

- Implemented a standard-library Python environment with 26 candidate rules and separate query/evaluation objects.
- Compared fixed, random, and disagreement-based query selection in paired synthetic trials.
- Added a condition where the correct three-attribute XOR rule is absent from the hypothesis set.
- Executed 100 trials per condition and saved raw records, summary statistics, and configuration.
- Checked unique hypotheses, legal query selection, balanced splitting, preservation of in-class targets, empty-set handling, determinism, and valid budget boundaries.
- Observed both an in-class advantage at six queries and poor held-out accuracy in the omitted-rule condition.

## Unresolved design decisions

1. Omitted rules are also more complex. A matched-target control is needed before attributing the difference specifically to omission.
2. Empty-model fallback affects the outcome and should be compared with abstention and model expansion.
3. The fixed strategy's lexicographic ordering is arbitrary and can be sensitive to feature encoding.
4. The vote distribution assumes a uniform prior over a small hand-designed set. It should not be read as unconditional certainty.
5. The analysis is descriptive. More seeds do not create more diverse task families.

## Personal review, pending

- Explain the query-selection function in your own words.
- Trace an individual trial and identify exactly when a candidate is eliminated.
- Reproduce the results locally and record the Python version.
- Make one deliberate change, predict its effect, and compare prediction with observation.
- Revise the draft reading notes after checking the full papers.

Future entries should distinguish a prediction made before running code from an explanation written after seeing the result.
