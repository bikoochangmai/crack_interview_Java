# System Design: Distributed Rate Limiter

**Interview level:** Senior / Staff / Solution Architect  
**Scenario / capacity assumption:** 1M requests/minute across regions. These are illustrative starting assumptions; clarify them with the interviewer.

## 1. Functional and non-functional requirements

Describe core user journeys, authorization and data lifecycle. Establish availability, latency, consistency, privacy, RTO/RPO and throughput targets. Distinguish essential MVP from optional features.

## 2. Capacity and sizing

Given **1M requests/minute across regions**, estimate peak requests/sec, bytes/request, read/write ratio, storage growth and headroom. Verify with realistic load tests. State your assumptions explicitly.

## 3. APIs

`HTTP middleware checks tenant/user token bucket`

Define authentication, idempotency, pagination, status codes, versioning and failure responses for each endpoint.

## 4. Data model

`LimitPolicy, Counter/TokenBucket`

Identify authoritative state, uniqueness constraints, indexes, TTL/retention, partition keys and transactional boundaries.

## 5. High-level architecture

```text
Edge/API Gateway → Redis cluster or local token buckets → backend
```

## 6. Core design decisions

Token bucket for bursts; bounded keys; fallback policy and headers.

## 7. Failure scenarios and trade-offs

Clock skew, Redis outage, hot tenants, fairness. Define retries with jitter, deadlines, backpressure, monitoring, compensations and a rollback plan.

## 8. Observability and security

Monitor Allowed/rejected requests, latency overhead, false rejects. Add structured logs, traces, SLOs, access controls, audit logs, encryption and secret management.

## 9. Interview follow-ups

1. Which component fails first at 10× traffic?
2. How do you avoid duplicate effects when clients retry?
3. What consistency guarantee is required for the critical write?
4. How would you deploy across two Azure regions?
5. Which cost dominates at scale and how would you measure it?
