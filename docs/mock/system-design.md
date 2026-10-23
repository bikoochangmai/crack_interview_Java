# Mock interview: System Design

Attempt each prompt before expanding/reading its solution. These are original model answers, not alleged company questions or claimed personal experiences. For behavioral/day-to-day examples, fill the structure with facts from your own work. Banking designs are engineering exercises; actual rail, security and control requirements must be established with the responsible owners.

[All mock rounds](README.md) · [LLD / HLD paths](../lld-hld-learning-path.md)

## 13. Design payment processing with idempotent transfers

### Interview prompt and example

Alice requests transfer T81 of 5,000 paise from authorized account A to account B; the client loses the response after commit.

### Begin with invariants and ownership

Clarify whether this is an internal same-ledger transfer or an external rail. For a same-currency internal transfer, accepted postings must balance, the caller may debit only authorized accounts, and one logical request must not create duplicate postings. Represent currency explicitly and use bounded integer minor units or an appropriate decimal money type, never binary floating-point for ledger amounts.

### API and data contract

POST /transfers carries source, destination, amount, currency and a stable idempotency key. Derive actor/tenant from verified credentials, verify debit permission and limits, and bind the key to the operation’s payload fingerprint. Store Transfer, immutable balanced Posting records, account concurrency state and an outbox event. Retain idempotency results under a documented policy.

### Follow the local transaction

Claim the scoped key under a unique constraint. Lock/serialize affected account state in a consistent order or use an equivalent guarded transactional design, validate available funds, write balanced postings and update the chosen balance projection with the transfer/result/outbox in one transaction. Retry serialization/deadlock failures within bounds using the same logical identity. A pre-transaction balance read is not sufficient.

### Handle the lost response

If commit succeeded, retrying T81 returns the recorded result. Concurrent same-key calls must not both execute the transfer. A different payload with the same key conflicts. If outcome is unknown after timeout, query by operation identity; do not create a fresh key and assume failure.

### External rails need another protocol

A remote bank/provider cannot share an ordinary local database commit. Record a pending instruction, deliver through a recoverable outbox/worker, use a stable provider reference and reconcile authenticated confirmations and statement data. Model PENDING/UNKNOWN/CONFIRMED/FAILED explicitly; reversals are new recorded postings, not deletion of history. A webhook or browser return URL alone is not sufficient evidence without its authenticity/state checks.

### Observe and test

Test simultaneous retries, competing debits, insufficient funds, crash before/after commit, lost provider acknowledgement and duplicate/out-of-order confirmations. Reconcile ledger versus balance projections and external statements. Monitor unbalanced journals, pending age, duplicate conflicts and reconciliation breaks. Scaling the service must preserve one authoritative account/transfer decision boundary; sharding adds cross-boundary coordination, not free atomicity.

### Interviewer follow-ups

- What does successful mean for an internal versus external transfer?

- How do you avoid deadlock when two transfers involve the same accounts in reverse order?

## 14. Design a real-time fraud detection pipeline

### Interview prompt and example

Transfer T81 reaches authorization while device and velocity signals may be stale; a decision must arrive within a bounded deadline.

### Define decision responsibility

Separate fast authorization-time risk decision from asynchronous investigation/retraining. Decide which events require block, step-up, hold or a documented fallback; availability of a model is not permission to approve every unknown transfer. A risk score is evidence for a policy decision, not an authenticated instruction to move money.

### Ingest trusted events

Record stable event ID, tenant/account scope, event and ingestion times, schema version and relevant verified signals. Authenticate producer workloads and minimize sensitive data. Stream ingestion must tolerate retries and out-of-order delivery. A transactional source outbox prevents a fraud event representing a transfer that never committed where the flow requires committed events.

### Build and read features

A stream processor updates windowed velocity/device/account features with explicit late-event and deduplication rules. The decision service reads a versioned feature snapshot, records feature freshness and calls a bounded rules/model evaluation. Keep event-time versus processing-time semantics visible; replaying an event must not double the velocity count.

### Make a bounded, auditable decision

Within the endpoint deadline, combine deterministic rules, model/version, available features and policy version into an allow/block/step-up/hold result. Store reason codes and input evidence references that explain the actual decision; do not fabricate a human-readable justification after the fact. Human review and customer-facing messaging have separate access and privacy requirements.

### Failures, safety and drift

If model/feature access times out, choose a preapproved conservative rules path, hold/step-up or unavailable result depending on transaction risk. Mark missing/stale features rather than substituting zero silently. Monitor false-positive rates, confirmed fraud, feature lag, model calibration and cohort performance. Delayed labels and adversarial behavior complicate evaluation; raw approval rate alone is insufficient.

### Validation and scale

