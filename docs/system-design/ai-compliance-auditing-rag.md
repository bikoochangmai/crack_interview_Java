# System Design: AI Compliance Auditing RAG

**Interview level:** Senior / Staff / Solution Architect  
**Scenario / capacity assumption:** 100K policy PDFs, 500 simultaneous auditors. These are illustrative starting assumptions; clarify them with the interviewer.

## 1. Functional and non-functional requirements

Describe core user journeys, authorization and data lifecycle. Establish availability, latency, consistency, privacy, RTO/RPO and throughput targets. Distinguish essential MVP from optional features.

## 2. Capacity and sizing

Given **100K policy PDFs, 500 simultaneous auditors**, estimate peak requests/sec, bytes/request, read/write ratio, storage growth and headroom. Verify with realistic load tests. State your assumptions explicitly.

## 3. APIs

`POST /documents; POST /ask; POST /findings/{id}/approve`

Define authentication, idempotency, pagination, status codes, versioning and failure responses for each endpoint.

## 4. Data model

`Document, Version, Chunk, Embedding, ACL, Finding, Approval, AuditEvent`

Identify authoritative state, uniqueness constraints, indexes, TTL/retention, partition keys and transactional boundaries.

## 5. High-level architecture

```text
Blob → ingestion/OCR → chunk/embed → pgvector; Entra → API → hybrid retrieval → LLM → cited answer → approval gate
```

## 6. Core design decisions

Tenant ACL filtering, versioned citations, outbox ingestion, structured output validation, human approval.

## 7. Failure scenarios and trade-offs

Prompt injection, wrong citations, ACL leaks, model drift, ingestion failures. Define retries with jitter, deadlines, backpressure, monitoring, compensations and a rollback plan.

## 8. Observability and security

Monitor Faithfulness, retrieval recall@k, tool accuracy, unauthorized retrieval=0. Add structured logs, traces, SLOs, access controls, audit logs, encryption and secret management.

## 9. Interview follow-ups

1. Which component fails first at 10× traffic?
2. How do you avoid duplicate effects when clients retry?
3. What consistency guarantee is required for the critical write?
4. How would you deploy across two Azure regions?
5. Which cost dominates at scale and how would you measure it?
