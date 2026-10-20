# Angular & TypeScript

20 questions · Source: existing interview portal question bank.

> These are concise revision cues, not exhaustive explanations. Verify behavior against the version you use.

## 122. Angular component lifecycle?

**Priority:** High

**Answer cue:** Constructor, ngOnInit, ngOnChanges, ngOnDestroy and render hooks.

**Practice:** Explain an example, a failure mode, and an alternative.

## 123. Standalone components vs NgModules?

**Priority:** High

**Answer cue:** Standalone imports dependencies directly; NgModules group legacy declarations.

**Practice:** Explain an example, a failure mode, and an alternative.

## 124. Change detection and OnPush?

**Priority:** High

**Answer cue:** Check strategies; immutable inputs, signals and observable emissions.

**Practice:** Explain an example, a failure mode, and an alternative.

## 125. Signals vs RxJS Observables?

**Priority:** High

**Answer cue:** Signals model synchronous reactive state; RxJS streams async events.

**Practice:** Explain an example, a failure mode, and an alternative.

## 126. Subject vs BehaviorSubject vs ReplaySubject?

**Priority:** High

**Answer cue:** No replay, latest value replay, configurable history replay.

**Practice:** Explain an example, a failure mode, and an alternative.

## 127. switchMap vs mergeMap vs concatMap vs exhaustMap?

**Priority:** High

**Answer cue:** Cancel prior, concurrent, sequential, ignore while busy.

**Practice:** Explain an example, a failure mode, and an alternative.

## 128. Async pipe and subscription cleanup?

**Priority:** High

**Answer cue:** Template subscription lifecycle; takeUntilDestroyed for imperative subscriptions.

**Practice:** Explain an example, a failure mode, and an alternative.

## 129. Reactive vs template-driven forms?

**Priority:** High

**Answer cue:** Explicit model/testability vs simpler template-managed forms.

**Practice:** Explain an example, a failure mode, and an alternative.

## 130. Custom validators and async validators?

**Priority:** High

**Answer cue:** Sync/async validation functions; manage pending and errors.

**Practice:** Explain an example, a failure mode, and an alternative.

## 131. Route guards and lazy loading?

**Priority:** Medium

**Answer cue:** Client navigation UX, not a replacement for server authorization.

**Practice:** Explain an example, a failure mode, and an alternative.

## 132. HTTP interceptors?

**Priority:** Medium

**Answer cue:** Cross-cutting request headers, errors, tracing; avoid token leaks.

**Practice:** Explain an example, a failure mode, and an alternative.

## 133. Angular authentication and token storage?

**Priority:** Medium

**Answer cue:** OIDC/PKCE; consider BFF HttpOnly cookies, CSRF and XSS risks.

**Practice:** Explain an example, a failure mode, and an alternative.

## 134. Content projection vs ViewChild?

**Priority:** Medium

**Answer cue:** Reusable projected content vs references to template children.

**Practice:** Explain an example, a failure mode, and an alternative.

## 135. trackBy / @for track and rendering?

**Priority:** Medium

**Answer cue:** Stable identity reduces unnecessary DOM work.

**Practice:** Explain an example, a failure mode, and an alternative.

## 136. Pure vs impure pipes?

**Priority:** Medium

**Answer cue:** Pure reruns on input reference/value changes; impure every check.

**Practice:** Explain an example, a failure mode, and an alternative.

## 137. TypeScript interface vs type alias?

**Priority:** Medium

**Answer cue:** Both describe types; interfaces support declaration merging.

**Practice:** Explain an example, a failure mode, and an alternative.

## 138. Generics, union and discriminated unions?

**Priority:** Medium

**Answer cue:** Reusable type parameters and safe variants.

**Practice:** Explain an example, a failure mode, and an alternative.

## 139. Angular performance troubleshooting?

**Priority:** Medium

**Answer cue:** Profiling, lazy routes, OnPush, virtual scrolling, request caching.

**Practice:** Explain an example, a failure mode, and an alternative.

## 140. State management service vs NgRx?

**Priority:** Medium

**Answer cue:** Choose by complexity, shared state and debugging needs.

**Practice:** Explain an example, a failure mode, and an alternative.

## 141. Unit tests and component integration tests?

**Priority:** Medium

**Answer cue:** Test behavior, services, HTTP mocking, accessibility.

**Practice:** Explain an example, a failure mode, and an alternative.
