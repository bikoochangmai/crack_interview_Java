# Java Collections, Streams & Java 8

15 questions · Source: existing interview portal question bank.

> These are concise revision cues, not exhaustive explanations. Verify behavior against the version you use.

## 16. HashMap internals and collisions?

**Priority:** High

**Answer cue:** Hashing, buckets, equals; tree bins may be used for high collisions; not thread-safe.

**Practice:** Explain an example, a failure mode, and an alternative.

## 17. HashMap vs ConcurrentHashMap?

**Priority:** High

**Answer cue:** ConcurrentHashMap supports concurrent operations; null keys/values not allowed.

**Practice:** Explain an example, a failure mode, and an alternative.

## 18. ArrayList vs LinkedList?

**Priority:** High

**Answer cue:** ArrayList offers efficient random access and locality; LinkedList has node overhead.

**Practice:** Explain an example, a failure mode, and an alternative.

## 19. HashSet vs TreeSet vs LinkedHashSet?

**Priority:** High

**Answer cue:** Hash-based unordered, sorted, and insertion-ordered respectively.

**Practice:** Explain an example, a failure mode, and an alternative.

## 20. Comparable vs Comparator?

**Priority:** High

**Answer cue:** Natural ordering in class vs external/custom ordering.

**Practice:** Explain an example, a failure mode, and an alternative.

## 21. computeIfAbsent() use and Java version?

**Priority:** High

**Answer cue:** Map default method since Java 8; lazy value creation for grouping or graph lists.

**Practice:** Explain an example, a failure mode, and an alternative.

## 22. Functional interface and lambda?

**Priority:** High

**Answer cue:** One abstract method; lambdas supply implementation.

**Practice:** Explain an example, a failure mode, and an alternative.

## 23. Method reference types?

**Priority:** High

**Answer cue:** Static, bound instance, unbound instance, constructor references.

**Practice:** Explain an example, a failure mode, and an alternative.

## 24. Stream intermediate vs terminal operations?

**Priority:** High

**Answer cue:** Intermediate lazy transformations; terminal triggers pipeline execution.

**Practice:** Explain an example, a failure mode, and an alternative.

## 25. map vs flatMap?

**Priority:** Medium

**Answer cue:** map transforms each element; flatMap flattens nested results.

**Practice:** Explain an example, a failure mode, and an alternative.

## 26. Collectors.groupingBy vs partitioningBy?

**Priority:** Medium

**Answer cue:** Grouping arbitrary keys; partitioning Boolean predicate.

**Practice:** Explain an example, a failure mode, and an alternative.

## 27. Optional best practices?

**Priority:** Medium

**Answer cue:** Use for return values; avoid blindly calling get() and usually avoid entity fields.

**Practice:** Explain an example, a failure mode, and an alternative.

## 28. Default/static methods in interfaces?

**Priority:** Medium

**Answer cue:** Added Java 8; support interface evolution and utility behavior.

**Practice:** Explain an example, a failure mode, and an alternative.

## 29. CompletableFuture thenApply vs thenCompose?

**Priority:** Medium

**Answer cue:** thenApply maps value; thenCompose flattens dependent asynchronous stages.

**Practice:** Explain an example, a failure mode, and an alternative.

## 30. Parallel streams: when avoid?

**Priority:** Medium

**Answer cue:** Avoid for blocking IO, shared mutation, small tasks and unpredictable common-pool contention.

**Practice:** Explain an example, a failure mode, and an alternative.
