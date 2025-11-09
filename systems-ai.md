---
layout: page
title: "Systems and AI"
---

## How I design systems behind the words

This page is here for teams who care how content scales, not just how it sounds.

![AI content workflow diagram](assets/ai-content-workflow.png)

        ┌────────────────────────────┐
        │        INPUTS              │
        │  UX flows • APIs • Data    │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │   CONTENT DESIGN SYSTEM    │
        │ IA • Templates • Tone • Docs│
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │  AI & AUTOMATION LAYER     │
        │ Prompts • Generation • Eval │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │ GOVERNANCE & REVIEW        │
        │ Ethics • Bias • Accuracy   │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │ OUTPUT                     │
        │ Docs • UI • Chat • Emails  │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │ FEEDBACK LOOP              │
        │ Analytics • Edits • QA     │
        └────────────────────────────┘

*Workflow illustrating content loops between docs, LLMs, and review systems.*

### Content operations for AI products

- Source of truth models for concepts, entities, and terminology
- Contribution models so PMs and engineers can update safely
- Review workflows for safety, legal, and brand

### Prompt and response design

- Structured prompt templates with slots for user context, guardrails, and citations
- Response patterns that stay faithful to policies and product constraints
- Evaluation criteria, for example, accuracy, disclaimers, bias checks, and UX fit

### Documentation and knowledge for LLMs

- Taxonomies for feeding product docs into RAG and search
- Strategies to keep content retrieval friendly, up to date, and auditable
- Experiments in making system behaviour legible for users and stakeholders

You can explore specific frameworks and examples in my case studies under **Work**.

Explore my [AI Prompt Library](ai-prompt-library.md) for examples of structured prompting and evaluation.