Replay fixed historical/test event sequences with deduplication, late data and stale features. Test endpoint deadlines, tenant isolation, replay determinism for recorded versions and malformed producer events. Partition feature updates by a key appropriate to the rule, recognizing that cross-account/device aggregation may require another stage. Keep an asynchronous investigation/retraining pipeline from becoming a synchronous dependency for every transfer.

### Interviewer follow-ups

- What happens if a velocity feature is ten minutes stale?

- Which decision artifacts let an investigator reproduce the applied policy?

## 15. Design trade settlement and reconciliation

### Interview prompt and example

An executed trade requires cash/securities obligations; one settlement confirmation arrives twice and a statement arrives late.

### Separate execution from settlement

An order-book fill is not proof assets and cash have settled. Record executed trade identity and contractual obligations, relevant parties, instrument/currency, amounts, lifecycle and business-date/calendar semantics. Settlement timing and rules vary by market; clarify them rather than assume one global schedule.

### Create durable obligations

Consume authenticated execution events with stable trade IDs; deduplicate and validate them, create versioned obligations and outbox instructions transactionally. Apply reference data and configured calendars/cutoffs using explicit time zones. Keep amendments/cancellations as versioned events with allowed transitions instead of overwriting the original evidence.

### Process external instructions

Workers submit instructions to the chosen custodian/clearing/settlement infrastructure with stable references. Authenticate and deduplicate confirmations. Model pending, matched, settled, failed and unknown states according to that rail’s contract. A timeout is not proof of rejection; reconcile before resending in a way that could duplicate settlement.

### Reconcile three views

Compare internal trade/obligation/ledger state, external confirmations and authoritative statements/positions using declared identifiers, amounts, currency, value date and version. Classify missing, duplicate, quantity/amount and timing breaks. Do not fuzzy-match ambiguous records into an automatic clean status merely to make totals agree.

### Resolve breaks with controls

Create a durable case with evidence and assigned owner. Automated safe retries and authorized manual repair require explicit policy, audit and appropriate separation of duties. Use adjustment/reversal records rather than deleting history. Late statements should update reconciliation state idempotently and may reopen a previously provisional comparison.

### Test recovery and reporting

Test duplicate instructions/confirmations, partial settlement where supported, calendar boundaries, late files, mismatched currency, ambiguous matches and restart during a batch. Version input files and reconciliation rules; checkpoint progress with sink idempotency. Report pending age, unreconciled exposure and break counts without labeling a matched instruction as finally settled unless the evidence supports it.

### Interviewer follow-ups

- How is a trade marked settled if one confirmation is missing?

- Why can two matching aggregate totals still conceal individual reconciliation breaks?

## 16. Design an audit log that cannot be tampered with

### Interview prompt and example

A privileged operator tries to modify or delete an earlier payment event and conceal that change.

### Challenge the absolute guarantee

Define the attacker and trust boundaries. No ordinary application table is absolutely tamper-proof against every administrator and compromised key. Aim for append-only access controls, independently verifiable tamper evidence, protected retention and monitored custody. Explain exactly which principals and failure modes the design resists.

### Record structured facts

Capture stable event ID, actor/workload identity, tenant, action, target, before/after references where appropriate, outcome, correlation ID, timestamp and schema/version. Avoid copying secrets or unnecessary personal data. Bind business-state changes and audit intent using a transactional outbox where possible; audit omissions also matter.

### Make modification detectable

An ordered stream can hash each canonically encoded event with the prior hash and sequence. Sign/anchor checkpoints in an independently controlled destination so rewriting an entire local chain or truncating its tail is detectable. Protect signing keys, rotate with verification metadata and define clock/ordering semantics. A hash chain alone does not stop an attacker who can rewrite all records and all anchors.

### Protect retention and access

Write protected object versions to an appropriate WORM/retention store with separate writer, reader and retention-administration privileges. Choose retention/hold rules with the responsible compliance team. For example, object-lock protections apply to specified object versions; a new object version/delete marker does not mean the protected version changed. Governance versus stricter retention modes have different bypass behavior.

### Verify and investigate

Run independent sequence/checkpoint/hash/signature verification, alert on gaps and failed writes, and keep redundant custody/backups. Auditors query an authorized index while verifying evidence against the protected source; rebuilding a search index must not rewrite original history. Access to the audit service itself is audited through a separate appropriate boundary.

### Failure and acceptance tests

Test attempted overwrite/delete, missing sequence, altered payload, chain rewrite without anchor authority, truncated tail, key rotation, clock anomalies and an unavailable archive. Decide which sensitive business operations must fail or durably buffer if required audit capture cannot be guaranteed. Do not return compliance assurances based solely on using a named storage product.

### Interviewer follow-ups

- How would you detect an attacker deleting the newest 100 events?

- What if the application and its signing key are both compromised?

## Reference documentation

- [PostgreSQL isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- [Object Lock version and retention boundaries](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)
