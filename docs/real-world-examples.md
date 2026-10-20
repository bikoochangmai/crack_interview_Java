# Real-world examples for interview questions

158 of the 232 interview questions have individually matched production scenarios. Other questions retain their original concise answer cues; contributions can extend them.

## Examples

### #4 — equals() and hashCode() contract?

**Answer:** Equal objects must have equal hash codes; use consistent immutable identity keys.

**Production example:** Two CustomerId instances represent the same ID. If equals returns true, their hashCode values must match so HashSet and HashMap behave correctly.

### #11 — Immutable class design?

**Answer:** Final fields, defensive copies, no mutable state exposure; records are shallowly immutable.

**Production example:** Design a high-traffic checkout service: define throughput, consistency and latency requirements, then justify storage, queues, caching and failure recovery.

### #13 — Singleton design pattern and pitfalls?

**Answer:** One instance; enum singleton or holder idiom; beware global state, tests and distributed instances.

**Production example:** An application needs one immutable configuration registry. Prefer a dependency-injected singleton bean rather than global mutable state.

### #16 — HashMap internals and collisions?

**Answer:** Hashing, buckets, equals; tree bins may be used for high collisions; not thread-safe.

**Production example:** A service caches user sessions by session ID. A HashMap gives average O(1) lookup; use ConcurrentHashMap if multiple threads mutate it.

### #17 — HashMap vs ConcurrentHashMap?

**Answer:** ConcurrentHashMap supports concurrent operations; null keys/values not allowed.

**Production example:** A service caches user sessions by session ID. A HashMap gives average O(1) lookup; use ConcurrentHashMap if multiple threads mutate it.

### #26 — Collectors.groupingBy vs partitioningBy?

**Answer:** Grouping arbitrary keys; partitioning Boolean predicate.

**Production example:** A Kafka topic uses customerId as its message key. Events for the same customer stay ordered within one partition, but global ordering is not guaranteed.

### #38 — Java 21 virtual threads?

**Answer:** Finalized in 21; lightweight threads for high-concurrency blocking workloads, not CPU speedups.

**Production example:** An API performs 200 concurrent slow HTTP calls. Virtual threads simplify blocking-style code, but downstream HTTP pools and database connections still cap throughput.

### #43 — Platform vs virtual threads?

**Answer:** Virtual threads are JVM-managed and scale blocking concurrency; platform threads map more directly to OS threads.

**Production example:** An API performs 200 concurrent slow HTTP calls. Virtual threads simplify blocking-style code, but downstream HTTP pools and database connections still cap throughput.

### #47 — volatile vs atomic variables?

**Answer:** volatile ensures visibility/order; atomics provide compound atomic operations.

**Production example:** A worker loops until a shutdown flag changes. A volatile boolean makes the update visible across threads, but does not make compound increments atomic.

### #48 — Race condition vs deadlock vs starvation?

**Answer:** Incorrect interleaving, circular waiting, and indefinite lack of progress.

**Production example:** Thread A locks account 1 then account 2, while thread B locks them in reverse order. Establish a consistent lock ordering and capture a thread dump to diagnose.

### #49 — ExecutorService and thread pools?

**Answer:** Manage task execution, queues, rejection, lifecycle; size by workload.

**Production example:** A web service uses a fixed worker pool to call a slow vendor API. Saturated workers cause queue growth; add timeouts, bulkheads and bounded queues.

### #52 — ConcurrentHashMap computeIfAbsent semantics?

**Answer:** Atomic key computation in ConcurrentHashMap; keep mapping function short.

**Production example:** A service caches user sessions by session ID. A HashMap gives average O(1) lookup; use ConcurrentHashMap if multiple threads mutate it.

### #69 — @Transactional behavior and proxy limitations?

**Answer:** Proxy-based transactions; self-invocation bypasses advice in common proxy mode.

**Production example:** An order placement method writes inventory and order rows. Put the operation behind a transactional service boundary; avoid external network calls inside the transaction.

### #71 — Isolation levels in Spring transactions?

**Answer:** Map to DB semantics; database support determines actual behavior.

**Production example:** An order placement method writes inventory and order rows. Put the operation behind a transactional service boundary; avoid external network calls inside the transaction.

### #79 — REST principles?

**Answer:** Resource orientation, stateless requests, uniform interface, cacheability.

**Production example:** Order and inventory services fail independently. Use asynchronous events, idempotent consumers, observability and a compensating action rather than a distributed DB transaction.

### #80 — HTTP GET/POST/PUT/PATCH/DELETE semantics?

**Answer:** GET safe, PUT/DELETE idempotent by intended semantics, POST usually not; PATCH depends.

**Production example:** Order and inventory services fail independently. Use asynchronous events, idempotent consumers, observability and a compensating action rather than a distributed DB transaction.

### #81 — What is idempotency?

**Answer:** Repeating same operation has same intended effect; use keys for payment/order POST retries.

**Production example:** A payment webhook arrives twice after a network retry. Persist the event ID with a unique constraint and return the previous result for the duplicate.

### #82 — HTTP status codes 200/201/202/204/400/401/403/404/409/429?

**Answer:** Success, created, accepted, no content, bad request, unauthenticated, forbidden, not found, conflict, rate limit.

