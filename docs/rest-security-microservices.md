# REST, Security & Microservices

18 questions · Source: existing interview portal question bank.

> These are concise revision cues, not exhaustive explanations. Verify behavior against the version you use.

## 79. REST principles?

**Priority:** High

**Answer cue:** Resource orientation, stateless requests, uniform interface, cacheability.

**Practice:** Explain an example, a failure mode, and an alternative.

## 80. HTTP GET/POST/PUT/PATCH/DELETE semantics?

**Priority:** High

**Answer cue:** GET safe, PUT/DELETE idempotent by intended semantics, POST usually not; PATCH depends.

**Practice:** Explain an example, a failure mode, and an alternative.

## 81. What is idempotency?

**Priority:** High

**Answer cue:** Repeating same operation has same intended effect; use keys for payment/order POST retries.

**Practice:** Explain an example, a failure mode, and an alternative.

## 82. HTTP status codes 200/201/202/204/400/401/403/404/409/429?

**Priority:** High

**Answer cue:** Success, created, accepted, no content, bad request, unauthenticated, forbidden, not found, conflict, rate limit.

**Practice:** Explain an example, a failure mode, and an alternative.

## 83. API versioning and pagination?

**Priority:** High

**Answer cue:** Compatibility strategy; cursor pagination for large changing datasets.

**Practice:** Explain an example, a failure mode, and an alternative.

## 84. Authentication vs authorization?

**Priority:** High

**Answer cue:** Verify identity vs enforce allowed actions.

**Practice:** Explain an example, a failure mode, and an alternative.

## 85. JWT vs session vs OIDC?

**Priority:** High

**Answer cue:** JWT token format; session state mechanism; OIDC authentication protocol.

**Practice:** Explain an example, a failure mode, and an alternative.

## 86. OAuth2 authorization code + PKCE?

**Priority:** High

**Answer cue:** Secure delegated sign-in flow for public clients.

**Practice:** Explain an example, a failure mode, and an alternative.

## 87. CORS vs CSRF?

**Priority:** High

**Answer cue:** Browser cross-origin access policy vs forged authenticated requests.

**Practice:** Explain an example, a failure mode, and an alternative.

## 88. RBAC vs ABAC?

**Priority:** Medium

**Answer cue:** Role-based permissions vs attribute/context policies.

**Practice:** Explain an example, a failure mode, and an alternative.

## 89. Monolith vs microservices trade-offs?

**Priority:** Medium

**Answer cue:** Deployment/team autonomy vs network, consistency and operational complexity.

**Practice:** Explain an example, a failure mode, and an alternative.

## 90. Service discovery and API gateway?

**Priority:** Medium

**Answer cue:** Find service instances and centralize edge routing/security.

**Practice:** Explain an example, a failure mode, and an alternative.

## 91. Circuit breaker, retry, timeout, bulkhead?

**Priority:** Medium

**Answer cue:** Bound failure impact; retries only safe with idempotency and budgets.

**Practice:** Explain an example, a failure mode, and an alternative.

## 92. Saga vs distributed transaction?

**Priority:** Medium

**Answer cue:** Compensating business steps vs coordinated atomic transactions.

**Practice:** Explain an example, a failure mode, and an alternative.

## 93. Outbox pattern and exactly-once claims?

**Priority:** Medium

**Answer cue:** Persist event with DB state, relay asynchronously; consumers still need idempotency.

**Practice:** Explain an example, a failure mode, and an alternative.

## 94. Eventual consistency and CQRS?

**Priority:** Medium

**Answer cue:** Asynchronous convergence; separate read/write models when warranted.

**Practice:** Explain an example, a failure mode, and an alternative.

## 95. Observability in microservices?

**Priority:** Medium

**Answer cue:** Correlation IDs, metrics, logs, distributed traces, SLOs.

**Practice:** Explain an example, a failure mode, and an alternative.

## 96. How secure service-to-service calls?

**Priority:** Medium

**Answer cue:** mTLS or workload identity/tokens, least privilege, rotation.

**Practice:** Explain an example, a failure mode, and an alternative.
