# 124 Foundational Interview Questions — Production Walkthroughs

All 124 previously guided-study questions now include a **specific production scenario**, failure mode, decision criteria and architecture flow. **21** questions also link to standalone Java 21 examples. Remaining entries are scenario-expanded, not claimed to have standalone runnable code.

Run Java examples with `javac examples/java21/Filename.java` and `java -cp examples/java21 ClassName` from the repository root.

## #14 — Factory vs strategy vs observer?

**Area:** Core Java — OOP & Language  

**Concept:** Factory constructs, strategy swaps algorithms, observer broadcasts changes.

**Why / decision:** Use this concept when designing a checkout service supporting card and UPI payments. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A checkout team chooses a payment gateway using a factory, injects a discount strategy, and notifies receipt listeners after successful payment.

**Architecture flow:** `Controller → Service → Domain interface → Concrete implementation`

**Failure / trade-off:** Hidden mutable state and tight coupling make changes difficult to test. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`FactoryStrategyObserver.java`](../examples/java21/FactoryStrategyObserver.java)

```powershell
javac examples/java21/FactoryStrategyObserver.java
java -cp examples/java21 FactoryStrategyObserver
```

**Interview follow-ups:**

- What changes if Factory vs strategy vs observer is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #15 — Dependency injection vs service locator?

**Area:** Core Java — OOP & Language  

**Concept:** DI makes dependencies explicit; locator hides dependencies and complicates tests.

**Why / decision:** Use this concept when designing a checkout service supporting card and UPI payments. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An OrderService constructor accepts PaymentGateway; tests pass a fake gateway without any global registry.

**Architecture flow:** `Controller → Service → Domain interface → Concrete implementation`

**Failure / trade-off:** Hidden mutable state and tight coupling make changes difficult to test. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Dependency injection vs service locator is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #18 — ArrayList vs LinkedList?

**Area:** Java Collections, Streams & Java 8  

**Concept:** ArrayList offers efficient random access and locality; LinkedList has node overhead.

**Why / decision:** Use this concept when designing an order-processing service indexing 50,000 orders per batch. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An API performs frequent index-based lookups over order IDs, favoring ArrayList; a work queue uses ArrayDeque instead of LinkedList.

**Architecture flow:** `Input batch → Transform / index → Validate → Persist`

**Failure / trade-off:** Incorrect collection choice or mutation under concurrency causes latency, data loss or unstable ordering. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`ListChoice.java`](../examples/java21/ListChoice.java)

```powershell
javac examples/java21/ListChoice.java
java -cp examples/java21 ListChoice
```

**Interview follow-ups:**

- What changes if ArrayList vs LinkedList is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #19 — HashSet vs TreeSet vs LinkedHashSet?

**Area:** Java Collections, Streams & Java 8  

**Concept:** Hash-based unordered, sorted, and insertion-ordered respectively.

**Why / decision:** Use this concept when designing an order-processing service indexing 50,000 orders per batch. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A batch import needs unique IDs, a deterministic insertion order for audit exports, and sorted IDs for a report: choose HashSet, LinkedHashSet, and TreeSet respectively.

**Architecture flow:** `Input batch → Transform / index → Validate → Persist`

**Failure / trade-off:** Incorrect collection choice or mutation under concurrency causes latency, data loss or unstable ordering. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`SetChoice.java`](../examples/java21/SetChoice.java)

```powershell
javac examples/java21/SetChoice.java
java -cp examples/java21 SetChoice
```

**Interview follow-ups:**

- What changes if HashSet vs TreeSet vs LinkedHashSet is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #20 — Comparable vs Comparator?

**Area:** Java Collections, Streams & Java 8  

**Concept:** Natural ordering in class vs external/custom ordering.

**Why / decision:** Use this concept when designing an order-processing service indexing 50,000 orders per batch. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Orders are naturally ordered by immutable order ID, but a dashboard sorts them by urgency using Comparator.

**Architecture flow:** `Input batch → Transform / index → Validate → Persist`

**Failure / trade-off:** Incorrect collection choice or mutation under concurrency causes latency, data loss or unstable ordering. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`Comparators.java`](../examples/java21/Comparators.java)

```powershell
javac examples/java21/Comparators.java
java -cp examples/java21 Comparators
```

**Interview follow-ups:**

- What changes if Comparable vs Comparator is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #22 — Functional interface and lambda?

**Area:** Java Collections, Streams & Java 8  

**Concept:** One abstract method; lambdas supply implementation.

**Why / decision:** Use this concept when designing an order-processing service indexing 50,000 orders per batch. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A reusable Predicate<Order> validates whether an order is eligible for shipment; lambdas avoid one-off implementation classes.

**Architecture flow:** `Input batch → Transform / index → Validate → Persist`

**Failure / trade-off:** Incorrect collection choice or mutation under concurrency causes latency, data loss or unstable ordering. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`Lambdas.java`](../examples/java21/Lambdas.java)

```powershell
javac examples/java21/Lambdas.java
java -cp examples/java21 Lambdas
```

**Interview follow-ups:**

- What changes if Functional interface and lambda is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #23 — Method reference types?

**Area:** Java Collections, Streams & Java 8  

**Concept:** Static, bound instance, unbound instance, constructor references.

**Why / decision:** Use this concept when designing an order-processing service indexing 50,000 orders per batch. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A pipeline uses Order::id, String::trim, Integer::parseInt, and ArrayList::new for instance, unbound, static, and constructor references.

**Architecture flow:** `Input batch → Transform / index → Validate → Persist`

**Failure / trade-off:** Incorrect collection choice or mutation under concurrency causes latency, data loss or unstable ordering. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Method reference types is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #26 — Collectors.groupingBy vs partitioningBy?

**Area:** Java Collections, Streams & Java 8  

**Concept:** Grouping arbitrary keys; partitioning Boolean predicate.

**Why / decision:** Use this concept when designing an order-processing service indexing 50,000 orders per batch. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A compliance dashboard groups findings by owner with groupingBy, then divides findings into open and closed with partitioningBy.

**Architecture flow:** `Input batch → Transform / index → Validate → Persist`

**Failure / trade-off:** Incorrect collection choice or mutation under concurrency causes latency, data loss or unstable ordering. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`GroupingCollectors.java`](../examples/java21/GroupingCollectors.java)

```powershell
javac examples/java21/GroupingCollectors.java
java -cp examples/java21 GroupingCollectors
```

**Interview follow-ups:**

- What changes if Collectors.groupingBy vs partitioningBy is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #27 — Optional best practices?

**Area:** Java Collections, Streams & Java 8  

**Concept:** Use for return values; avoid blindly calling get() and usually avoid entity fields.

**Why / decision:** Use this concept when designing an order-processing service indexing 50,000 orders per batch. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A repository returns Optional<Customer> to make a missing customer explicit; controllers translate absence into HTTP 404.

**Architecture flow:** `Input batch → Transform / index → Validate → Persist`

**Failure / trade-off:** Incorrect collection choice or mutation under concurrency causes latency, data loss or unstable ordering. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`OptionalReturn.java`](../examples/java21/OptionalReturn.java)

```powershell
javac examples/java21/OptionalReturn.java
java -cp examples/java21 OptionalReturn
```

**Interview follow-ups:**

- What changes if Optional best practices is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #28 — Default/static methods in interfaces?

**Area:** Java Collections, Streams & Java 8  

**Concept:** Added Java 8; support interface evolution and utility behavior.

**Why / decision:** Use this concept when designing an order-processing service indexing 50,000 orders per batch. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A shared repository interface adds a default pagination helper without forcing every implementation to change.

