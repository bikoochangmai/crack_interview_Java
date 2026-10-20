# System Design: Short URL

**Interview level:** Senior / Staff / Solution Architect  
**Scenario / capacity assumption:** 100M redirects/day, 1M creations/day. These are illustrative starting assumptions; clarify them with the interviewer.

## 1. Functional and non-functional requirements

Describe core user journeys, authorization and data lifecycle. Establish availability, latency, consistency, privacy, RTO/RPO and throughput targets. Distinguish essential MVP from optional features.

## 2. Capacity and sizing

Given **100M redirects/day, 1M creations/day**, estimate peak requests/sec, bytes/request, read/write ratio, storage growth and headroom. Verify with realistic load tests. State your assumptions explicitly.

## 3. APIs

`POST /links; GET /{code}`

Define authentication, idempotency, pagination, status codes, versioning and failure responses for each endpoint.

## 4. Data model

`Link(code PK, target_url, owner, expires_at, status)`

Identify authoritative state, uniqueness constraints, indexes, TTL/retention, partition keys and transactional boundaries.

## 5. High-level architecture

```text
Client → CDN/WAF → Redirect API → Redis → Link DB; click event → Kafka → analytics
```

## 6. Core design decisions

Base62 IDs; cache hot links; async click metrics; abuse scanning; 302 for mutable redirects.

## 7. Failure scenarios and trade-offs

Code collisions, expired links, phishing, hot keys, DB outage. Define retries with jitter, deadlines, backpressure, monitoring, compensations and a rollback plan.

## 8. Observability and security

Monitor p95 redirect <100ms from edge where practical; cache hit, errors, redirect QPS. Add structured logs, traces, SLOs, access controls, audit logs, encryption and secret management.

## 9. Interview follow-ups

1. Which component fails first at 10× traffic?
2. How do you avoid duplicate effects when clients retry?
3. What consistency guarantee is required for the critical write?
4. How would you deploy across two Azure regions?
5. Which cost dominates at scale and how would you measure it?
