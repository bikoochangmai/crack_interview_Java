# SQL, PostgreSQL & Database Design — Interview Study Guide

25 questions. Java examples use Java 21 unless noted; Angular and SQL snippets are labeled by language.

> **Quality note:** Entries marked “Guided study” include the original answer cue and a production discussion exercise; they are not yet fully curated standalone explanations.

## #97 Explain ACID with examples.

**Priority:** High · **Status:** Expanded

### Concept
ACID: atomicity groups writes, consistency preserves constraints, isolation controls concurrent transactions and durability retains committed data across crashes.

### Why / when
Use database transactions for orders, inventory reservations and approval state transitions.

### Production example
An audit approval inserts an approval row and changes finding status in one PostgreSQL transaction.

### Code example
```sql
BEGIN;
UPDATE findings SET status = 'APPROVED' WHERE id = 42;
INSERT INTO approvals(finding_id, approver_id) VALUES (42, 7);
COMMIT;
```

### Trade-offs and failure modes
ACID applies within a transaction boundary; external Kafka messages and HTTP calls require separate reliability patterns.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #98 Primary key vs unique key vs foreign key?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Identity, uniqueness, and referential integrity. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "Primary key vs unique key vs foreign key". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate primary key vs unique key vs foreign key with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #99 INNER vs LEFT vs FULL OUTER JOIN?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Matching rows, all left rows, all rows from both. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "INNER vs LEFT vs FULL OUTER JOIN". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate inner vs left vs full outer join with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #100 WHERE vs HAVING?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Filter rows before grouping vs groups after aggregation. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "WHERE vs HAVING". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate where vs having with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #101 GROUP BY and aggregate functions?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Group rows for COUNT/SUM/AVG/MIN/MAX. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "GROUP BY and aggregate functions". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate group by and aggregate functions with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #102 Window functions ROW_NUMBER, RANK, DENSE_RANK?

**Priority:** High · **Status:** Expanded

### Concept
Window functions calculate values across related rows without collapsing them into one row per group. ROW_NUMBER gives unique sequence, RANK leaves gaps on ties, DENSE_RANK does not.

### Why / when
Use them for latest event per document, leaderboards and top-N records per tenant.

### Production example
A compliance dashboard shows the newest audit finding for each document.

### Code example
```sql
SELECT * FROM (
  SELECT f.*, ROW_NUMBER() OVER (PARTITION BY document_id ORDER BY created_at DESC, id DESC) rn
  FROM findings f
) x WHERE rn = 1;
```

### Trade-offs and failure modes
Specify a deterministic ORDER BY; ties can otherwise produce unstable row selection.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #103 Find second-highest salary?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Use DENSE_RANK over salaries and filter rank 2; define tie behavior. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "Find second-highest salary". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate find second-highest salary with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #104 Find duplicate records?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
GROUP BY key HAVING COUNT(*)>1; use ROW_NUMBER to identify extras. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "Find duplicate records". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate find duplicate records with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #105 CTE vs subquery?

**Priority:** High · **Status:** Guided study — example needs review

### Concept
Named query expression vs inline nested query; optimizer-dependent performance. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "CTE vs subquery". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate cte vs subquery with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #106 UNION vs UNION ALL?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
UNION removes duplicates; UNION ALL preserves them. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "UNION vs UNION ALL". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate union vs union all with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #107 DELETE vs TRUNCATE vs DROP?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Delete rows, empty table, remove object; transaction semantics vary. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "DELETE vs TRUNCATE vs DROP". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate delete vs truncate vs drop with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #108 Indexes and composite index order?

**Priority:** Medium · **Status:** Expanded

### Concept
A B-tree index stores ordered keys for selective lookups and ranges. Composite index column order affects usable leading predicates and sort patterns.

### Why / when
Index frequent WHERE, JOIN and ORDER BY combinations based on real query plans.

### Production example
An audit list filters by tenant_id and status, then sorts by created_at.

### Code example
```sql
CREATE INDEX idx_findings_tenant_status_created
ON findings(tenant_id, status, created_at DESC);
```

### Trade-offs and failure modes
Indexes slow writes and consume storage; a low-selectivity column alone may not justify an index.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #109 B-tree vs GIN vs GiST indexes?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
General ordered lookups vs inverted/multidimensional access methods. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "B-tree vs GIN vs GiST indexes". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate b-tree vs gin vs gist indexes with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #110 EXPLAIN ANALYZE and slow SQL?

**Priority:** Medium · **Status:** Expanded

### Concept
EXPLAIN shows the PostgreSQL execution plan; EXPLAIN ANALYZE executes the query and reports actual timing and row counts.

### Why / when
Use it to diagnose sequential scans, bad estimates, missing indexes and expensive joins.

### Production example
A slow audit search is profiled under realistic tenant cardinality and compared before/after indexing.

### Code example
```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM findings WHERE tenant_id = 7 AND status = 'OPEN';
```

### Trade-offs and failure modes
EXPLAIN ANALYZE executes the query, so avoid running mutating statements on production without safeguards.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #111 Transactions and isolation anomalies?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Dirty/nonrepeatable/phantom reads, lost updates, write skew; DB-specific. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "Transactions and isolation anomalies". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate transactions and isolation anomalies with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #112 Optimistic vs pessimistic locking?

