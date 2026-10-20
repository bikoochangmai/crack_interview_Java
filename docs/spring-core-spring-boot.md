# Spring Core & Spring Boot

20 questions · Source: existing interview portal question bank.

> These are concise revision cues, not exhaustive explanations. Verify behavior against the version you use.

## 59. IoC vs DI?

**Priority:** High

**Answer cue:** Container controls lifecycle; dependencies supplied through injection.

**Practice:** Explain an example, a failure mode, and an alternative.

## 60. @Component vs @Service vs @Repository?

**Priority:** High

**Answer cue:** Stereotypes; Repository may translate persistence exceptions.

**Practice:** Explain an example, a failure mode, and an alternative.

## 61. @Controller vs @RestController?

**Priority:** High

**Answer cue:** RestController implies response-body serialization for handler methods.

**Practice:** Explain an example, a failure mode, and an alternative.

## 62. @RequestParam vs @PathVariable vs @RequestBody?

**Priority:** High

**Answer cue:** Query/form values, URL path segment, request payload.

**Practice:** Explain an example, a failure mode, and an alternative.

## 63. Bean scopes and lifecycle?

**Priority:** High

**Answer cue:** Singleton default, prototype, request/session scopes; initialization/destruction hooks.

**Practice:** Explain an example, a failure mode, and an alternative.

## 64. @Bean vs @Component?

**Priority:** High

**Answer cue:** Explicit factory method vs component scanning.

**Practice:** Explain an example, a failure mode, and an alternative.

## 65. Constructor vs field injection?

**Priority:** High

**Answer cue:** Constructor injection preferred for required dependencies and testability.

**Practice:** Explain an example, a failure mode, and an alternative.

## 66. @Configuration vs @SpringBootApplication?

**Priority:** High

**Answer cue:** Configuration defines beans; Boot annotation combines config, auto-config, scan.

**Practice:** Explain an example, a failure mode, and an alternative.

## 67. How does auto-configuration work?

**Priority:** High

**Answer cue:** Conditional configuration based on classpath, beans, properties.

**Practice:** Explain an example, a failure mode, and an alternative.

## 68. Profiles and external configuration?

**Priority:** Medium

**Answer cue:** Separate environment-specific properties, secrets and configuration.

**Practice:** Explain an example, a failure mode, and an alternative.

## 69. @Transactional behavior and proxy limitations?

**Priority:** Medium

**Answer cue:** Proxy-based transactions; self-invocation bypasses advice in common proxy mode.

**Practice:** Explain an example, a failure mode, and an alternative.

## 70. Propagation REQUIRED vs REQUIRES_NEW?

**Priority:** Medium

**Answer cue:** Join/create transaction vs independent new transaction.

**Practice:** Explain an example, a failure mode, and an alternative.

## 71. Isolation levels in Spring transactions?

**Priority:** Medium

**Answer cue:** Map to DB semantics; database support determines actual behavior.

**Practice:** Explain an example, a failure mode, and an alternative.

## 72. Spring MVC request lifecycle?

**Priority:** Medium

**Answer cue:** Servlet filters, DispatcherServlet, handler mapping, controller, serialization.

**Practice:** Explain an example, a failure mode, and an alternative.

## 73. Global exception handling?

**Priority:** Medium

**Answer cue:** @RestControllerAdvice and @ExceptionHandler produce consistent errors.

**Practice:** Explain an example, a failure mode, and an alternative.

## 74. Validation with @Valid?

**Priority:** Medium

**Answer cue:** Bean Validation on DTOs; translate violations to client-friendly errors.

**Practice:** Explain an example, a failure mode, and an alternative.

## 75. Spring Boot Actuator?

**Priority:** Medium

**Answer cue:** Health, metrics, info and observability endpoints; secure sensitive ones.

**Practice:** Explain an example, a failure mode, and an alternative.

## 76. Spring Boot testing layers?

**Priority:** Medium

**Answer cue:** Unit, slice tests, @SpringBootTest, Testcontainers integration.

**Practice:** Explain an example, a failure mode, and an alternative.

## 77. WebClient vs RestClient vs RestTemplate?

**Priority:** Medium

**Answer cue:** Reactive/nonblocking vs modern synchronous client vs older synchronous client.

**Practice:** Explain an example, a failure mode, and an alternative.

## 78. Spring Boot startup troubleshooting?

**Priority:** Medium

**Answer cue:** Inspect auto-config report, bean cycles, config, ports, dependencies.

**Practice:** Explain an example, a failure mode, and an alternative.
