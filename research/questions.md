# Questions I am exploring

**Status:** Exploratory research agenda, not a finalized PhD proposal or claim of novelty.

My starting interest is how computational systems shape what can be represented, interpreted, and trusted. For agents, this raises a practical question: how do the available explanations and the feedback mechanism shape the evidence an agent seeks?

| Question | Possible experiment | What would count as evidence? |
| --- | --- | --- |
| Which uncertainty is worth investigating? | Compare query-selection strategies with equal label budgets | Accuracy and query efficiency on held-out objects; report selection overhead separately |
| When should an agent question its explanation space? | Hold targets constant while selectively removing candidate rules | Detection of inadequacy and recovery, compared with a fixed explanation set |
| What can an unsuccessful attempt teach? | Compare retention of successes, failures, and informative intermediate states | Transfer to held-out tasks with matched experience budgets |
| Does repeated exploration improve the investigator? | Learn a selection policy across tasks, then freeze it for evaluation | Improvement on unseen task families, compared with a non-learning baseline |
| Who defines useful progress? | Compare objective correctness with learned or proxy feedback | Disagreement between feedback scores and independently measured outcomes |

Only an initial version of the first question, with a limited omission condition, is implemented. The other rows describe possible next experiments. Scientific discovery motivates these questions, but the current Boolean-rule exercise is not evidence of scientific discovery capability.
