# Design Patterns — Java & Distributed Systems

8 senior-level interview questions with architectural trade-offs, practical examples and follow-ups.

> Answers are original study material. Product capabilities and cloud SKUs should be checked against current vendor documentation before deployment.

## 266. Explain SOLID principles with Spring Boot examples.

**Concept:** SOLID helps change one concern without forcing unrelated changes.

**How and why:** SRP: separate pricing from persistence; OCP: new PaymentGateway; LSP: honor contracts; ISP: narrow interfaces; DIP: inject interfaces.

**Real-world example:** Add UPI payment provider without changing checkout workflow.

**Trade-offs / failure modes:** Too many abstractions can obscure a simple design.

**Interview follow-up:** When is inheritance an LSP violation?

## 267. Factory Method vs Abstract Factory vs Builder?

**Concept:** Creation patterns hide construction complexity or families of compatible objects.

**How and why:** Factory Method delegates creation; Abstract Factory creates related families; Builder assembles optional/complex fields.

**Real-world example:** Payment provider factory selects gateway; builder constructs immutable audit report.

**Trade-offs / failure modes:** Do not use factories for every trivial constructor.

**Interview follow-up:** How does Spring DI replace some factory use cases?

## 268. Strategy pattern with a Java payment example.

**Concept:** Strategy swaps an algorithm behind a stable interface at runtime.

**How and why:** Define PricingStrategy or PaymentGateway interface; inject implementation; choose via registry or policy.

**Real-world example:** Checkout uses different discount strategy for retail and wholesale customers.

**Trade-offs / failure modes:** Keep strategy selection separate from business operation.

**Interview follow-up:** Strategy vs State pattern?

## 269. Decorator, Adapter and Facade patterns in integrations.

**Concept:** They solve different integration problems: extend behavior, translate interfaces, simplify subsystem APIs.

**How and why:** Decorator wraps PaymentGateway for metrics; Adapter maps legacy SOAP to interface; Facade exposes unified document workflow.

**Real-world example:** Migrate Documentum to Alfresco behind a content repository adapter.

**Trade-offs / failure modes:** Over-wrapping can complicate debugging and error semantics.

**Interview follow-up:** Where does Spring AOP fit?

## 270. Observer vs Pub/Sub vs Mediator?

**Concept:** They decouple senders and receivers at different scales.

**How and why:** Observer notifies in-process listeners; Pub/Sub routes events via broker; Mediator coordinates interactions among objects.

**Real-world example:** OrderCreated Kafka event fans out to email and analytics services.

**Trade-offs / failure modes:** Events do not guarantee exactly-once side effects.

**Interview follow-up:** When would a direct synchronous call be better?

## 271. Singleton pattern and Spring singleton scope?

**Concept:** Singleton controls instance count, while Spring singleton is one instance per bean definition per container.

**How and why:** Prefer Spring-managed stateless services; avoid mutable shared state; enum singleton for JVM-level utility where justified.

**Real-world example:** Stateless Spring OrderService safely serves concurrent requests.

**Trade-offs / failure modes:** Singleton bean does not mean globally unique across application replicas.

**Interview follow-up:** Why is mutable state in singleton service risky?

## 272. Explain Repository, Unit of Work and Specification patterns.

**Concept:** They isolate persistence and compose queries while keeping domain intent readable.

**How and why:** Repository abstracts aggregate access; Unit of Work tracks transaction changes; Specification composes predicates.

**Real-world example:** Spring Data repository queries audit records by status, owner and date.

**Trade-offs / failure modes:** Avoid leaking ORM entities into external API contracts.

**Interview follow-up:** What is the N+1 query problem?

## 273. Explain Strangler Fig pattern for legacy modernization.

**Concept:** Gradual replacement reduces big-bang migration risk.

**How and why:** Route selected capabilities to new service behind proxy; migrate data incrementally; compare results; retire old paths.

**Real-world example:** Move legacy Documentum document retrieval to Alfresco service behind same API.

**Trade-offs / failure modes:** Dual writes need careful reconciliation and rollback plans.

**Interview follow-up:** How do you validate data parity?
