# Concurrency, JVM & Performance

14 questions · Source: existing interview portal question bank.

> These are concise revision cues, not exhaustive explanations. Verify behavior against the version you use.

## 45. Thread vs Runnable vs Callable?

**Priority:** High

**Answer cue:** Execution abstraction vs tasks; Callable returns value and throws checked exceptions.

**Practice:** Explain an example, a failure mode, and an alternative.

## 46. synchronized vs ReentrantLock?

**Priority:** High

**Answer cue:** Intrinsic monitor vs explicit lock with tryLock, interruptibility and conditions.

**Practice:** Explain an example, a failure mode, and an alternative.

## 47. volatile vs atomic variables?

**Priority:** High

**Answer cue:** volatile ensures visibility/order; atomics provide compound atomic operations.

**Practice:** Explain an example, a failure mode, and an alternative.

## 48. Race condition vs deadlock vs starvation?

**Priority:** High

**Answer cue:** Incorrect interleaving, circular waiting, and indefinite lack of progress.

**Practice:** Explain an example, a failure mode, and an alternative.

## 49. ExecutorService and thread pools?

**Priority:** High

**Answer cue:** Manage task execution, queues, rejection, lifecycle; size by workload.

**Practice:** Explain an example, a failure mode, and an alternative.

## 50. CompletableFuture exception handling?

**Priority:** High

**Answer cue:** exceptionally, handle, whenComplete differ in recovery/observation.

**Practice:** Explain an example, a failure mode, and an alternative.

## 51. CountDownLatch vs CyclicBarrier vs Semaphore?

**Priority:** High

**Answer cue:** One-shot countdown, reusable rendezvous, permit limit.

**Practice:** Explain an example, a failure mode, and an alternative.

## 52. ConcurrentHashMap computeIfAbsent semantics?

**Priority:** High

**Answer cue:** Atomic key computation in ConcurrentHashMap; keep mapping function short.

**Practice:** Explain an example, a failure mode, and an alternative.

## 53. ThreadLocal pitfalls?

**Priority:** High

**Answer cue:** Thread-pool reuse can leak context; remove state; rethink with virtual threads.

**Practice:** Explain an example, a failure mode, and an alternative.

## 54. Java Memory Model happens-before?

**Priority:** Medium

**Answer cue:** Rules guaranteeing visibility/order between operations across threads.

**Practice:** Explain an example, a failure mode, and an alternative.

## 55. Heap vs stack vs metaspace?

**Priority:** Medium

**Answer cue:** Heap objects, thread stack frames, native metaspace class metadata.

**Practice:** Explain an example, a failure mode, and an alternative.

## 56. GC concepts: G1 vs ZGC?

**Priority:** Medium

**Answer cue:** Throughput/latency trade-offs; benchmark realistic heaps and workloads.

**Practice:** Explain an example, a failure mode, and an alternative.

## 57. How diagnose memory leak?

**Priority:** Medium

**Answer cue:** Heap dumps, allocation profiling, retained references, metrics.

**Practice:** Explain an example, a failure mode, and an alternative.

## 58. How diagnose high CPU/slow requests?

**Priority:** Medium

**Answer cue:** Thread dumps, JFR, traces, profiles, lock and database analysis.

**Practice:** Explain an example, a failure mode, and an alternative.