**Architecture flow:** `Input batch → Transform / index → Validate → Persist`

**Failure / trade-off:** Incorrect collection choice or mutation under concurrency causes latency, data loss or unstable ordering. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Default/static methods in interfaces is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #30 — Parallel streams: when avoid?

**Area:** Java Collections, Streams & Java 8  

**Concept:** Avoid for blocking IO, shared mutation, small tasks and unpredictable common-pool contention.

**Why / decision:** Use this concept when designing an order-processing service indexing 50,000 orders per batch. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Parallel streams over blocking HTTP calls saturate the common ForkJoinPool; use a dedicated executor or virtual threads with bounded downstream concurrency.

**Architecture flow:** `Input batch → Transform / index → Validate → Persist`

**Failure / trade-off:** Incorrect collection choice or mutation under concurrency causes latency, data loss or unstable ordering. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Parallel streams: when avoid is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #31 — Java 9 key changes?

**Area:** Java 9–21 Evolution  

**Concept:** Modules (JPMS), List.of/Set.of/Map.of, private interface methods, JShell.

**Why / decision:** Use this concept when designing a Java 8 to Java 21 migration of a Spring Boot document platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A team introduces JPMS only after checking reflection-heavy frameworks and third-party modules; immutable collection factories simplify DTO constants.

**Architecture flow:** `Baseline tests → Dependency upgrade → Java 21 build → Canary → Rollback`

**Failure / trade-off:** Unverified library compatibility and module encapsulation can break production after an upgrade. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Java 9 key changes is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #32 — Java 10 key changes?

**Area:** Java 9–21 Evolution  

**Concept:** Local variable type inference with var; compile-time inferred, not dynamic typing.

**Why / decision:** Use this concept when designing a Java 8 to Java 21 migration of a Spring Boot document platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A migration replaces verbose local types with var where inference remains obvious, without changing the runtime type.

**Architecture flow:** `Baseline tests → Dependency upgrade → Java 21 build → Canary → Rollback`

**Failure / trade-off:** Unverified library compatibility and module encapsulation can break production after an upgrade. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Java 10 key changes is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #33 — Java 11 key changes?

**Area:** Java 9–21 Evolution  

**Concept:** Standard HTTP Client, String utilities, Files read/write convenience; long-term support release.

**Why / decision:** Use this concept when designing a Java 8 to Java 21 migration of a Spring Boot document platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A backend replaces an external HTTP utility with java.net.http.HttpClient while testing timeouts and connection reuse.

**Architecture flow:** `Baseline tests → Dependency upgrade → Java 21 build → Canary → Rollback`

**Failure / trade-off:** Unverified library compatibility and module encapsulation can break production after an upgrade. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Java 11 key changes is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #34 — Java 12–14 switch evolution?

**Area:** Java 9–21 Evolution  

**Concept:** Switch expressions finalized in Java 14; yield supports expression blocks.

**Why / decision:** Use this concept when designing a Java 8 to Java 21 migration of a Spring Boot document platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A pricing API uses a switch expression to map customer tiers to discount rates, ensuring every case returns a value.

**Architecture flow:** `Baseline tests → Dependency upgrade → Java 21 build → Canary → Rollback`

**Failure / trade-off:** Unverified library compatibility and module encapsulation can break production after an upgrade. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`SwitchExpression.java`](../examples/java21/SwitchExpression.java)

```powershell
javac examples/java21/SwitchExpression.java
java -cp examples/java21 SwitchExpression
```

**Interview follow-ups:**

- What changes if Java 12–14 switch evolution is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #35 — Java 15 text blocks?

**Area:** Java 9–21 Evolution  

**Concept:** Multiline string literals finalized in Java 15.

**Why / decision:** Use this concept when designing a Java 8 to Java 21 migration of a Spring Boot document platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A document service stores readable multiline SQL in a Java text block while continuing to bind user input as parameters.

**Architecture flow:** `Baseline tests → Dependency upgrade → Java 21 build → Canary → Rollback`

**Failure / trade-off:** Unverified library compatibility and module encapsulation can break production after an upgrade. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Java 15 text blocks is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #36 — Java 16 records and instanceof patterns?

**Area:** Java 9–21 Evolution  

**Concept:** Records and pattern matching for instanceof finalized in Java 16.

**Why / decision:** Use this concept when designing a Java 8 to Java 21 migration of a Spring Boot document platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A REST DTO is represented by a record, and instanceof patterns simplify validation and logging.

**Architecture flow:** `Baseline tests → Dependency upgrade → Java 21 build → Canary → Rollback`

**Failure / trade-off:** Unverified library compatibility and module encapsulation can break production after an upgrade. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`RecordPattern.java`](../examples/java21/RecordPattern.java)

```powershell
javac examples/java21/RecordPattern.java
java -cp examples/java21 RecordPattern
```

**Interview follow-ups:**

- What changes if Java 16 records and instanceof patterns is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #37 — Java 17 sealed classes?

**Area:** Java 9–21 Evolution  

**Concept:** Sealed classes/interfaces finalized; restrict permitted subtypes.

**Why / decision:** Use this concept when designing a Java 8 to Java 21 migration of a Spring Boot document platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A payment result hierarchy permits only Success, Declined and RetryableFailure, preventing unknown implementations.

**Architecture flow:** `Baseline tests → Dependency upgrade → Java 21 build → Canary → Rollback`

**Failure / trade-off:** Unverified library compatibility and module encapsulation can break production after an upgrade. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`SealedTypes.java`](../examples/java21/SealedTypes.java)

```powershell
javac examples/java21/SealedTypes.java
java -cp examples/java21 SealedTypes
```

**Interview follow-ups:**

- What changes if Java 17 sealed classes is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #39 — Java 21 sequenced collections?

**Area:** Java 9–21 Evolution  

**Concept:** Uniform first/last/reversed APIs for encounter-ordered collections.

**Why / decision:** Use this concept when designing a Java 8 to Java 21 migration of a Spring Boot document platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A timeline service reads the first and last audit events through sequenced collection APIs.

**Architecture flow:** `Baseline tests → Dependency upgrade → Java 21 build → Canary → Rollback`

**Failure / trade-off:** Unverified library compatibility and module encapsulation can break production after an upgrade. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`SequencedCollections.java`](../examples/java21/SequencedCollections.java)

```powershell
javac examples/java21/SequencedCollections.java
java -cp examples/java21 SequencedCollections
```

**Interview follow-ups:**

- What changes if Java 21 sequenced collections is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #40 — Java 21 record patterns?

**Area:** Java 9–21 Evolution  

**Concept:** Finalized in 21; deconstruct record components in patterns.

**Why / decision:** Use this concept when designing a Java 8 to Java 21 migration of a Spring Boot document platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An event handler destructures a record representing a payment event without manually calling each accessor.

**Architecture flow:** `Baseline tests → Dependency upgrade → Java 21 build → Canary → Rollback`

**Failure / trade-off:** Unverified library compatibility and module encapsulation can break production after an upgrade. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Java 21 record patterns is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #41 — Java 21 pattern matching switch?

**Area:** Java 9–21 Evolution  

**Concept:** Finalized in 21; type patterns and exhaustive matching.

**Why / decision:** Use this concept when designing a Java 8 to Java 21 migration of a Spring Boot document platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A rules engine switches over sealed event types and handles null explicitly, reducing fragile instanceof chains.

**Architecture flow:** `Baseline tests → Dependency upgrade → Java 21 build → Canary → Rollback`