**Production example:** Order and inventory services fail independently. Use asynchronous events, idempotent consumers, observability and a compensating action rather than a distributed DB transaction.

### #83 — API versioning and pagination?

**Answer:** Compatibility strategy; cursor pagination for large changing datasets.

**Production example:** Order and inventory services fail independently. Use asynchronous events, idempotent consumers, observability and a compensating action rather than a distributed DB transaction.

### #84 — Authentication vs authorization?

**Answer:** Verify identity vs enforce allowed actions.

**Production example:** Order and inventory services fail independently. Use asynchronous events, idempotent consumers, observability and a compensating action rather than a distributed DB transaction.

### #85 — JWT vs session vs OIDC?

**Answer:** JWT token format; session state mechanism; OIDC authentication protocol.

**Production example:** A mobile client sends a bearer JWT to a Java API. Validate token signature, issuer, audience and expiry; never trust claims from an unverified token.

### #86 — OAuth2 authorization code + PKCE?

**Answer:** Secure delegated sign-in flow for public clients.

**Production example:** A web app signs in with Microsoft Entra ID using OpenID Connect authorization code + PKCE, then sends access tokens to a protected API.

### #87 — CORS vs CSRF?

**Answer:** Browser cross-origin access policy vs forged authenticated requests.

**Production example:** Order and inventory services fail independently. Use asynchronous events, idempotent consumers, observability and a compensating action rather than a distributed DB transaction.

### #88 — RBAC vs ABAC?

**Answer:** Role-based permissions vs attribute/context policies.

**Production example:** Order and inventory services fail independently. Use asynchronous events, idempotent consumers, observability and a compensating action rather than a distributed DB transaction.

### #89 — Monolith vs microservices trade-offs?

**Answer:** Deployment/team autonomy vs network, consistency and operational complexity.

**Production example:** Order and inventory services fail independently. Use asynchronous events, idempotent consumers, observability and a compensating action rather than a distributed DB transaction.

### #90 — Service discovery and API gateway?

**Answer:** Find service instances and centralize edge routing/security.

**Production example:** Order and inventory services fail independently. Use asynchronous events, idempotent consumers, observability and a compensating action rather than a distributed DB transaction.

### #91 — Circuit breaker, retry, timeout, bulkhead?

**Answer:** Bound failure impact; retries only safe with idempotency and budgets.

**Production example:** A payment gateway times out. Retry only when the operation is safe or uses an idempotency key; apply exponential backoff and jitter.

### #92 — Saga vs distributed transaction?

**Answer:** Compensating business steps vs coordinated atomic transactions.

**Production example:** An order placement method writes inventory and order rows. Put the operation behind a transactional service boundary; avoid external network calls inside the transaction.

### #93 — Outbox pattern and exactly-once claims?

**Answer:** Persist event with DB state, relay asynchronously; consumers still need idempotency.

**Production example:** An order transaction commits but publishing OrderCreated to Kafka fails. Save an outbox row in the same DB transaction and publish it asynchronously.

### #94 — Eventual consistency and CQRS?

**Answer:** Asynchronous convergence; separate read/write models when warranted.

**Production example:** Order and inventory services fail independently. Use asynchronous events, idempotent consumers, observability and a compensating action rather than a distributed DB transaction.

### #95 — Observability in microservices?

**Answer:** Correlation IDs, metrics, logs, distributed traces, SLOs.

**Production example:** Order and inventory services fail independently. Use asynchronous events, idempotent consumers, observability and a compensating action rather than a distributed DB transaction.

### #96 — How secure service-to-service calls?

**Answer:** mTLS or workload identity/tokens, least privilege, rotation.

**Production example:** Order and inventory services fail independently. Use asynchronous events, idempotent consumers, observability and a compensating action rather than a distributed DB transaction.

### #97 — Explain ACID with examples.

**Answer:** Atomicity, consistency, isolation, durability; e.g. transferring money.

**Production example:** An order and its payment record must commit together. Wrap both updates in one database transaction; roll back both if either fails.

### #98 — Primary key vs unique key vs foreign key?

**Answer:** Identity, uniqueness, and referential integrity.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #99 — INNER vs LEFT vs FULL OUTER JOIN?

**Answer:** Matching rows, all left rows, all rows from both.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #100 — WHERE vs HAVING?

**Answer:** Filter rows before grouping vs groups after aggregation.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #101 — GROUP BY and aggregate functions?

**Answer:** Group rows for COUNT/SUM/AVG/MIN/MAX.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #102 — Window functions ROW_NUMBER, RANK, DENSE_RANK?

**Answer:** Rank rows within partitions without collapsing them.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #103 — Find second-highest salary?

**Answer:** Use DENSE_RANK over salaries and filter rank 2; define tie behavior.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #104 — Find duplicate records?

**Answer:** GROUP BY key HAVING COUNT(*)>1; use ROW_NUMBER to identify extras.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #105 — CTE vs subquery?

**Answer:** Named query expression vs inline nested query; optimizer-dependent performance.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #106 — UNION vs UNION ALL?

**Answer:** UNION removes duplicates; UNION ALL preserves them.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #107 — DELETE vs TRUNCATE vs DROP?

**Answer:** Delete rows, empty table, remove object; transaction semantics vary.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #108 — Indexes and composite index order?

**Answer:** Speed selective reads with write/storage cost; leftmost prefix often matters.

