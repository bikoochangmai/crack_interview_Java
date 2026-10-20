# Core Java — Interview Study Guide

15 questions. Java examples use Java 21 unless noted; Angular and SQL snippets are labeled by language.

> **Quality note:** Entries marked “Guided study” include the original answer cue and a production discussion exercise; they are not yet fully curated standalone explanations.

## #1 Explain OOP pillars with real Java examples.

**Priority:** High · **Status:** Expanded

### Concept
Object-oriented programming organizes state and behavior into objects. Encapsulation protects invariants; abstraction exposes contracts; inheritance models a genuine is-a relationship; polymorphism lets a caller use interchangeable implementations.

### Why / when
Encapsulation keeps invalid state out of domain objects. Abstraction and polymorphism allow payment, notification or storage implementations to change without rewriting business workflows. Inheritance should model substitutable behavior; composition usually reduces coupling.

### Production example
Spring Boot checkout injects a PaymentGateway interface. UpiGateway and CardGateway implement pay(); CheckoutService delegates through the interface. A BankAccount hides its balance and validates withdrawals in methods.

### Code example
```java
interface PaymentGateway { void pay(long amountPaise); }
class UpiGateway implements PaymentGateway {
    public void pay(long amountPaise) { System.out.println("UPI " + amountPaise); }
}
class CheckoutService {
    private final PaymentGateway gateway;
    CheckoutService(PaymentGateway gateway) { this.gateway = gateway; }
    void checkout(long amountPaise) {
        if (amountPaise <= 0) throw new IllegalArgumentException("amount");
        gateway.pay(amountPaise);
    }
}
```

### Trade-offs and failure modes
Prefer composition for changing behavior. Inheritance can violate Liskov substitution when subclasses narrow valid operations. Interfaces alone do not enforce domain invariants.

### Follow-up questions
- Abstraction vs encapsulation?
- Why prefer composition over inheritance?
- How does Spring DI implement dependency inversion?

---

## #2 Interface vs abstract class?

**Priority:** High · **Status:** Expanded

### Concept
An interface specifies a capability/contract; an abstract class can hold shared instance state, constructors and partial implementations. Modern Java interfaces support default, static and private methods.

### Why / when
Use an interface when unrelated classes should implement the same capability. Use an abstract base class when related classes share meaningful state or invariant behavior.

### Production example
PaymentGateway is an interface implemented by UPI and card providers; AbstractDocumentProcessor might own shared validation and metrics for related processors.

### Code example
```java
interface Storage { byte[] read(String key); }
abstract class ValidatedStorage implements Storage {
    protected void validate(String key) {
        if (key == null || key.isBlank()) throw new IllegalArgumentException();
    }
}
```

### Trade-offs and failure modes
Java supports implementing multiple interfaces but extending only one class. Avoid abstract base classes that force unrelated subclasses to inherit unused behavior.

### Follow-up questions
- Can an interface have private methods?
- When do default methods cause conflicts?

---

## #3 Overloading vs overriding?

**Priority:** High · **Status:** Expanded

### Concept
Overloading selects among methods with different parameter signatures at compile time. Overriding replaces an inherited instance method implementation and uses runtime dispatch.

### Why / when
Overloading offers convenient API variants; overriding enables polymorphic extension while honoring the base contract.

### Production example
OrderService.createOrder(String) and createOrder(CreateOrderRequest) overload; PaymentGateway implementations override pay().

### Code example
```java
class Formatter {
    String format(int value) { return Integer.toString(value); }
    String format(long value) { return Long.toString(value); }
}
interface Alert { void send(); }
class EmailAlert implements Alert {
    @Override public void send() { System.out.println("email"); }
}
```

### Trade-offs and failure modes
Static methods are hidden rather than overridden. Overloading with null and unrelated reference types can be ambiguous.

### Follow-up questions
- Can you override static methods?
- How does dynamic dispatch work?

---

## #4 equals() and hashCode() contract?

**Priority:** High · **Status:** Expanded

