-- Question #106: UNION vs UNION ALL?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_106.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
SELECT id FROM (VALUES(1),(1),(2)) AS a(id) UNION SELECT id FROM (VALUES(2),(3)) AS b(id); SELECT id FROM (VALUES(1),(1)) AS a(id) UNION ALL SELECT id FROM (VALUES(2)) AS b(id);
ROLLBACK;
