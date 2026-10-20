# Architecture — Senior / Staff Leadership

5 senior-level interview questions with architectural trade-offs, practical examples and follow-ups.

> Answers are original study material. Product capabilities and cloud SKUs should be checked against current vendor documentation before deployment.

## 310. How do you conduct an architecture decision record (ADR)?

**Concept:** ADRs document context, constraints, options, decision and consequences for future maintainers.

**How and why:** Capture measurable requirements, rejected alternatives, trade-offs, ownership and revisit triggers.

**Real-world example:** Record why compliance system chose pgvector over separate vector database at current scale.

**Trade-offs / failure modes:** An ADR is not an immutable decree; revisit when assumptions change.

**Interview follow-up:** How do you measure whether the decision was successful?

## 311. How do you migrate a legacy system without downtime?

**Concept:** Large migrations need controlled traffic shifting and data parity.

**How and why:** Inventory dependencies; introduce adapter; backfill; dual-read/compare; canary; cut over gradually; retain rollback.

**Real-world example:** Documentum→Alfresco migration with stable content API and checksums.

**Trade-offs / failure modes:** Dual-write drift and hidden integrations are common failure modes.

**Interview follow-up:** How do you handle document version history?

## 312. How do you design multi-tenant SaaS isolation?

**Concept:** Tenant isolation affects identity, data, caches, queues, logs and cost controls.

**How and why:** Choose DB-per-tenant, schema-per-tenant or shared tables with tenant_id and RLS; enforce at every boundary.

**Real-world example:** Enterprise audit customers must never see one another’s document chunks.

**Trade-offs / failure modes:** Shared resources risk noisy neighbors and accidental data exposure.

**Interview follow-up:** How would you test tenant isolation?

## 313. How do you define SLO, SLA, SLI and error budgets?

**Concept:** Reliability targets should reflect user experience and guide release decisions.

**How and why:** SLI is measurement, SLO is target, SLA is contractual commitment; track allowed failures over a window.

**Real-world example:** 99.9% monthly checkout availability permits ~43.2 minutes unavailable in a 30-day month.

**Trade-offs / failure modes:** Availability alone misses correctness and latency.

**Interview follow-up:** What should happen when error budget is exhausted?

## 314. How do you estimate cost and capacity for an architecture?

**Concept:** Architectural choices must meet performance goals within budget.

**How and why:** Estimate peak requests, bytes, storage growth, network egress, DB IOPS, GPU tokens/sec, replicas and operational overhead; load test assumptions.

**Real-world example:** RAG assistant cost model includes embeddings at ingestion and LLM output tokens per query.

**Trade-offs / failure modes:** Cloud egress and managed-service minimums are often overlooked.

**Interview follow-up:** What metrics would you collect during a proof of concept?
