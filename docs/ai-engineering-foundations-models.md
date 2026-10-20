# AI Engineering — Foundations & Models

6 senior-level interview questions with architectural trade-offs, practical examples and follow-ups.

> Answers are original study material. Product capabilities and cloud SKUs should be checked against current vendor documentation before deployment.

## 284. Explain AI vs ML vs deep learning vs generative AI vs LLM.

**Concept:** These terms describe nested or overlapping capabilities, not interchangeable products.

**How and why:** ML learns patterns from data; deep learning uses neural networks; generative models create content; LLMs model token sequences for language tasks.

**Real-world example:** Use classical anomaly detection for structured fraud signals and an LLM to explain audit evidence.

**Trade-offs / failure modes:** LLMs can hallucinate and are not deterministic rule engines.

**Interview follow-up:** When would you avoid an LLM?

## 285. What are tokens, context windows, temperature and top-p?

**Concept:** Inference behavior and cost depend on tokenization and sampling controls.

**How and why:** Context window limits input/output tokens; temperature and top-p influence sampling; enforce output schemas and token budgets.

**Real-world example:** Summarize 20 compliance policies by retrieval instead of stuffing all documents into prompt.

**Trade-offs / failure modes:** Long context can increase latency and degrade retrieval focus.

**Interview follow-up:** Why is deterministic decoding not a guarantee of factual correctness?

## 286. OpenAI API vs Claude API vs Gemini vs open-weight models?

**Concept:** These are model providers/families with different capabilities, terms and deployment options.

**How and why:** Compare structured output, tool calling, multimodal input, context limits, latency, evaluation quality, security and cost; use provider-neutral adapter.

**Real-world example:** Swap an approved OpenAI-compatible endpoint with another provider after regression evaluation.

**Trade-offs / failure modes:** Provider behavior and tool schema vary; do not assume identical responses.

**Interview follow-up:** How do you design graceful provider fallback?

## 287. What is Ollama and how does it differ from vLLM?

**Concept:** Ollama prioritizes convenient local model running; vLLM focuses on high-throughput serving.

**How and why:** Use Ollama for Windows/local prototyping; consider vLLM on supported GPU infrastructure for concurrent production inference.

**Real-world example:** Developer tests Qwen locally via Ollama and Open WebUI; production uses scaled inference endpoint.

**Trade-offs / failure modes:** Local CPU inference may have high latency and limited throughput.

**Interview follow-up:** How do you measure tokens/sec and time-to-first-token?

## 288. What is prompt engineering and structured output?

**Concept:** Prompts specify task and constraints; schemas constrain machine-consumed output.

**How and why:** Use system instructions, trusted context, delimiters, JSON schema validation, retries and output checks.

**Real-world example:** LLM returns audit findings as validated JSON with evidence IDs and severity.

**Trade-offs / failure modes:** Schema-valid does not mean factually correct.

**Interview follow-up:** How do you prevent prompt injection in retrieved text?

## 289. Fine-tuning vs RAG vs prompt engineering?

**Concept:** They solve different problems: behavior/style, knowledge retrieval and instruction quality.

**How and why:** Use prompts first, RAG for changing external knowledge, fine-tune when measured task-specific behavior warrants it.

**Real-world example:** Compliance regulations change monthly, so retrieval from versioned documents is preferable to retraining for every change.

**Trade-offs / failure modes:** Fine-tuning does not guarantee citations or eliminate hallucinations.

**Interview follow-up:** When is fine-tuning actually useful?
