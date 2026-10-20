# SQL, PostgreSQL & Database Design

25 questions · Source: existing interview portal question bank.

> These are concise revision cues, not exhaustive explanations. Verify behavior against the version you use.

## 97. Explain ACID with examples.

**Priority:** High

**Answer cue:** Atomicity, consistency, isolation, durability; e.g. transferring money.

**Practice:** Explain an example, a failure mode, and an alternative.

## 98. Primary key vs unique key vs foreign key?

**Priority:** High

**Answer cue:** Identity, uniqueness, and referential integrity.

**Practice:** Explain an example, a failure mode, and an alternative.

## 99. INNER vs LEFT vs FULL OUTER JOIN?

**Priority:** High

**Answer cue:** Matching rows, all left rows, all rows from both.

**Practice:** Explain an example, a failure mode, and an alternative.

## 100. WHERE vs HAVING?

**Priority:** High

**Answer cue:** Filter rows before grouping vs groups after aggregation.

**Practice:** Explain an example, a failure mode, and an alternative.

## 101. GROUP BY and aggregate functions?

**Priority:** High

**Answer cue:** Group rows for COUNT/SUM/AVG/MIN/MAX.

**Practice:** Explain an example, a failure mode, and an alternative.

## 102. Window functions ROW_NUMBER, RANK, DENSE_RANK?

**Priority:** High

**Answer cue:** Rank rows within partitions without collapsing them.

**Practice:** Explain an example, a failure mode, and an alternative.

## 103. Find second-highest salary?

**Priority:** High

**Answer cue:** Use DENSE_RANK over salaries and filter rank 2; define tie behavior.

**Practice:** Explain an example, a failure mode, and an alternative.

## 104. Find duplicate records?

**Priority:** High

**Answer cue:** GROUP BY key HAVING COUNT(*)>1; use ROW_NUMBER to identify extras.

**Practice:** Explain an example, a failure mode, and an alternative.

## 105. CTE vs subquery?

**Priority:** High

**Answer cue:** Named query expression vs inline nested query; optimizer-dependent performance.

**Practice:** Explain an example, a failure mode, and an alternative.

## 106. UNION vs UNION ALL?

**Priority:** Medium

**Answer cue:** UNION removes duplicates; UNION ALL preserves them.

**Practice:** Explain an example, a failure mode, and an alternative.

## 107. DELETE vs TRUNCATE vs DROP?

**Priority:** Medium

**Answer cue:** Delete rows, empty table, remove object; transaction semantics vary.

**Practice:** Explain an example, a failure mode, and an alternative.

## 108. Indexes and composite index order?

**Priority:** Medium

**Answer cue:** Speed selective reads with write/storage cost; leftmost prefix often matters.

**Practice:** Explain an example, a failure mode, and an alternative.

## 109. B-tree vs GIN vs GiST indexes?

**Priority:** Medium

**Answer cue:** General ordered lookups vs inverted/multidimensional access methods.

**Practice:** Explain an example, a failure mode, and an alternative.

## 110. EXPLAIN ANALYZE and slow SQL?

**Priority:** Medium

**Answer cue:** Inspect actual plans, row estimates, scans, join methods and timings.

**Practice:** Explain an example, a failure mode, and an alternative.

## 111. Transactions and isolation anomalies?

**Priority:** Medium

**Answer cue:** Dirty/nonrepeatable/phantom reads, lost updates, write skew; DB-specific.

**Practice:** Explain an example, a failure mode, and an alternative.

## 112. Optimistic vs pessimistic locking?

**Priority:** Medium

**Answer cue:** Version checks vs database locks; choose by contention.

**Practice:** Explain an example, a failure mode, and an alternative.

## 113. MVCC in PostgreSQL?

**Priority:** Medium

**Answer cue:** Row versions allow consistent reads while writers operate.

**Practice:** Explain an example, a failure mode, and an alternative.

## 114. Deadlocks in databases?

**Priority:** Medium

**Answer cue:** Conflicting lock order; detect/retry and enforce consistent ordering.

**Practice:** Explain an example, a failure mode, and an alternative.

## 115. Normalization 1NF/2NF/3NF vs denormalization?

**Priority:** Medium

**Answer cue:** Reduce anomalies vs optimize read models with controlled redundancy.

**Practice:** Explain an example, a failure mode, and an alternative.

## 116. Offset vs keyset pagination?

**Priority:** Medium

**Answer cue:** Offset easy but degrades/changes under writes; keyset efficient for stable order.

**Practice:** Explain an example, a failure mode, and an alternative.

## 117. Partitioning vs sharding vs replication?

**Priority:** Medium

**Answer cue:** Table partitioning, distributing data, copying data for availability/reads.

**Practice:** Explain an example, a failure mode, and an alternative.

## 118. Connection pooling and N+1 query issue?

**Priority:** Medium

**Answer cue:** Reuse connections; avoid per-row ORM queries using joins/fetch batching.

**Practice:** Explain an example, a failure mode, and an alternative.

## 119. JSONB vs relational columns?

**Priority:** Medium

**Answer cue:** Flexible indexed documents vs explicit constraints and relational modeling.

**Practice:** Explain an example, a failure mode, and an alternative.

## 120. PostgreSQL pgvector retrieval?

**Priority:** Medium

**Answer cue:** Embedding vector similarity search; choose indexes and filter permissions.

**Practice:** Explain an example, a failure mode, and an alternative.

## 121. Design schema for audit findings/approvals?

**Priority:** Medium

**Answer cue:** Foreign keys, tenant IDs, versioning, immutable audit trail and indexes.

**Practice:** Explain an example, a failure mode, and an alternative.
