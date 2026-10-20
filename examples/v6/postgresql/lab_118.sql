-- Question #118: Connection pooling and N+1 query issue?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_118.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_customers(id int,name text); CREATE TEMP TABLE v6_orders(id int,customer_id int); INSERT INTO v6_customers VALUES(1,'Ada'); INSERT INTO v6_orders VALUES(10,1); SELECT o.id,c.name FROM v6_orders o JOIN v6_customers c ON c.id=o.customer_id; -- one joined query instead of N+1
ROLLBACK;
