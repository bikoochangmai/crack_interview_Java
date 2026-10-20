# Crack Interview Java — Senior Full-Stack & Solution Architect

A GitHub Pages revision portal and Markdown knowledge base with **232 searchable questions** across Java 8–21, concurrency, Spring Boot, SQL/PostgreSQL, Angular, microservices, Azure and Kafka.

## Start here

- [Interactive interview portal](index.html) — works on GitHub Pages (loads `data/questions.json`).
- [7-day revision plan](docs/seven-day-revision-plan.md)
- [Senior Java concurrency](docs/java-concurrency-senior.md)
- [Kafka — 65 senior/staff questions](docs/apache-kafka-senior-staff.md)
- [Source and publication notes](docs/source-notes.md)

## Concept-wise Markdown guides

| Topic | Questions | Guide |
|---|---:|---|
| Core Java — OOP & Language | 15 | [Read](docs/core-java-oop-language.md) |
| Java Collections, Streams & Java 8 | 15 | [Read](docs/java-collections-streams-java-8.md) |
| Java 9–21 Evolution | 14 | [Read](docs/java-9-21-evolution.md) |
| Concurrency, JVM & Performance | 14 | [Read](docs/concurrency-jvm-performance.md) |
| Spring Core & Spring Boot | 20 | [Read](docs/spring-core-spring-boot.md) |
| REST, Security & Microservices | 18 | [Read](docs/rest-security-microservices.md) |
| SQL, PostgreSQL & Database Design | 25 | [Read](docs/sql-postgresql-database-design.md) |
| Angular & TypeScript | 20 | [Read](docs/angular-typescript.md) |
| Architecture, Azure & Leadership | 16 | [Read](docs/architecture-azure-leadership.md) |
| Behavioral & Project Deep Dives | 10 | [Read](docs/behavioral-project-deep-dives.md) |

## Publish to GitHub Pages

1. Place the contents of this repository at the root of your GitHub repository.
2. Open **Settings → Pages → Deploy from a branch → main → /(root)**.
3. Your site will appear at `https://USERNAME.github.io/crack_interview_Java/` if the repository is named `crack_interview_Java`.
4. Open the site to use search, filters, question checklists, and CSV export.

GitHub Pages publishes static content; no backend or Docker is needed. A local `file://` page may block loading JSON. To test locally:

```powershell
Set-Location "D:\workspace\Learnings\JAVA_QUESTIONS\crack_interview_Java"
py -m http.server 8000
```

Then open `http://localhost:8000/`.

## Contribute through pull requests

1. Fork the repository (or create a feature branch if you have write access).
2. Add/edit a question in `data/questions.json`, preserving existing IDs.
3. Optionally update the corresponding Markdown topic guide.
4. Open a pull request; the JSON validation workflow checks the schema and duplicate IDs.
5. After review and merge, GitHub Pages republishes automatically.

See [CONTRIBUTING.md](CONTRIBUTING.md). Note: Markdown guides are snapshots and **do not automatically regenerate** when JSON is edited; update them in the same PR.

## Security and publication

The site is public when published through public GitHub Pages. See [source notes](docs/source-notes.md) for PDF attribution, confidential-material restrictions and review requirements. Personal progress is stored only in each user's browser.
