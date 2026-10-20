-- Question #121: Design schema for audit findings/approvals?
-- Run: psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f lab_121.sql
-- Transaction ensures the demonstration leaves no persistent schema changes.
BEGIN;
CREATE TEMP TABLE v6_findings(id bigint PRIMARY KEY,control_id text NOT NULL,status text NOT NULL); CREATE TEMP TABLE v6_approvals(id bigint PRIMARY KEY,finding_id bigint REFERENCES v6_findings(id),decision text NOT NULL,reviewer text NOT NULL); INSERT INTO v6_findings VALUES(1,'AC-1','PENDING'); INSERT INTO v6_approvals VALUES(10,1,'APPROVED','reviewer-1'); SELECT f.control_id,a.decision FROM v6_findings f JOIN v6_approvals a ON a.finding_id=f.id;
ROLLBACK;
