# System Design: Video Streaming Platform

**Interview level:** Senior / Staff / Solution Architect  
**Scenario / capacity assumption:** 1M daily viewers, 100K concurrent streams. These are illustrative starting assumptions; clarify them with the interviewer.

## 1. Functional and non-functional requirements

Describe core user journeys, authorization and data lifecycle. Establish availability, latency, consistency, privacy, RTO/RPO and throughput targets. Distinguish essential MVP from optional features.

## 2. Capacity and sizing

Given **1M daily viewers, 100K concurrent streams**, estimate peak requests/sec, bytes/request, read/write ratio, storage growth and headroom. Verify with realistic load tests. State your assumptions explicitly.

## 3. APIs

`POST /uploads; GET /videos/{id}; GET /manifest/{id}`

Define authentication, idempotency, pagination, status codes, versioning and failure responses for each endpoint.

## 4. Data model

`Video, Asset, Rendition, PlaybackSession`

Identify authoritative state, uniqueness constraints, indexes, TTL/retention, partition keys and transactional boundaries.

## 5. High-level architecture

```text
Uploader → object store → transcode queue → workers → manifests/segments → CDN → player
```

## 6. Core design decisions

Adaptive bitrate HLS/DASH, CDN caching, async encoding, signed access.

## 7. Failure scenarios and trade-offs

Transcode backlog, storage cost, DRM, regional availability. Define retries with jitter, deadlines, backpressure, monitoring, compensations and a rollback plan.

## 8. Observability and security

Monitor Startup delay, buffering ratio, CDN hit rate. Add structured logs, traces, SLOs, access controls, audit logs, encryption and secret management.

## 9. Interview follow-ups

1. Which component fails first at 10× traffic?
2. How do you avoid duplicate effects when clients retry?
3. What consistency guarantee is required for the critical write?
4. How would you deploy across two Azure regions?
5. Which cost dominates at scale and how would you measure it?
