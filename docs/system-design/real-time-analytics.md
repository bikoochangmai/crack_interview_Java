# System Design: Real-time Analytics

**Interview level:** Senior / Staff / Solution Architect  
**Scenario / capacity assumption:** 1M events/sec burst. These are illustrative starting assumptions; clarify them with the interviewer.

## 1. Functional and non-functional requirements

Describe core user journeys, authorization and data lifecycle. Establish availability, latency, consistency, privacy, RTO/RPO and throughput targets. Distinguish essential MVP from optional features.

## 2. Capacity and sizing

Given **1M events/sec burst**, estimate peak requests/sec, bytes/request, read/write ratio, storage growth and headroom. Verify with realistic load tests. State your assumptions explicitly.

## 3. APIs

`POST /events; GET /dashboards`

Define authentication, idempotency, pagination, status codes, versioning and failure responses for each endpoint.

## 4. Data model

`Event stream, Aggregation, MaterializedView`

Identify authoritative state, uniqueness constraints, indexes, TTL/retention, partition keys and transactional boundaries.

## 5. High-level architecture

```text
Clients → Event Hubs/Kafka → stream processing → OLAP store → dashboard
```

## 6. Core design decisions

Partition keys, watermarking, late events, exactly-once-aware sinks.

## 7. Failure scenarios and trade-offs

Hot partitions, duplicate events, late arrivals, retention costs. Define retries with jitter, deadlines, backpressure, monitoring, compensations and a rollback plan.

## 8. Observability and security

Monitor End-to-end freshness, consumer lag, data correctness. Add structured logs, traces, SLOs, access controls, audit logs, encryption and secret management.

## 9. Interview follow-ups

1. Which component fails first at 10× traffic?
2. How do you avoid duplicate effects when clients retry?
3. What consistency guarantee is required for the critical write?
4. How would you deploy across two Azure regions?
5. Which cost dominates at scale and how would you measure it?
