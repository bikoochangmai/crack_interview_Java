# Mock interview: Behavioral

Attempt each prompt before expanding/reading its solution. These are original model answers, not alleged company questions or claimed personal experiences. For behavioral/day-to-day examples, fill the structure with facts from your own work. Banking designs are engineering exercises; actual rail, security and control requirements must be established with the responsible owners.

[All mock rounds](README.md) · [LLD / HLD paths](../lld-hld-learning-path.md)

## 30. Tell me about a time you pushed back on a risky change

### Interview prompt and example

Use a real event from your work; the structure below is a template, not a fabricated personal story.

### Situation and stakes

Describe the actual change, your responsibility and the specific customer/business invariant at risk. State what you knew then and what was uncertain. Avoid disclosing confidential customer details.

### Action with evidence

Explain how you tested or demonstrated the risk, who you involved and the concrete alternative you proposed. For example, an actual retry/idempotency concern should be supported by the real failure experiment or review finding, not a hypothetical claim presented as history.

### Decision and outcome

Describe how the decision was made, what shipped or changed, and the observed result. Use only real measurements; if an incident was avoided, do not pretend you can measure a counterfactual loss precisely. Credit collaborators and own any mistake in your own analysis.

### Reflection

Explain what you would repeat or improve: earlier invariants, smaller rollout, better failure tests or escalation timing. A strong answer shows constructive disagreement and accountability, not that you always won the argument.

### Interviewer follow-ups

- What evidence changed someone’s mind?

- What would you do if the owner accepted the risk anyway?

## 31. Describe a production incident you owned end to end

### Interview prompt and example

Choose an incident you actually handled and clearly distinguish your work from the team’s.

### Establish impact and timeline

Give the observed customer impact, detection signal and your role. Explain what was known at each stage rather than narrating with hindsight. State actual duration/scope only if you can substantiate it.

### Contain before speculating

Describe triage, ownership, communications and the reversible containment/rollback decision. Explain how you preserved evidence and avoided risky fixes while uncertain. Customer updates should separate confirmed facts from hypotheses.

### Recover and verify

Explain the fix or rollback, data reconciliation if applicable and how you verified the real user journey recovered. A green dashboard or restarted process alone may not prove correctness. Mention follow-up on stuck/duplicate operations if that happened in your real incident.

### Learn and close

Summarize contributing causes without blame, concrete owners/actions, and how their effectiveness was checked. Be candid about decisions you would change and avoid claiming sole credit for a coordinated response.

### Interviewer follow-ups

- How did you know recovery was correct, not merely available?

- Which follow-up action actually changed the next incident outcome?

## 32. How do you balance speed with compliance requirements?

### Interview prompt and example

Answer through a real delivery decision and your organization’s actual controls, not a promise to bypass requirements.

### Frame the trade-off

Identify the actual delivery goal, data/action risk, mandatory controls and accountable policy owners. Separate hard requirements from a process habit that can be improved. Do not give legal interpretations beyond your role.

### Move fast within safe boundaries

Offer a smaller scope, staged rollout, read-only release, synthetic-data prototype or automated evidence/test path that preserves required controls. Involve security/compliance reviewers early enough to change the design rather than ask for a rubber stamp at the end.

### Make the decision reviewable

Record the control mapping, test evidence, residual risk, approvals required by policy and rollback/operating plan. A deadline or an AI recommendation does not itself authorize an exception. Escalate a genuine unresolved conflict to the accountable owner.

### Use an honest outcome

Describe what your real team delivered, what was deferred, the actual customer/control result and what process improvement carried forward. The lesson should show proportionate rigor and good judgment, not speed versus safety as a false binary.

### Interviewer follow-ups

- Which part of the process did you automate without weakening the control?

- What would you refuse to trade away for the deadline?
