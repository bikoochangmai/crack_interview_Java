-- Question #114: Deadlocks in databases?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_114.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_lock(id int PRIMARY KEY); INSERT INTO v6_lock VALUES(1),(2); SELECT * FROM v6_lock ORDER BY id FOR UPDATE; -- Two-session deadlock exercise: session A locks 1 then 2; B locks 2 then 1; use lock_timeout
ROLLBACK;
