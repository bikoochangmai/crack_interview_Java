-- Question #119: JSONB vs relational columns?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_119.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_findings(id int PRIMARY KEY,status text,attributes jsonb); INSERT INTO v6_findings VALUES(1,'OPEN','{"severity":"high"}'); SELECT id FROM v6_findings WHERE status='OPEN' AND attributes->>'severity'='high';
ROLLBACK;