**Failure / trade-off:** Unverified library compatibility and module encapsulation can break production after an upgrade. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`PatternSwitch.java`](../examples/java21/PatternSwitch.java)

```powershell
javac examples/java21/PatternSwitch.java
java -cp examples/java21 PatternSwitch
```

**Interview follow-ups:**

- What changes if Java 21 pattern matching switch is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #42 — Java 21 preview vs finalized features?

**Area:** Java 9–21 Evolution  

**Concept:** String templates, scoped values, structured concurrency were preview in 21; avoid treating as final.

**Why / decision:** Use this concept when designing a Java 8 to Java 21 migration of a Spring Boot document platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A production migration uses finalized Java 21 features by default; preview features require --enable-preview and explicit support decisions.

**Architecture flow:** `Baseline tests → Dependency upgrade → Java 21 build → Canary → Rollback`

**Failure / trade-off:** Unverified library compatibility and module encapsulation can break production after an upgrade. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Java 21 preview vs finalized features is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #43 — Platform vs virtual threads?

**Area:** Java 9–21 Evolution  

**Concept:** Virtual threads are JVM-managed and scale blocking concurrency; platform threads map more directly to OS threads.

**Why / decision:** Use this concept when designing a Java 8 to Java 21 migration of a Spring Boot document platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A high-concurrency REST endpoint uses virtual threads for blocking HTTP calls but still caps JDBC connections at the pool size.

**Architecture flow:** `Baseline tests → Dependency upgrade → Java 21 build → Canary → Rollback`

**Failure / trade-off:** Unverified library compatibility and module encapsulation can break production after an upgrade. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Platform vs virtual threads is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #44 — How migrate Java 8 to 21?

**Area:** Java 9–21 Evolution  

**Concept:** Review dependencies, reflection/module encapsulation, GC, testing, build tools and runtime behavior.

**Why / decision:** Use this concept when designing a Java 8 to Java 21 migration of a Spring Boot document platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A Java 8 service migrates in a branch, updates Spring/Gradle dependencies, tests reflective libraries and GC, and canaries before full rollout.

**Architecture flow:** `Baseline tests → Dependency upgrade → Java 21 build → Canary → Rollback`

**Failure / trade-off:** Unverified library compatibility and module encapsulation can break production after an upgrade. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if How migrate Java 8 to 21 is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #45 — Thread vs Runnable vs Callable?

**Area:** Concurrency, JVM & Performance  

**Concept:** Execution abstraction vs tasks; Callable returns value and throws checked exceptions.

**Why / decision:** Use this concept when designing a Spring Boot service handling 2,000 concurrent document uploads. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An audit import submits Callable<Report> tasks to an executor because each task must return a report or checked exception.

**Architecture flow:** `Request → Bounded executor / virtual thread → Downstream resource pool → Response`

**Failure / trade-off:** Unbounded queues, blocking dependencies and unsafe shared state can cause contention and outages. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`CallableExample.java`](../examples/java21/CallableExample.java)

```powershell
javac examples/java21/CallableExample.java
java -cp examples/java21 CallableExample
```

**Interview follow-ups:**

- What changes if Thread vs Runnable vs Callable is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #48 — Race condition vs deadlock vs starvation?

**Area:** Concurrency, JVM & Performance  

**Concept:** Incorrect interleaving, circular waiting, and indefinite lack of progress.

**Why / decision:** Use this concept when designing a Spring Boot service handling 2,000 concurrent document uploads. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Two workers decrement inventory without atomic updates (race); opposing lock order creates deadlock; a saturated pool starves queued tasks.

**Architecture flow:** `Request → Bounded executor / virtual thread → Downstream resource pool → Response`

**Failure / trade-off:** Unbounded queues, blocking dependencies and unsafe shared state can cause contention and outages. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Race condition vs deadlock vs starvation is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #49 — ExecutorService and thread pools?

**Area:** Concurrency, JVM & Performance  

**Concept:** Manage task execution, queues, rejection, lifecycle; size by workload.

**Why / decision:** Use this concept when designing a Spring Boot service handling 2,000 concurrent document uploads. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A PDF conversion service uses a bounded executor and rejection policy to prevent a backlog from exhausting memory.

**Architecture flow:** `Request → Bounded executor / virtual thread → Downstream resource pool → Response`

**Failure / trade-off:** Unbounded queues, blocking dependencies and unsafe shared state can cause contention and outages. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`BoundedExecutor.java`](../examples/java21/BoundedExecutor.java)

```powershell
javac examples/java21/BoundedExecutor.java
java -cp examples/java21 BoundedExecutor
```

**Interview follow-ups:**

- What changes if ExecutorService and thread pools is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #50 — CompletableFuture exception handling?

**Area:** Concurrency, JVM & Performance  

**Concept:** exceptionally, handle, whenComplete differ in recovery/observation.

**Why / decision:** Use this concept when designing a Spring Boot service handling 2,000 concurrent document uploads. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A remote risk-scoring call uses exceptionally for fallback, handle for success/error transformation, and whenComplete for logging.

**Architecture flow:** `Request → Bounded executor / virtual thread → Downstream resource pool → Response`

**Failure / trade-off:** Unbounded queues, blocking dependencies and unsafe shared state can cause contention and outages. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`FutureRecovery.java`](../examples/java21/FutureRecovery.java)

```powershell
javac examples/java21/FutureRecovery.java
java -cp examples/java21 FutureRecovery
```

**Interview follow-ups:**

- What changes if CompletableFuture exception handling is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #51 — CountDownLatch vs CyclicBarrier vs Semaphore?

**Area:** Concurrency, JVM & Performance  

**Concept:** One-shot countdown, reusable rendezvous, permit limit.

**Why / decision:** Use this concept when designing a Spring Boot service handling 2,000 concurrent document uploads. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A batch job uses CountDownLatch to await workers, CyclicBarrier for phases, and Semaphore to cap external API calls.

**Architecture flow:** `Request → Bounded executor / virtual thread → Downstream resource pool → Response`

**Failure / trade-off:** Unbounded queues, blocking dependencies and unsafe shared state can cause contention and outages. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`SemaphoreLimit.java`](../examples/java21/SemaphoreLimit.java)

```powershell
javac examples/java21/SemaphoreLimit.java
java -cp examples/java21 SemaphoreLimit
```

**Interview follow-ups:**

- What changes if CountDownLatch vs CyclicBarrier vs Semaphore is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #52 — ConcurrentHashMap computeIfAbsent semantics?

**Area:** Concurrency, JVM & Performance  

**Concept:** Atomic key computation in ConcurrentHashMap; keep mapping function short.

**Why / decision:** Use this concept when designing a Spring Boot service handling 2,000 concurrent document uploads. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A per-tenant counter uses ConcurrentHashMap.computeIfAbsent with LongAdder; the mapping function stays short and side-effect-free.

**Architecture flow:** `Request → Bounded executor / virtual thread → Downstream resource pool → Response`

**Failure / trade-off:** Unbounded queues, blocking dependencies and unsafe shared state can cause contention and outages. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`ConcurrentCache.java`](../examples/java21/ConcurrentCache.java)

```powershell
javac examples/java21/ConcurrentCache.java
java -cp examples/java21 ConcurrentCache
```

**Interview follow-ups:**

- What changes if ConcurrentHashMap computeIfAbsent semantics is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #53 — ThreadLocal pitfalls?

**Area:** Concurrency, JVM & Performance  

**Concept:** Thread-pool reuse can leak context; remove state; rethink with virtual threads.

