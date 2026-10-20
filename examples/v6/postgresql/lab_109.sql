-- Question #109: B-tree vs GIN vs GiST indexes?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_109.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_documents(id int PRIMARY KEY,metadata jsonb,tags text[]); CREATE INDEX ON v6_documents USING gin(metadata); CREATE INDEX ON v6_documents USING gin(tags); INSERT INTO v6_documents VALUES(1,'{"status":"open"}',ARRAY['audit']); SELECT * FROM v6_documents WHERE metadata @> '{"status":"open"}';
ROLLBACK;
