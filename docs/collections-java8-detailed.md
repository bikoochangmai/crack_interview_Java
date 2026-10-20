# Java Collections, Streams & Java 8 — Interview Study Guide

15 questions. Java examples use Java 21 unless noted; Angular and SQL snippets are labeled by language.

> **Quality note:** Entries marked “Guided study” include the original answer cue and a production discussion exercise; they are not yet fully curated standalone explanations.

## #16 HashMap internals and collisions?

**Priority:** High · **Status:** Expanded

### Concept
HashMap hashes keys to buckets; collisions share buckets and may become balanced tree bins under qualifying conditions. Key equality and stable hashCode determine correctness.

### Why / when
Choose it for single-threaded indexing and lookup by stable identifiers.

### Production example
An audit importer maps document IDs to deduplicate incoming records before writing to PostgreSQL.

### Code example
```java
Map<String, AuditEvent> byId = new HashMap<>();
for (AuditEvent e : events) byId.putIfAbsent(e.id(), e);
```

### Trade-offs and failure modes
HashMap is not safe for concurrent mutation; mutable key fields can make entries unfindable.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #17 HashMap vs ConcurrentHashMap?

**Priority:** High · **Status:** Expanded

### Concept
HashMap has no concurrency guarantees; ConcurrentHashMap supports safe concurrent access and atomic operations such as computeIfAbsent.

### Why / when
Use ConcurrentHashMap for shared in-memory per-key counters or cached lookup results.

### Production example
Multiple Spring request threads update a per-tenant in-memory throttle counter.

### Code example
```java
ConcurrentHashMap<String, LongAdder> hits = new ConcurrentHashMap<>();
hits.computeIfAbsent(tenantId, k -> new LongAdder()).increment();
```

### Trade-offs and failure modes
A multi-step get-then-put is still racy; use atomic map methods. In-memory state is not shared across application replicas.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #18 ArrayList vs LinkedList?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
ArrayList offers efficient random access and locality; LinkedList has node overhead. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in in-memory indexing and transformations: choose the mechanism when its specific guarantees solve a real requirement in an order and audit aggregation worker. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an order and audit aggregation worker, identify a requirement involving "ArrayList vs LinkedList". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess mutable keys, concurrent mutation and unexpectedly large collections. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate arraylist vs linkedlist with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an order and audit aggregation worker?

---

## #19 HashSet vs TreeSet vs LinkedHashSet?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Hash-based unordered, sorted, and insertion-ordered respectively. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in in-memory indexing and transformations: choose the mechanism when its specific guarantees solve a real requirement in an order and audit aggregation worker. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an order and audit aggregation worker, identify a requirement involving "HashSet vs TreeSet vs LinkedHashSet". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess mutable keys, concurrent mutation and unexpectedly large collections. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate hashset vs treeset vs linkedhashset with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an order and audit aggregation worker?

---

## #20 Comparable vs Comparator?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Natural ordering in class vs external/custom ordering. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in in-memory indexing and transformations: choose the mechanism when its specific guarantees solve a real requirement in an order and audit aggregation worker. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an order and audit aggregation worker, identify a requirement involving "Comparable vs Comparator". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess mutable keys, concurrent mutation and unexpectedly large collections. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate comparable vs comparator with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an order and audit aggregation worker?

---

## #21 computeIfAbsent() use and Java version?

**Priority:** High · **Status:** Expanded

### Concept
computeIfAbsent(key, mappingFunction) returns the existing value or computes and stores one when absent (or mapped to null for ordinary Map implementations). It was introduced on Map in Java 8.

### Why / when
Use it to initialize grouping lists or lazily constructed cache entries without separate containsKey logic.

### Production example
An order processor groups orders by customer before building a batch response.

### Code example
```java
Map<String,List<Order>> grouped = new HashMap<>();
for (Order order : orders)
    grouped.computeIfAbsent(order.customerId(), k -> new ArrayList<>()).add(order);
```

### Trade-offs and failure modes
Avoid side effects and recursive modifications to the same map inside the mapping function; thread-safety depends on the implementation.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #22 Functional interface and lambda?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
One abstract method; lambdas supply implementation. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in in-memory indexing and transformations: choose the mechanism when its specific guarantees solve a real requirement in an order and audit aggregation worker. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an order and audit aggregation worker, identify a requirement involving "Functional interface and lambda". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess mutable keys, concurrent mutation and unexpectedly large collections. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate functional interface and lambda with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an order and audit aggregation worker?