**Why / decision:** Use this concept when designing a Spring Boot service handling 2,000 concurrent document uploads. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A servlet thread pool reuses worker threads; trace IDs in ThreadLocal must be removed in finally to avoid cross-request leakage.

**Architecture flow:** `Request → Bounded executor / virtual thread → Downstream resource pool → Response`

**Failure / trade-off:** Unbounded queues, blocking dependencies and unsafe shared state can cause contention and outages. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`ThreadLocalCleanup.java`](../examples/java21/ThreadLocalCleanup.java)

```powershell
javac examples/java21/ThreadLocalCleanup.java
java -cp examples/java21 ThreadLocalCleanup
```

**Interview follow-ups:**

- What changes if ThreadLocal pitfalls is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #55 — Heap vs stack vs metaspace?

**Area:** Concurrency, JVM & Performance  

**Concept:** Heap objects, thread stack frames, native metaspace class metadata.

**Why / decision:** Use this concept when designing a Spring Boot service handling 2,000 concurrent document uploads. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A heap dump shows retained documents in a static cache; thread dumps reveal deep call stacks; metaspace metrics reveal class-loader leaks.

**Architecture flow:** `Request → Bounded executor / virtual thread → Downstream resource pool → Response`

**Failure / trade-off:** Unbounded queues, blocking dependencies and unsafe shared state can cause contention and outages. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Heap vs stack vs metaspace is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #56 — GC concepts: G1 vs ZGC?

**Area:** Concurrency, JVM & Performance  

**Concept:** Throughput/latency trade-offs; benchmark realistic heaps and workloads.

**Why / decision:** Use this concept when designing a Spring Boot service handling 2,000 concurrent document uploads. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A low-latency payment API compares G1 and ZGC using real allocation rate, pause-time percentiles and throughput under load.

**Architecture flow:** `Request → Bounded executor / virtual thread → Downstream resource pool → Response`

**Failure / trade-off:** Unbounded queues, blocking dependencies and unsafe shared state can cause contention and outages. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if GC concepts: G1 vs ZGC is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #57 — How diagnose memory leak?

**Area:** Concurrency, JVM & Performance  

**Concept:** Heap dumps, allocation profiling, retained references, metrics.

**Why / decision:** Use this concept when designing a Spring Boot service handling 2,000 concurrent document uploads. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A growing document cache retains request objects; heap-dump dominator analysis identifies the retaining map.

**Architecture flow:** `Request → Bounded executor / virtual thread → Downstream resource pool → Response`

**Failure / trade-off:** Unbounded queues, blocking dependencies and unsafe shared state can cause contention and outages. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if How diagnose memory leak is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #58 — How diagnose high CPU/slow requests?

**Area:** Concurrency, JVM & Performance  

**Concept:** Thread dumps, JFR, traces, profiles, lock and database analysis.

**Why / decision:** Use this concept when designing a Spring Boot service handling 2,000 concurrent document uploads. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A high-CPU incident uses JFR and thread dumps to distinguish a busy JSON serializer from blocked JDBC calls.

**Architecture flow:** `Request → Bounded executor / virtual thread → Downstream resource pool → Response`

**Failure / trade-off:** Unbounded queues, blocking dependencies and unsafe shared state can cause contention and outages. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if How diagnose high CPU/slow requests is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #59 — IoC vs DI?

**Area:** Spring Core & Spring Boot  

**Concept:** Container controls lifecycle; dependencies supplied through injection.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Spring creates CheckoutService and supplies PaymentGateway through its constructor rather than the service constructing the gateway.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if IoC vs DI is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #60 — @Component vs @Service vs @Repository?

**Area:** Spring Core & Spring Boot  

**Concept:** Stereotypes; Repository may translate persistence exceptions.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A persistence adapter is annotated @Repository so database exceptions are translated consistently; @Service marks business orchestration.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if @Component vs @Service vs @Repository is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #62 — @RequestParam vs @PathVariable vs @RequestBody?

**Area:** Spring Core & Spring Boot  

**Concept:** Query/form values, URL path segment, request payload.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** GET /orders/{id}?includeItems=true uses @PathVariable for id, @RequestParam for includeItems, and @RequestBody for POST payloads.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if @RequestParam vs @PathVariable vs @RequestBody is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #63 — Bean scopes and lifecycle?

**Area:** Spring Core & Spring Boot  

**Concept:** Singleton default, prototype, request/session scopes; initialization/destruction hooks.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A singleton pricing service is stateless; a request-scoped context holds request metadata; prototype scope is not an automatic resource cleanup mechanism.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Bean scopes and lifecycle is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #64 — @Bean vs @Component?

**Area:** Spring Core & Spring Boot  

**Concept:** Explicit factory method vs component scanning.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A third-party HTTP client is created in a @Bean factory method, while an application service is discovered with @Component.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if @Bean vs @Component is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #65 — Constructor vs field injection?

**Area:** Spring Core & Spring Boot  

**Concept:** Constructor injection preferred for required dependencies and testability.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Constructor injection makes an OrderService dependency mandatory and straightforward to replace in a unit test.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Constructor vs field injection is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #67 — How does auto-configuration work?

**Area:** Spring Core & Spring Boot  

**Concept:** Conditional configuration based on classpath, beans, properties.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Spring Boot creates an HTTP client or data source conditionally based on available classes, configuration and missing user-defined beans.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if How does auto-configuration work is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #68 — Profiles and external configuration?

**Area:** Spring Core & Spring Boot  

**Concept:** Separate environment-specific properties, secrets and configuration.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Local, staging and production use different URLs and feature flags; secrets come from environment variables or Key Vault rather than source control.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Profiles and external configuration is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #69 — @Transactional behavior and proxy limitations?

**Area:** Spring Core & Spring Boot  

**Concept:** Proxy-based transactions; self-invocation bypasses advice in common proxy mode.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A @Transactional method called through this.method() bypasses a Spring proxy in common proxy mode; move the boundary to a separate bean.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if @Transactional behavior and proxy limitations is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #70 — Propagation REQUIRED vs REQUIRES_NEW?

**Area:** Spring Core & Spring Boot  

**Concept:** Join/create transaction vs independent new transaction.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Order creation runs in REQUIRED, while an independent audit entry may use REQUIRES_NEW; consider the extra connection and rollback semantics.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Propagation REQUIRED vs REQUIRES_NEW is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #71 — Isolation levels in Spring transactions?

**Area:** Spring Core & Spring Boot  

**Concept:** Map to DB semantics; database support determines actual behavior.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An inventory reservation tests READ COMMITTED versus SERIALIZABLE under concurrent orders, and retries serialization failures.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Isolation levels in Spring transactions is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #72 — Spring MVC request lifecycle?

**Area:** Spring Core & Spring Boot  

**Concept:** Servlet filters, DispatcherServlet, handler mapping, controller, serialization.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An HTTP request crosses filters, DispatcherServlet, handler mapping, argument resolution, controller and response serialization.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Spring MVC request lifecycle is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #74 — Validation with @Valid?

**Area:** Spring Core & Spring Boot  

**Concept:** Bean Validation on DTOs; translate violations to client-friendly errors.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A POST DTO uses @NotBlank and @Positive; @Valid triggers validation and a controller advice returns a consistent 400 payload.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Validation with @Valid is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #75 — Spring Boot Actuator?

**Area:** Spring Core & Spring Boot  

**Concept:** Health, metrics, info and observability endpoints; secure sensitive ones.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Operations exposes health and metrics securely, keeping sensitive environment and configuration endpoints private.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Spring Boot Actuator is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #76 — Spring Boot testing layers?

