# Homework 3: AI Orchestration with Kestra

**Course:** LLM Zoomcamp 2026 — Module 3

**Topic:** AI Orchestration with Kestra


---

## Homework Overview

Module 3 homework is observational and conceptual rather than purely code-based. The questions test understanding of context engineering, RAG grounding, token economics, and the appropriate use of agents vs. deterministic workflows. Several questions require running live Kestra flows and reading execution logs.

All flows were imported from `03-orchestration/flows/` and executed against a locally running Kestra instance with API keys configured via `.env`.

---

## Question 1: Context Engineering

**Question:** After running the same prompt in ChatGPT vs Kestra's AI Copilot ("Create a Kestra flow that loads NYC taxi data from BigQuery"), what is the primary reason the Copilot generates better Kestra flows?

**Answer:** AI Copilot has access to current Kestra plugin documentation.


---

## Question 2: RAG vs No RAG

**Question:** After running `1_chat_without_rag.yaml` and `2_chat_with_rag.yaml`, the non-RAG response about Kestra 1.1 features is best described as:

**Answer:** Vague, generic, or fabricated — the model guesses from training data.


---

## Question 3: Token Usage — Short Summary

**Question:** After running `4_simple_agent.yaml` with `summary_length = short`, what is the approximate output token count for `multilingual_agent`?

**Answer:** 60–100 tokens.


---

## Question 4: Token Usage — Long Summary

**Question:** Compared to the short summary result from Q3, how many times more output tokens does the long summary use?

**Answer:** 2–5x more.


---

## Question 5: Modifying a Flow

**Question:** After changing the `english_brevity` task prompt from 1 sentence to 3 sentences and running with `summary_length = long`, how does the output token count compare to the original 1-sentence version?

**Answer:** 2–4x more.


---

## Question 6: Best Practices

**Question:** For production workflows requiring deterministic, repeatable results with strict compliance requirements (financial reporting, regulated industries), which approach is most appropriate?

**Answer:** Use traditional task-based workflows for predictability and auditability.


---