**Production example:** A customer search on email is slow with millions of rows. Create an index on the searched column, inspect EXPLAIN ANALYZE, and compare read gains against write overhead.

### #109 — B-tree vs GIN vs GiST indexes?

**Answer:** General ordered lookups vs inverted/multidimensional access methods.

**Production example:** A customer search on email is slow with millions of rows. Create an index on the searched column, inspect EXPLAIN ANALYZE, and compare read gains against write overhead.

### #110 — EXPLAIN ANALYZE and slow SQL?

**Answer:** Inspect actual plans, row estimates, scans, join methods and timings.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #111 — Transactions and isolation anomalies?

**Answer:** Dirty/nonrepeatable/phantom reads, lost updates, write skew; DB-specific.

**Production example:** An order placement method writes inventory and order rows. Put the operation behind a transactional service boundary; avoid external network calls inside the transaction.

### #112 — Optimistic vs pessimistic locking?

**Answer:** Version checks vs database locks; choose by contention.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #113 — MVCC in PostgreSQL?

**Answer:** Row versions allow consistent reads while writers operate.

**Production example:** A reporting query runs while orders are updated. PostgreSQL MVCC allows the reader to see a consistent snapshot without blocking ordinary writes.

### #114 — Deadlocks in databases?

**Answer:** Conflicting lock order; detect/retry and enforce consistent ordering.

**Production example:** Thread A locks account 1 then account 2, while thread B locks them in reverse order. Establish a consistent lock ordering and capture a thread dump to diagnose.

### #115 — Normalization 1NF/2NF/3NF vs denormalization?

**Answer:** Reduce anomalies vs optimize read models with controlled redundancy.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #116 — Offset vs keyset pagination?

**Answer:** Offset easy but degrades/changes under writes; keyset efficient for stable order.

**Production example:** A Kafka consumer processes an order but crashes before committing the offset. The record can replay, so the handler must be idempotent.

### #117 — Partitioning vs sharding vs replication?

**Answer:** Table partitioning, distributing data, copying data for availability/reads.

**Production example:** A Kafka topic uses customerId as its message key. Events for the same customer stay ordered within one partition, but global ordering is not guaranteed.

### #118 — Connection pooling and N+1 query issue?

**Answer:** Reuse connections; avoid per-row ORM queries using joins/fetch batching.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #119 — JSONB vs relational columns?

**Answer:** Flexible indexed documents vs explicit constraints and relational modeling.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #120 — PostgreSQL pgvector retrieval?

**Answer:** Embedding vector similarity search; choose indexes and filter permissions.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #121 — Design schema for audit findings/approvals?

**Answer:** Foreign keys, tenant IDs, versioning, immutable audit trail and indexes.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #122 — Angular component lifecycle?

**Answer:** Constructor, ngOnInit, ngOnChanges, ngOnDestroy and render hooks.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #123 — Standalone components vs NgModules?

**Answer:** Standalone imports dependencies directly; NgModules group legacy declarations.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #124 — Change detection and OnPush?

**Answer:** Check strategies; immutable inputs, signals and observable emissions.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #125 — Signals vs RxJS Observables?

**Answer:** Signals model synchronous reactive state; RxJS streams async events.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #126 — Subject vs BehaviorSubject vs ReplaySubject?

**Answer:** No replay, latest value replay, configurable history replay.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #127 — switchMap vs mergeMap vs concatMap vs exhaustMap?

**Answer:** Cancel prior, concurrent, sequential, ignore while busy.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #128 — Async pipe and subscription cleanup?

**Answer:** Template subscription lifecycle; takeUntilDestroyed for imperative subscriptions.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #129 — Reactive vs template-driven forms?

**Answer:** Explicit model/testability vs simpler template-managed forms.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #130 — Custom validators and async validators?

**Answer:** Sync/async validation functions; manage pending and errors.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #131 — Route guards and lazy loading?

**Answer:** Client navigation UX, not a replacement for server authorization.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #132 — HTTP interceptors?

**Answer:** Cross-cutting request headers, errors, tracing; avoid token leaks.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #133 — Angular authentication and token storage?

**Answer:** OIDC/PKCE; consider BFF HttpOnly cookies, CSRF and XSS risks.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #134 — Content projection vs ViewChild?

**Answer:** Reusable projected content vs references to template children.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #135 — trackBy / @for track and rendering?

**Answer:** Stable identity reduces unnecessary DOM work.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #136 — Pure vs impure pipes?

**Answer:** Pure reruns on input reference/value changes; impure every check.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #137 — TypeScript interface vs type alias?

**Answer:** Both describe types; interfaces support declaration merging.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #138 — Generics, union and discriminated unions?

**Answer:** Reusable type parameters and safe variants.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #139 — Angular performance troubleshooting?

**Answer:** Profiling, lazy routes, OnPush, virtual scrolling, request caching.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #140 — State management service vs NgRx?

**Answer:** Choose by complexity, shared state and debugging needs.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #141 — Unit tests and component integration tests?

**Answer:** Test behavior, services, HTTP mocking, accessibility.

**Production example:** An Angular search box uses RxJS debounceTime and switchMap to cancel stale requests as a user types, preventing old results from overwriting new ones.

### #142 — HLD vs LLD?