**Area:** Spring Core & Spring Boot  

**Concept:** Unit, slice tests, @SpringBootTest, Testcontainers integration.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Pure business logic gets unit tests; MVC controllers get slice tests; persistence and transactions get Testcontainers integration tests.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Spring Boot testing layers is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #77 — WebClient vs RestClient vs RestTemplate?

**Area:** Spring Core & Spring Boot  

**Concept:** Reactive/nonblocking vs modern synchronous client vs older synchronous client.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A synchronous Spring MVC service uses RestClient for an HTTP dependency; a reactive pipeline uses WebClient without blocking.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if WebClient vs RestClient vs RestTemplate is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #78 — Spring Boot startup troubleshooting?

**Area:** Spring Core & Spring Boot  

**Concept:** Inspect auto-config report, bean cycles, config, ports, dependencies.

**Why / decision:** Use this concept when designing a Spring Boot order and payment API. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A failed deployment checks missing beans, conflicting ports, profile overrides and auto-configuration conditions before changing code.

**Architecture flow:** `HTTP → Filter → Controller → Service → Repository → PostgreSQL`

**Failure / trade-off:** Incorrect bean wiring, proxy boundaries and configuration can cause startup or transactional failures. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Spring Boot startup troubleshooting is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #79 — REST principles?

**Area:** REST, Security & Microservices  

**Concept:** Resource orientation, stateless requests, uniform interface, cacheability.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An order API exposes resources and HTTP semantics rather than tunneling every operation through a generic POST /execute endpoint.

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if REST principles is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #81 — What is idempotency?

**Area:** REST, Security & Microservices  

**Concept:** Repeating same operation has same intended effect; use keys for payment/order POST retries.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A payment API stores an idempotency key with the request fingerprint and result; retries return the same result rather than charging twice.

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`IdempotentCheckout.java`](../examples/java21/IdempotentCheckout.java)

```powershell
javac examples/java21/IdempotentCheckout.java
java -cp examples/java21 IdempotentCheckout
```

**Interview follow-ups:**

- What changes if What is idempotency is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #82 — HTTP status codes 200/201/202/204/400/401/403/404/409/429?

**Area:** REST, Security & Microservices  

**Concept:** Success, created, accepted, no content, bad request, unauthenticated, forbidden, not found, conflict, rate limit.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A POST creates a resource (201), queues work (202), rejects an invalid body (400), and rate-limits excessive requests (429).

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if HTTP status codes 200/201/202/204/400/401/403/404/409/429 is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #83 — API versioning and pagination?

**Area:** REST, Security & Microservices  

**Concept:** Compatibility strategy; cursor pagination for large changing datasets.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A growing audit history uses stable cursor pagination and a documented API version policy to avoid missing rows during concurrent writes.

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if API versioning and pagination is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #84 — Authentication vs authorization?

**Area:** REST, Security & Microservices  

**Concept:** Verify identity vs enforce allowed actions.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An authenticated employee can view their own reports but cannot approve another department’s restricted finding.

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Authentication vs authorization is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #85 — JWT vs session vs OIDC?

**Area:** REST, Security & Microservices  

**Concept:** JWT token format; session state mechanism; OIDC authentication protocol.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A browser signs in through OIDC; the backend validates access tokens; sessions are a separate state-management choice.

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if JWT vs session vs OIDC is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #86 — OAuth2 authorization code + PKCE?

**Area:** REST, Security & Microservices  

**Concept:** Secure delegated sign-in flow for public clients.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An Angular SPA uses authorization code + PKCE with a trusted identity provider and does not embed a client secret.

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if OAuth2 authorization code + PKCE is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #87 — CORS vs CSRF?

**Area:** REST, Security & Microservices  

**Concept:** Browser cross-origin access policy vs forged authenticated requests.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** CORS controls browser cross-origin reads, while CSRF protects cookie-authenticated state-changing requests from forged submissions.

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if CORS vs CSRF is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #88 — RBAC vs ABAC?

**Area:** REST, Security & Microservices  

**Concept:** Role-based permissions vs attribute/context policies.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An auditor role can read findings, but ABAC also checks tenant, department and document sensitivity.

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if RBAC vs ABAC is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #89 — Monolith vs microservices trade-offs?

**Area:** REST, Security & Microservices  

**Concept:** Deployment/team autonomy vs network, consistency and operational complexity.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A small team starts with a modular monolith and splits services only when deployment and ownership boundaries justify distributed complexity.

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Monolith vs microservices trade-offs is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #90 — Service discovery and API gateway?

**Area:** REST, Security & Microservices  

**Concept:** Find service instances and centralize edge routing/security.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An API gateway routes /orders and /payments, enforces edge authentication and rate limits, while services still authorize business actions.

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Service discovery and API gateway is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #92 — Saga vs distributed transaction?

**Area:** REST, Security & Microservices  

**Concept:** Compensating business steps vs coordinated atomic transactions.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An order saga reserves inventory, authorizes payment and creates shipment; failures trigger compensating steps.

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Saga vs distributed transaction is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #94 — Eventual consistency and CQRS?

**Area:** REST, Security & Microservices  

**Concept:** Asynchronous convergence; separate read/write models when warranted.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** The write model commits an order; an asynchronous read projection catches up later, requiring explicit staleness UX.

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Eventual consistency and CQRS is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #95 — Observability in microservices?

**Area:** REST, Security & Microservices  

**Concept:** Correlation IDs, metrics, logs, distributed traces, SLOs.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A checkout trace carries trace/span IDs across gateway, order, payment and inventory services.

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Observability in microservices is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #96 — How secure service-to-service calls?

**Area:** REST, Security & Microservices  

**Concept:** mTLS or workload identity/tokens, least privilege, rotation.

**Why / decision:** Use this concept when designing an e-commerce checkout API used by web and mobile clients. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Service A calls Service B using short-lived workload identity and TLS, with authorization scoped to the operation.

**Architecture flow:** `Client → API Gateway → AuthN/AuthZ → Service → Idempotency store → DB`

**Failure / trade-off:** Retries, weak authorization and incompatible clients can create duplicate operations or security exposure. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if How secure service-to-service calls is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #98 — Primary key vs unique key vs foreign key?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** Identity, uniqueness, and referential integrity.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A finding table uses a surrogate primary key, a unique tenant-specific external ID and a foreign key to the audit.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Primary key vs unique key vs foreign key is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #99 — INNER vs LEFT vs FULL OUTER JOIN?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** Matching rows, all left rows, all rows from both.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An audit report uses INNER JOIN for matched findings and LEFT JOIN to include audits with zero findings.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if INNER vs LEFT vs FULL OUTER JOIN is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #100 — WHERE vs HAVING?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** Filter rows before grouping vs groups after aggregation.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A report filters individual findings with WHERE before grouping, then filters grouped counts with HAVING.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if WHERE vs HAVING is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #101 — GROUP BY and aggregate functions?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** Group rows for COUNT/SUM/AVG/MIN/MAX.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A compliance report groups by department and calculates COUNT and AVG over findings.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if GROUP BY and aggregate functions is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #103 — Find second-highest salary?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** Use DENSE_RANK over salaries and filter rank 2; define tie behavior.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A payroll report uses DISTINCT salary values ordered descending and OFFSET 1, avoiding duplicate top salaries.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`SecondHighestSalary.java`](../examples/java21/SecondHighestSalary.java)

```powershell
javac examples/java21/SecondHighestSalary.java
java -cp examples/java21 SecondHighestSalary
```

**Interview follow-ups:**

