-- Question #111: Transactions and isolation anomalies?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_111.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_balance(account int PRIMARY KEY,cents int); INSERT INTO v6_balance VALUES(1,100); SAVEPOINT before_update; UPDATE v6_balance SET cents=0 WHERE account=1; ROLLBACK TO SAVEPOINT before_update; SELECT * FROM v6_balance; -- Test isolation anomalies with TWO sessions, not this single session
ROLLBACK;