### Concept
equals defines logical equality. hashCode must return equal hashes for objects that compare equal. Unequal objects may share a hash.

### Why / when
HashMap and HashSet use hashCode to locate buckets and equals to distinguish keys within collisions.

### Production example
Two CustomerId records with the same UUID should behave as the same key in a HashMap.

### Code example
```java
record CustomerId(java.util.UUID value) {}
var id = java.util.UUID.randomUUID();
var counts = new java.util.HashMap<CustomerId, Integer>();
counts.put(new CustomerId(id), 1);
System.out.println(counts.get(new CustomerId(id))); // 1
```

### Trade-offs and failure modes
Do not mutate fields used by equals/hashCode after insertion into hash-based collections.

### Follow-up questions
- What happens if hashCode changes after insertion?
- Can unequal objects have same hash?

---

## #5 String vs StringBuilder vs StringBuffer?

**Priority:** High · **Status:** Expanded

### Concept
String is immutable and safe to share; StringBuilder is a mutable, unsynchronized character buffer; StringBuffer synchronizes its operations. String concatenation in loops can create avoidable intermediate objects.

### Why / when
Use String for API values and keys; use a local StringBuilder when assembling a report or CSV row.

### Production example
An audit export worker appends 10,000 row fragments into one StringBuilder and converts to String only when complete.

### Code example
```java
StringBuilder sb = new StringBuilder();
for (String id : auditIds) sb.append(id).append("\n");
String report = sb.toString();
```

### Trade-offs and failure modes
Do not share a StringBuilder across worker threads. StringBuffer synchronizes individual methods but does not make compound workflows atomic.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #6 final vs finally vs finalize()?

**Priority:** High · **Status:** Expanded

### Concept
final prevents reassignment, overriding or subclassing depending on placement. finally is a block used for cleanup; finalize() was an unreliable GC-triggered callback and is deprecated for removal.

### Why / when
Prefer try-with-resources for closeable JDBC streams and files, rather than relying on finalization.

### Production example
An ingestion job closes its InputStream even when parsing fails.

### Code example
```java
try (var input = java.nio.file.Files.newInputStream(path)) {
    return input.readAllBytes();
}
```

### Trade-offs and failure modes
A final reference does not make the referenced object immutable. finally does not replace resource ownership.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #7 Checked vs unchecked exceptions?

**Priority:** High · **Status:** Expanded

### Concept
Checked exceptions must be caught or declared; unchecked exceptions extend RuntimeException and can propagate without declaration.

### Why / when
Checked exceptions can communicate recoverable external conditions; unchecked exceptions often represent programming errors or violated preconditions.

### Production example
A document import may report a recoverable IOException, while invalid request input can raise IllegalArgumentException.

### Code example
```java
try { importDocument(file); }
catch (java.io.IOException e) {
    throw new ImportFailedException("Unable to read document", e);
}
```

### Trade-offs and failure modes
Do not catch Exception and silently continue. Define exception translation at API boundaries and preserve the original cause.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #8 Generics, wildcards, PECS?

**Priority:** High · **Status:** Expanded

### Concept
Generics provide compile-time type checking. ? extends T is a producer from which you can read T; ? super T is a consumer into which you can add T (PECS).

### Why / when
Use wildcard variance for reusable library APIs without unsafe casts.

### Production example
A reporting method reads List<? extends AuditEvent> while an event collector accepts List<? super AuditEvent>.

### Code example
```java
static double sum(List<? extends Number> xs) {
    return xs.stream().mapToDouble(Number::doubleValue).sum();
}
```

### Trade-offs and failure modes
Java generics are invariant: List<Integer> is not a List<Number>. Wildcards restrict operations intentionally.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #9 What is type erasure?

**Priority:** High · **Status:** Expanded

### Concept
Java generics use type erasure: most type parameters are removed from runtime representation, with compiler-inserted casts and bridges where needed.

### Why / when
It enables interoperability with older bytecode, but limits reflection and overload choices.

