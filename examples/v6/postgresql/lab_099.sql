-- Question #99: INNER vs LEFT vs FULL OUTER JOIN?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_099.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_users(id int PRIMARY KEY); CREATE TEMP TABLE v6_orders(id int,user_id int); INSERT INTO v6_users VALUES(1),(2); INSERT INTO v6_orders VALUES(10,1); SELECT u.id,o.id FROM v6_users u LEFT JOIN v6_orders o ON o.user_id=u.id;
ROLLBACK;
