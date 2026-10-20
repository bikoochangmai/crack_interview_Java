# Concurrency, JVM & Performance — Interview Study Guide

14 questions. Java examples use Java 21 unless noted; Angular and SQL snippets are labeled by language.

> **Quality note:** Entries marked “Guided study” include the original answer cue and a production discussion exercise; they are not yet fully curated standalone explanations.

## #45 Thread vs Runnable vs Callable?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Execution abstraction vs tasks; Callable returns value and throws checked exceptions. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in concurrent request processing: choose the mechanism when its specific guarantees solve a real requirement in a Spring Boot ingestion pipeline with many concurrent jobs. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Spring Boot ingestion pipeline with many concurrent jobs, identify a requirement involving "Thread vs Runnable vs Callable". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess data races, resource exhaustion, deadlocks and unbounded queues. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate thread vs runnable vs callable with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Spring Boot ingestion pipeline with many concurrent jobs?

---

## #46 synchronized vs ReentrantLock?

**Priority:** High · **Status:** Expanded

### Concept
synchronized uses intrinsic monitors with automatic release; ReentrantLock offers timed, interruptible and optionally fair acquisition plus multiple Condition objects.

### Why / when
Use synchronized for straightforward short critical sections; choose ReentrantLock for specific coordination features.

### Production example
A bounded queue uses notEmpty and notFull conditions to coordinate producers and consumers.

### Code example
```java
lock.lock();
try { updateSharedState(); }
finally { lock.unlock(); }
```

### Trade-offs and failure modes
Always unlock in finally; neither locking approach prevents logical deadlock from inconsistent acquisition order.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #47 volatile vs atomic variables?

**Priority:** High · **Status:** Expanded

### Concept
volatile gives visibility and ordering guarantees for a variable, but incrementing it is not atomic. AtomicInteger uses atomic operations for read-modify-write.

### Why / when
Use volatile for a cancellation flag; AtomicInteger for a concurrent counter.

### Production example
A background reconciliation worker checks a volatile shutdown flag while many request threads increment an AtomicInteger metric.

### Code example
```java
private volatile boolean running = true;
private final AtomicInteger count = new AtomicInteger();
void record() { count.incrementAndGet(); }
```

### Trade-offs and failure modes
volatile count++ can lose updates; atomics do not make multi-field invariants transactional.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #48 Race condition vs deadlock vs starvation?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Incorrect interleaving, circular waiting, and indefinite lack of progress. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in concurrent request processing: choose the mechanism when its specific guarantees solve a real requirement in a Spring Boot ingestion pipeline with many concurrent jobs. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Spring Boot ingestion pipeline with many concurrent jobs, identify a requirement involving "Race condition vs deadlock vs starvation". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess data races, resource exhaustion, deadlocks and unbounded queues. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate race condition vs deadlock vs starvation with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Spring Boot ingestion pipeline with many concurrent jobs?

---

## #49 ExecutorService and thread pools?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Manage task execution, queues, rejection, lifecycle; size by workload. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in concurrent request processing: choose the mechanism when its specific guarantees solve a real requirement in a Spring Boot ingestion pipeline with many concurrent jobs. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Spring Boot ingestion pipeline with many concurrent jobs, identify a requirement involving "ExecutorService and thread pools". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess data races, resource exhaustion, deadlocks and unbounded queues. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate executorservice and thread pools with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Spring Boot ingestion pipeline with many concurrent jobs?

---

## #50 CompletableFuture exception handling?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
exceptionally, handle, whenComplete differ in recovery/observation. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in concurrent request processing: choose the mechanism when its specific guarantees solve a real requirement in a Spring Boot ingestion pipeline with many concurrent jobs. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Spring Boot ingestion pipeline with many concurrent jobs, identify a requirement involving "CompletableFuture exception handling". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess data races, resource exhaustion, deadlocks and unbounded queues. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate completablefuture exception handling with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Spring Boot ingestion pipeline with many concurrent jobs?

---

## #51 CountDownLatch vs CyclicBarrier vs Semaphore?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
One-shot countdown, reusable rendezvous, permit limit. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in concurrent request processing: choose the mechanism when its specific guarantees solve a real requirement in a Spring Boot ingestion pipeline with many concurrent jobs. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Spring Boot ingestion pipeline with many concurrent jobs, identify a requirement involving "CountDownLatch vs CyclicBarrier vs Semaphore". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess data races, resource exhaustion, deadlocks and unbounded queues. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate countdownlatch vs cyclicbarrier vs semaphore with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Spring Boot ingestion pipeline with many concurrent jobs?

