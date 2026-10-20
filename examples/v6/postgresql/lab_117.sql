-- Question #117: Partitioning vs sharding vs replication?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_117.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_partitioned(id int,created_at date) PARTITION BY RANGE(created_at); CREATE TEMP TABLE v6_oct PARTITION OF v6_partitioned FOR VALUES FROM ('2026-10-01') TO ('2026-11-01'); INSERT INTO v6_partitioned VALUES(1,'2026-10-20'); SELECT tableoid::regclass,id FROM v6_partitioned;
ROLLBACK;
