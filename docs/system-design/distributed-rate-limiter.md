# Distributed rate limiter: a worked design

**Real-world situation:** Protect a shared API from a tenant sending far more traffic than its plan permits.

This is an illustrative architecture, not a claim about a specific company’s implementation.

## What we need and why

Enforce per-tenant budgets across API instances with bounded latency and explicit behavior during limiter outages.

## API and data ownership

Middleware check(tenant, route, cost). Policy(capacity, refill_rate), Bucket(tokens, last_refill, expiry). Use bounded key space.

## Component diagram

![Distributed rate limiter architecture](diagrams/distributed-rate-limiter.svg)

Arrows show requests or emitted data. Responses generally return to callers and are omitted. Branches can be alternatives rather than steps that always run.

## Follow one request

Compute replenished tokens from elapsed time, capped at capacity, then atomically consume the request cost. Admit only on success. Reject without a token using 429 and useful retry guidance. The allowed and rejection arrows are alternatives, not sequential calls.

## Why these components exist

A capacity-20 bucket refilling 10/second allows a short burst and sustained 10/second. Per-region budgets are simpler but can overshoot a global limit unless coordinated.

## Failure walkthrough

Decide fail-open versus fail-closed by endpoint risk. Centralized hot keys and datastore outages can turn the limiter into a bottleneck; monitor decision latency.

## Capacity worked example

One million requests/minute is about 16,667 limiter decisions/second, so the check must be cheap and measured under contention.

## Explain it back

Why is GET tokens followed by SET tokens unsafe under concurrent requests?

[Beginner glossary and learning order](visual-learning-guide.md) · [All case studies](README.md)
