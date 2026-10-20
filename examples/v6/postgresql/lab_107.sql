-- Question #107: DELETE vs TRUNCATE vs DROP?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_107.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_rows(id int); INSERT INTO v6_rows VALUES(1),(2); DELETE FROM v6_rows WHERE id=1; TRUNCATE v6_rows; DROP TABLE v6_rows;
ROLLBACK;
