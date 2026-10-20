# REST, Security & Microservices — Interview Study Guide

18 questions. Java examples use Java 21 unless noted; Angular and SQL snippets are labeled by language.

> **Quality note:** Entries marked “Guided study” include the original answer cue and a production discussion exercise; they are not yet fully curated standalone explanations.

## #79 REST principles?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Resource orientation, stateless requests, uniform interface, cacheability. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "REST principles". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate rest principles with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---

## #80 HTTP GET/POST/PUT/PATCH/DELETE semantics?

**Priority:** High · **Status:** Expanded

### Concept
Idempotency means repeating the same logical request has the same externally visible effect as performing it once. POST is not automatically idempotent.

### Why / when
Use a unique idempotency key for payment creation and retries after network timeouts.

### Production example
A client retries checkout with Idempotency-Key; the server returns the previously stored result rather than charging twice.

### Code example
```java
// DB: UNIQUE(tenant_id, idempotency_key)
// In a transaction, look up or insert request result before charging.
```

### Trade-offs and failure modes
Key scope, expiry, concurrent requests and parameter mismatch must be defined; database uniqueness or locking is required.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #81 What is idempotency?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Repeating same operation has same intended effect; use keys for payment/order POST retries. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "What is idempotency". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate what is idempotency with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---

## #82 HTTP status codes 200/201/202/204/400/401/403/404/409/429?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Success, created, accepted, no content, bad request, unauthenticated, forbidden, not found, conflict, rate limit. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "HTTP status codes 200/201/202/204/400/401/403/404/409/429". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate http status codes 200/201/202/204/400/401/403/404/409/429 with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---

## #83 API versioning and pagination?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Compatibility strategy; cursor pagination for large changing datasets. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "API versioning and pagination". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate api versioning and pagination with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---

## #84 Authentication vs authorization?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Verify identity vs enforce allowed actions. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "Authentication vs authorization". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate authentication vs authorization with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---

## #85 JWT vs session vs OIDC?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
JWT token format; session state mechanism; OIDC authentication protocol. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "JWT vs session vs OIDC". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate jwt vs session vs oidc with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---

## #86 OAuth2 authorization code + PKCE?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Secure delegated sign-in flow for public clients. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "OAuth2 authorization code + PKCE". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate oauth2 authorization code + pkce with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---

## #87 CORS vs CSRF?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Browser cross-origin access policy vs forged authenticated requests. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "CORS vs CSRF". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate cors vs csrf with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---

## #88 RBAC vs ABAC?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Role-based permissions vs attribute/context policies. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "RBAC vs ABAC". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate rbac vs abac with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---

## #89 Monolith vs microservices trade-offs?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Deployment/team autonomy vs network, consistency and operational complexity. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "Monolith vs microservices trade-offs". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate monolith vs microservices trade-offs with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---

## #90 Service discovery and API gateway?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Find service instances and centralize edge routing/security. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "Service discovery and API gateway". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate service discovery and api gateway with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---

## #91 Circuit breaker, retry, timeout, bulkhead?

**Priority:** Medium · **Status:** Expanded

### Concept
Timeouts cap waiting, retries handle transient failures, circuit breakers stop repeatedly calling failing dependencies, and bulkheads isolate resource pools.

### Why / when
Apply these to external payment, shipping and identity APIs.

### Production example
When shipping API latency spikes, checkout times out quickly and uses a fallback shipping estimate rather than exhausting request threads.

### Code example
```java
// Resilience4j: configure TimeLimiter/CircuitBreaker/Retry per dependency
// Only retry operations proven safe or protected by idempotency keys.
```

### Trade-offs and failure modes
Retries on non-idempotent operations can duplicate charges; exponential backoff with jitter and budgets is safer than unbounded retries.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #92 Saga vs distributed transaction?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Compensating business steps vs coordinated atomic transactions. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "Saga vs distributed transaction". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate saga vs distributed transaction with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---

## #93 Outbox pattern and exactly-once claims?

**Priority:** Medium · **Status:** Expanded

### Concept
Transactional outbox writes business state and an event record in the same database transaction. A relay later publishes the event to Kafka.

### Why / when
Use it when an order DB update and Kafka publication must not diverge.

### Production example
Checkout inserts Order and OutboxEvent together; a relay publishes OrderPlaced; consumers deduplicate by event ID.

### Code example
```java
@Transactional
void placeOrder(Order order) {
    orders.save(order);
    outbox.save(new OutboxEvent(order.id(), "OrderPlaced"));
}
```

### Trade-offs and failure modes
Delivery is generally at least once, not magical end-to-end exactly once; outbox rows need monitoring and cleanup.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #94 Eventual consistency and CQRS?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Asynchronous convergence; separate read/write models when warranted. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "Eventual consistency and CQRS". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate eventual consistency and cqrs with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---

## #95 Observability in microservices?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Correlation IDs, metrics, logs, distributed traces, SLOs. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "Observability in microservices". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate observability in microservices with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---

## #96 How secure service-to-service calls?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
mTLS or workload identity/tokens, least privilege, rotation. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in service contracts and integration: choose the mechanism when its specific guarantees solve a real requirement in an e-commerce checkout API calling payment and inventory services. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an e-commerce checkout API calling payment and inventory services, identify a requirement involving "How secure service-to-service calls". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess duplicate retries, inconsistent state and unbounded downstream latency. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate how secure service-to-service calls with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an e-commerce checkout API calling payment and inventory services?

---