- What changes if Find second-highest salary is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #104 — Find duplicate records?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** GROUP BY key HAVING COUNT(*)>1; use ROW_NUMBER to identify extras.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An import checks duplicate document IDs with GROUP BY and HAVING COUNT(*) > 1 before adding a unique constraint.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Find duplicate records is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #105 — CTE vs subquery?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** Named query expression vs inline nested query; optimizer-dependent performance.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A multi-stage report uses CTEs for readable transformations, while query plans determine whether materialization matters.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if CTE vs subquery is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #106 — UNION vs UNION ALL?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** UNION removes duplicates; UNION ALL preserves them.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Two monthly reports combine with UNION ALL to preserve all rows; UNION removes duplicates at extra cost.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if UNION vs UNION ALL is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #107 — DELETE vs TRUNCATE vs DROP?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** Delete rows, empty table, remove object; transaction semantics vary.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A cleanup deletes selected expired rows; TRUNCATE clears a staging table; DROP removes the table definition.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if DELETE vs TRUNCATE vs DROP is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #109 — B-tree vs GIN vs GiST indexes?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** General ordered lookups vs inverted/multidimensional access methods.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** B-tree supports ordered timestamps, GIN supports JSONB/arrays/full-text, and GiST supports appropriate spatial or range queries.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if B-tree vs GIN vs GiST indexes is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #111 — Transactions and isolation anomalies?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** Dirty/nonrepeatable/phantom reads, lost updates, write skew; DB-specific.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Two transactions read and update the same inventory row; isolation level determines whether anomalies are possible.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Transactions and isolation anomalies is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #114 — Deadlocks in databases?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** Conflicting lock order; detect/retry and enforce consistent ordering.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Concurrent workflows lock order and payment rows in opposite order; enforcing a consistent lock order reduces deadlocks.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Deadlocks in databases is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #115 — Normalization 1NF/2NF/3NF vs denormalization?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** Reduce anomalies vs optimize read models with controlled redundancy.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A normalized orders/items schema avoids duplicated customer fields; a read projection may denormalize totals for reporting.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Normalization 1NF/2NF/3NF vs denormalization is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #117 — Partitioning vs sharding vs replication?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** Table partitioning, distributing data, copying data for availability/reads.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A large audit table partitions by date, replicas serve reads, and tenant sharding is considered only after operational trade-offs.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Partitioning vs sharding vs replication is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #118 — Connection pooling and N+1 query issue?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** Reuse connections; avoid per-row ORM queries using joins/fetch batching.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A JPA endpoint loads 100 orders and lazily fetches each customer, causing N+1 queries; use fetch joins/projections and a bounded pool.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Connection pooling and N+1 query issue is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #119 — JSONB vs relational columns?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** Flexible indexed documents vs explicit constraints and relational modeling.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Stable searchable columns remain relational, while optional vendor-specific metadata can live in JSONB with targeted indexes.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if JSONB vs relational columns is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #121 — Design schema for audit findings/approvals?

**Area:** SQL, PostgreSQL & Database Design  

**Concept:** Foreign keys, tenant IDs, versioning, immutable audit trail and indexes.

**Why / decision:** Use this concept when designing a PostgreSQL-backed compliance audit system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Audit findings link to audit runs, evidence and approval decisions with tenant IDs, foreign keys and immutable approval history.

**Architecture flow:** `API → Connection pool → PostgreSQL transaction → Index / lock → Commit`

**Failure / trade-off:** Poor indexes, lock contention and long transactions can turn small requests into database-wide latency. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Design schema for audit findings/approvals is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #122 — Angular component lifecycle?

**Area:** Angular & TypeScript  

**Concept:** Constructor, ngOnInit, ngOnChanges, ngOnDestroy and render hooks.

**Why / decision:** Use this concept when designing an Angular dashboard displaying live audit findings. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An Angular findings page fetches data on initialization, reacts to input changes, and releases resources on destruction.

**Architecture flow:** `Route → Component → Service / RxJS → HTTP interceptor → API`

**Failure / trade-off:** Leaked subscriptions, unguarded routes and expensive rendering can degrade UX or expose data. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Angular component lifecycle is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #123 — Standalone components vs NgModules?

**Area:** Angular & TypeScript  

**Concept:** Standalone imports dependencies directly; NgModules group legacy declarations.

**Why / decision:** Use this concept when designing an Angular dashboard displaying live audit findings. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A modern Angular feature uses standalone components and route-level lazy loading instead of requiring an NgModule.

**Architecture flow:** `Route → Component → Service / RxJS → HTTP interceptor → API`

**Failure / trade-off:** Leaked subscriptions, unguarded routes and expensive rendering can degrade UX or expose data. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Standalone components vs NgModules is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #126 — Subject vs BehaviorSubject vs ReplaySubject?

**Area:** Angular & TypeScript  

**Concept:** No replay, latest value replay, configurable history replay.

**Why / decision:** Use this concept when designing an Angular dashboard displaying live audit findings. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A live status widget uses BehaviorSubject for the latest state and ReplaySubject when late subscribers need historical events.

**Architecture flow:** `Route → Component → Service / RxJS → HTTP interceptor → API`

**Failure / trade-off:** Leaked subscriptions, unguarded routes and expensive rendering can degrade UX or expose data. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Subject vs BehaviorSubject vs ReplaySubject is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #128 — Async pipe and subscription cleanup?

**Area:** Angular & TypeScript  

**Concept:** Template subscription lifecycle; takeUntilDestroyed for imperative subscriptions.

**Why / decision:** Use this concept when designing an Angular dashboard displaying live audit findings. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An Angular template uses async pipe to subscribe and unsubscribe automatically when a component is destroyed.

**Architecture flow:** `Route → Component → Service / RxJS → HTTP interceptor → API`

**Failure / trade-off:** Leaked subscriptions, unguarded routes and expensive rendering can degrade UX or expose data. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Async pipe and subscription cleanup is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #130 — Custom validators and async validators?

**Area:** Angular & TypeScript  

**Concept:** Sync/async validation functions; manage pending and errors.

**Why / decision:** Use this concept when designing an Angular dashboard displaying live audit findings. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A registration form uses a synchronous password rule and an asynchronous username-availability validator.

**Architecture flow:** `Route → Component → Service / RxJS → HTTP interceptor → API`

**Failure / trade-off:** Leaked subscriptions, unguarded routes and expensive rendering can degrade UX or expose data. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Custom validators and async validators is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #131 — Route guards and lazy loading?

**Area:** Angular & TypeScript  

**Concept:** Client navigation UX, not a replacement for server authorization.

**Why / decision:** Use this concept when designing an Angular dashboard displaying live audit findings. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An admin route is lazy-loaded and guarded for UX; the server still checks authorization on every API call.

**Architecture flow:** `Route → Component → Service / RxJS → HTTP interceptor → API`

**Failure / trade-off:** Leaked subscriptions, unguarded routes and expensive rendering can degrade UX or expose data. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Route guards and lazy loading is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #133 — Angular authentication and token storage?

**Area:** Angular & TypeScript  

**Concept:** OIDC/PKCE; consider BFF HttpOnly cookies, CSRF and XSS risks.

**Why / decision:** Use this concept when designing an Angular dashboard displaying live audit findings. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An Angular client uses OIDC authorization code + PKCE, protects against XSS and avoids relying on route guards for security.

**Architecture flow:** `Route → Component → Service / RxJS → HTTP interceptor → API`

**Failure / trade-off:** Leaked subscriptions, unguarded routes and expensive rendering can degrade UX or expose data. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Angular authentication and token storage is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #134 — Content projection vs ViewChild?

