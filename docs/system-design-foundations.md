# System Design — Foundations

10 senior-level interview questions with architectural trade-offs, practical examples and follow-ups.

> Answers are original study material. Product capabilities and cloud SKUs should be checked against current vendor documentation before deployment.

## 233. How do you approach a system design interview?

**Concept:** Translate vague requirements into measurable functional and non-functional requirements.

**How and why:** Clarify users, reads/writes, latency, availability, retention and consistency. Estimate QPS and storage, draw APIs and data model, then evolve the architecture from bottlenecks.

**Real-world example:** For a shopping app, distinguish catalog browsing (read-heavy) from checkout (stronger correctness requirements).

**Trade-offs / failure modes:** Avoid premature microservices; start simple, justify each component.

**Interview follow-up:** How do you estimate peak QPS from daily active users?

## 234. Explain client-server architecture and HTTP request lifecycle.

**Concept:** The client handles interaction while the server authenticates, applies business rules and manages persistent state.

**How and why:** DNS resolves hostname; TCP/TLS establishes transport; HTTP request reaches CDN/WAF/load balancer, application and database; response returns to client.

**Real-world example:** Angular SPA calls Spring Boot REST APIs through Azure Front Door and API Management.

**Trade-offs / failure modes:** Stateless servers scale horizontally but need shared session/token design.

**Interview follow-up:** Where should authorization be enforced?

## 235. How do load balancers, reverse proxies, API gateways and CDNs differ?

**Concept:** They solve different routing, security and performance problems.

**How and why:** Load balancer spreads requests; reverse proxy fronts servers; API gateway handles API policy/routing; CDN caches edge content.

**Real-world example:** Azure Front Door serves cached assets; API Management validates API policies; backend ingress distributes requests.

**Trade-offs / failure modes:** Do not use API gateway as a business-logic monolith.

**Interview follow-up:** What changes for WebSockets?

## 236. How do you choose between SQL, NoSQL and search engines?

**Concept:** Pick storage based on invariants, query patterns, data shape and scale rather than fashion.

**How and why:** Relational DB for transactional constraints/joins; document or key-value for flexible/access-pattern data; Elasticsearch for search; vector index for semantic retrieval.

**Real-world example:** Orders in PostgreSQL, product search in Elasticsearch, semantic document chunks in pgvector.

**Trade-offs / failure modes:** Polyglot persistence adds synchronization and operational burden.

**Interview follow-up:** How do you keep search index consistent with the database?

## 237. Explain caching strategies and cache invalidation.

**Concept:** Caching reduces read latency and backend load but creates stale-data risk.

**How and why:** Use cache-aside for common reads, TTL with jitter, explicit invalidation on writes and request coalescing for hot keys.

**Real-world example:** Product detail cache in Redis; price and inventory checked against authoritative source at checkout.

**Trade-offs / failure modes:** Never assume cache consistency equals database consistency.

**Interview follow-up:** How do you prevent cache stampede and hot-key overload?

## 238. How do you design for high availability and disaster recovery?

**Concept:** Availability requires redundancy and operational recovery plans.

**How and why:** Define SLO, RTO and RPO; distribute across availability zones; use backups, restore drills, failover and graceful degradation.

**Real-world example:** Checkout runs across Azure zones; replicated database plus tested backups and region recovery playbook.

**Trade-offs / failure modes:** Multi-region active-active is costly and creates data conflict challenges.

**Interview follow-up:** Difference between RTO and RPO?

## 239. Explain CAP theorem, consistency and quorum.

**Concept:** During a network partition, a distributed data system must choose between serving every request and preserving a defined consistency guarantee.

**How and why:** Describe consistency model explicitly; choose read/write quorums where supported and define behavior under partition.

**Real-world example:** Shopping cart may favor availability; payment ledger favors correctness and may reject writes during partition.

**Trade-offs / failure modes:** CAP is about partitions, not a generic ranking of databases.

**Interview follow-up:** How do you handle stale reads after a write?

## 240. Explain rate limiting, throttling and backpressure.

**Concept:** Protect dependencies and fairness when demand exceeds capacity.

**How and why:** Token bucket or sliding window at edge; bounded queues and concurrency limits in services; return 429 with Retry-After when appropriate.

**Real-world example:** Short URL API limits anonymous creation requests while redirect traffic remains highly optimized.

**Trade-offs / failure modes:** Aggressive limits harm legitimate bursty traffic.

**Interview follow-up:** Where do distributed rate-limit counters live?

## 241. How do you design idempotent APIs?

**Concept:** Retries happen due to timeouts, so duplicate requests must not duplicate side effects.

**How and why:** Client sends idempotency key; persist request fingerprint and final result atomically with operation or coordinate via unique constraints.

**Real-world example:** Payment POST with key returns same transaction result when client retries.

**Trade-offs / failure modes:** Key expiry and mismatched payloads require explicit policy.

**Interview follow-up:** How do you handle concurrent requests with same key?

## 242. What are horizontal scaling, partitioning and sharding?

**Concept:** Horizontal scaling adds nodes; sharding distributes data ownership to scale storage/write throughput.

**How and why:** Select shard key with even distribution; route requests and plan rebalancing; use read replicas separately.

**Real-world example:** Messaging platform partitions chat events by conversation ID for ordering.

**Trade-offs / failure modes:** Hot shards and cross-shard transactions complicate design.

**Interview follow-up:** How do you handle celebrity hot keys?
