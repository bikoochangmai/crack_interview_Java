# Modern AI Ecosystem — Tools, Concepts, Architecture & Interview Guide

The user-provided AI ecosystem image organizes tools into LLM, Agentic AI, RAG, Embedding, MCP, AI Security, Observability, Memory, AI Agent, Automation and Vector Database. The categories below follow that organization. **Tools are examples, not endorsements, and some products span multiple categories.** Availability and exact features change over time.

| Layer | What it solves | Tools shown in image | Example in an enterprise system |
|---|---|---|---|
| LLM & serving | Generate/reason over text; serve model inference | OpenAI GPT, Anthropic Claude, Google Gemini, Meta Llama, Mistral AI, Cohere, Hugging Face, Ollama, vLLM | Extract structured audit finding with cited evidence |
| Agentic AI | Coordinate steps, tools and branching | LangGraph, CrewAI, Microsoft AutoGen, Microsoft Agent Framework, LlamaIndex Workflows, AWS Strands Agents, CAMEL, Agno | Plan evidence retrieval, request approval, then create ticket |
| RAG | Retrieve enterprise knowledge before generating | LangChain, LlamaIndex, Haystack, DSPy, RAGFlow, GraphRAG, Unstructured, EmbedChain | Answer from current policy PDFs with citations |
| Embeddings | Convert content into semantic vectors | OpenAI Embeddings, Cohere Embed, Voyage AI, Sentence Transformers, BGE, Google Vertex AI Embeddings, Azure OpenAI Embeddings | Match “travel reimbursement” to “expense claims policy” |
| MCP | Standard tool/resource connectivity for AI applications | MCP SDK, FastMCP, MCP Registry, GitHub MCP Server, Slack MCP Server, PostgreSQL MCP Server, Google Drive MCP Server, Filesystem MCP Server | Read-only policy search tool exposed to an AI assistant |
| AI Security | Guard data and tool use; enforce governance | NVIDIA NeMo Guardrails, Guardrails AI, Microsoft Presidio, Lakera Guard, Prompt Security, Protect AI, Azure AI Content Safety, AWS Bedrock Guardrails | Redact PII, detect risky output, enforce tool allowlist |
| Observability | Trace and evaluate AI workflows | LangSmith, Langfuse, Arize Phoenix, Weights & Biases Weave, TruLens, Ragas, Promptfoo, Helicone | Compare prompt/model versions and trace retrieval failures |
| Memory | Retain state, user context or knowledge | Mem0, Zep, Letta, LangGraph Memory, Redis, PostgreSQL, Neo4j, Chroma | Persist approval workflow state and scoped preferences |
| AI Agent SDKs | Build tool-using assistants | OpenAI Agents SDK, LangChain Agents, PydanticAI, Semantic Kernel, Google ADK, AWS Bedrock Agents, Azure AI Foundry Agent Service | Compliance assistant with bounded tools and approval gates |
| Automation | Schedule and orchestrate integrations | n8n, Zapier, Make, Microsoft Power Automate, Temporal, Apache Airflow, Prefect, Kestra, Pipedream | Run document ingestion and notify reviewer |
| Vector Database | Efficient semantic nearest-neighbor search | Pinecone, Weaviate, Qdrant, Milvus, Chroma, pgvector, Elasticsearch, Redis, MongoDB Atlas Vector Search | Retrieve top-k policy passages scoped by tenant ACL |

## Recommended architecture for Java + Angular + PostgreSQL + Azure

```text
Angular UI → Spring Boot API (Entra ID / RBAC)
                  │
                  ├─ PostgreSQL: documents, tenants, findings, approvals, outbox
                  ├─ Azure Blob Storage: PDFs / original files
                  └─ Python AI service (or Java AI integration)
                       ├─ Ingestion → extraction → chunks → embeddings → pgvector
                       ├─ Query → tenant ACL filter → hybrid retrieval → rerank
                       ├─ LLM adapter → OpenAI / Claude / approved Azure model / Ollama
                       ├─ Tool layer → allowlisted APIs / scoped MCP servers
                       ├─ Human approval → durable state machine
                       └─ Traces + RAG evaluation + security policy
```

## Critical architecture distinctions

- **RAG vs fine-tuning:** RAG updates knowledge from documents; fine-tuning adapts learned behavior. They are complementary, not interchangeable.
- **MCP vs REST vs tool calling:** REST is an application API; model tool calling chooses actions; MCP standardizes AI-host-to-tool-server integration.
- **Agent vs workflow:** Agent chooses steps dynamically; workflow follows explicit logic. Use deterministic flows for high-risk approvals.
- **Embedding vs LLM:** Embeddings support semantic similarity; generative models produce answers. An embedding vector is not a source citation.
- **Vector store vs source of truth:** Store versioned source documents and ACLs in authoritative storage; vector indexes are derived and rebuildable.
- **Observability vs evaluation:** Traces show what happened; evaluation assesses whether retrieval and answers were correct.

## Security checklist

1. Authenticate users and enforce tenant/document ACLs before exposing retrieved passages.
2. Treat document text and tool results as untrusted; never follow instructions embedded in them.
3. Expose least-privilege read-only tools by default; require authenticated approval for writes.
4. Redact sensitive data from telemetry and test sets; define retention policies.
5. Evaluate citation support, retrieval recall, answer accuracy, tool-selection accuracy and failure handling.

## Suggested hands-on project

Build a compliance audit assistant using Spring Boot + Angular + PostgreSQL/pgvector + Python ingestion + an approved LLM. Start with document upload and cited read-only Q&A. Add structured findings and human approval later. Benchmark a local Ollama model against a managed endpoint with the same evaluation set.

## Illustrated study companion

[Generative AI — Complete Developer Study Notes](generative-ai/index.html) recreates all 20 supplied image pages in one HTML page with subsections, colorful diagrams, comparison tables, formulas, code, search and revision checkboxes.