### Production example
A JSON serializer needs a TypeReference<List<Order>> to preserve element type metadata during deserialization.

### Code example
```java
List<String> names = new ArrayList<>();
// At runtime, names is an ArrayList; element type is not reified.
```

### Trade-offs and failure modes
You cannot create new T() or use instanceof List<String>; overloaded methods cannot differ only in erased generic arguments.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #10 Composition vs inheritance?

**Priority:** Medium · **Status:** Expanded

### Concept
Inheritance establishes an is-a relationship; composition builds behavior by delegating to collaborators.

### Why / when
Prefer composition for payment methods, notification channels and storage backends that vary independently of the workflow.

### Production example
OrderService contains a PricingPolicy instead of extending one pricing subclass per region.

### Code example
```java
interface PricingPolicy { long price(Order order); }
record Checkout(PricingPolicy pricing) {
    long total(Order order) { return pricing.price(order); }
}
```

### Trade-offs and failure modes
Deep inheritance trees are fragile; a subclass that changes valid behavior can violate substitutability.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #11 Immutable class design?

**Priority:** Medium · **Status:** Expanded

### Concept
An immutable class cannot change its observable state after construction. Use final fields, validation, no setters and defensive copies of mutable inputs.

### Why / when
Immutable value objects are easier to cache, share across threads and use as map keys.

### Production example
A Money value object stores currency and minor units; a booking request snapshot cannot be mutated after validation.

### Code example
```java
record Booking(String id, List<String> passengers) {
    Booking { passengers = List.copyOf(passengers); }
}
```

### Trade-offs and failure modes
A final field holding a mutable List does not make its contents immutable. Copy collections on input and output.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #12 SOLID principles?

**Priority:** Medium · **Status:** Expanded

### Concept
SOLID: single responsibility, open/closed, Liskov substitution, interface segregation and dependency inversion. These are design heuristics, not requirements to create an interface for every class.

### Why / when
Use them when changes in one subsystem repeatedly break unrelated workflows.

### Production example
A checkout flow depends on PaymentGateway; provider-specific integrations change without modifying checkout orchestration.

### Code example
```java
interface PaymentGateway { Receipt charge(Payment request); }
record CheckoutService(PaymentGateway gateway) {
    Receipt checkout(Payment request) { return gateway.charge(request); }
}
```

### Trade-offs and failure modes
Over-abstraction can make a simple application harder to navigate; validate abstractions against real variation.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #13 Singleton design pattern and pitfalls?

**Priority:** Medium · **Status:** Expanded

### Concept
A Singleton restricts a class to one instance per class loader. An enum singleton handles serialization and reflection pitfalls better than many hand-written implementations.

### Why / when
Use it sparingly for stateless shared coordination; in Spring, container-managed singleton scope is generally clearer and testable.

### Production example
A configuration catalog is shared across requests, while request-specific user state is never stored in a singleton bean.

### Code example
```java
enum AppSettings { INSTANCE;
    String region() { return "eu-west"; }
}
```

### Trade-offs and failure modes
Singletons with mutable state create test interference and race conditions; Spring singleton scope is per application context, not global across processes.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #14 Factory vs strategy vs observer?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Factory constructs, strategy swaps algorithms, observer broadcasts changes. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Java domain model and API design: choose the mechanism when its specific guarantees solve a real requirement in an enterprise document authoring service. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an enterprise document authoring service, identify a requirement involving "Factory vs strategy vs observer". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess invalid state, unnecessary inheritance and untested boundary conditions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate factory vs strategy vs observer with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an enterprise document authoring service?

---

## #15 Dependency injection vs service locator?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
DI makes dependencies explicit; locator hides dependencies and complicates tests. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in Java domain model and API design: choose the mechanism when its specific guarantees solve a real requirement in an enterprise document authoring service. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an enterprise document authoring service, identify a requirement involving "Dependency injection vs service locator". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess invalid state, unnecessary inheritance and untested boundary conditions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate dependency injection vs service locator with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an enterprise document authoring service?

---
