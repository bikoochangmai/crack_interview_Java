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


## Detailed virtual-thread study

[Virtual threads: scheduling, platform comparison, Java 21/24 pinning, runnable example and production limits](java-virtual-threads.md).

## Thread, Runnable and Callable

Virtual threads are ordinary java.lang.Thread instances whose scheduling is managed by the JVM. A platform thread generally maps to an operating-system thread; many virtual threads share a smaller set of carrier platform threads. Java 21 finalized virtual threads (JEP 444). A Runnable describes work without a result; Callable describes work returning a result and allowing checked exceptions. Either task abstraction can run on a platform or virtual thread.

## Scheduling, blocking and carriers

When supported blocking I/O parks a virtual thread, the JVM can unmount it from its carrier and later resume it on an available carrier. This lets many waiting tasks coexist without one OS thread per task. Concurrency means overlapping task lifetimes; parallelism means simultaneous CPU execution. Virtual threads improve throughput for many waiting tasks; they do not accelerate CPU computation or make a single remote call faster.

Execution flow: request → virtual thread → carrier while running → unmount during supported blocking I/O → resume on a carrier → complete Future.

Calling run() directly runs on the caller; start() schedules a new thread. Thread.ofVirtual().start(task) starts a virtual thread; Thread.ofPlatform().start(task) starts a platform thread. With an executor, submit returns a Future for the result and failure. Join/get waits for completion and establishes the specified visibility relationship.

## Choosing a model

| Workload | Starting point | Reason |
|---|---|---|
| Many blocking HTTP/JDBC calls | One virtual thread per task | Waiting does not generally need a dedicated OS thread |
| CPU-intensive transformations | Bounded platform executor | CPU cores limit parallelism |
| Existing asynchronous/reactive pipeline | Measure before changing | Virtual threads do not automatically improve an existing nonblocking design |

## Production scenario and resource limits

For a service waiting on independent remote calls, a platform pool of 100 threads can become occupied by 100 waiting requests. Virtual threads allow more requests to wait cheaply, while a semaphore can still limit a remote service to four calls. The runnable demo submits 12 tasks, limits the simulated I/O section to four, releases permits in finally, checks isVirtual(), propagates failures and cancels outstanding tasks on error. It demonstrates scheduling/resource boundaries, not a performance benchmark.

The virtual-thread-per-task executor is unbounded: one fresh virtual thread per submitted task. Do not pool virtual threads to control resources. Use a semaphore, connection pool, admission control and timeouts to bound downstream work; also bound incoming requests because waiting tasks still consume memory. Shared mutable state still requires synchronization. ThreadLocal works but large per-thread caches multiply memory use. Virtual threads are daemon threads; keep an owning scope alive and wait for completion. Cancellation is cooperative; configure real HTTP/JDBC timeouts because interruption may not stop every operation.

## Runnable Java 21 example

```java
import java.util.ArrayList;
import java.util.concurrent.*;

public class VirtualThreadDemo {
 public static void main(String[] args) throws Exception {
  var permits = new Semaphore(4); // simulated downstream capacity
  var results = new ArrayList<Future<String>>();
  try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
   for (int i = 0; i < 12; i++) {
    final int id = i;
    results.add(executor.submit(() -> {
     if (!permits.tryAcquire(1, TimeUnit.SECONDS))
      throw new TimeoutException("Downstream busy");
     try {
      Thread.sleep(20); // simulate waiting for I/O; no network needed
      return id + ": virtual=" + Thread.currentThread().isVirtual();
     } finally { permits.release(); }
    }));
   }
   try {
    for (var result : results) System.out.println(result.get(2, TimeUnit.SECONDS));
   } catch (InterruptedException e) {
    results.forEach(f -> f.cancel(true));
    Thread.currentThread().interrupt();
    throw e;
   } catch (ExecutionException | TimeoutException e) {
    results.forEach(f -> f.cancel(true));
    throw e;
   }
  } // close waits for tasks to finish
 }
}
```

Run from the repository root:

```powershell
javac examples/java21/VirtualThreadDemo.java
java -cp examples/java21 VirtualThreadDemo
```

Expected: twelve lines ending in virtual=true; completion order is not guaranteed. Results are printed in submission order. Future.get timeout applies to that wait, not an end-to-end deadline. The executor close waits for termination, so real services also need bounded I/O timeouts and a shutdown policy.

## Java 21 versus later JDK pinning

On Java 21, blocking while holding a synchronized monitor can pin a carrier; long native/foreign calls can also occupy carriers. Diagnose with JFR jdk.VirtualThreadPinned events and -Djdk.tracePinnedThreads=full on Java 21. JDK 24 (JEP 491) removes monitor-related pinning; do not repeat the Java 21 synchronized warning as a universal rule or replace every monitor with ReentrantLock. Lock contention and native-code limits still matter. Virtual threads need no preview flag in Java 21; other concurrency APIs have their own release status.

## Interview answer

I use virtual threads for many independent tasks that mostly wait on blocking I/O. The JVM multiplexes them over carrier threads, so waiting tasks use fewer OS-thread resources. I still limit downstream concurrency, protect shared state, set deadlines and measure under load. CPU-bound work remains limited by CPU capacity, and pinning analysis depends on the runtime version.

## Follow-up questions

- Why does a virtual thread not remove the JDBC pool limit?
- How do you bound incoming work as well as active downstream calls?
- What is the difference between pinning on Java 21 and Java 24?
- What happens when a Future times out but the remote call ignores interruption?
- Why use a fixed platform pool for CPU-heavy computation?
