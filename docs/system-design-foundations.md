# System Design — Foundations

Read the example, follow the flow, then explain the failure case. These are illustrative designs, not documented company internals.

[Beginner guide and glossary](system-design/visual-learning-guide.md) · [Case studies](system-design/README.md)

## 233. How do you approach a system design interview?

### Plan before drawing boxes

Design a college canteen app. Students browse menus and place orders; staff prepare them.

### What it means

Functional requirements describe actions. Non-functional requirements describe acceptable latency, availability and data loss. Begin with one API and database; add components only to solve a demonstrated constraint.

### Worked real-world example

Assume 10,000 students placing two orders/day over ten hours: 20,000/36,000 = 0.56 orders/second on average. If 20% arrive in a ten-minute rush, peak is 4,000/600 = 6.7/second. Reads may be much higher.

![Plan before drawing boxes](system-design/diagrams/topic-233.svg)

### Follow the flow

1. **Clarify requirements:** Ask whether cancellation, payment and offline recovery are required.

2. **Estimate demand:** Calculate average and peak separately; state assumptions instead of guessing.

3. **Define API and data:** POST /orders takes item IDs, quantity and an idempotency key. The server computes prices.

4. **Start and measure:** Use a stateless application and transactional database. Measure bottlenecks before adding caches or queues.

### Failure and trade-offs

Premature microservices add network failures and deployment work. A design is justified by requirements, not box count.

### Check your understanding

If traffic grows 100 times, which measurement would guide your first change?

## 234. Explain client-server architecture and HTTP request lifecycle.

### Follow a browser request

A student opens GET /orders/42 to see their lunch order.

### What it means

The browser is the client. The server verifies identity and access, applies rules and uses durable storage. The browser should never connect directly to your application database.

### Worked real-world example

Knowing an order ID is not permission to see it. The API must verify that order 42 belongs to the authenticated student.

![Follow a browser request](system-design/diagrams/topic-234.svg)

### Follow the flow

1. **Resolve hostname:** DNS finds the network address; a cached result can skip a fresh lookup.

2. **Connect securely:** Establish secure transport. TCP plus TLS is common; HTTP/3 uses QUIC.

3. **Authorize and query:** Check credentials and order ownership, then query with parameters.

4. **Return response:** Send JSON and HTTP status; the browser renders it. A timeout leaves the outcome unknown.

### Failure and trade-offs

UI-only authorization can be bypassed. Correlation IDs help identify where a request spent time.

### Check your understanding

If a response times out but the order exists, should the client create a fresh order?

## 235. How do load balancers, reverse proxies, API gateways and CDNs differ?

### Understand the front-door components

A shopping page loads a public logo and a private order history.

### What it means

A CDN caches eligible content near users. A reverse proxy fronts upstream servers. A load balancer selects healthy servers. An API gateway adds API policies such as authentication and quotas. One product may perform several roles.

### Worked real-world example

A cached logo can return from the CDN without reaching the application. Private history needs authorization and an appropriate private cache policy.

![Understand the front-door components](system-design/diagrams/topic-235.svg)

### Follow the flow

1. **Check edge cache:** On an eligible cache hit, return immediately; the remaining steps are for forwarded API requests.

2. **Apply gateway policy:** Validate token and quota. Keep business rules in the application.

3. **Balance the request:** Choose a healthy backend instance; configure connection and idle timeouts.

4. **Enforce object access:** The application checks whose order is requested, loads it and returns the response.

### Failure and trade-offs

Caching private responses publicly leaks data. WebSockets also need long-lived connection routing and a way to locate connected users.

### Check your understanding

Why does gateway token validation not replace order-ownership checks?

## 236. How do you choose between SQL, NoSQL and search engines?

### Choose storage by access pattern

Orders require a ledger; product discovery requires a searchable index.

### What it means