---

## #52 ConcurrentHashMap computeIfAbsent semantics?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Atomic key computation in ConcurrentHashMap; keep mapping function short. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in concurrent request processing: choose the mechanism when its specific guarantees solve a real requirement in a Spring Boot ingestion pipeline with many concurrent jobs. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Spring Boot ingestion pipeline with many concurrent jobs, identify a requirement involving "ConcurrentHashMap computeIfAbsent semantics". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess data races, resource exhaustion, deadlocks and unbounded queues. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate concurrenthashmap computeifabsent semantics with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Spring Boot ingestion pipeline with many concurrent jobs?

---

## #53 ThreadLocal pitfalls?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Thread-pool reuse can leak context; remove state; rethink with virtual threads. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in concurrent request processing: choose the mechanism when its specific guarantees solve a real requirement in a Spring Boot ingestion pipeline with many concurrent jobs. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Spring Boot ingestion pipeline with many concurrent jobs, identify a requirement involving "ThreadLocal pitfalls". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess data races, resource exhaustion, deadlocks and unbounded queues. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate threadlocal pitfalls with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Spring Boot ingestion pipeline with many concurrent jobs?

---

## #54 Java Memory Model happens-before?

**Priority:** Medium · **Status:** Expanded

### Concept
The Java Memory Model defines when writes become visible across threads. Happens-before edges arise from program order, synchronization, volatile accesses and thread start/join.

### Why / when
Use happens-before reasoning to prove safe publication and avoid data races.

### Production example
A producer publishes an immutable task into a BlockingQueue and a worker safely consumes it.

### Code example
```java
BlockingQueue<Task> queue = new LinkedBlockingQueue<>();
queue.put(task);
Task received = queue.take();
```

### Trade-offs and failure modes
Without proper publication, another thread may observe stale state; timing-based tests cannot prove a program race-free.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #55 Heap vs stack vs metaspace?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Heap objects, thread stack frames, native metaspace class metadata. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in concurrent request processing: choose the mechanism when its specific guarantees solve a real requirement in a Spring Boot ingestion pipeline with many concurrent jobs. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Spring Boot ingestion pipeline with many concurrent jobs, identify a requirement involving "Heap vs stack vs metaspace". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess data races, resource exhaustion, deadlocks and unbounded queues. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate heap vs stack vs metaspace with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Spring Boot ingestion pipeline with many concurrent jobs?

---

## #56 GC concepts: G1 vs ZGC?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Throughput/latency trade-offs; benchmark realistic heaps and workloads. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in concurrent request processing: choose the mechanism when its specific guarantees solve a real requirement in a Spring Boot ingestion pipeline with many concurrent jobs. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Spring Boot ingestion pipeline with many concurrent jobs, identify a requirement involving "GC concepts: G1 vs ZGC". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess data races, resource exhaustion, deadlocks and unbounded queues. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate gc concepts: g1 vs zgc with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Spring Boot ingestion pipeline with many concurrent jobs?

---

## #57 How diagnose memory leak?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Heap dumps, allocation profiling, retained references, metrics. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in concurrent request processing: choose the mechanism when its specific guarantees solve a real requirement in a Spring Boot ingestion pipeline with many concurrent jobs. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Spring Boot ingestion pipeline with many concurrent jobs, identify a requirement involving "How diagnose memory leak". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess data races, resource exhaustion, deadlocks and unbounded queues. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate how diagnose memory leak with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Spring Boot ingestion pipeline with many concurrent jobs?

---

## #58 How diagnose high CPU/slow requests?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Thread dumps, JFR, traces, profiles, lock and database analysis. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in concurrent request processing: choose the mechanism when its specific guarantees solve a real requirement in a Spring Boot ingestion pipeline with many concurrent jobs. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Spring Boot ingestion pipeline with many concurrent jobs, identify a requirement involving "How diagnose high CPU/slow requests". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess data races, resource exhaustion, deadlocks and unbounded queues. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate how diagnose high cpu/slow requests with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Spring Boot ingestion pipeline with many concurrent jobs?

---