**Answer:** Services/data flows/trade-offs vs classes/contracts/algorithms.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #143 — CAP theorem and consistency models?

**Answer:** Under network partition choose consistency or availability; nuance required.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #144 — Horizontal vs vertical scaling?

**Answer:** More instances vs bigger instances.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #145 — Load balancer, CDN and cache?

**Answer:** Traffic distribution, edge content delivery, latency reduction.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #146 — Azure App Service vs VM vs AKS?

**Answer:** Managed web hosting vs full VM control vs orchestrated containers.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #147 — Azure Service Bus vs Event Hubs?

**Answer:** Enterprise messaging/commands vs high-throughput event ingestion.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #148 — Azure Blob vs PostgreSQL storage?

**Answer:** Object binaries vs transactional structured metadata.

**Production example:** A high-volume audit table grows rapidly. Partition by date where justified, monitor query plans, and archive old partitions according to retention policy.

### #149 — Design multi-tenant isolation?

**Answer:** Tenant scoping, authorization, RLS/schema/database separation.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #150 — RTO vs RPO and disaster recovery?

**Answer:** Recovery time objective vs acceptable data loss.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #151 — Zero-downtime deployments?

**Answer:** Backward-compatible migrations, rolling/canary releases, health checks.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #152 — Design a rate limiter?

**Answer:** Token bucket or sliding window, Redis atomicity and fairness.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #153 — Design URL shortener?

**Answer:** IDs, redirects, cache, hot keys, analytics, collision strategy.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #154 — Design document ingestion + RAG?

**Answer:** Upload, parse, chunk, embed, vector search, ACL filtering, citations.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #155 — Design human-in-loop approvals?

**Answer:** State machine, RBAC, audit trail, optimistic locking.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #156 — How handle incidents and RCA?

**Answer:** Contain impact, evidence, blameless root cause and corrective action.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #157 — How defend architecture trade-offs?

**Answer:** Requirements, alternatives, measurable constraints and failure modes.

**Production example:** A Spring Boot API is deployed to Azure App Service with managed identity for secrets, PostgreSQL for persistence, and Application Insights for telemetry.

### #168 — What is Kafka, and why use it instead of a traditional message broker?

**Answer:** Apache Kafka is a distributed event-streaming platform. It stores ordered records in partitioned, replicated logs and lets multiple applications publish and consume events independently. It is especially useful for high-throughput event pipelines, replay, and decoupling services. Unlike many queue-only designs, Kafka retains events according to configured retention policies, so consumers can reread them.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #169 — What are topics, partitions, brokers, and offsets?

**Answer:** A topic is a named stream of records. A partition is an ordered log within a topic. A broker is a Kafka server that stores partition replicas and serves client requests. An offset is the position of a record within one partition; offsets are not globally unique across a topic.

**Production example:** A Kafka consumer processes an order but crashes before committing the offset. The record can replay, so the handler must be idempotent.

### #170 — Can multiple producers publish to the same topic?

**Answer:** Yes. Multiple producers can publish concurrently to the same topic. Records are routed to partitions according to the producer's partitioner, key, and configuration. Ordering is guaranteed within a partition, not across the whole topic.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #171 — Can multiple consumer groups consume the same topic?

**Answer:** Yes. Each consumer group tracks its own progress, so different applications can independently consume the same records. For example, one group can update an order database while another updates analytics.

**Production example:** A topic has 6 partitions and a consumer group has 3 active consumers. Kafka can assign 2 partitions to each consumer; a fourth consumer can share work after rebalance.

### #172 — What is the difference between a consumer and a consumer group?

**Answer:** A consumer is a client that reads records. A consumer group is a set of consumers that cooperate to consume subscribed partitions. Within one group, each partition is assigned to at most one consumer at a time; different groups can independently read the same partition.

**Production example:** A topic has 6 partitions and a consumer group has 3 active consumers. Kafka can assign 2 partitions to each consumer; a fourth consumer can share work after rebalance.

### #173 — How are messages distributed across partitions?

**Answer:** A producer can select a partition explicitly, use a key-based partitioner, or use a partitioning strategy for records without keys. With keyed records, records sharing a key are commonly routed to the same partition, preserving per-key ordering while the partition count and partitioning strategy remain stable.

**Production example:** A Kafka topic uses customerId as its message key. Events for the same customer stay ordered within one partition, but global ordering is not guaranteed.

### #174 — What is the difference between an offset and a message key?

**Answer:** A key is application data used for partitioning or identifying related records. An offset is Kafka's position number for a record in a specific partition. Keys may repeat; offsets identify positions within a partition.

**Production example:** A Kafka consumer processes an order but crashes before committing the offset. The record can replay, so the handler must be idempotent.

### #175 — Can Kafka guarantee message ordering?

**Answer:** Kafka guarantees order within a single partition. It does not guarantee total ordering across multiple partitions. To preserve order for a particular entity, such as an orderId, publish its events with that entity as the key so they normally go to the same partition.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #176 — How does Kafka assign partitions to consumers?

**Answer:** The group coordinator manages group membership and offsets, while the group leader and configured assignor determine partition assignments. Assignment strategies include range, round-robin, sticky, and cooperative-sticky approaches, depending on client configuration and version.

**Production example:** A topic has 6 partitions and a consumer group has 3 active consumers. Kafka can assign 2 partitions to each consumer; a fourth consumer can share work after rebalance.

