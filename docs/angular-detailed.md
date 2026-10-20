# Angular & TypeScript — Interview Study Guide

20 questions. Java examples use Java 21 unless noted; Angular and SQL snippets are labeled by language.

> **Quality note:** Entries marked “Guided study” include the original answer cue and a production discussion exercise; they are not yet fully curated standalone explanations.

## #122 Angular component lifecycle?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Constructor, ngOnInit, ngOnChanges, ngOnDestroy and render hooks. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in reactive client behavior: choose the mechanism when its specific guarantees solve a real requirement in an Angular audit dashboard backed by Spring Boot. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an Angular audit dashboard backed by Spring Boot, identify a requirement involving "Angular component lifecycle". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess stale UI state, memory leaks and client-only security assumptions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate angular component lifecycle with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an Angular audit dashboard backed by Spring Boot?

---

## #123 Standalone components vs NgModules?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Standalone imports dependencies directly; NgModules group legacy declarations. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in reactive client behavior: choose the mechanism when its specific guarantees solve a real requirement in an Angular audit dashboard backed by Spring Boot. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an Angular audit dashboard backed by Spring Boot, identify a requirement involving "Standalone components vs NgModules". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess stale UI state, memory leaks and client-only security assumptions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate standalone components vs ngmodules with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an Angular audit dashboard backed by Spring Boot?

---

## #124 Change detection and OnPush?

**Priority:** High · **Status:** Expanded

### Concept
OnPush reduces Angular change detection work by checking components under specific triggers, including changed inputs and relevant events or reactive notifications.

### Why / when
Use it for large tables and nested dashboards with immutable inputs.

### Production example
An audit findings list receives new immutable page data instead of mutating an existing array in place.

### Code example
```typescript
@Component({selector:"audit-list", changeDetection: ChangeDetectionStrategy.OnPush, template:"..."})
export class AuditListComponent {}
```

### Trade-offs and failure modes
Mutating an object without notifying Angular may leave stale UI; profile before optimizing.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #125 Signals vs RxJS Observables?

**Priority:** High · **Status:** Expanded

### Concept
Angular signals model synchronous reactive state; RxJS Observables model asynchronous streams, cancellation and composition over time.

### Why / when
Use signals for local UI state and RxJS for HTTP, websocket and event pipelines.

### Production example
A compliance dashboard uses a signal for selected tab and switchMap for a server-side search query.

### Code example
```typescript
readonly selectedTab = signal("open");
readonly results$ = this.query$.pipe(
  debounceTime(250), switchMap(q => this.api.search(q))
);
```

### Trade-offs and failure modes
Do not replace every Observable with a signal; cancellation and stream operators remain useful.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #126 Subject vs BehaviorSubject vs ReplaySubject?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
No replay, latest value replay, configurable history replay. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in reactive client behavior: choose the mechanism when its specific guarantees solve a real requirement in an Angular audit dashboard backed by Spring Boot. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an Angular audit dashboard backed by Spring Boot, identify a requirement involving "Subject vs BehaviorSubject vs ReplaySubject". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess stale UI state, memory leaks and client-only security assumptions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate subject vs behaviorsubject vs replaysubject with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an Angular audit dashboard backed by Spring Boot?

---

## #127 switchMap vs mergeMap vs concatMap vs exhaustMap?

**Priority:** High · **Status:** Expanded

### Concept
switchMap cancels previous inner subscriptions, mergeMap runs concurrently, concatMap serializes, and exhaustMap ignores new emissions while one is active.

### Why / when
Choose based on desired concurrency semantics, not stylistic preference.

### Production example
Use switchMap for search-as-you-type, concatMap for ordered uploads, exhaustMap to ignore repeated login clicks.

### Code example
```typescript
search$.pipe(debounceTime(300), switchMap(q => http.get("/api/search", {params:{q}})));
```

### Trade-offs and failure modes
switchMap is dangerous for must-complete writes; canceling a client subscription does not guarantee server rollback.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #128 Async pipe and subscription cleanup?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Template subscription lifecycle; takeUntilDestroyed for imperative subscriptions. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in reactive client behavior: choose the mechanism when its specific guarantees solve a real requirement in an Angular audit dashboard backed by Spring Boot. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an Angular audit dashboard backed by Spring Boot, identify a requirement involving "Async pipe and subscription cleanup". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess stale UI state, memory leaks and client-only security assumptions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate async pipe and subscription cleanup with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an Angular audit dashboard backed by Spring Boot?

---

## #129 Reactive vs template-driven forms?

**Priority:** High · **Status:** Expanded

### Concept
Reactive forms define controls and validators in TypeScript; template-driven forms primarily configure them in templates.

### Why / when
Choose reactive forms for complex conditional validation and enterprise forms.

### Production example
An audit approval form requires reason text when an exception is granted.

### Code example
```typescript
form = new FormGroup({
  reason: new FormControl("", {nonNullable:true, validators:[Validators.required]})
});
```

### Trade-offs and failure modes
Client-side validation is UX only; validate all business rules again in Spring Boot.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #130 Custom validators and async validators?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Sync/async validation functions; manage pending and errors. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in reactive client behavior: choose the mechanism when its specific guarantees solve a real requirement in an Angular audit dashboard backed by Spring Boot. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an Angular audit dashboard backed by Spring Boot, identify a requirement involving "Custom validators and async validators". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess stale UI state, memory leaks and client-only security assumptions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate custom validators and async validators with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an Angular audit dashboard backed by Spring Boot?

---

