# System Design — E-commerce & Payments

5 senior-level interview questions with architectural trade-offs, practical examples and follow-ups.

> Answers are original study material. Product capabilities and cloud SKUs should be checked against current vendor documentation before deployment.

## 250. Design an e-commerce platform from catalog to checkout.

**Concept:** Catalog, search, cart, inventory, orders and payments have different scaling and consistency needs.

**How and why:** Separate clear bounded contexts; product search index; cart cache/DB; reserve stock atomically; create order state machine; payment through PSP; emit events via outbox.

**Real-world example:** Flash sale creates 10,000 concurrent checkout attempts for 100 units.

**Trade-offs / failure modes:** Avoid distributed 2PC across all services; model compensation and business invariants.

**Interview follow-up:** How do you prevent overselling?

## 251. How do you prevent overselling during a flash sale?

**Concept:** Inventory must never become negative even under concurrency.

**How and why:** Use atomic conditional update WHERE available >= quantity, reservation TTL, and unique order idempotency keys; release stock on failure.

**Real-world example:** Two checkout requests race for the final item; exactly one reservation succeeds.

**Trade-offs / failure modes:** Redis counters alone are not durable source of truth without reconciliation.

**Interview follow-up:** How do you expire abandoned reservations?

## 252. How do you design a reliable checkout and payment workflow?

**Concept:** Payments are externally managed and cannot participate in one database transaction.

**How and why:** Create pending order, reserve inventory, initiate payment with idempotency key, verify signed webhook, transition state, and compensate on failure.

**Real-world example:** Payment succeeds but response times out; webhook later finalizes the order without double charge.

**Trade-offs / failure modes:** Out-of-order webhooks and retries require state-machine guards.

**Interview follow-up:** How do you reconcile PSP and local ledger?

## 253. What is the transactional outbox pattern?

**Concept:** Writing DB state and publishing an event separately can lose events.

**How and why:** Within one DB transaction write business row and outbox event; relay publishes with retry; consumers deduplicate.

**Real-world example:** Order insert and OrderCreated event stored atomically, then Kafka receives it.

**Trade-offs / failure modes:** At-least-once relay means consumers still need idempotency.

**Interview follow-up:** Compare outbox polling with CDC.

## 254. Design product search, filtering and recommendations.

**Concept:** Search requires full-text relevance and faceting beyond transactional joins.

**How and why:** Index product projection in Elasticsearch; update via outbox/CDC; add filters/facets; optionally embed descriptions for semantic similarity.

**Real-world example:** Search “lightweight running shoes” with size, price and brand facets.

**Trade-offs / failure modes:** Search results may be eventually consistent; checkout revalidates price and stock.

**Interview follow-up:** How do you handle zero-result queries?
