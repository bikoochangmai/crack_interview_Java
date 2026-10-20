# System Design: WhatsApp-style Messaging

**Interview level:** Senior / Staff / Solution Architect  
**Scenario / capacity assumption:** 1M concurrent connections; delivery to offline users. These are illustrative starting assumptions; clarify them with the interviewer.

## 1. Functional and non-functional requirements

Describe core user journeys, authorization and data lifecycle. Establish availability, latency, consistency, privacy, RTO/RPO and throughput targets. Distinguish essential MVP from optional features.

## 2. Capacity and sizing

Given **1M concurrent connections; delivery to offline users**, estimate peak requests/sec, bytes/request, read/write ratio, storage growth and headroom. Verify with realistic load tests. State your assumptions explicitly.

## 3. APIs

`WebSocket send/ack; GET /conversations/{id}/messages`

Define authentication, idempotency, pagination, status codes, versioning and failure responses for each endpoint.

## 4. Data model

`Conversation, Member, Message(id, conversation_id, seq, ciphertext, status)`

Identify authoritative state, uniqueness constraints, indexes, TTL/retention, partition keys and transactional boundaries.

## 5. High-level architecture

```text
Mobile → WebSocket gateway → Message service → durable store → queue → recipient gateway/push
```

## 6. Core design decisions

Per-conversation sequencing; message IDs and dedupe; durable offline queue; end-to-end encryption.

## 7. Failure scenarios and trade-offs

Reconnection duplicates, reordering, offline retention, group fan-out, encryption keys. Define retries with jitter, deadlines, backpressure, monitoring, compensations and a rollback plan.

## 8. Observability and security

Monitor Delivery latency, queue lag, duplicate rate, reconnect success. Add structured logs, traces, SLOs, access controls, audit logs, encryption and secret management.

## 9. Interview follow-ups

1. Which component fails first at 10× traffic?
2. How do you avoid duplicate effects when clients retry?
3. What consistency guarantee is required for the critical write?
4. How would you deploy across two Azure regions?
5. Which cost dominates at scale and how would you measure it?
