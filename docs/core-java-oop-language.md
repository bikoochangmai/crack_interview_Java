# Core Java — OOP & Language

15 questions · Source: existing interview portal question bank.

> These are concise revision cues, not exhaustive explanations. Verify behavior against the version you use.

## 1. Explain OOP pillars with real Java examples.

**Priority:** High

**Answer cue:** Encapsulation, abstraction, inheritance, polymorphism; favor composition when inheritance creates coupling.

**Practice:** Explain an example, a failure mode, and an alternative.

## 2. Interface vs abstract class?

**Priority:** High

**Answer cue:** Interfaces define capabilities; abstract classes share state/implementation. Java interfaces can have default/static/private methods.

**Practice:** Explain an example, a failure mode, and an alternative.

## 3. Overloading vs overriding?

**Priority:** High

**Answer cue:** Overloading resolves by compile-time signature; overriding uses runtime dispatch.

**Practice:** Explain an example, a failure mode, and an alternative.

## 4. equals() and hashCode() contract?

**Priority:** High

**Answer cue:** Equal objects must have equal hash codes; use consistent immutable identity keys.

**Practice:** Explain an example, a failure mode, and an alternative.

## 5. String vs StringBuilder vs StringBuffer?

**Priority:** High

**Answer cue:** String immutable; Builder mutable non-synchronized; Buffer synchronized.

**Practice:** Explain an example, a failure mode, and an alternative.

## 6. final vs finally vs finalize()?

**Priority:** High

**Answer cue:** final restricts reassignment/inheritance; finally cleanup block; finalize is deprecated and unsuitable for cleanup.

**Practice:** Explain an example, a failure mode, and an alternative.

## 7. Checked vs unchecked exceptions?

**Priority:** High

**Answer cue:** Checked require handling/declaration; unchecked RuntimeException indicates programming or runtime failures.

**Practice:** Explain an example, a failure mode, and an alternative.

## 8. Generics, wildcards, PECS?

**Priority:** High

**Answer cue:** Producer extends, consumer super; generics provide compile-time type safety with erasure.

**Practice:** Explain an example, a failure mode, and an alternative.

## 9. What is type erasure?

**Priority:** High

**Answer cue:** Generic type arguments mostly erased at runtime; bridge methods may be generated.

**Practice:** Explain an example, a failure mode, and an alternative.

## 10. Composition vs inheritance?

**Priority:** Medium

**Answer cue:** Composition delegates behavior and reduces rigid subtype coupling.

**Practice:** Explain an example, a failure mode, and an alternative.

## 11. Immutable class design?

**Priority:** Medium

**Answer cue:** Final fields, defensive copies, no mutable state exposure; records are shallowly immutable.

**Practice:** Explain an example, a failure mode, and an alternative.

## 12. SOLID principles?

**Priority:** Medium

**Answer cue:** Single responsibility, open/closed, Liskov, interface segregation, dependency inversion.

**Practice:** Explain an example, a failure mode, and an alternative.

## 13. Singleton design pattern and pitfalls?

**Priority:** Medium

**Answer cue:** One instance; enum singleton or holder idiom; beware global state, tests and distributed instances.

**Practice:** Explain an example, a failure mode, and an alternative.

## 14. Factory vs strategy vs observer?

**Priority:** Medium

**Answer cue:** Factory constructs, strategy swaps algorithms, observer broadcasts changes.

**Practice:** Explain an example, a failure mode, and an alternative.

## 15. Dependency injection vs service locator?

**Priority:** Medium

**Answer cue:** DI makes dependencies explicit; locator hides dependencies and complicates tests.

**Practice:** Explain an example, a failure mode, and an alternative.
