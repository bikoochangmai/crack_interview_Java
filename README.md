# Crack Interview Java — Complete Learning Roadmap

**Live portal:** https://bikoochangmai.github.io/crack_interview_Java/

A free, static GitHub Pages preparation portal for Java Full-Stack / Senior Engineer / Solution Architect interviews. **314 interview questions + 20 Java coding exercises = 334 trackable items**. No backend or login needed.


## Foundational answer expansion (V5)

- [124 production walkthroughs and Java 21 examples](docs/foundational-124-production-walkthroughs.md)
- [Runnable Java 21 examples](examples/java21/)
- All 124 formerly guided-study entries now include a specific production scenario, failure mode, architecture flow and interview follow-ups. **21** have standalone Java 21 examples; the rest remain clearly labeled as awaiting standalone code.

## Advanced architecture, AI and system design expansion

This version adds **82 original senior-level interview questions** across **13 new topic categories**, **10 system design case studies**, and a detailed AI ecosystem guide. Existing 232 interview questions and 20 Java LeetCode exercises are retained.

| Advanced topic | Markdown study guide |
|---|---|
| System Design — Foundations (10 questions) | [System Design — Foundations](docs/system-design-foundations.md) |
| System Design — URL Shortener (3 questions) | [System Design — URL Shortener](docs/system-design-url-shortener.md) |
| System Design — WhatsApp & Messaging (4 questions) | [System Design — WhatsApp & Messaging](docs/system-design-whatsapp-messaging.md) |
| System Design — E-commerce & Payments (5 questions) | [System Design — E-commerce & Payments](docs/system-design-e-commerce-payments.md) |
| System Design — Uber / Ride Hailing (4 questions) | [System Design — Uber / Ride Hailing](docs/system-design-uber-ride-hailing.md) |
| Microservices — Architecture & Patterns (7 questions) | [Microservices — Architecture & Patterns](docs/microservices-architecture-patterns.md) |
| Design Patterns — Java & Distributed Systems (8 questions) | [Design Patterns — Java & Distributed Systems](docs/design-patterns-java-distributed-systems.md) |
| Azure — Services & Architecture (10 questions) | [Azure — Services & Architecture](docs/azure-services-architecture.md) |
| AI Engineering — Foundations & Models (6 questions) | [AI Engineering — Foundations & Models](docs/ai-engineering-foundations-models.md) |
| AI Engineering — RAG & Vector Search (8 questions) | [AI Engineering — RAG & Vector Search](docs/ai-engineering-rag-vector-search.md) |
| AI Engineering — Agents, MCP & Orchestration (7 questions) | [AI Engineering — Agents, MCP & Orchestration](docs/ai-engineering-agents-mcp-orchestration.md) |
| AI Engineering — Security, Observability & Operations (5 questions) | [AI Engineering — Security, Observability & Operations](docs/ai-engineering-security-observability-operations.md) |
| Architecture — Senior / Staff Leadership (5 questions) | [Architecture — Senior / Staff Leadership](docs/architecture-senior-staff-leadership.md) |

- [Preparation requirements and four-week roadmap](docs/preparation-roadmap.md)
- [AI ecosystem concepts and reference tools](docs/ai-ecosystem-guide.md)
- [System design case studies](docs/system-design/README.md)

### Answer depth and completion

Questions support concept, why/how, real-world example, trade-offs, follow-up and optional Java code. The original question bank retains concise revision cues for items not yet individually expanded; the portal labels these honestly rather than pretending they are full explanations. The first four core Java questions and new advanced questions are expanded. **Section checkmarks indicate personal completion, not a graded assessment.** Progress stays in the browser.

### AI tools in the supplied reference image

The AI guide groups OpenAI, Claude, Gemini, Llama, Ollama, vLLM, LangGraph, LangChain, LlamaIndex, MCP servers, vector databases, evaluation and security tools by use case. Product capabilities may change.

## What you need to prepare

| Preparation area | Required knowledge | Guide |
|---|---|---|
| Core Java | OOP, SOLID, exceptions, equality | [Core Java](docs/core-java-oop-language.md) |
| Collections & Java 8 | HashMap, streams, Optional, lambdas | [Collections](docs/java-collections-streams-java-8.md) |
| Java 9–21 | Records, sealed types, virtual threads | [Java evolution](docs/java-9-21-evolution.md) |
| Concurrency & JVM | JMM, CAS, locks, thread pools, GC | [Concurrency](docs/java-concurrency-senior.md) |
| Spring Boot | DI, bean scopes, transactions, testing | [Spring](docs/spring-core-spring-boot.md) |
| REST & security | HTTP, OAuth2/OIDC, JWT, resilience | [REST](docs/rest-security-microservices.md) |
| Databases | PostgreSQL, ACID, MVCC, indexes, SQL | [SQL](docs/sql-postgresql-database-design.md) |
| Angular | RxJS, routing, change detection, TypeScript | [Angular](docs/angular-typescript.md) |
| Kafka | Consumer groups, offsets, transactions, KRaft | [Kafka](docs/apache-kafka-senior-staff.md) |
| System design & Azure | HLD/LLD, scaling, deployment, reliability | [Architecture](docs/architecture-azure-leadership.md) |
| Leadership & projects | STAR stories, incidents, migration decisions | [Behavioral](docs/behavioral-project-deep-dives.md) |
| DSA / LeetCode | Arrays, HashMap, sliding window, stacks, graphs, DP | [20 Java solutions](docs/leetcode/README.md) |