### #177 — Can two consumers in the same group read the same partition simultaneously?

**Answer:** Under normal group assignment, no: a partition is assigned to at most one consumer in that group at a time. Two consumers in different groups can read that same partition independently.

**Production example:** A topic has 6 partitions and a consumer group has 3 active consumers. Kafka can assign 2 partitions to each consumer; a fourth consumer can share work after rebalance.

### #178 — What happens when consumers outnumber partitions?

**Answer:** Some consumers in the group remain without partition assignments and cannot consume records from that topic. Adding consumers beyond the partition count does not increase parallel consumption of those partitions.

**Production example:** A topic has 6 partitions and a consumer group has 3 active consumers. Kafka can assign 2 partitions to each consumer; a fourth consumer can share work after rebalance.

### #179 — How does a consumer group rebalance work?

**Answer:** Kafka redistributes partition assignments when group membership or subscription changes, or when a consumer is considered unavailable. During reassignment, consumption can pause or be disrupted depending on the protocol and assignor. Cooperative rebalancing can reduce the amount of work that must be revoked.

**Production example:** A topic has 6 partitions and a consumer group has 3 active consumers. Kafka can assign 2 partitions to each consumer; a fourth consumer can share work after rebalance.

### #180 — What triggers a rebalance?

**Answer:** Common triggers include a consumer joining or leaving, a consumer failing heartbeats or exceeding poll limits, topic/partition changes, subscription changes, or group metadata changes.

**Production example:** A topic has 6 partitions and a consumer group has 3 active consumers. Kafka can assign 2 partitions to each consumer; a fourth consumer can share work after rebalance.

### #181 — Who maintains consumer offsets?

**Answer:** Kafka stores committed offsets in the internal __consumer_offsets topic. Progress is tracked per consumer group and topic-partition. The consumer application typically controls when to commit, either automatically or explicitly.

**Production example:** A topic has 6 partitions and a consumer group has 3 active consumers. Kafka can assign 2 partitions to each consumer; a fourth consumer can share work after rebalance.

### #182 — What is the difference between auto-commit and manual commit?

**Answer:** Auto-commit periodically commits offsets based on consumer configuration. Manual commits let the application choose when progress is committed, which can better align with successful processing. Incorrect commit timing can cause message loss from the application's perspective or duplicate processing.

**Production example:** A topic has 6 partitions and a consumer group has 3 active consumers. Kafka can assign 2 partitions to each consumer; a fourth consumer can share work after rebalance.

### #183 — What happens if a consumer crashes after processing a message but before committing its
 offset?

**Answer:** After restart or reassignment, Kafka may deliver that record again because the committed position did not advance. This is at-least-once behavior and can cause duplicate side effects unless processing is idempotent.

**Production example:** A topic has 6 partitions and a consumer group has 3 active consumers. Kafka can assign 2 partitions to each consumer; a fourth consumer can share work after rebalance.

### #184 — How do you handle duplicate message processing?

**Answer:** Use idempotent processing: for example, enforce a unique event ID in the database, use an upsert, or store processed-event IDs transactionally with the business update. Kafka producer idempotence helps prevent certain duplicate writes from producer retries, but it does not by itself make external database effects exactly once.

**Production example:** A topic has 6 partitions and a consumer group has 3 active consumers. Kafka can assign 2 partitions to each consumer; a fourth consumer can share work after rebalance.

### #185 — What are leader and follower replicas?

**Answer:** Each partition has a leader replica that handles normal reads and writes, and zero or more follower replicas that replicate the leader's log. Replicas are typically distributed across brokers for fault tolerance.

**Production example:** A shared counter receives updates from many requests. AtomicInteger.incrementAndGet uses atomic read-modify-write operations rather than a synchronized critical section.

### #186 — What happens when a partition leader's broker crashes?

**Answer:** If an eligible in-sync replica is available, Kafka can elect it as the new leader. The partition may be briefly unavailable during detection and election. If no eligible replica is available, availability depends on the configuration and recovery situation.

**Production example:** A Kafka topic uses customerId as its message key. Events for the same customer stay ordered within one partition, but global ordering is not guaranteed.

### #187 — What is the ISR (in-sync replica) list?

**Answer:** ISR means in-sync replicas: replicas considered sufficiently caught up with the leader under Kafka's replication rules. The ISR is important for safe leader election and for interpreting acknowledgements such as acks=all.

**Production example:** A Kafka broker holding a partition leader fails. An in-sync replica may become leader; replication factor and min.insync.replicas affect durability.

### #188 — What do replication.

**Answer:** factor, min.insync.replicas, and acks mean? replication.factor sets how many replicas are configured per partition. min.insync.replicas is the minimum ISR size required for writes with acks=all. Producer acks controls the acknowledgement level: 0 waits for none, 1 waits for the leader, and all waits for the in-sync replicas required by the protocol. These settings work together to balance durability and availability.

**Production example:** A Kafka broker holding a partition leader fails. An in-sync replica may become leader; replication factor and min.insync.replicas affect durability.

### #189 — What happens when all replicas are unavailable?

**Answer:** The partition becomes unavailable until a suitable replica can serve as leader. If replicas later recover with their logs intact, data can become available again. If all copies are permanently lost, replication cannot recover the data.

