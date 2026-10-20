-- Question #100: WHERE vs HAVING?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_100.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_sales(team text,amount int); INSERT INTO v6_sales VALUES('a',10),('a',20),('b',2); SELECT team,sum(amount) FROM v6_sales WHERE amount>0 GROUP BY team HAVING sum(amount)>10;
ROLLBACK;
