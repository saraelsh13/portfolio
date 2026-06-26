---
layout: page
title: "AI Support Knowledge System"
---

# AI-assisted support knowledge system

**Independent portfolio prototype · 2026**

## The challenge

A technical SaaS Support team has knowledge spread across product documentation, internal pages, release notes, tickets, issue trackers, and informal conversations. Specialists waste time deciding what is current. An AI assistant can retrieve answers quickly, but it can also repeat stale, unsupported, or policy-sensitive guidance.

The design question was not, "How do we add a chatbot?" It was:

> How might a Support organisation make knowledge accurate, traceable, easy to find, and safe for both Specialists and AI systems to use?

## North Star

**Verified first-contact resolution**. The percentage of support conversations resolved in the first interaction using a current, traceable, policy-compliant knowledge source.

## System design

```text
Support ticket or product-release signal
                  ↓
Intent and product-area classification
                  ↓
Retrieval from approved, structured knowledge
                  ↓
AI answer draft or article recommendation
                  ↓
Quality checks: source, freshness, risk, completeness
                  ↓
High confidence: Specialist uses verified guidance
Low confidence: Human review or SME escalation
                  ↓
Content gap, correction, and evaluation findings feed the backlog
```

## Information architecture

The internal knowledge base is organised around the work Support must complete, not the company org chart:

- **Product areas**. Accounts and permissions, billing, collaboration, integrations
- **Support workflows**. Troubleshooting, known issues, escalations, customer communication
- **Release knowledge**. Product changes, deprecations, incident updates
- **Governance**. Standards, templates, article owners, review queue, decision history

Every article is structured with metadata that supports ownership, retrieval, evaluation, and review:

```yaml
title:
content_type:
product_area:
audience:
owner:
subject_matter_expert:
source_of_truth:
last_reviewed:
next_review_date:
risk_level:
related_release:
related_ticket_intents:
approved_for_ai_retrieval:
```

## Human oversight by design

AI does not publish content or provide unverified guidance without constraints. The system requires review when:

| Signal | System response |
|---|---|
| No approved source is found | Create a content gap and route to a Support lead or SME |
| The source is outside its review window | Mark guidance as potentially stale and require verification |
| Sources conflict | Route to the accountable source-of-truth owner |
| The topic involves billing, security, access, or policy | Require Specialist review before use |
| The response lacks a source reference | Do not mark it as verified guidance |
| Ticket volume reveals an uncovered intent | Add the gap to content-prioritisation review |

## Quality evaluation framework

Each sampled AI response is assessed for:

1. **Groundedness**. Are claims supported by an approved source?
2. **Accuracy**. Does the answer match documented product behaviour?
3. **Freshness**. Is the source still within its review window?
4. **Completeness**. Does the answer include the necessary next step, caveat, or diagnostic question?
5. **Clarity**. Can a Specialist understand and adapt the guidance quickly?
6. **Escalation behaviour**. Does the system recognise uncertainty and route correctly?

## Measures for a pilot

These are proposed pilot measures, not reported production outcomes:

- First-contact resolution
- Customer satisfaction after support interaction
- Specialist time to find verified guidance
- Percentage of high-volume ticket intents covered by approved content
- Percentage of articles with owners and current review dates
- Grounded-answer rate and unsupported-answer rate
- Time from product change to validated knowledge update
- Specialist confidence in the system

## What this demonstrates

This prototype shows how I approach support knowledge as an operating system. It combines information architecture, content modelling, governance, AI evaluation, human oversight, automation requirements, and outcome measurement.

**Next build artefacts**: a structured sample knowledge set, content quality validator, sample ticket webhook, and a GitHub Actions quality-check workflow.

---

[Home](index.md) · [Work](work.md) · [Content Systems](content-systems.md) · [Systems & AI](systems-ai.md) · [Writing](writing.md)
