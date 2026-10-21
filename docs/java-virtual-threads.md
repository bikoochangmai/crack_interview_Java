# Virtual threads — from thread basics to production

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

## Sources

- [JEP 444 — Virtual Threads](https://openjdk.org/jeps/444)
- [Oracle JDK 24 migration guide — JEP 491](https://docs.oracle.com/en/java/javase/24/migrate/jdk-migration-guide.pdf)