**Production example:** A shared counter receives updates from many requests. AtomicInteger.incrementAndGet uses atomic read-modify-write operations rather than a synchronized critical section.

### #190 — What is unclean leader election?

**Answer:** Unclean leader election permits a replica outside the ISR to become leader when no ISR replica is available. This can restore availability but may lose records that existed only on the previous leader. Disabling it favors data safety over availability in that situation.

**Production example:** A Kafka broker holding a partition leader fails. An in-sync replica may become leader; replication factor and min.insync.replicas affect durability.

### #191 — Can Kafka lose messages even with replication factor 3?

**Answer:** Yes. Possible causes include simultaneous permanent loss of all replicas, weak producer acknowledgements, unsafe leader election, misconfiguration, operator deletion, retention expiry, or an application committing offsets before processing is safely complete. Replication reduces risk but is not a backup against every failure.

**Production example:** A Kafka broker holding a partition leader fails. An in-sync replica may become leader; replication factor and min.insync.replicas affect durability.

### #192 — How do you design a highly available Kafka cluster?

**Answer:** Use multiple brokers across independent failure domains, appropriate replication (often factor 3), a suitable min.insync.replicas with acks=all, safe leader-election settings, monitoring, capacity headroom, tested recovery procedures, and backups or replication to another cluster when required. Availability and durability requirements must be balanced explicitly.

**Production example:** A Kafka broker holding a partition leader fails. An in-sync replica may become leader; replication factor and min.insync.replicas affect durability.

### #193 — What are at-most-once, at-least-once, and exactly-once delivery?

**Answer:** At-most-once means a record may be lost but is not intentionally retried after progress is committed. At-least-once means records are retried until processing succeeds, so duplicates are possible. Exactly-once means each intended effect is reflected once within a clearly defined transactional boundary; it should not be claimed for arbitrary external systems without additional coordination.

**Production example:** An order placement method writes inventory and order rows. Put the operation behind a transactional service boundary; avoid external network calls inside the transaction.

### #194 — Does Kafka guarantee exactly-once processing end to end?

**Answer:** Kafka supports transactions and exactly-once processing patterns between Kafka topics when producers, consumers, offsets, and isolation settings are configured correctly. End-to-end exactly-once effects involving a relational database, email service, or other external system usually require idempotency, an outbox/inbox pattern, or a coordinated transaction strategy.

**Production example:** An order placement method writes inventory and order rows. Put the operation behind a transactional service boundary; avoid external network calls inside the transaction.

### #195 — What is idempotent production?

**Answer:** An idempotent producer uses producer IDs and sequence numbers so Kafka can deduplicate retrying writes from the same producer session and preserve ordering under supported retry scenarios. It reduces duplicate records caused by producer retries, but it does not deduplicate arbitrary application-level repeated sends.

**Production example:** A payment webhook arrives twice after a network retry. Persist the event ID with a unique constraint and return the previous result for the duplicate.

### #196 — How do Kafka transactions work?

**Answer:** A transactional producer can write records to multiple partitions and commit or abort them as a unit. Consumers configured with isolation.level=read_committed read only committed transactional records. Transactions can also include consumed offsets, enabling atomic consume-process-produce flows within Kafka.

**Production example:** An order placement method writes inventory and order rows. Put the operation behind a transactional service boundary; avoid external network calls inside the transaction.

### #197 — What is the difference between producer idempotence and consumer idempotency?

**Answer:** Producer idempotence prevents certain duplicate log writes caused by producer retries. Consumer idempotency makes repeated processing of the same event safe, such as by using a unique event ID and a database uniqueness constraint. They protect different boundaries.

**Production example:** A payment webhook arrives twice after a network retry. Persist the event ID with a unique constraint and return the previous result for the duplicate.

### #198 — How do you atomically write output records and commit consumed offsets?

**Answer:** Use a transactional producer: begin a transaction, produce output records, add the consumed offsets to the transaction using the consumer group metadata, and commit. If the transaction aborts, output records and offsets are not committed as a successful unit. Exact APIs depend on the Kafka client version.

**Production example:** An order placement method writes inventory and order rows. Put the operation behind a transactional service boundary; avoid external network calls inside the transaction.

### #199 — How would you prevent duplicate database updates?

**Answer:** Make the handler idempotent. A common pattern is to assign each event a stable ID and, in one database transaction, insert that ID into a processed-events table with a unique constraint and apply the business update. If the ID already exists, skip the duplicate. Carefully coordinate offset commits with successful database commits.

**Production example:** An order placement method writes inventory and order rows. Put the operation behind a transactional service boundary; avoid external network calls inside the transaction.

### #200 — How do you implement a retry and dead-letter topic strategy?

**Answer:** Retry transient failures with bounded attempts and backoff, then route poison or exhausted messages to a dead-letter topic with the original topic, partition, offset, key, error, and timestamp in headers or metadata. Define replay procedures and alerting. Avoid blocking a partition indefinitely, and preserve ordering where the business requires it.

**Production example:** An order placement method writes inventory and order rows. Put the operation behind a transactional service boundary; avoid external network calls inside the transaction.

### #201 — How do producer acknowledgments work?

