# AI Engineering — Security, Observability & Operations

5 senior-level interview questions with architectural trade-offs, practical examples and follow-ups.

> Answers are original study material. Product capabilities and cloud SKUs should be checked against current vendor documentation before deployment.

## 305. How do you secure enterprise LLM applications?

**Concept:** Enterprise AI introduces data leakage, prompt injection, unsafe tool execution and model supply-chain risks.

**How and why:** Use Entra auth, RBAC, tenant filters, DLP/redaction, encrypted stores, rate limits, prompt/tool audits, policy gates and least privilege.

**Real-world example:** Internal assistant answers policy questions without exposing restricted payroll documents.

**Trade-offs / failure modes:** Guardrail products reduce risk but cannot guarantee correctness.

**Interview follow-up:** What is the threat model for a tool-using agent?

## 306. How do you monitor LLM applications in production?

**Concept:** Traditional uptime metrics miss answer quality and token cost.

**How and why:** Track p50/p95 latency, tokens, cost, retrieval quality, tool errors, safety incidents, user feedback and trace spans; sample and redact logs.

**Real-world example:** OpenTelemetry traces ingestion, vector retrieval, rerank, model call and approval.

**Trade-offs / failure modes:** Avoid logging raw secrets or sensitive prompts.

**Interview follow-up:** What triggers an AI quality rollback?

## 307. What are LangSmith, Langfuse, Phoenix, Ragas and Promptfoo used for?

**Concept:** These tools focus on tracing, evaluation, experiment comparison and regression testing.

**How and why:** Use traces for diagnosis, labeled datasets for evaluation, Ragas-like RAG metrics and Promptfoo-style scenario tests; verify current features per product.

**Real-world example:** Run nightly regression suite for 100 audit questions after prompt or model change.

**Trade-offs / failure modes:** Automated scores need human calibration.

**Interview follow-up:** How would you evaluate tool-selection accuracy?

## 308. How do you deploy and scale inference services?

**Concept:** Inference capacity is constrained by model memory, batching, concurrency and GPU resources.

**How and why:** Estimate tokens/sec, KV cache, VRAM, TTFT, autoscaling and queue limits; benchmark vLLM or managed endpoints.

**Real-world example:** Scale Qwen inference workers behind an internal API, separate from Spring Boot business services.

**Trade-offs / failure modes:** GPU cost and cold start can dominate economics.

**Interview follow-up:** How do you handle load shedding?

## 309. How do you design AI model fallback and versioning?

**Concept:** Models and providers can fail or change behavior across versions.

**How and why:** Pin model/prompt versions, test compatibility, implement timeouts and fallback policy, retain eval history and audit output provenance.

**Real-world example:** Fallback to approved smaller model for document classification, but block high-risk approval decisions if quality is inadequate.

**Trade-offs / failure modes:** Fallback can silently reduce accuracy.

**Interview follow-up:** How do you detect model drift?
