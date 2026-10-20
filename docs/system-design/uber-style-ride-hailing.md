# System Design: Uber-style Ride Hailing

**Interview level:** Senior / Staff / Solution Architect  
**Scenario / capacity assumption:** 100K active drivers, location update every 5s. These are illustrative starting assumptions; clarify them with the interviewer.

## 1. Functional and non-functional requirements

Describe core user journeys, authorization and data lifecycle. Establish availability, latency, consistency, privacy, RTO/RPO and throughput targets. Distinguish essential MVP from optional features.

## 2. Capacity and sizing

Given **100K active drivers, location update every 5s**, estimate peak requests/sec, bytes/request, read/write ratio, storage growth and headroom. Verify with realistic load tests. State your assumptions explicitly.

## 3. APIs

`POST /rides; POST /rides/{id}/accept; driver location stream`

Define authentication, idempotency, pagination, status codes, versioning and failure responses for each endpoint.

## 4. Data model

`DriverLocation, DriverAvailability, Ride, Offer, TripEvent`

Identify authoritative state, uniqueness constraints, indexes, TTL/retention, partition keys and transactional boundaries.

## 5. High-level architecture

```text
Driver GPS → location ingest → geo-index; rider → match service → offers → trip state → payment
```

## 6. Core design decisions

H3/geohash candidate search; ETA ranking; atomic ride assignment; TTL offers.

## 7. Failure scenarios and trade-offs

Stale GPS, double acceptance, hot cells, surge fairness. Define retries with jitter, deadlines, backpressure, monitoring, compensations and a rollback plan.

## 8. Observability and security

Monitor Match latency, offer acceptance, GPS staleness, trip completion. Add structured logs, traces, SLOs, access controls, audit logs, encryption and secret management.

## 9. Interview follow-ups

1. Which component fails first at 10× traffic?
2. How do you avoid duplicate effects when clients retry?
3. What consistency guarantee is required for the critical write?
4. How would you deploy across two Azure regions?
5. Which cost dominates at scale and how would you measure it?