**Priority:** Medium · **Status:** Expanded

### Concept
Optimistic locking detects conflicting writes, often with a version column. Pessimistic locking acquires database locks before changes.

### Why / when
Use optimistic locking when contention is rare; pessimistic locking when conflicts are frequent or expensive.

### Production example
Two auditors try to approve the same finding; only one UPDATE with matching version succeeds.

### Code example
```sql
UPDATE findings SET status='APPROVED', version=version+1
WHERE id=42 AND version=3;
-- Check updated row count is exactly 1.
```

### Trade-offs and failure modes
Optimistic retries need user-friendly conflict handling; pessimistic locks can reduce throughput and deadlock.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #113 MVCC in PostgreSQL?

**Priority:** Medium · **Status:** Expanded

### Concept
PostgreSQL MVCC keeps row versions so readers and writers can proceed with less blocking under supported isolation levels.

### Why / when
Use it to reason about concurrent reads, snapshots and vacuum maintenance.

### Production example
A reporting query reads a consistent snapshot while an ingestion transaction inserts new findings.

### Code example
```sql
SELECT * FROM pg_stat_activity WHERE state = 'idle in transaction';
```

### Trade-offs and failure modes
Long-running transactions can prevent cleanup of dead tuples; monitor vacuum and transaction age.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #114 Deadlocks in databases?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Conflicting lock order; detect/retry and enforce consistent ordering. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "Deadlocks in databases". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate deadlocks in databases with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #115 Normalization 1NF/2NF/3NF vs denormalization?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Reduce anomalies vs optimize read models with controlled redundancy. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "Normalization 1NF/2NF/3NF vs denormalization". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate normalization 1nf/2nf/3nf vs denormalization with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #116 Offset vs keyset pagination?

**Priority:** Medium · **Status:** Expanded

### Concept
OFFSET pagination skips rows and can become slow or inconsistent as the dataset changes. Keyset pagination resumes after the last sort key.

### Why / when
Use keyset pagination for high-volume activity feeds and audit logs.

### Production example
A compliance UI fetches 50 events after the last (created_at,id) cursor.

### Code example
```sql
SELECT * FROM audit_events
WHERE (created_at,id) < (:lastTime,:lastId)
ORDER BY created_at DESC,id DESC LIMIT 50;
```

### Trade-offs and failure modes
Cursor ordering must be stable and unique; arbitrary page-number jumps are harder with keyset pagination.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #117 Partitioning vs sharding vs replication?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Table partitioning, distributing data, copying data for availability/reads. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "Partitioning vs sharding vs replication". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate partitioning vs sharding vs replication with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #118 Connection pooling and N+1 query issue?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Reuse connections; avoid per-row ORM queries using joins/fetch batching. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "Connection pooling and N+1 query issue". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate connection pooling and n+1 query issue with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #119 JSONB vs relational columns?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Flexible indexed documents vs explicit constraints and relational modeling. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "JSONB vs relational columns". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate jsonb vs relational columns with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---

## #120 PostgreSQL pgvector retrieval?

**Priority:** Medium · **Status:** Expanded

### Concept
pgvector adds vector similarity search to PostgreSQL. Store embedding vectors and retrieve candidates by distance, then apply metadata filters and reranking as needed.

### Why / when
Use it for RAG over compliance policies when the operational team already uses PostgreSQL.

### Production example
A user asks about audit evidence retention; embed the query, retrieve policy chunks by vector similarity, then pass citations to the LLM.

### Code example
```sql
SELECT chunk_id, content FROM policy_chunks
WHERE tenant_id = :tenant
ORDER BY embedding <=> :query_embedding LIMIT 8;
```

### Trade-offs and failure modes
Similarity does not prove factual relevance; evaluate retrieval recall, chunking, permissions and grounding.

### Follow-up questions
- What production problem would this solve?
- What are its main failure modes and trade-offs?

---

## #121 Design schema for audit findings/approvals?

**Priority:** Medium · **Status:** Guided study — example needs review

### Concept
Foreign keys, tenant IDs, versioning, immutable audit trail and indexes. In an interview, define the behavior precisely, describe the mechanism or contract, and distinguish it from the nearest alternative.

### Why / when
This matters in relational data correctness and query plans: choose the mechanism when its specific guarantees solve a real requirement in a PostgreSQL multi-tenant compliance database. State the preconditions and how you would verify it with tests or measurements.

### Production example
Production discussion prompt: In a PostgreSQL multi-tenant compliance database, identify a requirement involving "Design schema for audit findings/approvals". Explain which component owns the behavior, what data flows through it, and how you would validate the expected outcome. This is a scenario prompt, not a tested implementation.

### Trade-offs and failure modes
Assess locking contention, bad plans and missing tenant filters. State what the mechanism does not guarantee, which metrics or tests would detect a failure, and what simpler alternative you would consider.

### Follow-up questions
- How would you demonstrate design schema for audit findings/approvals with a small reproducible example?
- Which production failure would reveal incorrect use of this concept?
- How would you measure or test the trade-off in a PostgreSQL multi-tenant compliance database?

---