**Answer:** acks=0 means no broker acknowledgement is awaited; acks=1 waits for the leader's local write; acks=all waits for acknowledgement from the in-sync replicas according to Kafka's replication protocol and min.insync.replicas constraints. Higher durability can increase latency or reduce write availability.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #202 — What are batching, linger.

**Answer:** ms, and compression? The producer batches records per partition. linger.ms allows a short wait to build larger batches; batch.size limits batch size. Compression (such as gzip, lz4, or zstd, depending on client support) reduces network and disk traffic, trading some CPU for throughput.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #203 — How do keys affect partition selection and ordering?

**Answer:** A key commonly determines the partition, keeping events with the same key together and ordered within that partition. If the partition count or partitioner changes, key-to-partition mapping may change, so strict long-term ordering for a key needs careful topic and migration design.

**Production example:** A Kafka topic uses customerId as its message key. Events for the same customer stay ordered within one partition, but global ordering is not guaranteed.

### #204 — What happens when a hot key overloads one partition?

**Answer:** A high-volume key can concentrate traffic on one partition while others are underused. Options include changing the key strategy, sharding the key, increasing partitions where appropriate, or splitting the workload. Sharding can weaken per-entity ordering and must be designed around business requirements.

**Production example:** A Kafka topic uses customerId as its message key. Events for the same customer stay ordered within one partition, but global ordering is not guaranteed.

### #205 — How do you tune producer throughput and latency?

**Answer:** Measure first. Tune batch.size, linger.ms, compression.type, buffer.memory, request limits, acknowledgements, and partition count based on throughput, latency, durability, and broker capacity. Monitor retries, request latency, record errors, and buffer exhaustion.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #206 — What are backpressure and consumer lag?

**Answer:** Backpressure is the mechanism by which a slower downstream system limits upstream intake. Consumer lag describes how far a consumer group's position is behind the log end, commonly measured in records or offsets. Lag can grow because of slow processing, insufficient consumers/partitions, broker issues, or traffic spikes.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #207 — How do you investigate increasing consumer lag?

**Answer:** Check lag by partition, input rate versus processing rate, consumer errors and latency, rebalance frequency, poll/heartbeat settings, downstream database/API latency, GC and CPU, broker/network health, and partition skew. Scale consumers only when there are unassigned partitions or partition parallelism can be increased safely.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #208 — How do you choose the number of partitions?

**Answer:** Estimate throughput per partition, required consumer parallelism, message ordering needs, retention and storage, and broker capacity. More partitions can improve parallelism but increase metadata, file handles, recovery work, and operational overhead. Load-test and leave room for growth.

**Production example:** A Kafka topic uses customerId as its message key. Events for the same customer stay ordered within one partition, but global ordering is not guaranteed.

### #209 — How does Kafka store records on disk?

**Answer:** Kafka stores partition data as an append-only log split into segment files. Records are written sequentially, which supports efficient disk and network use. The operating system page cache often plays an important role in read performance.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #210 — What are segments, indexes, and log retention?

**Answer:** A partition log is divided into segments. Indexes help locate offsets and timestamps efficiently. Retention policies remove old or excess log segments based on time or size; deleting old data is separate from consumer offset commits.

**Production example:** A customer search on email is slow with millions of rows. Create an index on the searched column, inspect EXPLAIN ANALYZE, and compare read gains against write overhead.

### #211 — What is log compaction?

**Answer:** Compaction retains the latest known value for each key over time, while allowing older values for the same key to be removed. It is useful for changelog or state-reconstruction topics. It is asynchronous, and tombstone records mark deleted keys for removal during compaction.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #212 — What are retention by time, size, and compaction?

**Answer:** Time retention removes segments after a configured age; size retention removes older segments to stay within a configured log-size limit; compaction keeps the latest value per key rather than preserving every historical value indefinitely. A topic can be configured with policies appropriate to its use case.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #213 — What is the role of the controller?

**Answer:** The controller manages cluster metadata and coordination tasks such as partition leadership and broker state changes. In modern Kafka using KRaft, controller nodes use the metadata quorum rather than ZooKeeper to manage cluster metadata.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #214 — What is KRaft, and how does it differ from ZooKeeper-based Kafka?

**Answer:** KRaft is Kafka's built-in consensus-based metadata management mode. Older Kafka deployments used ZooKeeper for cluster metadata and controller coordination. KRaft removes the separate ZooKeeper dependency and uses a Kafka metadata log and controller quorum.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #215 — How does replication work internally?

**Answer:** Followers fetch records from the leader and append them to their own logs. Replica progress is tracked, and leader election uses replica eligibility and ISR state. Replication is asynchronous in typical operation, so acknowledgement settings matter for durability.

**Production example:** A Kafka broker holding a partition leader fails. An in-sync replica may become leader; replication factor and min.insync.replicas affect durability.

### #216 — What is the high-watermark concept?

**Answer:** The high watermark is the offset boundary up to which records are considered replicated sufficiently for normal consumer visibility. It helps distinguish records that are safe to expose from records that may not yet be safely replicated. Exact behavior depends on Kafka's replication protocol and version.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #217 — How do you configure Kafka producers and consumers in Spring Boot?

**Answer:** Set bootstrap servers, serializers/deserializers, group ID, offset policy, and security settings in application configuration. Use KafkaTemplate for producing and @KafkaListener for consuming. Configure error handling, retry policy, transactions, and observability explicitly for production.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #218 — What are @KafkaListener and ConsumerRecord?