SQL supports relations and transactional invariants. Key-value stores suit known-key lookups. Documents suit aggregate retrieval. Search engines rank text and support filters. NoSQL products do not all share the same guarantees.

### Worked real-world example

Store orders and lines transactionally in PostgreSQL; derive a product search index for queries such as waterproof hiking shoe.

![Choose storage by access pattern](system-design/diagrams/topic-236.svg)

### Follow the flow

1. **Write authoritative data:** Commit related order records together; use constraints for uniqueness and valid relationships.

2. **Record a change event:** For catalog changes, commit an outbox event alongside the product update.

3. **Build search view:** An idempotent indexer applies versioned changes; replay can rebuild the index.

4. **Read the right source:** Search the derived index; checkout rechecks authoritative price and stock.

### Failure and trade-offs

A second store adds synchronization, rebuilds and monitoring. Search can lag behind the source.

### Check your understanding

What happens if search shows a product that just sold out?

## 237. Explain caching strategies and cache invalidation.

### Cache a replaceable copy

A waiter remembers the menu but checks the kitchen before promising the last meal.

### What it means

A cache avoids repeated expensive reads. In cache-aside, the application checks cache first, loads the database on a miss and stores a copy with expiry. TTL limits lifetime; it does not promise freshness.

### Worked real-world example

Product 42 gets 1,000 reads/minute and two changes/day. Cache its description; final stock and price checks still use authoritative state.

![Cache a replaceable copy](system-design/diagrams/topic-237.svg)

### Follow the flow

1. **Look up product:42:** On a permitted fresh-enough hit, return the copy and skip database access.

2. **Load only on miss:** Query the database. Coalesce simultaneous refreshes for the same key.

3. **Store with expiry:** Use a TTL and random expiry jitter to spread refresh load.

4. **Handle writes:** Commit the change then invalidate/update the copy; account for a concurrent stale reader refilling it.

### Failure and trade-offs

Cache failure can overwhelm the database through fallback. Bound fallback load; consider safe stale reads and version checks.

### Check your understanding

Why can invalidation race with a cache refill?

## 238. How do you design for high availability and disaster recovery?

### Separate availability and recovery

A spare counter handles a broken counter; an off-site backup handles a destroyed building.

### What it means

High availability keeps serving during component failures. Disaster recovery restores service after major loss. Replicas provide live copies; backups provide historical recovery. Neither replaces a tested procedure.

### Worked real-world example

Assume a recovery-time objective (RTO) of 30 minutes and recovery-point objective (RPO) of five minutes. The first limits downtime; the second limits lost committed data.

![Separate availability and recovery](system-design/diagrams/topic-238.svg)

### Follow the flow

1. **Detect failure:** Health checks remove unhealthy API instances from routing.

2. **Protect data:** Use suitable database replication plus encrypted recoverable backups and transaction logs.

3. **Recover safely:** Promote the recovery database and fence the previous writer before switching traffic.

4. **Verify recovery:** Test real user journeys and measure actual downtime and data loss against objectives.

### Failure and trade-offs

Async replication may lose recent writes. Replicas also copy accidental deletes, so backups and restore drills remain essential.

### Check your understanding

How would you recover from an accidental delete while every server remains healthy?

## 239. Explain CAP theorem, consistency and quorum.

### Handle disagreement during a partition

Two disconnected ticket counters cannot both safely sell the last seat.

### What it means

During a network partition, a distributed shared-data service cannot always offer both linearizable consistency and a successful response to every request. CAP consistency refers to a single up-to-date logical history, not SQL constraint validity.

### Worked real-world example

For three replicas A, B and C, suppose A can reach B but C is isolated. A write requiring two acknowledgements cannot succeed on C alone.

![Handle disagreement during a partition](system-design/diagrams/topic-239.svg)

### Follow the flow

1. **Network splits:** A and B communicate; C cannot reach them. Define the guarantee required by stock reservations.

2. **Require write quorum:** With N=3 and W=2, two participating replicas must acknowledge.

