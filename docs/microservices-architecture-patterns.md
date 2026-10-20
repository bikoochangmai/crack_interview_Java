# Microservices — Architecture & Patterns

7 senior-level interview questions with architectural trade-offs, practical examples and follow-ups.

> Answers are original study material. Product capabilities and cloud SKUs should be checked against current vendor documentation before deployment.

## 259. Monolith vs modular monolith vs microservices?

**Concept:** Architecture should match team boundaries, domain complexity and deployment needs.

**How and why:** Start with modular monolith when boundaries unclear; extract services when independent scaling, ownership or release cycles justify cost.

**Real-world example:** Compliance audit starts modular, later separates document ingestion from approval workflow.

**Trade-offs / failure modes:** Microservices add network failure, observability and data consistency costs.

**Interview follow-up:** How would you decide service boundaries using DDD?

## 260. Explain saga orchestration vs choreography.

**Concept:** Long-running distributed transactions need compensating actions rather than ACID across services.

**How and why:** Orchestrator commands steps and compensations; choreography reacts to events. Persist saga state and handle duplicate/out-of-order events.

**Real-world example:** Order saga reserves inventory, charges payment, schedules shipping; refund and release inventory on failure.

**Trade-offs / failure modes:** Choreography can obscure workflow and create event spaghetti.

**Interview follow-up:** What if compensation itself fails?

## 261. Explain circuit breaker, retry, timeout and bulkhead.

**Concept:** Cascading failures occur when one slow dependency consumes all resources.

**How and why:** Set end-to-end deadlines, retry only safe operations with jitter, open circuit on failure, isolate pools/concurrency.

**Real-world example:** Catalog recommendations time out but checkout continues without personalized results.

**Trade-offs / failure modes:** Retries can amplify outages; avoid retry storms.

**Interview follow-up:** What metrics indicate a circuit should open?

## 262. How do you implement distributed tracing and correlation IDs?

**Concept:** A single request crosses many services; logs alone are insufficient.

**How and why:** Propagate W3C trace context, record OpenTelemetry spans, link logs/metrics, sample traces and redact PII.

**Real-world example:** Track API Management→Spring Boot→Kafka consumer→PostgreSQL for an order.

**Trade-offs / failure modes:** Asynchronous traces need context propagation across messages.

**Interview follow-up:** What is the difference between trace ID and idempotency key?

## 263. Explain CQRS and event sourcing.

**Concept:** CQRS separates command and query models; event sourcing persists state changes as an append-only event log.

**How and why:** Use CQRS selectively for read/write asymmetry; event sourcing when auditability and replay justify complexity.

**Real-world example:** Compliance audit uses append-only approval events and materialized read views.

**Trade-offs / failure modes:** Schema evolution, replay and eventual consistency increase complexity.

**Interview follow-up:** Can you use CQRS without event sourcing?

## 264. How do you version APIs without breaking clients?

**Concept:** Distributed consumers upgrade at different speeds.

**How and why:** Prefer additive changes, tolerant readers, contract tests, deprecation policy and explicit versioning for breaking changes.

**Real-world example:** Mobile app old version continues working while backend adds optional field.

**Trade-offs / failure modes:** Silent semantic changes break clients even when schema is compatible.

**Interview follow-up:** How would you migrate a required field?

## 265. What are BFF and API composition patterns?

**Concept:** Different clients need different payloads and orchestration.

**How and why:** Backend-for-frontend shapes responses per client; API composition joins data at read time with timeouts and partial-failure policy.

**Real-world example:** Angular admin dashboard gets consolidated audit metrics via dedicated BFF.

**Trade-offs / failure modes:** BFF must not duplicate core business rules.

**Interview follow-up:** How do you prevent N+1 backend calls?