## #131 Route guards and lazy loading?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Client navigation UX, not a replacement for server authorization. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in reactive client behavior: choose the mechanism when its specific guarantees solve a real requirement in an Angular audit dashboard backed by Spring Boot. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an Angular audit dashboard backed by Spring Boot, identify a requirement involving "Route guards and lazy loading". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess stale UI state, memory leaks and client-only security assumptions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate route guards and lazy loading with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an Angular audit dashboard backed by Spring Boot?

---

## #132 HTTP interceptors?

**Priority:** Medium · **Status:** Expanded

### Concept
HTTP interceptors transform outgoing requests and incoming responses in a centralized pipeline.

### Why / when
Use them for correlation IDs, auth headers and consistent error translation.

### Production example
Angular adds X-Correlation-ID so a failed approval can be traced through Spring Boot and Kafka consumers.

### Code example
```typescript
export const correlationInterceptor: HttpInterceptorFn = (req,next) =>
  next(req.clone({setHeaders:{"X-Correlation-ID":crypto.randomUUID()}}));
```

### Trade-offs and failure modes
Avoid infinite retry loops; never log access tokens or sensitive response bodies.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #133 Angular authentication and token storage?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
OIDC/PKCE; consider BFF HttpOnly cookies, CSRF and XSS risks. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in reactive client behavior: choose the mechanism when its specific guarantees solve a real requirement in an Angular audit dashboard backed by Spring Boot. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an Angular audit dashboard backed by Spring Boot, identify a requirement involving "Angular authentication and token storage". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess stale UI state, memory leaks and client-only security assumptions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate angular authentication and token storage with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an Angular audit dashboard backed by Spring Boot?

---

## #134 Content projection vs ViewChild?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Reusable projected content vs references to template children. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in reactive client behavior: choose the mechanism when its specific guarantees solve a real requirement in an Angular audit dashboard backed by Spring Boot. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an Angular audit dashboard backed by Spring Boot, identify a requirement involving "Content projection vs ViewChild". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess stale UI state, memory leaks and client-only security assumptions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate content projection vs viewchild with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an Angular audit dashboard backed by Spring Boot?

---

## #135 trackBy / @for track and rendering?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Stable identity reduces unnecessary DOM work. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in reactive client behavior: choose the mechanism when its specific guarantees solve a real requirement in an Angular audit dashboard backed by Spring Boot. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an Angular audit dashboard backed by Spring Boot, identify a requirement involving "trackBy / @for track and rendering". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess stale UI state, memory leaks and client-only security assumptions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate trackby / @for track and rendering with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an Angular audit dashboard backed by Spring Boot?

---

## #136 Pure vs impure pipes?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Pure reruns on input reference/value changes; impure every check. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in reactive client behavior: choose the mechanism when its specific guarantees solve a real requirement in an Angular audit dashboard backed by Spring Boot. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an Angular audit dashboard backed by Spring Boot, identify a requirement involving "Pure vs impure pipes". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess stale UI state, memory leaks and client-only security assumptions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate pure vs impure pipes with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an Angular audit dashboard backed by Spring Boot?

---

## #137 TypeScript interface vs type alias?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Both describe types; interfaces support declaration merging. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in reactive client behavior: choose the mechanism when its specific guarantees solve a real requirement in an Angular audit dashboard backed by Spring Boot. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an Angular audit dashboard backed by Spring Boot, identify a requirement involving "TypeScript interface vs type alias". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess stale UI state, memory leaks and client-only security assumptions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate typescript interface vs type alias with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an Angular audit dashboard backed by Spring Boot?

---

## #138 Generics, union and discriminated unions?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Reusable type parameters and safe variants. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in reactive client behavior: choose the mechanism when its specific guarantees solve a real requirement in an Angular audit dashboard backed by Spring Boot. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an Angular audit dashboard backed by Spring Boot, identify a requirement involving "Generics, union and discriminated unions". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess stale UI state, memory leaks and client-only security assumptions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate generics, union and discriminated unions with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an Angular audit dashboard backed by Spring Boot?

---

## #139 Angular performance troubleshooting?

**Priority:** Medium · **Status:** Expanded

### Concept
Angular performance problems may arise from oversized bundles, unnecessary change detection, expensive template functions or rendering huge lists.

### Why / when
Profile first, then use lazy routes, track keys, OnPush, virtual scrolling or memoization as justified.

### Production example
A 20,000-row audit table renders only visible rows and pages results from the API.

### Code example
```typescript
@for (finding of findings(); track finding.id) {
  <app-finding-row [finding]="finding" />
}
```

### Trade-offs and failure modes
Track keys must be stable; excessive client-side data loading wastes memory and bandwidth.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #140 State management service vs NgRx?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Choose by complexity, shared state and debugging needs. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in reactive client behavior: choose the mechanism when its specific guarantees solve a real requirement in an Angular audit dashboard backed by Spring Boot. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an Angular audit dashboard backed by Spring Boot, identify a requirement involving "State management service vs NgRx". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess stale UI state, memory leaks and client-only security assumptions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate state management service vs ngrx with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an Angular audit dashboard backed by Spring Boot?

---

## #141 Unit tests and component integration tests?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Test behavior, services, HTTP mocking, accessibility. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in reactive client behavior: choose the mechanism when its specific guarantees solve a real requirement in an Angular audit dashboard backed by Spring Boot. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In an Angular audit dashboard backed by Spring Boot, identify a requirement involving "Unit tests and component integration tests". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess stale UI state, memory leaks and client-only security assumptions. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate unit tests and component integration tests with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in an Angular audit dashboard backed by Spring Boot?

---
