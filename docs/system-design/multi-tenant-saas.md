# Multi-tenant SaaS: a worked design

**Real-world situation:** Two companies share one project-tracking service but must never see each other’s tasks.

This is an illustrative architecture, not a claim about a specific company’s implementation.

## What we need and why

Tenant isolation in every data path, per-tenant authorization/quotas, recoverable onboarding and fair resource use.

## API and data ownership

GET /projects derives tenant from authenticated membership. Project primary/unique keys and queries include tenant_id. Tenant, Membership, Project, AuditRecord.

## Component diagram

![Multi-tenant SaaS architecture](diagrams/multi-tenant-saas.svg)

Arrows show requests or emitted data. Responses generally return to callers and are omitted. Branches can be alternatives rather than steps that always run.

## Follow one request

Resolve tenant from verified identity and membership. Apply it in database access, cache keys, search filters and object storage authorization. Jobs carry trusted tenant context and recheck permissions as required. Test cross-tenant IDs deliberately, not only happy-path requests.

## Why these components exist

Shared tables are economical but need strict isolation controls; database-per-tenant offers different isolation and operating costs. Large tenants may need separate resource pools.

## Failure walkthrough

Missing tenant filters leak data. Unscoped cache keys collide. A noisy tenant can consume shared pools, so use per-tenant quotas and workload isolation.

## Capacity worked example

Size for both total tenants and largest tenant. One tenant with 80% of requests can invalidate an average-per-tenant capacity estimate.

## Explain it back

If database queries are scoped correctly but Redis keys omit tenant_id, is isolation complete?

[Beginner glossary and learning order](visual-learning-guide.md) · [All case studies](README.md)
