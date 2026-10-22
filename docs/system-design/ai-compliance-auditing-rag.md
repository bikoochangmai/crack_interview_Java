# AI compliance auditing with RAG: a worked design

**Real-world situation:** An auditor asks which policy governs storing customer records.

This is an illustrative architecture, not a claim about a specific company’s implementation.

## What we need and why

Answer from approved, authorized documents with citations; abstain when evidence is missing. Retrieved text is data, not permission to run its instructions.

## API and data ownership

POST /documents for ingestion; POST /questions for retrieval. Document(tenant, version, ACL), Chunk(source/page, text), Embedding, AuditRecord.

## Component diagram

![AI compliance auditing with RAG architecture](diagrams/ai-compliance-auditing-rag.svg)

Arrows show requests or emitted data. Responses generally return to callers and are omitted. Branches can be alternatives rather than steps that always run.

## Follow one request

Ingestion extracts approved document versions, chunks them, records provenance and indexes embeddings. At query time enforce tenant/ACL filtering, retrieve evidence, build a constrained prompt, then return citations and an audit record. Ingestion is a separate pipeline from the query arrows.

## Why these components exist

Similarity finds candidates, not truth. Verify citation linkage, document currency and access again as needed. Evaluate retrieval recall separately from answer faithfulness.

## Failure walkthrough

A deleted or newly restricted document must be removed or filtered in retrieval. Prompt injection in a retrieved chunk must not grant tool authority. Missing evidence should produce abstention.

## Capacity worked example

For 10,000 documents × 30 chunks, store 300,000 chunks; estimate vector bytes from dimension × bytes/value plus index overhead.

## Explain it back

Can a perfectly fluent answer still be wrong if it cites an outdated policy?

[Beginner glossary and learning order](visual-learning-guide.md) · [All case studies](README.md)