**Area:** Angular & TypeScript  

**Concept:** Reusable projected content vs references to template children.

**Why / decision:** Use this concept when designing an Angular dashboard displaying live audit findings. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A reusable modal accepts projected content via ng-content and accesses its child input using ViewChild.

**Architecture flow:** `Route → Component → Service / RxJS → HTTP interceptor → API`

**Failure / trade-off:** Leaked subscriptions, unguarded routes and expensive rendering can degrade UX or expose data. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Content projection vs ViewChild is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #135 — trackBy / @for track and rendering?

**Area:** Angular & TypeScript  

**Concept:** Stable identity reduces unnecessary DOM work.

**Why / decision:** Use this concept when designing an Angular dashboard displaying live audit findings. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A table with 5,000 findings uses @for (item of items; track item.id) to reuse DOM nodes across updates.

**Architecture flow:** `Route → Component → Service / RxJS → HTTP interceptor → API`

**Failure / trade-off:** Leaked subscriptions, unguarded routes and expensive rendering can degrade UX or expose data. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if trackBy / @for track and rendering is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #136 — Pure vs impure pipes?

**Area:** Angular & TypeScript  

**Concept:** Pure reruns on input reference/value changes; impure every check.

**Why / decision:** Use this concept when designing an Angular dashboard displaying live audit findings. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A pure formatting pipe recalculates only when inputs change by reference; an impure pipe runs more frequently.

**Architecture flow:** `Route → Component → Service / RxJS → HTTP interceptor → API`

**Failure / trade-off:** Leaked subscriptions, unguarded routes and expensive rendering can degrade UX or expose data. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Pure vs impure pipes is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #137 — TypeScript interface vs type alias?

**Area:** Angular & TypeScript  

**Concept:** Both describe types; interfaces support declaration merging.

**Why / decision:** Use this concept when designing an Angular dashboard displaying live audit findings. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An API DTO uses interface for an extendable object contract, while type alias expresses unions and mapped types.

**Architecture flow:** `Route → Component → Service / RxJS → HTTP interceptor → API`

**Failure / trade-off:** Leaked subscriptions, unguarded routes and expensive rendering can degrade UX or expose data. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if TypeScript interface vs type alias is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #138 — Generics, union and discriminated unions?

**Area:** Angular & TypeScript  

**Concept:** Reusable type parameters and safe variants.

**Why / decision:** Use this concept when designing an Angular dashboard displaying live audit findings. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A network response is modeled as a discriminated union of loading, success and error states, enabling exhaustive narrowing.

**Architecture flow:** `Route → Component → Service / RxJS → HTTP interceptor → API`

**Failure / trade-off:** Leaked subscriptions, unguarded routes and expensive rendering can degrade UX or expose data. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Generics, union and discriminated unions is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #140 — State management service vs NgRx?

**Area:** Angular & TypeScript  

**Concept:** Choose by complexity, shared state and debugging needs.

**Why / decision:** Use this concept when designing an Angular dashboard displaying live audit findings. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A small dashboard uses a signal-based service; a complex multi-team workflow may justify NgRx and explicit effects.

**Architecture flow:** `Route → Component → Service / RxJS → HTTP interceptor → API`

**Failure / trade-off:** Leaked subscriptions, unguarded routes and expensive rendering can degrade UX or expose data. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if State management service vs NgRx is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #141 — Unit tests and component integration tests?

**Area:** Angular & TypeScript  

**Concept:** Test behavior, services, HTTP mocking, accessibility.

**Why / decision:** Use this concept when designing an Angular dashboard displaying live audit findings. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A service unit test mocks HttpClient; a component integration test checks the rendered error state and user interactions.

**Architecture flow:** `Route → Component → Service / RxJS → HTTP interceptor → API`

**Failure / trade-off:** Leaked subscriptions, unguarded routes and expensive rendering can degrade UX or expose data. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Unit tests and component integration tests is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #142 — HLD vs LLD?

**Area:** Architecture, Azure & Leadership  

**Concept:** Services/data flows/trade-offs vs classes/contracts/algorithms.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A URL-shortener HLD defines services and data flows; its LLD specifies API contracts, tables and ID generation.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if HLD vs LLD is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #143 — CAP theorem and consistency models?

**Area:** Architecture, Azure & Leadership  

**Concept:** Under network partition choose consistency or availability; nuance required.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A globally distributed messaging service chooses availability during partitions while documenting stale reads and reconciliation.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if CAP theorem and consistency models is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #144 — Horizontal vs vertical scaling?

**Area:** Architecture, Azure & Leadership  

**Concept:** More instances vs bigger instances.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A document processing worker scales out across instances when CPU or queue depth grows; a larger VM alone has limits.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Horizontal vs vertical scaling is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #145 — Load balancer, CDN and cache?

**Area:** Architecture, Azure & Leadership  

**Concept:** Traffic distribution, edge content delivery, latency reduction.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A global content portal uses CDN for static assets, load balancer for application traffic and Redis for hot metadata.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Load balancer, CDN and cache is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #146 — Azure App Service vs VM vs AKS?

**Area:** Architecture, Azure & Leadership  

**Concept:** Managed web hosting vs full VM control vs orchestrated containers.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A simple API starts on App Service; AKS is considered when orchestration requirements justify cluster operations.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Azure App Service vs VM vs AKS is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #147 — Azure Service Bus vs Event Hubs?

**Area:** Architecture, Azure & Leadership  

**Concept:** Enterprise messaging/commands vs high-throughput event ingestion.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Service Bus handles business commands and durable work; Event Hubs ingests high-volume telemetry streams.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Azure Service Bus vs Event Hubs is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #148 — Azure Blob vs PostgreSQL storage?

**Area:** Architecture, Azure & Leadership  

**Concept:** Object binaries vs transactional structured metadata.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** PDF binaries go to Blob Storage; relational metadata, permissions and workflow states go to PostgreSQL.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Azure Blob vs PostgreSQL storage is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #149 — Design multi-tenant isolation?

**Area:** Architecture, Azure & Leadership  

**Concept:** Tenant scoping, authorization, RLS/schema/database separation.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Every database query and cache key includes tenant context; integration tests verify cross-tenant access is rejected.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Design multi-tenant isolation is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #150 — RTO vs RPO and disaster recovery?

**Area:** Architecture, Azure & Leadership  

**Concept:** Recovery time objective vs acceptable data loss.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A recovery plan defines a 15-minute RPO and one-hour RTO, then validates both through restoration drills.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if RTO vs RPO and disaster recovery is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #151 — Zero-downtime deployments?

**Area:** Architecture, Azure & Leadership  

**Concept:** Backward-compatible migrations, rolling/canary releases, health checks.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A deployment introduces backward-compatible schema changes, rolls out application instances gradually and retains rollback options.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Zero-downtime deployments is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #152 — Design a rate limiter?

**Area:** Architecture, Azure & Leadership  

**Concept:** Token bucket or sliding window, Redis atomicity and fairness.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An API uses a token bucket at the gateway and distributed Redis counters to enforce per-client quotas across replicas.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Runnable Java 21 example:** [`TokenBucket.java`](../examples/java21/TokenBucket.java)

```powershell
javac examples/java21/TokenBucket.java
java -cp examples/java21 TokenBucket
```

**Interview follow-ups:**

- What changes if Design a rate limiter is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #153 — Design URL shortener?

**Area:** Architecture, Azure & Leadership  

**Concept:** IDs, redirects, cache, hot keys, analytics, collision strategy.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A URL-shortener generates collision-resistant codes, stores redirects durably and caches popular lookups.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Design URL shortener is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #154 — Design document ingestion + RAG?

