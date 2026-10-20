-- Question #115: Normalization 1NF/2NF/3NF vs denormalization?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_115.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_customers(id int PRIMARY KEY,name text); CREATE TEMP TABLE v6_orders(id int PRIMARY KEY,customer_id int REFERENCES v6_customers(id)); INSERT INTO v6_customers VALUES(1,'Ada'); INSERT INTO v6_orders VALUES(10,1); SELECT o.id,c.name FROM v6_orders o JOIN v6_customers c ON c.id=o.customer_id;
ROLLBACK;
