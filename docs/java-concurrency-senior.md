# Java Concurrency — Senior / Architect Revision

**Sources:** Uploaded *Java Senior Concurrency Interview Guide* (4 pages), and *Java Senior/Lead Concurrency Interview Handbook* (4 pages). This is an original topic-level synthesis, **not a verbatim reproduction**. The second PDF carries a **Confidential & Proprietary** notice: obtain permission before publishing any of its content. This public-ready guide uses independently phrased general Java knowledge and topics also covered by the first guide.

## Java Memory Model (JMM) and happens-before

**Interview question:** How does one thread reliably see another thread's writes?

- The JMM specifies ordering and visibility guarantees, rather than promising a particular CPU cache flush instruction.
- A monitor unlock happens-before a subsequent lock of that monitor. A volatile write happens-before a subsequent read of the same field. Thread start/join also provide specified ordering.
- `volatile` provides visibility and ordering, **not** atomicity for `counter++`.
- Interview exercise: implement a safely published immutable object and explain why it is safe.

## CAS, atomic operations and ABA

- Compare-and-set conditionally updates a location if its observed value equals the expected value.
- `AtomicInteger`, `AtomicReference`, `VarHandle` and `LongAdder` solve different synchronization/throughput needs.
- ABA: A changes to B and back to A; a CAS may miss intermediate changes. Version stamps can help when the algorithm requires them.
- A lock-free algorithm is not automatically starvation-free or faster under high contention.

## False sharing

- Independent frequently written variables may occupy the same CPU cache line, increasing coherence traffic.
- Diagnose through profiling/benchmarking rather than assuming cache-line sizes or timing numbers are universal.
- Internal JVM annotations such as `@Contended` are not a general portable application API.

## Java 21 virtual threads

- Virtual threads are lightweight JVM-managed threads suited to many concurrent blocking I/O tasks.
- They do not speed up CPU-bound work or remove downstream limits (database connections, API quotas, memory).
- **Java 21 pinning:** blocking inside a `synchronized` region or native/foreign calls may pin a carrier; diagnose with JFR and `-Djdk.tracePinnedThreads` where supported.
- Pinning behavior has evolved in later Java releases; always state the runtime version.
- Avoid pooling virtual threads as a concurrency limit; use semaphores or resource-specific limits when necessary.

```java
try (var executor = java.util.concurrent.Executors.newVirtualThreadPerTaskExecutor()) {
    var tasks = java.util.stream.IntStream.range(0, 100)
        .mapToObj(i -> executor.submit(() -> fetchRemoteData(i)))
        .toList();
    for (var task : tasks) task.get();
}
```

`fetchRemoteData` is a placeholder method. For real code, handle errors, timeouts and cancellation.

## Locks, conditions and bounded buffers

**Challenge:** Implement a bounded producer-consumer ring buffer without `BlockingQueue`.

Design checklist:

1. Reject non-positive capacity.
2. Guard shared head, tail, count and array with one `ReentrantLock`.
3. Use separate `notFull` and `notEmpty` conditions.
4. Always use `while` around `await()` because of spurious wakeups.
5. Preserve interruption and timeout semantics; release locks in `finally`.
6. Null removed slots so objects can be garbage collected.
7. Test multiple producers/consumers, cancellation, zero/one capacity, and shutdown.

## Lock-free Treiber stack

**Challenge:** Implement push/pop using an `AtomicReference<Node<T>>` head and CAS retry loop.

- `push`: read head, link new node, CAS new head; retry on failure.
- `pop`: read head, return empty if null, CAS head to `head.next`; retry on failure.
- Discuss linearization points, contention, ABA and garbage-collected memory versus manually reclaimed memory.

## Production troubleshooting

| Symptom | Investigate | Possible response |
|---|---|---|
| High CPU | JFR, thread dump, busy loops, allocation | Fix hot loops, lock contention or GC causes |
| Deadlock | Lock ownership and wait cycles in thread dumps | Consistent lock ordering, timeouts, simpler lock hierarchy |
| Request timeouts | Downstream latency, executor queue, DB pool saturation | Backpressure, timeouts, bulkheads, measured pool tuning |
| Virtual-thread throughput collapse | Carrier pinning, blocking sections, DB connections | Profile, reduce blocking in synchronized sections, bound scarce resources |
| Consumer-producer stalls | Full/empty conditions, missed signals, interrupts | Correct `while` waits and targeted condition signaling |

## Interview questions to practise

1. Explain `volatile`, `synchronized`, `ReentrantLock`, `AtomicInteger`, and their trade-offs.
2. Why is double-checked locking safe only with a `volatile` instance field?
3. What does happens-before guarantee, and what does it not guarantee?
4. Explain CAS and a realistic ABA failure scenario.
5. How would you test a concurrent bounded buffer?
6. Why do virtual threads not eliminate JDBC connection pool limits?
7. How do you diagnose deadlock or virtual-thread pinning in production?
8. When would you choose `LongAdder` over `AtomicLong`?
9. What are the differences among deadlock, livelock and starvation?
10. How do you safely shut down an `ExecutorService`?

## References

- [Java 21 virtual threads (JEP 444)](https://openjdk.org/jeps/444)
- [Java Memory Model (JLS 17)](https://docs.oracle.com/javase/specs/jls/se21/html/jls-17.html)
- [Java concurrency API](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/package-summary.html)


## Detailed virtual-thread study

[Virtual threads: scheduling, platform comparison, Java 21/24 pinning, runnable example and production limits](java-virtual-threads.md).
