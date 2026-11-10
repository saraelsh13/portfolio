# AdA: questions about rapid adaptation

**Source:** Adaptive Agent Team et al. (2023), [Human-Timescale Adaptation in an Open-Ended Task Space](https://arxiv.org/abs/2301.07608), ICML 2023.

**Status:** Draft based on the abstract. Full-paper and personal review pending. This is not a replication or a record of completed personal reading.

## What the paper studies

The authors investigate rapid adaptation to unfamiliar embodied 3D tasks. AdA combines meta-reinforcement learning, attention-based memory, and an automated curriculum prioritizing tasks near its capability frontier. The abstract reports hypothesis-driven exploration and rapid adaptation on held-out dynamics, with scaling studied across model size, memory, and task diversity.

## Interpretation to investigate

This suggests a distinction between learning general adaptation strategies during training and using them in a new task. A useful next reading question is how the evaluation separates new-task adaptation from familiarity with training variations. The abstract alone is insufficient to assess that distinction fully.

## Connection to the portfolio

The small query-selection experiment isolates one question about choosing evidence. It does not implement meta-RL, curriculum learning, or learned exploration. Its hand-enumerated explanations are much more restrictive than AdA's learned representation.

## Questions for full-paper review

- How is the curriculum frontier operationalized?
- What controls establish the role of memory versus training diversity?
- What evidence supports the description of exploration as hypothesis-driven?
- How is interaction cost compared across agents and humans?

Possible extension: compare query selection under complete and incomplete hypothesis spaces while keeping target tasks fixed.