**Area:** Architecture, Azure & Leadership  

**Concept:** Upload, parse, chunk, embed, vector search, ACL filtering, citations.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A document pipeline extracts text, chunks with metadata, embeds, indexes pgvector and retrieves tenant-authorized passages.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Design document ingestion + RAG is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #155 — Design human-in-loop approvals?

**Area:** Architecture, Azure & Leadership  

**Concept:** State machine, RBAC, audit trail, optimistic locking.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An AI compliance agent proposes a remediation action, but a human approval gate controls execution and records the audit trail.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Design human-in-loop approvals is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #156 — How handle incidents and RCA?

**Area:** Architecture, Azure & Leadership  

**Concept:** Contain impact, evidence, blameless root cause and corrective action.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An incident review reconstructs the timeline, blast radius, immediate mitigation, contributing causes and prevention owners.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if How handle incidents and RCA is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #157 — How defend architecture trade-offs?

**Area:** Architecture, Azure & Leadership  

**Concept:** Requirements, alternatives, measurable constraints and failure modes.

**Why / decision:** Use this concept when designing a multi-region Azure-hosted document management system. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An ADR compares App Service and AKS using scale, deployment, security, operations and cost constraints.

**Architecture flow:** `Client → Front Door → App Service / AKS → Database + Cache + Queue`

**Failure / trade-off:** A single point of failure or undocumented recovery process can violate availability targets. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if How defend architecture trade-offs is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #158 — Describe a production incident you led.

**Area:** Behavioral & Project Deep Dives  

**Concept:** Use STAR; metrics, your actions, outcome, prevention.

**Why / decision:** Use this concept when designing a production migration of a legacy content platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Use a real incident you personally handled, with baseline, detection, actions, metrics, recovery and lessons; never invent figures.

**Architecture flow:** `Situation → Constraint → Decision → Measured result → Lesson`

**Failure / trade-off:** A vague incident narrative without metrics, ownership and learning is difficult to defend in an interview. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Describe a production incident you led. is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #159 — Explain a difficult architecture decision.

**Area:** Behavioral & Project Deep Dives  

**Concept:** Alternatives, constraints, decision record and measurable results.

**Why / decision:** Use this concept when designing a production migration of a legacy content platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Explain one actual architecture decision with options considered, explicit constraints and measurable consequences.

**Architecture flow:** `Situation → Constraint → Decision → Measured result → Lesson`

**Failure / trade-off:** A vague incident narrative without metrics, ownership and learning is difficult to defend in an interview. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Explain a difficult architecture decision. is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #160 — How modernize a legacy Java application?

**Area:** Behavioral & Project Deep Dives  

**Concept:** Strangler pattern, contract tests, incremental migration.

**Why / decision:** Use this concept when designing a production migration of a legacy content platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A legacy monolith is modularized, wrapped with APIs and migrated incrementally behind a strangler facade.

**Architecture flow:** `Situation → Constraint → Decision → Measured result → Lesson`

**Failure / trade-off:** A vague incident narrative without metrics, ownership and learning is difficult to defend in an interview. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if How modernize a legacy Java application is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #161 — How migrate Documentum to Alfresco?

**Area:** Behavioral & Project Deep Dives  

**Concept:** Inventory, metadata/ACL mapping, migration batches, validation, rollback.

**Why / decision:** Use this concept when designing a production migration of a legacy content platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A Documentum-to-Alfresco migration maps document metadata, ACLs, versions and retention policies, then verifies parity.

**Architecture flow:** `Situation → Constraint → Decision → Measured result → Lesson`

**Failure / trade-off:** A vague incident narrative without metrics, ownership and learning is difficult to defend in an interview. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if How migrate Documentum to Alfresco is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #162 — How integrate Elasticsearch with a content platform?

**Area:** Behavioral & Project Deep Dives  

**Concept:** Index pipeline, ACL-aware search, consistency and reindexing.

**Why / decision:** Use this concept when designing a production migration of a legacy content platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An Alfresco ingestion listener indexes authorized content in Elasticsearch and reconciles missed events.

**Architecture flow:** `Situation → Constraint → Decision → Measured result → Lesson`

**Failure / trade-off:** A vague incident narrative without metrics, ownership and learning is difficult to defend in an interview. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if How integrate Elasticsearch with a content platform is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #163 — How ensure RAG faithfulness?

**Area:** Behavioral & Project Deep Dives  

**Concept:** Grounded citations, eval datasets, human review, retrieval metrics.

**Why / decision:** Use this concept when designing a production migration of a legacy content platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A RAG evaluation set checks evidence recall, citation validity and unsupported claims before promotion.

**Architecture flow:** `Situation → Constraint → Decision → Measured result → Lesson`

**Failure / trade-off:** A vague incident narrative without metrics, ownership and learning is difficult to defend in an interview. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if How ensure RAG faithfulness is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #164 — How mentor engineers and manage code quality?

**Area:** Behavioral & Project Deep Dives  

**Concept:** Design reviews, standards, feedback, coaching and measurable outcomes.

**Why / decision:** Use this concept when designing a production migration of a legacy content platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Code review standards, architecture workshops and mentoring improve lead time and defect escape rate.

**Architecture flow:** `Situation → Constraint → Decision → Measured result → Lesson`

**Failure / trade-off:** A vague incident narrative without metrics, ownership and learning is difficult to defend in an interview. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if How mentor engineers and manage code quality is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #165 — How estimate system capacity?

**Area:** Behavioral & Project Deep Dives  

**Concept:** QPS, peak factors, storage growth, latency budgets, headroom.

**Why / decision:** Use this concept when designing a production migration of a legacy content platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** Estimate peak RPS, data volume, growth, connection count and egress costs before selecting Azure capacity.

**Architecture flow:** `Situation → Constraint → Decision → Measured result → Lesson`

**Failure / trade-off:** A vague incident narrative without metrics, ownership and learning is difficult to defend in an interview. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if How estimate system capacity is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #166 — How resolve disagreements?

**Area:** Behavioral & Project Deep Dives  

**Concept:** Make trade-offs explicit, prototype, gather evidence and document decision.

**Why / decision:** Use this concept when designing a production migration of a legacy content platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** A design disagreement is resolved with a time-boxed spike, explicit evaluation criteria and an ADR.

**Architecture flow:** `Situation → Constraint → Decision → Measured result → Lesson`

**Failure / trade-off:** A vague incident narrative without metrics, ownership and learning is difficult to defend in an interview. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if How resolve disagreements is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---

## #167 — Explain your compliance auditing architecture.

**Area:** Behavioral & Project Deep Dives  

**Concept:** End-to-end Angular/Spring/Python/pgvector, auth, tenancy, observability.

**Why / decision:** Use this concept when designing a production migration of a legacy content platform. In an interview, identify the requirements first, compare a plausible alternative, and explain the consequences for correctness, latency, maintainability and operations.

**Production walkthrough:** An auditing system ingests policies, retrieves tenant-filtered passages, proposes findings and requires approval before changes.

**Architecture flow:** `Situation → Constraint → Decision → Measured result → Lesson`

**Failure / trade-off:** A vague incident narrative without metrics, ownership and learning is difficult to defend in an interview. Validate the decision with tests, metrics and a rollback or recovery plan where applicable.

**Interview follow-ups:**

- What changes if Explain your compliance auditing architecture. is used at 10× load?
- Which alternative would you choose, and under what constraints?
- How would you test the main failure mode in production-like conditions?

---
