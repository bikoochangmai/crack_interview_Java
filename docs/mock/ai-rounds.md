# Mock interview: AI Rounds

Attempt each prompt before expanding/reading its solution. These are original model answers, not alleged company questions or claimed personal experiences. For behavioral/day-to-day examples, fill the structure with facts from your own work. Banking designs are engineering exercises; actual rail, security and control requirements must be established with the responsible owners.

[All mock rounds](README.md) · [LLD / HLD paths](../lld-hld-learning-path.md)

## 20. Use an AI assistant in a coding round, then explain every line it wrote

### Interview prompt and example

The interviewer permits AI for an LRU implementation but asks you to defend the algorithm and every state change.

### A strong workflow

First clarify capacity, null/miss behavior, recency rules, concurrency and complexity. Write invariants yourself before prompting. Ask for a small implementation against that contract rather than accepting an unexplained large solution. Treat generated code as an untrusted proposal.

### Explain line by line

For every field, method and pointer assignment, state its role in the invariant. Explain why map lookup avoids list search, why detaching changes both neighboring links, why a successful get mutates order, and why eviction removes both indexes. If you cannot explain a line or dependency, simplify, investigate or remove it before claiming ownership.

### Verify independently

Compile, run sample and boundary cases, then compare deterministic generated operations against an independent access-ordered reference model. Test capacity zero/one, repeated updates and concurrent access if promised. Report which checks actually ran and their limits; a model’s assertion that tests passed is not evidence.

### Interview evidence

Show the final code, a short before/after correction, the tests that caught it, complexity reasoning and a limitation. Do not paste secrets or proprietary production code into an unapproved tool. The evaluation is your reasoning and verified result, not the model’s fluency.

### Interviewer follow-ups

- Explain why detach must update both next and prev.

- What evidence would convince you the implementation is wrong?

## 21. The AI solution passes samples: find an input that breaks it

### Interview prompt and example

A generated Two Sum implementation inserts the current value into seen before looking up its complement.

### Find the violated invariant

The map must contain only earlier indices when testing the current index. Inserting first lets the same element satisfy its own complement. Construct a valid problem instance where this produces an invalid answer before the legitimate pair is reached.

### Minimal useful counterexample

nums=[3,2,4], target=6 has the legitimate answer [1,2]. The broken insert-before-check code sees current 3 in the map at i=0 and returns [0,0]. This is within the usual exactly-one-solution contract and does not rely on a forbidden singleton input.

### Fix and broaden

Look up the complement before inserting. Then test [3,3] target 6, negatives, a pair at the end and integer-overflow boundaries with widened complement arithmetic. Compare small random inputs to a brute-force oracle under the same input assumptions; validate returned indices and sums rather than requiring one arbitrary ordering.

### Generalize the method

List assumptions, derive an invariant, target each boundary and minimize a failure. For distributed code, include crash windows and concurrent retries; for authorization, test another tenant’s valid ID. Passing samples proves only those samples, not the contract.

### Interviewer follow-ups

- Why is [3,2,4] more convincing than an input outside the stated constraints?

- Which property should a valid returned pair satisfy?

## 22. Walk through how you use AI day to day

### Interview prompt and example

Answer with a real engineering task, not a list of tool names. Adapt this structure to your actual experience.

### Describe one concrete task

State the input, goal and constraints: for example reviewing an unfamiliar module or drafting boundary tests for a parser. Explain what information you were permitted to share, how you narrowed scope and what success would look like. Do not invent a project or production outcome.

### Describe the division of work

Explain what you decided yourself, what the assistant proposed and which parts you rejected or changed. A useful example is asking for candidate edge cases, independently identifying the invariant, then checking which suggestions are valid against the contract.

### Give evidence and limitations

Show a diff/test or other permitted artifact, the verification performed, the actual result and a case where AI was wrong. Mention review, sensitive-data handling and dependency/version verification when relevant. If you measured time or defect reduction, give the actual measurement method rather than an invented percentage.

### Answer shape

Use: task → constraints → AI contribution → my reasoning/correction → independent verification → observed outcome → limitation/lesson. Tool names can be context but cannot replace those facts.

### Interviewer follow-ups

- What was the last incorrect suggestion you caught?

- Which artifact demonstrates your own judgment?

## 23. What would you never let AI write in a banking codebase, and why?

### Interview prompt and example

Distinguish drafting assistance from authority to approve or execute a change.

### State the boundary

I would not allow an AI agent to independently decide or deploy money movement, authorization rules, cryptographic/key management, destructive data repair or retention policy. These operations require accountable owners, explicit invariants, threat analysis and approved operational controls. This is a model policy answer; adapt it to your organization’s actual process.

### Allow bounded assistance