---

## #23 Method reference types?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Static, bound instance, unbound instance, constructor references. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in in-memory indexing and transformations: choose the mechanism when its specific guarantees solve a real requirement in an order and audit aggregation worker. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an order and audit aggregation worker, identify a requirement involving "Method reference types". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess mutable keys, concurrent mutation and unexpectedly large collections. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate method reference types with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an order and audit aggregation worker?

---

## #24 Stream intermediate vs terminal operations?

**Priority:** High · **Status:** Expanded

### Concept
Stream intermediate operations such as map and filter are lazy; terminal operations such as collect, count and forEach trigger traversal.

### Why / when
Use streams for readable transformations over bounded in-memory collections.

### Production example
Filter rejected compliance findings, map to DTOs and collect into a response.

### Code example
```java
List<String> ids = findings.stream()
    .filter(Finding::isOpen).map(Finding::id).toList();
```

### Trade-offs and failure modes
Do not assume side-effect execution order; avoid using streams for complicated mutation-heavy logic.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #25 map vs flatMap?

**Priority:** Medium · **Status:** Expanded

### Concept
map transforms one input element into one output; flatMap transforms each input into a stream and flattens nested streams.

### Why / when
Use flatMap when a customer has multiple orders and each order contains multiple line items.

### Production example
An e-commerce analytics endpoint collects all SKUs purchased across an order batch.

### Code example
```java
List<String> skus = orders.stream()
    .flatMap(o -> o.items().stream())
    .map(LineItem::sku).toList();
```

### Trade-offs and failure modes
flatMap can create large intermediate results; use database queries or pagination for large data.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #26 Collectors.groupingBy vs partitioningBy?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Grouping arbitrary keys; partitioning Boolean predicate. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in in-memory indexing and transformations: choose the mechanism when its specific guarantees solve a real requirement in an order and audit aggregation worker. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an order and audit aggregation worker, identify a requirement involving "Collectors.groupingBy vs partitioningBy". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess mutable keys, concurrent mutation and unexpectedly large collections. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate collectors.groupingby vs partitioningby with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an order and audit aggregation worker?

---

## #27 Optional best practices?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Use for return values; avoid blindly calling get() and usually avoid entity fields. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in in-memory indexing and transformations: choose the mechanism when its specific guarantees solve a real requirement in an order and audit aggregation worker. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an order and audit aggregation worker, identify a requirement involving "Optional best practices". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess mutable keys, concurrent mutation and unexpectedly large collections. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate optional best practices with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an order and audit aggregation worker?

---

## #28 Default/static methods in interfaces?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Added Java 8; support interface evolution and utility behavior. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in in-memory indexing and transformations: choose the mechanism when its specific guarantees solve a real requirement in an order and audit aggregation worker. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an order and audit aggregation worker, identify a requirement involving "Default/static methods in interfaces". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess mutable keys, concurrent mutation and unexpectedly large collections. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate default/static methods in interfaces with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an order and audit aggregation worker?

---

## #29 CompletableFuture thenApply vs thenCompose?

**Priority:** Medium · **Status:** Expanded

### Concept
thenApply maps the result of a CompletableFuture synchronously within the completion chain; thenCompose flattens a function that returns another CompletableFuture.

### Why / when
Use thenCompose for dependent asynchronous calls without nested futures.

### Production example
After fetching a user profile asynchronously, fetch permissions for that user.

### Code example
```java
CompletableFuture<Permissions> result = fetchUser(id)
    .thenCompose(user -> fetchPermissions(user.id()));
```

### Trade-offs and failure modes
Avoid blocking join() inside common-pool tasks; supply appropriate executors for blocking work.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #30 Parallel streams: when avoid?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Avoid for blocking IO, shared mutation, small tasks and unpredictable common-pool contention. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in in-memory indexing and transformations: choose the mechanism when its specific guarantees solve a real requirement in an order and audit aggregation worker. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an order and audit aggregation worker, identify a requirement involving "Parallel streams: when avoid". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess mutable keys, concurrent mutation and unexpectedly large collections. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate parallel streams: when avoid with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an order and audit aggregation worker?

---
