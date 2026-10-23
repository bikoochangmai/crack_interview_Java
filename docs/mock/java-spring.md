# Mock interview: Java / Spring

Attempt each prompt before expanding/reading its solution. These are original model answers, not alleged company questions or claimed personal experiences. For behavioral/day-to-day examples, fill the structure with facts from your own work. Banking designs are engineering exercises; actual rail, security and control requirements must be established with the responsible owners.

[All mock rounds](README.md) · [LLD / HLD paths](../lld-hld-learning-path.md)

## 17. HashMap internals and what changed in Java 8

### Interview prompt and example

Many distinct keys collide in one bucket, and a mutable key is changed after insertion.

### Lookup mechanics

A HashMap uses hash spreading to choose a bucket, then checks hash and equals among entries. Equal keys must have equal hashCode; unequal keys may collide. Power-of-two table capacity allows a bit-mask index. Resizing redistributes bins as capacity grows; default load factor is a sizing policy, not a guarantee of constant latency.

### Java 8 change

OpenJDK HashMap can convert a heavily populated collision bin into a balanced tree when thresholds and minimum table capacity permit. Common OpenJDK constants are treeify threshold 8 and minimum table capacity 64; below that it may resize rather than treeify. These are implementation details, not a universal Map contract. Tree-bin tie breaking/comparability details matter; do not promise identical asymptotic guarantees for every pathological key type.

### Practical mistakes

Changing fields used by equals/hashCode after insertion can make lookup fail even though iteration still shows the entry. HashMap is not thread-safe; fail-fast iteration is best effort, not a concurrency control. Null handling differs from ConcurrentHashMap. To safely accumulate concurrently, use documented atomic concurrent-map operations rather than synchronized-looking combinations of get and put.

### Explain and test

Demonstrate two equal key instances retrieving one mapping, distinct colliding keys retaining separate values, resizing with stable keys and a mutable-key lookup failure. Explain expected/amortized behavior and why poorly distributed hashes and unnecessary resizing hurt. The LLD striped-map lab makes collisions, MIN_VALUE hashing and atomic updates explicit without pretending to be OpenJDK internals.

### Interviewer follow-ups

- When does a bin resize rather than treeify?

- Why does a mutable hash key break lookup even without removal?

## 18. How does @Transactional work, and when does it silently fail?

### Interview prompt and example

A service calls this.transfer() internally and expects the annotation on transfer to start a transaction.

### What actually runs

In Spring’s typical proxy mode, a call entering through a configured transactional proxy is intercepted. The selected transaction manager starts or joins the resource transaction according to propagation/isolation settings, invokes the method and completes commit/rollback according to outcome and rules. The annotation itself is metadata; it is not a Java keyword that wraps every call.

### Common no-advice boundaries

Self-invocation through this bypasses proxy advice in the usual proxy mode. Manually constructed objects are not automatically managed/advised. Private methods cannot be advised through ordinary proxy interception, and final/class/method and visibility rules depend on the proxy mechanism and framework setup. State the actual configuration rather than claiming every non-public method always behaves identically.

### Rollback surprises

Default Spring rollback rules normally roll back on unchecked exceptions/Error, while checked exceptions require appropriate configuration unless configured defaults differ. Swallowing an exception may make the interceptor see normal completion, though a participating operation may already have marked rollback-only. An outer transaction can then fail at commit rather than silently succeed. readOnly is not a universal write prohibition.

### Resource/thread limits

Thread-bound imperative transactions do not automatically propagate to a new executor thread. Reactive transactions have different context rules. A local database transaction does not include an HTTP payment call or another unrelated transaction manager. Holding database locks while waiting on remote I/O increases risk and does not make the remote effect atomic.

### Fix and verify

Move the transactional use case to an injected service entered through its proxy, or use an appropriate programmatic boundary when justified. Define propagation/rollback deliberately. Use integration tests against the real database and failure path, checking final committed rows from outside the test’s own transaction so a test rollback cannot hide an error.

### Interviewer follow-ups

- How can a caught exception still result in UnexpectedRollbackException?

- Why does a test annotated @Transactional sometimes hide a missing production boundary?

## 19. synchronized vs ReentrantLock

### Interview prompt and example

Two threads update a shared local invariant; another operation needs a timed wait for a lock.

### Common guarantee

Both provide mutual exclusion and the required visibility/ordering relationship for properly protected shared state. Both are reentrant for the owning thread. Neither fixes lock-order deadlock or a workflow that reads state outside the protected boundary; neither coordinates separate JVMs.

### Choose deliberately

synchronized offers structured intrinsic-monitor acquisition/release when entering/leaving a block, including exceptional exits. ReentrantLock adds tryLock, timed/interruptible acquisition, optional fairness and multiple Condition queues. Explicit locks must be released in finally, and unlock only after acquisition succeeded.

### Wait and signal correctly

wait/notify belong to an owned intrinsic monitor; Condition await/signal belong to the matching held Lock. Recheck predicates in a loop because wakeups do not guarantee the desired state still holds. Fairness can trade throughput for an ordering policy and does not guarantee arbitrary application progress.

### Virtual-thread version caveat

On Java 21, blocking while holding synchronized can pin a carrier. JDK 24 changed monitor-related pinning through JEP 491. Do not replace every synchronized block based on an outdated universal warning; state the target runtime, keep critical sections short and measure contention. Native/foreign behavior and other resource limits still require analysis.

### Interviewer follow-ups

- When would timed tryLock be a business requirement?

- Why is a lock around only put insufficient for a multi-step reservation?

## Reference documentation

- [OpenJDK 21 HashMap source](https://github.com/openjdk/jdk/blob/jdk-21%2B35/src/java.base/share/classes/java/util/HashMap.java)
- [Spring transaction interception](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html)
- [ReentrantLock contract](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/locks/ReentrantLock.html)
