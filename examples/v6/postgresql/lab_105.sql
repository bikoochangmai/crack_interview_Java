-- Question #105: CTE vs subquery?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_105.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_orders(id int,amount int); INSERT INTO v6_orders VALUES(1,100),(2,20); WITH expensive AS (SELECT * FROM v6_orders WHERE amount>=100) SELECT * FROM expensive;
ROLLBACK;
