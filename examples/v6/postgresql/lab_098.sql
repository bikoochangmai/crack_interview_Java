-- Question #98: Primary key vs unique key vs foreign key?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_098.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_parent(id int PRIMARY KEY, email text UNIQUE); CREATE TEMP TABLE v6_child(id int PRIMARY KEY, parent_id int REFERENCES v6_parent(id)); INSERT INTO v6_parent VALUES (1,'a@example.test'); INSERT INTO v6_child VALUES (10,1); SELECT * FROM v6_child;
ROLLBACK;
