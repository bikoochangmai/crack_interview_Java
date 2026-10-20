-- Question #104: Find duplicate records?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_104.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_events(event_key text); INSERT INTO v6_events VALUES('x'),('x'),('y'); SELECT event_key,count(*) FROM v6_events GROUP BY event_key HAVING count(*)>1;
ROLLBACK;
