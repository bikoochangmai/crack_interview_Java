# Architecture, Azure & Leadership

16 questions · Source: existing interview portal question bank.

> These are concise revision cues, not exhaustive explanations. Verify behavior against the version you use.

## 142. HLD vs LLD?

**Priority:** High

**Answer cue:** Services/data flows/trade-offs vs classes/contracts/algorithms.

**Practice:** Explain an example, a failure mode, and an alternative.

## 143. CAP theorem and consistency models?

**Priority:** High

**Answer cue:** Under network partition choose consistency or availability; nuance required.

**Practice:** Explain an example, a failure mode, and an alternative.

## 144. Horizontal vs vertical scaling?

**Priority:** High

**Answer cue:** More instances vs bigger instances.

**Practice:** Explain an example, a failure mode, and an alternative.

## 145. Load balancer, CDN and cache?

**Priority:** High

**Answer cue:** Traffic distribution, edge content delivery, latency reduction.

**Practice:** Explain an example, a failure mode, and an alternative.

## 146. Azure App Service vs VM vs AKS?

**Priority:** High

**Answer cue:** Managed web hosting vs full VM control vs orchestrated containers.

**Practice:** Explain an example, a failure mode, and an alternative.

## 147. Azure Service Bus vs Event Hubs?

**Priority:** High

**Answer cue:** Enterprise messaging/commands vs high-throughput event ingestion.

**Practice:** Explain an example, a failure mode, and an alternative.

## 148. Azure Blob vs PostgreSQL storage?

**Priority:** High

**Answer cue:** Object binaries vs transactional structured metadata.

**Practice:** Explain an example, a failure mode, and an alternative.

## 149. Design multi-tenant isolation?

**Priority:** High

**Answer cue:** Tenant scoping, authorization, RLS/schema/database separation.

**Practice:** Explain an example, a failure mode, and an alternative.

## 150. RTO vs RPO and disaster recovery?

**Priority:** High

**Answer cue:** Recovery time objective vs acceptable data loss.

**Practice:** Explain an example, a failure mode, and an alternative.

## 151. Zero-downtime deployments?

**Priority:** Medium

**Answer cue:** Backward-compatible migrations, rolling/canary releases, health checks.

**Practice:** Explain an example, a failure mode, and an alternative.

## 152. Design a rate limiter?

**Priority:** Medium

**Answer cue:** Token bucket or sliding window, Redis atomicity and fairness.

**Practice:** Explain an example, a failure mode, and an alternative.

## 153. Design URL shortener?

**Priority:** Medium

**Answer cue:** IDs, redirects, cache, hot keys, analytics, collision strategy.

**Practice:** Explain an example, a failure mode, and an alternative.

## 154. Design document ingestion + RAG?

**Priority:** Medium

**Answer cue:** Upload, parse, chunk, embed, vector search, ACL filtering, citations.

**Practice:** Explain an example, a failure mode, and an alternative.

## 155. Design human-in-loop approvals?

**Priority:** Medium

**Answer cue:** State machine, RBAC, audit trail, optimistic locking.

**Practice:** Explain an example, a failure mode, and an alternative.

## 156. How handle incidents and RCA?

**Priority:** Medium

**Answer cue:** Contain impact, evidence, blameless root cause and corrective action.

**Practice:** Explain an example, a failure mode, and an alternative.

## 157. How defend architecture trade-offs?

**Priority:** Medium

**Answer cue:** Requirements, alternatives, measurable constraints and failure modes.

**Practice:** Explain an example, a failure mode, and an alternative.
