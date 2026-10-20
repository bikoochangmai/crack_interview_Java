# Spring Core & Spring Boot — Interview Study Guide

20 questions. Java examples use Java 21 unless noted; Angular and SQL snippets are labeled by language.

> **Quality note:** Entries marked “Guided study” include the original answer cue and a production discussion exercise; they are not yet fully curated standalone explanations.

## #59 IoC vs DI?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Container controls lifecycle; dependencies supplied through injection. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "IoC vs DI". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate ioc vs di with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #60 @Component vs @Service vs @Repository?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Stereotypes; Repository may translate persistence exceptions. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "@Component vs @Service vs @Repository". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate @component vs @service vs @repository with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #61 @Controller vs @RestController?

**Priority:** High · **Status:** Expanded

### Concept
@Controller is a Spring MVC stereotype typically used with view rendering; @RestController combines @Controller and @ResponseBody so return values are serialized as HTTP response bodies.

### Why / when
Use @RestController for JSON APIs consumed by Angular, and @Controller for server-rendered views.

### Production example
An Angular dashboard calls GET /api/audits and receives JSON from an AuditController.

### Code example
```java
@RestController
@RequestMapping("/api/audits")
class AuditController {
    @GetMapping("/{id}")
    AuditDto get(@PathVariable long id) { return service.find(id); }
}
```

### Trade-offs and failure modes
Use explicit HTTP statuses and DTOs; do not return JPA entities containing sensitive fields.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #62 @RequestParam vs @PathVariable vs @RequestBody?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Query/form values, URL path segment, request payload. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "@RequestParam vs @PathVariable vs @RequestBody". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate @requestparam vs @pathvariable vs @requestbody with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #63 Bean scopes and lifecycle?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Singleton default, prototype, request/session scopes; initialization/destruction hooks. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "Bean scopes and lifecycle". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate bean scopes and lifecycle with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #64 @Bean vs @Component?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Explicit factory method vs component scanning. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "@Bean vs @Component". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate @bean vs @component with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #65 Constructor vs field injection?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Constructor injection preferred for required dependencies and testability. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "Constructor vs field injection". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate constructor vs field injection with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #66 @Configuration vs @SpringBootApplication?

**Priority:** High · **Status:** Expanded

### Concept
@Transactional wraps eligible method invocations in a transaction through Spring interception, typically a proxy. It controls commit/rollback for supported resources.

### Why / when
Use it around a cohesive database unit of work such as creating an order and reserving inventory.

### Production example
An order service writes an order and its line items atomically.

### Code example
```java
@Transactional
public OrderId place(CreateOrder cmd) {
    var order = orders.save(map(cmd));
    inventory.reserve(cmd.items());
    return order.id();
}
```

### Trade-offs and failure modes
Self-invocation bypasses proxy advice in proxy mode; remote HTTP calls cannot be rolled back by a local DB transaction.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #67 How does auto-configuration work?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Conditional configuration based on classpath, beans, properties. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "How does auto-configuration work". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate how does auto-configuration work with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #68 Profiles and external configuration?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Separate environment-specific properties, secrets and configuration. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "Profiles and external configuration". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate profiles and external configuration with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #69 @Transactional behavior and proxy limitations?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Proxy-based transactions; self-invocation bypasses advice in common proxy mode. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "@Transactional behavior and proxy limitations". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate @transactional behavior and proxy limitations with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #70 Propagation REQUIRED vs REQUIRES_NEW?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Join/create transaction vs independent new transaction. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "Propagation REQUIRED vs REQUIRES_NEW". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate propagation required vs requires_new with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #71 Isolation levels in Spring transactions?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Map to DB semantics; database support determines actual behavior. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "Isolation levels in Spring transactions". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate isolation levels in spring transactions with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #72 Spring MVC request lifecycle?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Servlet filters, DispatcherServlet, handler mapping, controller, serialization. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "Spring MVC request lifecycle". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate spring mvc request lifecycle with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #73 Global exception handling?

**Priority:** Medium · **Status:** Expanded

### Concept
Spring Security applies an ordered filter chain to incoming HTTP requests. Authentication establishes identity; authorization checks permissions.

### Why / when
Use resource-server JWT validation for an API behind an OAuth2/OIDC identity provider.

### Production example
An Angular app calls a Spring Boot compliance API with an access token; a policy checks the auditor role for approvals.

### Code example
```java
http.authorizeHttpRequests(a -> a
    .requestMatchers("/api/admin/**").hasRole("ADMIN")
    .anyRequest().authenticated())
    .oauth2ResourceServer(o -> o.jwt());
```

### Trade-offs and failure modes
Do not trust client-side role checks; validate issuer, audience, signature and expiry server-side.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #74 Validation with @Valid?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Bean Validation on DTOs; translate violations to client-friendly errors. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "Validation with @Valid". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate validation with @valid with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #75 Spring Boot Actuator?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Health, metrics, info and observability endpoints; secure sensitive ones. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "Spring Boot Actuator". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate spring boot actuator with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #76 Spring Boot testing layers?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Unit, slice tests, @SpringBootTest, Testcontainers integration. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "Spring Boot testing layers". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate spring boot testing layers with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #77 WebClient vs RestClient vs RestTemplate?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Reactive/nonblocking vs modern synchronous client vs older synchronous client. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "WebClient vs RestClient vs RestTemplate". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate webclient vs restclient vs resttemplate with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---

## #78 Spring Boot startup troubleshooting?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Inspect auto-config report, bean cycles, config, ports, dependencies. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Spring application lifecycle and persistence: choose the mechanism when its specific guarantees solve a real requirement in a transactional audit approvals API. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a transactional audit approvals API, identify a requirement involving "Spring Boot startup troubleshooting". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess proxy boundaries, incorrect transaction scope and configuration drift. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate spring boot startup troubleshooting with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a transactional audit approvals API?

---
