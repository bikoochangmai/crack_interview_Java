# Version 6 — 103 executable foundational labs

This release adds **103 individually addressable, runnable focused labs** to the 103 V5 questions previously labeled `code pending`. The labs demonstrate an invariant or a small behavior; **they are not complete Spring Boot, Angular, Azure, OAuth or distributed-system implementations**.

## Requirements

- **Java 21**: 73 Java files, JDK 21 required (virtual threads, record patterns, etc.).
- **PostgreSQL / psql**: 16 transaction-wrapped SQL examples. Set `DATABASE_URL` to a disposable test database; examples use temporary tables and `ROLLBACK`.
- **Node 22 + TypeScript compiler (`tsc`)**: 14 standalone TypeScript examples. These are pure TypeScript, **not Angular TestBed apps**.

## Quick start

```powershell
cd "D:\workspace\Learnings\JAVA_QUESTIONS\crack_interview_Java"
py .\scripts\validate_questions.py
py .\scripts\validate_leetcode.py
py .\scripts\validate_v6_labs.py
```

## All 103 labs

| # | Topic | Runtime | File |
|---:|---|---|---|
| 15 | Dependency injection vs service locator? | Java 21 | `examples/v6/java21/Lab015.java` |
| 23 | Method reference types? | Java 21 | `examples/v6/java21/Lab023.java` |
| 28 | Default/static methods in interfaces? | Java 21 | `examples/v6/java21/Lab028.java` |
| 30 | Parallel streams: when avoid? | Java 21 | `examples/v6/java21/Lab030.java` |
| 31 | Java 9 key changes? | Java 21 | `examples/v6/java21/Lab031.java` |
| 32 | Java 10 key changes? | Java 21 | `examples/v6/java21/Lab032.java` |
| 33 | Java 11 key changes? | Java 21 | `examples/v6/java21/Lab033.java` |
| 35 | Java 15 text blocks? | Java 21 | `examples/v6/java21/Lab035.java` |
| 40 | Java 21 record patterns? | Java 21 | `examples/v6/java21/Lab040.java` |
| 42 | Java 21 preview vs finalized features? | Java 21 | `examples/v6/java21/Lab042.java` |
| 43 | Platform vs virtual threads? | Java 21 | `examples/v6/java21/Lab043.java` |
| 44 | How migrate Java 8 to 21? | Java 21 | `examples/v6/java21/Lab044.java` |
| 48 | Race condition vs deadlock vs starvation? | Java 21 | `examples/v6/java21/Lab048.java` |
| 55 | Heap vs stack vs metaspace? | Java 21 | `examples/v6/java21/Lab055.java` |
| 56 | GC concepts: G1 vs ZGC? | Java 21 | `examples/v6/java21/Lab056.java` |
| 57 | How diagnose memory leak? | Java 21 | `examples/v6/java21/Lab057.java` |
| 58 | How diagnose high CPU/slow requests? | Java 21 | `examples/v6/java21/Lab058.java` |
| 59 | IoC vs DI? | Java 21 | `examples/v6/java21/Lab059.java` |
| 60 | @Component vs @Service vs @Repository? | Java 21 | `examples/v6/java21/Lab060.java` |
| 62 | @RequestParam vs @PathVariable vs @RequestBody? | Java 21 | `examples/v6/java21/Lab062.java` |
| 63 | Bean scopes and lifecycle? | Java 21 | `examples/v6/java21/Lab063.java` |
| 64 | @Bean vs @Component? | Java 21 | `examples/v6/java21/Lab064.java` |
| 65 | Constructor vs field injection? | Java 21 | `examples/v6/java21/Lab065.java` |
| 67 | How does auto-configuration work? | Java 21 | `examples/v6/java21/Lab067.java` |
| 68 | Profiles and external configuration? | Java 21 | `examples/v6/java21/Lab068.java` |
| 69 | @Transactional behavior and proxy limitations? | Java 21 | `examples/v6/java21/Lab069.java` |
| 70 | Propagation REQUIRED vs REQUIRES_NEW? | Java 21 | `examples/v6/java21/Lab070.java` |
| 71 | Isolation levels in Spring transactions? | Java 21 | `examples/v6/java21/Lab071.java` |
| 72 | Spring MVC request lifecycle? | Java 21 | `examples/v6/java21/Lab072.java` |
| 74 | Validation with @Valid? | Java 21 | `examples/v6/java21/Lab074.java` |
| 75 | Spring Boot Actuator? | Java 21 | `examples/v6/java21/Lab075.java` |
| 76 | Spring Boot testing layers? | Java 21 | `examples/v6/java21/Lab076.java` |
| 77 | WebClient vs RestClient vs RestTemplate? | Java 21 | `examples/v6/java21/Lab077.java` |
| 78 | Spring Boot startup troubleshooting? | Java 21 | `examples/v6/java21/Lab078.java` |
| 79 | REST principles? | Java 21 | `examples/v6/java21/Lab079.java` |
| 82 | HTTP status codes 200/201/202/204/400/401/403/404/409/429? | Java 21 | `examples/v6/java21/Lab082.java` |
| 83 | API versioning and pagination? | Java 21 | `examples/v6/java21/Lab083.java` |
| 84 | Authentication vs authorization? | Java 21 | `examples/v6/java21/Lab084.java` |
| 85 | JWT vs session vs OIDC? | Java 21 | `examples/v6/java21/Lab085.java` |
| 86 | OAuth2 authorization code + PKCE? | Java 21 | `examples/v6/java21/Lab086.java` |
| 87 | CORS vs CSRF? | Java 21 | `examples/v6/java21/Lab087.java` |
| 88 | RBAC vs ABAC? | Java 21 | `examples/v6/java21/Lab088.java` |
| 89 | Monolith vs microservices trade-offs? | Java 21 | `examples/v6/java21/Lab089.java` |
| 90 | Service discovery and API gateway? | Java 21 | `examples/v6/java21/Lab090.java` |
| 92 | Saga vs distributed transaction? | Java 21 | `examples/v6/java21/Lab092.java` |
| 94 | Eventual consistency and CQRS? | Java 21 | `examples/v6/java21/Lab094.java` |
| 95 | Observability in microservices? | Java 21 | `examples/v6/java21/Lab095.java` |
| 96 | How secure service-to-service calls? | Java 21 | `examples/v6/java21/Lab096.java` |
| 98 | Primary key vs unique key vs foreign key? | PostgreSQL | `examples/v6/postgresql/lab_098.sql` |
| 99 | INNER vs LEFT vs FULL OUTER JOIN? | PostgreSQL | `examples/v6/postgresql/lab_099.sql` |
| 100 | WHERE vs HAVING? | PostgreSQL | `examples/v6/postgresql/lab_100.sql` |
| 101 | GROUP BY and aggregate functions? | PostgreSQL | `examples/v6/postgresql/lab_101.sql` |
| 104 | Find duplicate records? | PostgreSQL | `examples/v6/postgresql/lab_104.sql` |
| 105 | CTE vs subquery? | PostgreSQL | `examples/v6/postgresql/lab_105.sql` |
| 106 | UNION vs UNION ALL? | PostgreSQL | `examples/v6/postgresql/lab_106.sql` |
| 107 | DELETE vs TRUNCATE vs DROP? | PostgreSQL | `examples/v6/postgresql/lab_107.sql` |
| 109 | B-tree vs GIN vs GiST indexes? | PostgreSQL | `examples/v6/postgresql/lab_109.sql` |
| 111 | Transactions and isolation anomalies? | PostgreSQL | `examples/v6/postgresql/lab_111.sql` |
| 114 | Deadlocks in databases? | PostgreSQL | `examples/v6/postgresql/lab_114.sql` |
| 115 | Normalization 1NF/2NF/3NF vs denormalization? | PostgreSQL | `examples/v6/postgresql/lab_115.sql` |
| 117 | Partitioning vs sharding vs replication? | PostgreSQL | `examples/v6/postgresql/lab_117.sql` |
| 118 | Connection pooling and N+1 query issue? | PostgreSQL | `examples/v6/postgresql/lab_118.sql` |
| 119 | JSONB vs relational columns? | PostgreSQL | `examples/v6/postgresql/lab_119.sql` |
| 121 | Design schema for audit findings/approvals? | PostgreSQL | `examples/v6/postgresql/lab_121.sql` |
| 122 | Angular component lifecycle? | TypeScript | `examples/v6/typescript/lab_122.ts` |
| 123 | Standalone components vs NgModules? | TypeScript | `examples/v6/typescript/lab_123.ts` |
| 126 | Subject vs BehaviorSubject vs ReplaySubject? | TypeScript | `examples/v6/typescript/lab_126.ts` |
| 128 | Async pipe and subscription cleanup? | TypeScript | `examples/v6/typescript/lab_128.ts` |
| 130 | Custom validators and async validators? | TypeScript | `examples/v6/typescript/lab_130.ts` |
| 131 | Route guards and lazy loading? | TypeScript | `examples/v6/typescript/lab_131.ts` |
| 133 | Angular authentication and token storage? | TypeScript | `examples/v6/typescript/lab_133.ts` |
| 134 | Content projection vs ViewChild? | TypeScript | `examples/v6/typescript/lab_134.ts` |
| 135 | trackBy / @for track and rendering? | TypeScript | `examples/v6/typescript/lab_135.ts` |
| 136 | Pure vs impure pipes? | TypeScript | `examples/v6/typescript/lab_136.ts` |
| 137 | TypeScript interface vs type alias? | TypeScript | `examples/v6/typescript/lab_137.ts` |
| 138 | Generics, union and discriminated unions? | TypeScript | `examples/v6/typescript/lab_138.ts` |
| 140 | State management service vs NgRx? | TypeScript | `examples/v6/typescript/lab_140.ts` |
| 141 | Unit tests and component integration tests? | TypeScript | `examples/v6/typescript/lab_141.ts` |
| 142 | HLD vs LLD? | Java 21 | `examples/v6/java21/Lab142.java` |
| 143 | CAP theorem and consistency models? | Java 21 | `examples/v6/java21/Lab143.java` |
| 144 | Horizontal vs vertical scaling? | Java 21 | `examples/v6/java21/Lab144.java` |
| 145 | Load balancer, CDN and cache? | Java 21 | `examples/v6/java21/Lab145.java` |
| 146 | Azure App Service vs VM vs AKS? | Java 21 | `examples/v6/java21/Lab146.java` |
| 147 | Azure Service Bus vs Event Hubs? | Java 21 | `examples/v6/java21/Lab147.java` |
| 148 | Azure Blob vs PostgreSQL storage? | Java 21 | `examples/v6/java21/Lab148.java` |
| 149 | Design multi-tenant isolation? | Java 21 | `examples/v6/java21/Lab149.java` |
| 150 | RTO vs RPO and disaster recovery? | Java 21 | `examples/v6/java21/Lab150.java` |
| 151 | Zero-downtime deployments? | Java 21 | `examples/v6/java21/Lab151.java` |
| 153 | Design URL shortener? | Java 21 | `examples/v6/java21/Lab153.java` |
| 154 | Design document ingestion + RAG? | Java 21 | `examples/v6/java21/Lab154.java` |
| 155 | Design human-in-loop approvals? | Java 21 | `examples/v6/java21/Lab155.java` |
| 156 | How handle incidents and RCA? | Java 21 | `examples/v6/java21/Lab156.java` |
| 157 | How defend architecture trade-offs? | Java 21 | `examples/v6/java21/Lab157.java` |
| 158 | Describe a production incident you led. | Java 21 | `examples/v6/java21/Lab158.java` |
| 159 | Explain a difficult architecture decision. | Java 21 | `examples/v6/java21/Lab159.java` |
| 160 | How modernize a legacy Java application? | Java 21 | `examples/v6/java21/Lab160.java` |
| 161 | How migrate Documentum to Alfresco? | Java 21 | `examples/v6/java21/Lab161.java` |
| 162 | How integrate Elasticsearch with a content platform? | Java 21 | `examples/v6/java21/Lab162.java` |
| 163 | How ensure RAG faithfulness? | Java 21 | `examples/v6/java21/Lab163.java` |
| 164 | How mentor engineers and manage code quality? | Java 21 | `examples/v6/java21/Lab164.java` |
| 165 | How estimate system capacity? | Java 21 | `examples/v6/java21/Lab165.java` |
| 166 | How resolve disagreements? | Java 21 | `examples/v6/java21/Lab166.java` |
| 167 | Explain your compliance auditing architecture. | Java 21 | `examples/v6/java21/Lab167.java` |

## Interview workflow

1. Explain the concept and why the chosen technique is appropriate.
2. Run the small lab and explain its invariant or output.
3. Name at least one production failure mode and a test or metric that detects it.
4. For Spring Boot, Azure, Angular, OAuth and distributed systems, describe the extra framework/infrastructure work the lab omits.

## Safety and fidelity

- Java examples use JDK 21 standard APIs, avoiding downloads or external services.
- SQL uses `BEGIN` / `ROLLBACK` and temporary tables; use only a disposable database.
- TypeScript examples demonstrate language/state patterns, not real Angular component rendering.
- The original 314 question IDs and progress keys are unchanged.
