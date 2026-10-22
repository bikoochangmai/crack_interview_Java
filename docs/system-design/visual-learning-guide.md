# System design: understand one request at a time

System design means deciding **where work runs, where data lives, and what happens when part of the system fails**. Start with a familiar action: opening a product, buying the last item, or sending an offline friend a message. Every component should solve a specific problem in that journey.

These examples use real-world situations and illustrative numbers. They are not screenshots of actual production systems or claims about company internals. The portal diagrams and step buttons work locally without a remote drawing service.

## Start with a small system

A browser sends `POST /orders` to a Java application. The application checks identity, validates quantities, computes price and saves an order in a database. It returns an order ID. That is already a system design.

Add a cache when repeated reads are expensive. Add a queue when non-immediate work should survive temporary downstream failure. Add application instances when measured service capacity needs to grow. Each addition introduces its own failure modes.

## How to read the diagrams

- A box is a role or data store. One deployed product may implement multiple roles.
- An arrow is a labeled request or transfer of data, not necessarily a new server.
- Component diagrams omit most return responses to stay readable.
- Numbered diagrams explain a request path. Conditions such as cache hit/miss can skip later work; read the step text.
- A transaction boundary matters more than physical closeness on the page. Two boxes do not automatically share an atomic commit.
- The portal step buttons change the explanation locally. They are an educational walkthrough, not a connection to a live production system.

## Recommended learning order

1. [Foundations: requirements, requests, gateways, databases, caches, recovery, CAP, limits, idempotency and scaling](../system-design-foundations.md). Read questions 233–242 in order.
2. [Short links](../system-design-url-shortener.md): connect a simple database lookup to caching, uniqueness and traffic estimates.
3. [Messaging](../system-design-whatsapp-messaging.md): understand durable acceptance, offline delivery, ordering, group fan-out and encryption.
4. [Shopping and payments](../system-design-e-commerce-payments.md): practice last-item races, unknown payment results and outbox recovery.
5. [Ride hailing](../system-design-uber-ride-hailing.md): distinguish approximate location from authoritative assignment.
6. [Ten worked case studies](README.md): apply the same reasoning to video, notifications, RAG, tenant isolation, rate limits and analytics.

## Words used throughout the lessons

| Term | Plain meaning | Concrete example |
|---|---|---|
| Client / server | The caller and the service answering it | Phone requests an order from a Java API |
| API | The agreed request/response contract | POST /orders returns order ID and status |
| Stateless instance | A server that does not keep required user state only in its own memory | A retry can use another API instance |
| Durable | Survives the failures promised by the storage contract | A committed message is available after an API restart |
| Source of truth | The authority used for the business decision | Inventory DB decides whether the final unit can be reserved |
| Cache | Replaceable copy that speeds reads | Product description in Redis |
| Queue / broker | Holds or transports work/events until consumers process them | Email jobs waiting for workers |
| Worker | A process doing background work | A payment worker handles a queued payment request |
| Synchronous / asynchronous | Wait for the result now / continue through later processing | Read stock now; send confirmation email later |
| Transaction | All-or-nothing local changes under a database’s isolation rules | Stock reservation and pending order commit together |
| Race condition | Concurrent actions overlap in a way that breaks a rule | Two buyers both read one remaining unit |
| Idempotency | Retrying one operation does not repeat its intended effect | One order despite a lost response and retry |
| At least once | Work may be delivered again until acknowledged | A worker must tolerate the same event twice |
| Outbox | Event intent stored in the business transaction | Confirmed order and fulfillment event commit together |
| Saga / compensation | Recorded multi-step workflow / business action to undo an effect | Refund an already charged payment |
| Partition / shard | A data subset / independently operated node holding subsets | Messages routed by conversation ID |
| Replica | Another copy of the same data | Database copy used for suitable failover/read workloads |
| Consistency | The promised relationship between concurrent writes and later reads | Does a read see an already completed reservation? |
| Availability | Ability to serve requests under a defined failure model | A surviving instance continues serving after one fails |
| QPS / throughput | Requests per second / completed work per unit time | 60,000 requests/minute is 1,000 requests/second |
| Latency / p95 | Time one operation takes / threshold 95% finish within | p95 200 ms means about 5% take longer |
| Backpressure | Tell upstream there is insufficient processing capacity | Reject excess work instead of growing an unbounded queue |
| TTL | Expiry lifetime | A cached description expires after its configured duration |
| RTO / RPO | Recovery time target / acceptable committed-data loss window | Recover in 30 minutes with at most five minutes of loss |
| Event time / processing time | When the event happened / when it was processed | Yesterday’s offline order arrives today |
| ACL / tenant | Access rules / customer organization | Company A cannot retrieve Company B’s policy chunks |
| Encryption / TLS / E2EE | Protect bytes / connection encryption / content keys at endpoints | The chat server routes ciphertext it cannot decrypt |

## Practice with one complete example

**Situation:** the last mug is available and two buyers click Buy.

1. Each buyer sends a distinct purchase operation with a stable retry key.
2. Each request tries a conditional stock update in a transaction. One can reserve the last unit; the other gets sold out.
3. The winner commits pending order, reservation and payment-request outbox together.
4. A worker requests payment using a stable provider key outside that database transaction.
5. A timeout leaves payment unknown. Verify or reconcile its outcome before charging again or releasing inventory.
6. A guarded successful order transition schedules fulfillment. Duplicate events do not create a second shipment.

![Checkout component example](diagrams/e-commerce-checkout.svg)

Ask yourself: **which fact is authoritative, what can be stale, what can retry, and what survives a crash?** If you can answer those for every arrow, you understand more than a memorized diagram.

## Further reading for precise guarantees

- [PostgreSQL row locking and concurrency](https://www.postgresql.org/docs/18/explicit-locking.html)
- [Amazon Builders’ Library: making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)
- [Cassandra replication and quorum behavior](https://cassandra.apache.org/doc/stable/cassandra/architecture/dynamo)

The lessons are original teaching examples; consult the chosen system’s documentation before relying on a particular isolation, ordering or delivery guarantee.
