---
layout: page
title: "AI Prompt Library"
---

# Prompt Patterns and Evaluation Frameworks

These examples illustrate how I design language for LLM workflows inside enterprise tools.

## 1. Diagnostic Prompts
**Purpose:** Clarify ambiguous inputs without oversteering the model.  
**Template:**
> Given the user's query `{query}`, identify what product feature or intent they likely mean and respond with one clarifying question before giving an answer.

**Evaluation Criteria:**
- Clarity of diagnostic question  
- Neutrality of tone  
- Latency impact (<500 ms average)

---

## 2. Explainability Prompts
**Goal:** surface model reasoning transparently.  
**Template:**
> Explain your answer in one paragraph, using numbered points and confidence labels between 0 and 1.  

**Safeguards:** truncation rule at 200 tokens; check for speculation phrases.

---

## 3. Refusal & Escalation Patterns
**Intent:** maintain safety and compliance.  
**Example:**
> I'm not able to generate investment recommendations.  
> Would you like to see documentation about risk categories instead?

**Evaluation Metrics:** refusal accuracy > 95%, escalation click-through ≥ 60%.

---

_These prompt families align with FrostLogic-style AI content design and Anthropic’s Constitutional AI principles._