3. **Read with overlap:** R=2 and W=2 overlap for the same replica set because R+W>N; reconcile versions.

4. **Handle the minority:** Reject or time out operations that cannot meet their contract, then reconcile after connectivity returns.

### Failure and trade-offs

Quorum overlap alone does not prove linearizability. Version selection, concurrent writers and leader rules matter; sloppy quorums may use different replica sets.

### Check your understanding

Why can a social feed tolerate stale data more easily than last-seat booking?

## 240. Explain rate limiting, throttling and backpressure.

### Control overload

A gate limits arrivals, a bounded queue holds a few people, and backpressure asks upstream to slow down.

### What it means

Rate limiting caps arrivals over time. Throttling reduces or delays work. Backpressure propagates lack of capacity toward producers. Queues absorb short bursts but cannot fix sustained overload.

### Worked real-world example

A token bucket with capacity 20 and refill 10 tokens/second allows an idle customer a short burst, then limits the sustained rate.

![Control overload](system-design/diagrams/topic-240.svg)

### Follow the flow

1. **Identify caller:** Authenticate and derive the correct tenant/user key; do not trust an arbitrary tenant header.

2. **Consume atomically:** Refill and consume in one atomic operation; separate reads and writes race.

3. **Admit or reject:** A token admits work; no token returns HTTP 429 with retry guidance.

4. **Bound downstream work:** Cap in-flight requests and queue length; signal pressure when consumers cannot keep up.

### Failure and trade-offs

Five independent per-node quotas can multiply the effective limit. Define fail-open/fail-closed behavior during limiter failure.

### Check your understanding

If five servers each allow 10 requests/second locally, what aggregate rate is possible?

## 241. How do you design idempotent APIs?

### Make one operation safe to retry

A purchase receipt number tells reception that a repeated call refers to the same order.

### What it means

Idempotency means retries of one logical request cause one intended business effect. A durable, concurrency-safe key identifies the operation. An in-memory map on one application instance is not sufficient.

### Worked real-world example

Order-request-81 commits, but its response is lost. A retry with the same key should return the original order rather than create another.

![Make one operation safe to retry](system-design/diagrams/topic-241.svg)

### Follow the flow

1. **Send stable key:** Generate one key per logical purchase and reuse it only for retries.

2. **Claim uniquely:** Persist a tenant-scoped key and payload fingerprint under a unique constraint.

3. **Commit local effect:** Create order and idempotent result in one local transaction; handle concurrent in-progress requests explicitly.

4. **Replay or reconcile:** Return the stored result. Remote payment requires its own stable provider key and outcome reconciliation.

### Failure and trade-offs

Reject reuse with a different payload. Define key retention. A local transaction cannot atomically commit a remote card charge.

### Check your understanding

What if identical keys arrive simultaneously at two API instances?

## 242. What are horizontal scaling, partitioning and sharding?

### Scale workers versus divide data

More cashiers can share one order book; sharding gives different cashiers different books.

### What it means

Horizontal scaling adds service instances. Partitioning splits a dataset. Sharding puts partitions on independently operated database nodes. Replication copies the same data. More API instances do not automatically increase database write capacity.

### Worked real-world example

Partition chat messages by conversation ID so one conversation can be read without querying every shard.

![Scale workers versus divide data](system-design/diagrams/topic-242.svg)

### Follow the flow

1. **Scale stateless APIs:** A load balancer sends requests to multiple instances; persistent state remains external.

2. **Choose partition key:** Conversation ID keeps typical message queries within one partition.

3. **Route ownership:** A routing map or hash identifies the shard owning that conversation.

4. **Rebalance carefully:** Move partitions with explicit ownership/version rules; monitor hot conversations.

### Failure and trade-offs

A celebrity group can overload a shard. Cross-shard transactions, global ordering and migrations add complexity.

### Check your understanding

Why can sharding by country leave one database overloaded?