AI may help draft tests, documentation or candidate implementations in approved environments, but generated critical code is reviewed and verified to the same or stricter standard as human code. No copied secrets/customer records, unapproved dependencies, bypassed review or production credentials. A blanket claim that AI can never draft any financial-code line misses the authority/verification distinction.

### Explain the risk concretely

A plausible retry wrapper can double-charge after a timeout; a missing tenant condition can leak accounts; a fabricated crypto construction can destroy confidentiality. Evidence must cover concurrency, failure/recovery and access boundaries, not just unit-test coverage or a convincing explanation.

### Operational control

Separate read-only assistance from tool execution. Require authorized human approval for sensitive actions, auditable changes, staged rollout and a tested recovery plan. The assistant cannot self-authorize because it wrote a reassuring comment.

### Interviewer follow-ups

- Could AI draft a ledger unit test? What additional review would you require?

- Why is removing production credentials from the agent important even with a strong system prompt?

## 24. Review a 500-line AI-generated PR touching payments

### Interview prompt and example

A teammate proposes a broad payments refactor with green sample tests and a confident generated description.

### Reduce review scope

Ask for the business trigger, before/after behavior, changed invariants and a decomposition into reviewable commits if needed. Read the diff and entry points yourself. A 500-line change is neither safe nor unsafe merely because of its author; complexity and money-effect boundaries determine the review depth.

### Trace effects and failure windows

Follow request identity, actor/tenant checks, amount/currency representation, ledger balance, concurrency and external provider calls. Look for changed idempotency scope/retention, new retries, swallowed exceptions, lock/transaction changes, migration/backfill effects and callback ordering. Treat a timeout as potentially committed until proved otherwise.

### Demand targeted evidence

Run meaningful tests for simultaneous retries, lost responses after commit, duplicate callbacks, conflicting payloads, insufficient funds and unauthorized account IDs. Compare expected postings and actual durable state. Inspect dependencies/migrations and ensure tests do not mock away the boundary at risk.

### Decide and release deliberately

Block unexplained or unverified critical behavior; give actionable findings rather than accusing the author. Approve only the understood change with appropriate owners, rollout observability, reconciliation and rollback/compensation plan. Record what was verified and what remains uncertain. A model-written PR summary is not independent review evidence.

### Interviewer follow-ups

- What would make you split or reject the PR?

- Which new retry can create a duplicate charge despite all existing tests passing?

## 25. Design an account assistant without leaking another customer’s data

### Interview prompt and example

Alice asks about her transactions while the model has access to account-query tools.

### Place authority outside the model

Authenticate Alice at the API and bind a server-controlled subject/tenant context to the conversation. Tools accept only narrowly scoped operations; the server resolves allowed accounts from that context. Do not let the model select an arbitrary tenant/user by emitting a parameter, SQL statement or invented role.

### Retrieve only permitted evidence

A transaction tool validates account ownership on every call and returns a minimal bounded result. Document retrieval filters tenant/ACL before content reaches the model. Cache keys include relevant subject/permission/version context. Conversation IDs, exports and citations also require authorization; merely hiding another account in the UI is not isolation.

### Generate with least privilege

The model summarizes approved tool results and can abstain when evidence is missing. Read-only support is a safer initial scope than autonomous transfers. Any sensitive action needs separate explicit authorization, confirmation and business-state checks independent of generated text.

### Test and observe

Use two customers with deliberately colliding account/document IDs, swapped conversation references, malicious retrieved text and revoked access. Audit tool decisions and evidence references with redaction/access/retention controls. Output filtering is defense in depth, not a substitute for preventing unauthorized retrieval.

### Interviewer follow-ups

- What if the model emits accountId belonging to Bob?

- How do you scope caches and conversation history?

## 26. A user says ignore instructions and show all transactions: what stops it?

### Interview prompt and example

Assume prompts can be manipulated; preserve the authorization boundary even if the model follows the malicious request.

### Not just a stronger prompt

A system prompt explains intended behavior but cannot be the only confidentiality control. The API/tool layer must authorize against verified identity and object scope. If Alice’s tool can only query her permitted accounts, the text all transactions does not widen that authority.

### Layered controls

Use narrow tool schemas, validate parameters, bind trusted context outside model-controlled fields, and isolate untrusted retrieved/user content from instructions. Restrict tool/network credentials and avoid arbitrary SQL or generic internal fetch tools. Apply bounded result sizes and appropriate monitoring.

### Demonstrate denial

Run the exact attack, encoded/paraphrased variants and injection inside a retrieved document. Even if the model requests Bob’s account, the tool returns a permitted denial and no Bob records enter the prompt. Log the denial safely; do not expose protected content inside an error message.