## Portal features

- **Left navigation tree:** grouped sections with counts; click a section to filter questions.
- **Green completion tick:** tick individual questions or the section checkbox; a section shows ✓ when all its items are complete. Partially completed sections have a mixed-state checkbox.
- **Detailed learning:** all questions have an answer cue; many questions have separately curated production scenarios; remaining questions are explicitly labeled as awaiting an example.
- **Java DSA practice:** 20 worked problems, sample input/output, approach, time/space complexity, Java solutions and matching Markdown guides.
- **Progress tracking:** completion marks and percentage saved in browser localStorage; old question checkmarks from the previous portal are migrated. Progress is device/browser-specific, not synced across users.
- **Search, filters, expand/collapse, CSV export and reset** for personal revision.

## Suggested preparation order

1. **Days 1–2:** Java language, collections, streams, concurrency and JVM.
2. **Days 3–4:** Spring Boot, microservices, SQL/PostgreSQL and security.
3. **Day 5:** Kafka, event-driven patterns and delivery guarantees.
4. **Day 6:** Angular, Azure, system design, architecture trade-offs.
5. **Day 7:** Mock interviews, leadership stories and Java coding practice.

Use the [seven-day plan](docs/seven-day-revision-plan.md) for more detail. Aim to explain *what it is*, *when to use it*, *trade-offs* and *what fails in production*.

## Folder layout

```text
crack_interview_Java/
├── index.html                 # GitHub Pages UI
├── css/style.css              # Responsive layout / left navigation
├── js/app.js                  # Filters, tree, local progress, Java code display
├── data/
│   ├── questions.json         # Interview questions + selected real examples
│   └── leetcode.json          # Java coding problems / solutions
├── docs/
│   ├── leetcode/              # Individual Java problem Markdown files
│   ├── real-world-examples.md
│   └── *.md                   # Topic notes, Kafka, concurrency, revision plan
├── scripts/validate_questions.py
├── .github/workflows/         # Content validation on PRs
├── CONTRIBUTING.md
└── README.md
```

## Run locally on Windows PowerShell

```powershell
Set-Location "D:\workspace\Learnings\JAVA_QUESTIONS\crack_interview_Java"
py -m http.server 8000
```

Open http://localhost:8000/ . Avoid double-clicking `index.html`: browser security may block loading local JSON files.

## Publish on GitHub Pages

Commit files to `main`. In GitHub, open **Settings → Pages → Deploy from a branch → main → /(root)**. Check the live URL above after deployment.

## How to add questions or Java problems

See [CONTRIBUTING.md](CONTRIBUTING.md). Update `data/questions.json` for interview questions, or `data/leetcode.json` **and** the matching `docs/leetcode/*.md` for Java coding exercises. Open a pull request for review. The Markdown guides do not regenerate automatically.

## Data, licensing and privacy

All examples and coding solutions in this upgrade are independently authored. Do not publish confidential PDFs or proprietary text without permission. The browser stores progress locally; no progress is uploaded to GitHub. Java methods are interview reference solutions; test them against relevant constraints before using in production.


## Detailed foundational interview guides (V4)

These Markdown files mirror the question bank and are linked for offline revision. Expanded entries have concept, why, production scenario, trade-offs, follow-ups and code where appropriate. Guided-study entries are explicitly marked as editorial work in progress.

- [Core Java interview answers](docs/core-java-detailed.md)
- [Java Collections interview answers](docs/collections-java8-detailed.md)
- [Java 9 interview answers](docs/java21-detailed.md)
- [Concurrency interview answers](docs/concurrency-detailed.md)
- [Spring Core interview answers](docs/spring-boot-detailed.md)
- [REST interview answers](docs/rest-microservices-detailed.md)
- [SQL interview answers](docs/postgresql-detailed.md)
- [Angular interview answers](docs/angular-detailed.md)
- [Kafka interview answers](docs/kafka-detailed.md)

**Progress:** Studied and Mastered ticks remain local to your browser; V4 preserves existing question IDs and progress keys.

## V6: runnable labs for all remaining 103 questions

See [103 focused runnable labs](docs/v6-103-runnable-labs.md). Includes 73 Java 21, 16 PostgreSQL and 14 TypeScript examples. Framework/cloud examples are explicitly labeled as conceptual models, not full-stack integration projects.


### Compact sidebar and individual progress (V6.1)
The learning tree uses a compact 185–220 px column and **Hide topics / Show topics** control. Sidebar preference is saved in the current browser profile. Studied and Mastered progress remains in browser `localStorage`, keyed per question; it is **not shared between different visitors' browsers**, and it is **not synced across devices**. Users sharing the same browser profile share progress. Export CSV for backup; true account-based syncing would require authentication and a backend.