**Answer:** @KafkaListener marks a Spring-managed method that receives records from Kafka. ConsumerRecord provides record metadata such as topic, partition, offset, key, value, timestamp, and headers. Listener signatures can also receive just the value or other supported metadata types.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #219 — How do you configure retries and error handlers?

**Answer:** Use Spring Kafka's error-handling facilities, such as DefaultErrorHandler and configured backoff, and a dead-letter publishing recoverer when appropriate. Decide which exceptions are retryable, bound attempts, and ensure DLT publishing failures are handled.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #220 — How do you handle deserialization errors?

**Answer:** Use appropriate serializers/deserializers and validation. Spring Kafka can use error-handling deserializers to capture deserialization failures and route or recover those records. Record enough metadata for investigation without exposing sensitive payload data.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #221 — How do you manage database transactions with Kafka consumers?

**Answer:** A Kafka transaction does not automatically include an ordinary database transaction. A robust approach is often database idempotency plus carefully ordered commits, or an outbox/inbox pattern. If using Spring transaction support, understand exactly which resources are coordinated and what failure windows remain.

**Production example:** An order placement method writes inventory and order rows. Put the operation behind a transactional service boundary; avoid external network calls inside the transaction.

### #222 — How do you test Kafka integrations?

**Answer:** Unit-test business logic separately. For integration tests, use an embedded broker or a containerized Kafka test environment, publish test records, verify outputs and error behavior, and test retry, serialization, and restart scenarios. Avoid tests that depend on arbitrary sleeps when a deterministic condition can be used.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #223 — How do you manage schemas and backward compatibility?

**Answer:** Use a schema format and registry where appropriate, define compatibility rules, and evolve schemas additively where possible. Ensure old and new consumers can handle deployed versions, and test producer/consumer compatibility before rollout.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #224 — How do you monitor consumer lag and broker health?

**Answer:** Monitor lag by group and partition, throughput, request latency, under-replicated partitions, offline partitions, ISR changes, disk usage, CPU, network, produce/fetch errors, rebalances, and consumer processing latency. Alert on sustained symptoms tied to service-level objectives.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #225 — Design an event-driven order processing system using Kafka.

**Answer:** Publish an OrderCreated event keyed by orderId. Separate consumers handle inventory, payment, shipping, and notifications through their own groups. Use schema versioning, idempotent handlers, bounded retries, DLTs, tracing, and an outbox pattern to reliably publish events from a database transaction. Define compensation for cross-service failures rather than assuming one global transaction.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #226 — Design a multi-channel notification platform using Kafka.

**Answer:** An API validates requests and persists accepted notification jobs, preferably with an outbox. Kafka distributes events to channel-specific workers for push, email, SMS, or in-app delivery. Use per-channel consumer groups, provider rate limits, retry topics, DLTs, idempotency keys, preference/consent checks, delivery-status events, metrics, and prioritization. Partition by a suitable key and size capacity for peak traffic.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #227 — Design a payment event pipeline with strong durability guarantees.

**Answer:** Use durable replicated topics, acks=all, suitable min.insync.replicas, idempotent producers, strict schema governance, and idempotent consumers. Persist payment state transactionally and use unique transaction/event IDs. Keep an audit trail, reconcile with the payment provider, monitor lag and replication health, and define recovery and replay procedures.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #228 — How would you process 1 million events per second?

**Answer:** Start by measuring record size, key distribution, latency target, and downstream capacity. Partition enough to parallelize producers and consumers, scale brokers and consumers horizontally, batch and compress, use efficient serialization, and avoid hot keys. Load-test end-to-end and monitor disk/network throughput, replication, lag, and failure recovery. No fixed partition count guarantees a target rate.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #229 — How do you handle poison messages without blocking a partition?

**Answer:** Classify failures. Retry transient issues with bounded backoff; route repeatedly failing records to a DLT or retry topic with diagnostic metadata. Ensure offset handling does not skip records unintentionally. If strict ordering is required, decide whether later records for that key must wait until the failed event is repaired.

**Production example:** A Kafka topic uses customerId as its message key. Events for the same customer stay ordered within one partition, but global ordering is not guaranteed.

### #230 — How would you migrate a live system to Kafka without losing events?

**Answer:** Use a controlled dual-write or transactional outbox approach, define an authoritative source, and reconcile counts or event IDs. If replaying from a database or old broker, establish a consistent cutover point, make consumers idempotent, monitor duplicates and gaps, and perform a staged cutover with rollback criteria.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #231 — How do you replay historical events safely?

**Answer:** Choose a replay strategy such as a dedicated consumer group, a new topic, or resetting offsets in a controlled group. Make side effects idempotent, throttle replay to protect downstream systems, preserve event versions, and separate replay traffic from live traffic if needed. Understand retention and compaction before relying on historical records.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

### #232 — How would you evolve topic schemas without breaking consumers?

**Answer:** Use backward/forward compatibility rules, add optional fields with safe defaults, and deploy consumers that tolerate old and new versions before producers begin emitting new fields. Avoid changing field meaning or types in place. Test compatibility and use versioned events or topics for breaking changes.

**Production example:** A retail order service publishes OrderPlaced events. Inventory and notifications consume independently; use schemas, retry/DLT policies and consumer idempotency.