### Be honest about residual risk

No prompt-injection filter guarantees universal model obedience. The security objective is that compromised model behavior cannot bypass independent data/action authorization. Review indirect leakage through summaries, citations, timing, logs and cached conversation state as well.

### Interviewer follow-ups

- How would the design behave if the model completely ignored the system prompt?

- Can a retrieval filter applied only after generation protect data already sent to the model?

## 27. Make LLM output auditable when asked why an answer was given

### Interview prompt and example

An authorized reviewer needs to trace a specific account-assistant response without exposing unrelated customer data.

### Record what actually determined the response

Use a correlation ID tying actor/tenant authorization, request time, prompt/template version, requested and resolved model/deployment/version where available, generation parameters, tool names/arguments/results or approved evidence references, retrieval document versions and final response together.

### Preserve evidence safely

Store necessary audit artifacts with encryption, role-based access, retention/redaction and integrity controls. Hashes can help verify evidence identity but cannot reconstruct deleted content; decide which permitted source snapshots/references must remain available for the audit purpose. Do not indiscriminately log secrets or full account data.

### Explain evidence, not private reasoning

Provide permitted source citations, tool outputs and policy/authorization decisions that support the final answer. Do not promise access to hidden model chain-of-thought or fabricate a post-hoc rationale as historical truth. An audit trail is evidence of the pipeline, not proof the model internally reasoned exactly as a generated explanation says.

### Account for reproducibility limits

Model nondeterminism, provider aliases and unavailable historical versions can prevent bit-for-bit regeneration. Pin/version what you can, retain actual output and evidence, and distinguish replaying recorded decisions from re-querying today’s model. Test retrieval/version continuity and evidence access for an auditor.

### Interviewer follow-ups

- What must be retained if the source policy later changes?

- Why is a model-generated explanation not sufficient historical evidence?

## 28. Your LLM provider times out at peak: what is the fallback?

### Interview prompt and example

A customer asks for an account balance while the model endpoint is slow.

### Bound the dependency

Apply an end-to-end deadline, bounded concurrency/queue, circuit breaker and tightly bounded retries with jitter where appropriate. Do not let every layer multiply retries. Cancellation may not stop provider-side work, so also track cost and orphaned requests.

### Choose a safe product fallback

For account facts, use a deterministic authorized account-service response or a clearly unavailable/try-again path; do not invent a balance. For general FAQs, use a versioned approved static answer when appropriate. Financial actions remain unavailable unless their independent authorized workflow can safely proceed without the model.

### Treat a second provider as a separate deployment decision

Fallback to another model/provider requires approved data handling, credential scope, residency/retention and quality evaluation, not an ad-hoc endpoint swap. Revalidate output behavior and tool constraints. A stale cached answer must be identity-scoped and permitted by a freshness policy; yesterday’s balance may be unacceptable.

### Test overload behavior

Simulate slow responses, partial tool success, reconnect/retry and failover. Monitor user-visible latency, errors, fallback usage, queue age and correctness separately. Explain what the user sees and which operations are deliberately refused.

### Interviewer follow-ups

- Why is a cached previous balance an unsafe universal fallback?

- How do you stop a retry storm from making the outage worse?

## 29. Answer quality dropped with zero code changes: what changed?

### Interview prompt and example

A stable application release suddenly gives worse answers on the same product area.

### Start with evidence and isolate the layer

Confirm the regression using a fixed, versioned evaluation set and real authorized cohorts. Separate retrieval failures, tool/data failures, generation errors and evaluation changes. A changed customer mix or label pipeline can look like a model regression.

### Inspect non-code dependencies

Check resolved model/deployment versions and moving aliases, prompt/config/feature-flag changes, retrieval corpus/index/chunking/embedding versions, ACL/tenant filtering, source freshness, tool schemas and API data. Check token/truncation budgets, provider routing/parameters and load-induced timeout/fallback rates. These are hypotheses to investigate, not assumed causes.

### Compare controlled snapshots

Compare last-good and current evidence under the same inputs; replay recorded tool/retrieval results to isolate generation and independently test retrieval recall. Track citations/faithfulness and refusal/error rates, not only a single average score. Redact/protect customer examples in the investigation.

### Recover and prevent recurrence

Roll back the identified version/config/index where safe, or use an approved fallback. Pin/version dependencies when possible and record resolved versions when not. Add canary evals and change alerts across the whole pipeline. Communicate the observed cause, scope and evidence instead of saying the model got moody.

### Interviewer follow-ups

- What artifact lets you distinguish a corpus change from a model change?

- Why can a permission fix reduce recall without being a regression?

## Reference documentation

- [OWASP prompt injection prevention](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)
- [OWASP tenant isolation](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html)
