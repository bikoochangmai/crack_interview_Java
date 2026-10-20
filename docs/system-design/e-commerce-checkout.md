# System Design: E-commerce Checkout

**Interview level:** Senior / Staff / Solution Architect  
**Scenario / capacity assumption:** 100K product views/minute; 5K checkouts/minute at peak. These are illustrative starting assumptions; clarify them with the interviewer.

## 1. Functional and non-functional requirements

Describe core user journeys, authorization and data lifecycle. Establish availability, latency, consistency, privacy, RTO/RPO and throughput targets. Distinguish essential MVP from optional features.

## 2. Capacity and sizing

Given **100K product views/minute; 5K checkouts/minute at peak**, estimate peak requests/sec, bytes/request, read/write ratio, storage growth and headroom. Verify with realistic load tests. State your assumptions explicitly.

## 3. APIs

`GET /products; POST /orders; POST /payments`

Define authentication, idempotency, pagination, status codes, versioning and failure responses for each endpoint.

## 4. Data model

`Product, Inventory(sku, available), Reservation, Order, Payment, Outbox`

Identify authoritative state, uniqueness constraints, indexes, TTL/retention, partition keys and transactional boundaries.

## 5. High-level architecture

```text
Angular → API gateway → Catalog/Search; Checkout → Inventory → Payment PSP → Order → Outbox/Kafka
```

## 6. Core design decisions

Atomic inventory reservation; idempotency key; payment webhook state machine; saga compensation.

## 7. Failure scenarios and trade-offs

Oversell, PSP timeout, duplicate webhook, eventual search consistency. Define retries with jitter, deadlines, backpressure, monitoring, compensations and a rollback plan.

## 8. Observability and security

Monitor Oversell count=0, checkout success, payment reconciliation mismatch. Add structured logs, traces, SLOs, access controls, audit logs, encryption and secret management.

## 9. Interview follow-ups

1. Which component fails first at 10× traffic?
2. How do you avoid duplicate effects when clients retry?
3. What consistency guarantee is required for the critical write?
4. How would you deploy across two Azure regions?
5. Which cost dominates at scale and how would you measure it?
