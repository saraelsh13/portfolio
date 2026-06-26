---
layout: page
title: "Systems and AI"
---

# AI content systems with a quality bar

AI is useful in content operations when it is connected to trustworthy source material, explicit quality criteria, and people who can intervene when evidence is weak or risk is high.

I design the system around the content, not around the model.

![AI content workflow diagram](assets/ai-content-workflow.png)

```text
Product changes + support signals + user questions
                        ↓
      Structured source content and source-of-truth rules
                        ↓
      Retrieval, prompting, drafting, and recommendation
                        ↓
Quality checks: source support, freshness, risk, completeness
                        ↓
  High confidence: approved use by the intended audience
 Low confidence: human review, escalation, or content-gap creation
                        ↓
          Evaluation data and prioritised system improvements
```

## What makes AI-assisted content dependable

### Governed source content

AI should retrieve from content that has an owner, defined scope, review date, source-of-truth status, and explicit approval for its intended use.

### Clear human oversight

A person must be able to see the source, understand the system’s confidence, correct an answer, and escalate uncertainty. High-risk guidance, conflicting sources, and unreviewed product changes should not be treated as routine automation.

### Evaluation that reflects real use

I evaluate responses for:

- Groundedness and source traceability
- Product accuracy and content freshness
- Completeness, clarity, and accessible language
- Policy and risk compliance
- Appropriate uncertainty and escalation behaviour
- Fit for the specific audience and task

### Feedback loops that create better knowledge

Support tickets, search failures, user feedback, product releases, and AI-quality findings should feed a single prioritisation process. This turns recurring failures into maintained content, stronger patterns, and clearer product guidance.

## Practical applications

- AI-assisted knowledge retrieval for Support Specialists
- Structured prompts for product workflows and customer communication
- Content quality checks before publishing or enabling AI retrieval
- Source-aware responses with citations or linked evidence
- Content-gap detection from ticket clusters and failed searches
- Human review queues for content that is stale, risky, or ambiguous

## Related work

- [AI-assisted support knowledge system](support-knowledge-system.md)
- [Content systems operating model](content-systems.md)
- [AI governance documentation for enterprise platforms](ai-governance-docs.md)

---

[Home](index.md) · [Work](work.md) · [Content Systems](content-systems.md) · [Writing](writing.md)
