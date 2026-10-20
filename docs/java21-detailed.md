# Java 9–21 Evolution — Interview Study Guide

14 questions. Java examples use Java 21 unless noted; Angular and SQL snippets are labeled by language.

> **Quality note:** Entries marked “Guided study” include the original answer cue and a production discussion exercise; they are not yet fully curated standalone explanations.

## #31 Java 9 key changes?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Modules (JPMS), List.of/Set.of/Map.of, private interface methods, JShell. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in language modernization: choose the mechanism when its specific guarantees solve a real requirement in a Java 8 to Java 21 Spring Boot migration. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Java 8 to Java 21 Spring Boot migration, identify a requirement involving "Java 9 key changes". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess runtime compatibility, preview-feature reliance and library upgrades. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate java 9 key changes with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Java 8 to Java 21 Spring Boot migration?

---

## #32 Java 10 key changes?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Local variable type inference with var; compile-time inferred, not dynamic typing. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in language modernization: choose the mechanism when its specific guarantees solve a real requirement in a Java 8 to Java 21 Spring Boot migration. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Java 8 to Java 21 Spring Boot migration, identify a requirement involving "Java 10 key changes". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess runtime compatibility, preview-feature reliance and library upgrades. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate java 10 key changes with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Java 8 to Java 21 Spring Boot migration?

---

## #33 Java 11 key changes?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Standard HTTP Client, String utilities, Files read/write convenience; long-term support release. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in language modernization: choose the mechanism when its specific guarantees solve a real requirement in a Java 8 to Java 21 Spring Boot migration. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Java 8 to Java 21 Spring Boot migration, identify a requirement involving "Java 11 key changes". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess runtime compatibility, preview-feature reliance and library upgrades. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate java 11 key changes with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Java 8 to Java 21 Spring Boot migration?

---

## #34 Java 12–14 switch evolution?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Switch expressions finalized in Java 14; yield supports expression blocks. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in language modernization: choose the mechanism when its specific guarantees solve a real requirement in a Java 8 to Java 21 Spring Boot migration. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Java 8 to Java 21 Spring Boot migration, identify a requirement involving "Java 12–14 switch evolution". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess runtime compatibility, preview-feature reliance and library upgrades. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate java 12–14 switch evolution with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Java 8 to Java 21 Spring Boot migration?

---

## #35 Java 15 text blocks?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Multiline string literals finalized in Java 15. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in language modernization: choose the mechanism when its specific guarantees solve a real requirement in a Java 8 to Java 21 Spring Boot migration. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Java 8 to Java 21 Spring Boot migration, identify a requirement involving "Java 15 text blocks". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess runtime compatibility, preview-feature reliance and library upgrades. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate java 15 text blocks with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Java 8 to Java 21 Spring Boot migration?

---

## #36 Java 16 records and instanceof patterns?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Records and pattern matching for instanceof finalized in Java 16. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in language modernization: choose the mechanism when its specific guarantees solve a real requirement in a Java 8 to Java 21 Spring Boot migration. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Java 8 to Java 21 Spring Boot migration, identify a requirement involving "Java 16 records and instanceof patterns". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess runtime compatibility, preview-feature reliance and library upgrades. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate java 16 records and instanceof patterns with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Java 8 to Java 21 Spring Boot migration?

---

## #37 Java 17 sealed classes?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Sealed classes/interfaces finalized; restrict permitted subtypes. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in language modernization: choose the mechanism when its specific guarantees solve a real requirement in a Java 8 to Java 21 Spring Boot migration. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Java 8 to Java 21 Spring Boot migration, identify a requirement involving "Java 17 sealed classes". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess runtime compatibility, preview-feature reliance and library upgrades. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate java 17 sealed classes with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Java 8 to Java 21 Spring Boot migration?

---

## #38 Java 21 virtual threads?

**Priority:** High · **Status:** Expanded

### Concept
Java 21 virtual threads are lightweight Java threads scheduled onto carrier platform threads. They simplify high-concurrency blocking I/O code, but do not make downstream systems faster.

### Why / when
Use virtual threads for many concurrent request handlers or network I/O operations where thread-per-request platform threads are expensive.

### Production example
A document-processing API handles thousands of mostly-waiting remote storage requests using a virtual-thread-per-task executor.

### Code example
```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    var result = executor.submit(() -> client.fetchDocument(id));
    System.out.println(result.get());
}
```

### Trade-offs and failure modes
In Java 21, long blocking operations inside synchronized sections can pin carriers; JDBC connection pools and service quotas still bound throughput.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #39 Java 21 sequenced collections?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Uniform first/last/reversed APIs for encounter-ordered collections. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in language modernization: choose the mechanism when its specific guarantees solve a real requirement in a Java 8 to Java 21 Spring Boot migration. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Java 8 to Java 21 Spring Boot migration, identify a requirement involving "Java 21 sequenced collections". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess runtime compatibility, preview-feature reliance and library upgrades. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate java 21 sequenced collections with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Java 8 to Java 21 Spring Boot migration?

---

## #40 Java 21 record patterns?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Finalized in 21; deconstruct record components in patterns. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in language modernization: choose the mechanism when its specific guarantees solve a real requirement in a Java 8 to Java 21 Spring Boot migration. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Java 8 to Java 21 Spring Boot migration, identify a requirement involving "Java 21 record patterns". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess runtime compatibility, preview-feature reliance and library upgrades. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate java 21 record patterns with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Java 8 to Java 21 Spring Boot migration?

---

## #41 Java 21 pattern matching switch?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Finalized in 21; type patterns and exhaustive matching. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in language modernization: choose the mechanism when its specific guarantees solve a real requirement in a Java 8 to Java 21 Spring Boot migration. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Java 8 to Java 21 Spring Boot migration, identify a requirement involving "Java 21 pattern matching switch". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess runtime compatibility, preview-feature reliance and library upgrades. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate java 21 pattern matching switch with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Java 8 to Java 21 Spring Boot migration?

---

## #42 Java 21 preview vs finalized features?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
String templates, scoped values, structured concurrency were preview in 21; avoid treating as final. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in language modernization: choose the mechanism when its specific guarantees solve a real requirement in a Java 8 to Java 21 Spring Boot migration. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Java 8 to Java 21 Spring Boot migration, identify a requirement involving "Java 21 preview vs finalized features". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess runtime compatibility, preview-feature reliance and library upgrades. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate java 21 preview vs finalized features with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Java 8 to Java 21 Spring Boot migration?

---

## #43 Platform vs virtual threads?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Virtual threads are JVM-managed and scale blocking concurrency; platform threads map more directly to OS threads. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in language modernization: choose the mechanism when its specific guarantees solve a real requirement in a Java 8 to Java 21 Spring Boot migration. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Java 8 to Java 21 Spring Boot migration, identify a requirement involving "Platform vs virtual threads". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess runtime compatibility, preview-feature reliance and library upgrades. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate platform vs virtual threads with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Java 8 to Java 21 Spring Boot migration?

---

## #44 How migrate Java 8 to 21?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Review dependencies, reflection/module encapsulation, GC, testing, build tools and runtime behavior. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in language modernization: choose the mechanism when its specific guarantees solve a real requirement in a Java 8 to Java 21 Spring Boot migration. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a Java 8 to Java 21 Spring Boot migration, identify a requirement involving "How migrate Java 8 to 21". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess runtime compatibility, preview-feature reliance and library upgrades. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate how migrate java 8 to 21 with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a Java 8 to Java 21 Spring Boot migration?

---
