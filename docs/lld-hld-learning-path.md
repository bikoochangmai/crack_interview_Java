# LLD and HLD: two study paths, ten worked problems

**LLD asks how objects, methods, state and synchronization implement a contract. HLD asks how services, durable stores and network boundaries satisfy a user journey under load and failure.** Use the same concrete examples at both levels instead of memorizing disconnected pattern names.

## Low-Level Design (LLD)

1. [Parking lot](lld/parking-lot.md): numbered levels, entry/exit gates, slot-selection policy, tickets and competing admissions.
2. [Tic Tac Toe](lld/tic-tac-toe.md): OOP roles, legal moves, turn handling, win/draw and terminal states. This is the chosen Chess-or-Tic-Tac-Toe exercise; it does not claim to implement chess rules.
3. [LRU cache from scratch](lld/lru-cache.md): map plus doubly linked list, access/update order, eviction and expected O(1) operations.
4. [Thread-safe HashMap](lld/thread-safe-hashmap.md): buckets, locks, atomic compute, collisions and snapshot semantics; compare with ConcurrentHashMap.
5. [Rate limiter class and distributed boundary](lld/rate-limiter.md): tested token bucket, injected time, tenant budgets and cluster-wide ownership. Continue to [the scalable rate-limiter tutorial](system-design/distributed-rate-limiter.md).

Each LLD lesson has a runnable Java 21 lab, a four-step diagram, explicit invariants, error cases and an explanation of what is not provided by a process-local implementation.

## High-Level Design (HLD)

1. [URL Shortener](system-design/short-url.md): domain ownership, DNS/TLS, code mapping, browser redirect, authorization and outages.
2. [Real-time Chat](system-design/whatsapp-style-messaging.md): durable send, offline delivery, ordering, group fan-out and encryption.
3. [Distributed Key-Value Store](system-design/distributed-key-value-store.md): routing, replicated log, leader/quorum, versioned operations, reads, partitions and recovery.
4. [Uber-style Ride Matching](system-design/uber-style-ride-hailing.md): geographic candidates, expiring offers, atomic assignment and trip lifecycle.
5. [Notification System](system-design/notification-platform.md): authorized event intent, channel fan-out, provider retries, deduplication and delivery tracking.

The existing HLD tutorials retain their stable portal IDs and progress. The new Notifications and Distributed Key-Value Store entries make those topics directly trackable too.

## How to practice

For LLD, write the operation contract and state invariants, sketch collaborating types, trace one call, run boundary/concurrency tests, then discuss complexity and extensions. For HLD, follow one authenticated user request through authoritative state, acknowledgement, timeout/retry and recovery before discussing scale.

[Foundation tutorials](system-design-foundations.md) · [All system-design tutorials](system-design/README.md)
