# Seven-Day Senior Java / Architect Revision Plan

Aim for **5–6 hours daily**. Answer aloud and connect each concept to a production scenario.

| Day | Focus | Output |
|---|---|---|
| 1 | Core Java, collections, Java 8–21 | HashMap, Streams, records, sealed types |
| 2 | Concurrency and Java 21 | JMM, CAS, locks, virtual threads, bounded buffer |
| 3 | Spring Boot and Security | REST, transactions, OAuth2/OIDC, idempotency |
| 4 | SQL/PostgreSQL | ACID, MVCC, locks, indexes, query plans |
| 5 | Kafka | Partitions, groups, offsets, retry/DLT, outbox |
| 6 | Angular, Azure, system design | RxJS, performance, cloud trade-offs, HLD/LLD |
| 7 | Mock interviews | Two coding rounds, one architecture exercise, behavioral STAR |

## Per-question answer structure

1. Define the concept accurately.
2. Show a concise Java/SQL/TypeScript example.
3. Explain complexity, correctness, or consistency properties.
4. Identify one production failure mode and mitigation.
5. State when you would *not* use the approach.

## Practice scenarios

- Build an idempotent order-processing consumer with PostgreSQL and Kafka.
- Design a document ingestion pipeline with Spring Boot, object storage, vector retrieval and approval workflow.
- Investigate Spring Boot latency after switching to Java 21 virtual threads.
- Optimize a PostgreSQL query with joins, composite indexes and EXPLAIN ANALYZE.
- Explain Angular `switchMap` vs `mergeMap` for typeahead and writes.
