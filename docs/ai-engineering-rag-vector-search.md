# AI Engineering — RAG & Vector Search

8 senior-level interview questions with architectural trade-offs, practical examples and follow-ups.

> Answers are original study material. Product capabilities and cloud SKUs should be checked against current vendor documentation before deployment.

## 290. Design a production RAG pipeline end to end.

**Concept:** RAG grounds generation in retrieved enterprise documents rather than relying only on model weights.

**How and why:** Ingest Blob/PDF→extract/OCR if needed→clean→chunk→embed→store vectors+metadata→query embed→hybrid retrieve→rerank→prompt with citations→evaluate.

**Real-world example:** Audit assistant retrieves policy section and cites document/version when answering “Which controls are missing?”

**Trade-offs / failure modes:** Retrieval failure can produce confident but unsupported output.

**Interview follow-up:** How do you test faithfulness and retrieval recall?

## 291. How do you choose chunk size, overlap and metadata?

**Concept:** Chunks balance retrieval precision with context completeness.

**How and why:** Split by headings/semantic boundaries; include tenant, ACL, document version, page and section; tune chunk size via evaluation.

**Real-world example:** Keep a policy exception clause and its conditions together rather than splitting mid-sentence.

**Trade-offs / failure modes:** Large chunks waste context; tiny chunks lose meaning.

**Interview follow-up:** How do you handle tables and scanned PDFs?

## 292. What are embeddings and cosine similarity?

**Concept:** Embeddings map text to vectors whose geometry approximates semantic relatedness.

**How and why:** Generate document and query vectors with compatible model; compare cosine or inner product; index with ANN when needed.

**Real-world example:** “employee travel reimbursement” retrieves policy titled “expense claims” despite different wording.

**Trade-offs / failure modes:** Similarity is not proof of correctness; embedding model changes require reindexing strategy.

**Interview follow-up:** What is embedding dimensionality?

## 293. pgvector vs Pinecone vs Qdrant vs Elasticsearch vector search?

**Concept:** Vector stores differ in operations, filtering, hybrid search and scale.

**How and why:** pgvector suits existing Postgres/transactional metadata; dedicated vector engines scale specialized ANN; Elasticsearch combines text and vector retrieval.

**Real-world example:** Compliance system starts with PostgreSQL pgvector and ACL-aware SQL filters.

**Trade-offs / failure modes:** Benchmark actual data, index type, latency and recall.

**Interview follow-up:** What is HNSW and why tune ef_search?

## 294. What is hybrid search and reranking?

**Concept:** Lexical search catches exact terms; semantic search catches paraphrases.

**How and why:** Combine BM25/full-text and vector scores via reciprocal rank fusion; rerank top candidates with cross-encoder where justified.

**Real-world example:** Find exact policy ID “ISO 27001 A.5.1” and semantically similar access-control requirements.

**Trade-offs / failure modes:** Reranking adds latency and compute cost.

**Interview follow-up:** How do you evaluate precision@k and nDCG?

## 295. How do you enforce document permissions in RAG?

**Concept:** Search must never reveal unauthorized documents or snippets.

**How and why:** Propagate authenticated tenant/user claims, enforce ACL before returning content, use row-level security or trusted metadata filtering; audit access.

**Real-world example:** Auditor in tenant A cannot retrieve tenant B policy chunks even if vector similarity is high.

**Trade-offs / failure modes:** Prompt instructions alone are not access control.

**Interview follow-up:** How do you prevent cross-tenant cache leaks?

## 296. What is GraphRAG and when would you use it?

**Concept:** Graph-based retrieval helps multi-hop questions across entities and relationships.

**How and why:** Extract validated entities/edges, store graph, traverse relationships then combine with source text and citations.

**Real-world example:** Find all controls impacted by a vendor, linked policies and dependent business processes.

**Trade-offs / failure modes:** Graph extraction errors propagate; ordinary RAG may be simpler.

**Interview follow-up:** When does GraphRAG add little value?

## 297. How do you evaluate RAG quality and hallucination?

**Concept:** A RAG system must be tested for both retrieving relevant evidence and generating faithful answers.

**How and why:** Create labeled question/evidence set; measure retrieval recall@k, citation support, faithfulness, answer correctness, latency and cost; add regression gates.

**Real-world example:** Release only if audit answers cite supporting policy sections and do not invent controls.

**Trade-offs / failure modes:** LLM-as-judge can be biased; include human review and calibrated samples.

**Interview follow-up:** How do you build a gold evaluation dataset?
