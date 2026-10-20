# Preparation Roadmap — Senior Java / Staff / Solution Architect

Use the green section tick only after you can explain the concept, its use cases and failure modes without notes. The website tracks completion locally in each browser.

| Area | Expected depth | Hands-on evidence |
|---|---|---|
| Java 8–21 & OOP | Language design, JMM, concurrency, GC, performance | Explain Java 7 vs 21 thread models; implement safe bounded queue |
| Spring Boot & Security | DI, transactions, Spring Security, OAuth2/OIDC | Build secure REST API with integration tests |
| Data | PostgreSQL MVCC, indexing, locking, partitioning | EXPLAIN ANALYZE slow query and fix indexes |
| Kafka & distributed systems | Partitioning, ordering, retries, outbox, sagas | Outbox publisher and idempotent consumer |
| Angular & TypeScript | RxJS, forms, signals, state, security | Admin dashboard with auth and cancellation |
| Design patterns | SOLID, Strategy, Adapter, Factory, Decorator, Strangler | Refactor legacy integration behind interface |
| System design | Requirements, capacity, APIs, consistency, reliability | ShortURL, WhatsApp, e-commerce, Uber, RAG HLD |
| Azure | App Service/VM/AKS, messaging, networking, data, security | Draw deployment with private endpoints and managed identity |
| AI engineering | LLM, RAG, embeddings, MCP, agents, evaluation, security | Tenant-safe cited RAG with human approval |
| LeetCode in Java | Arrays, maps, windows, graphs, heaps, DP | Explain brute force, optimal solution, complexity |
| Leadership | ADR, cost, migration, incident management | STAR stories with measurable results |

## Interview answer template

1. **What:** Define the mechanism precisely.
2. **Why:** What failure or constraint does it solve?
3. **How:** Explain implementation and data flow.
4. **Example:** Show Java code or a real production scenario.
5. **Trade-offs:** Discuss alternatives, failure modes, observability and cost.
6. **Follow-up:** Answer the next-level architectural question.

## Suggested four-week plan

- Week 1: Java, concurrency, Spring Boot, SQL; 2 Java coding problems/day.
- Week 2: Kafka, microservices, patterns, security; design ShortURL and e-commerce.
- Week 3: Azure, system design (WhatsApp, Uber), multi-tenancy, reliability; design AI RAG.
- Week 4: AI agents/MCP/evaluation, mock interviews, leadership, portfolio case studies.

## AI ecosystem reference

[Modern AI ecosystem concepts and tools](ai-ecosystem-guide.md) — categorized from the provided reference image, with usage examples and architecture.

## Detailed case studies

[System design case study index](system-design/README.md).
