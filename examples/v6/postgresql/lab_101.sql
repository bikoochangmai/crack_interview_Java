-- Question #101: GROUP BY and aggregate functions?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_101.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_sales(team text,amount int); INSERT INTO v6_sales VALUES('a',10),('a',20),('b',2); SELECT team,count(*),sum(amount),avg(amount) FROM v6_sales GROUP BY team;
ROLLBACK;
