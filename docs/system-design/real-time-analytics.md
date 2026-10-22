# Real-time analytics: a worked design

**Real-world situation:** A dashboard shows recent orders by minute while events arrive late or twice.

This is an illustrative architecture, not a claim about a specific company’s implementation.

## What we need and why

Durable event ingestion, repeatable aggregates, bounded freshness, late-event handling and tenant-scoped dashboard reads.

## API and data ownership

Event(id, event_time, tenant, order_value); Aggregate(tenant, window, version); GET /metrics?window=. Define event-time versus processing-time semantics.

## Component diagram

![Real-time analytics architecture](diagrams/real-time-analytics.svg)

Arrows show requests or emitted data. Responses generally return to callers and are omitted. Branches can be alternatives rather than steps that always run.

## Follow one request

Append events durably. A processor groups by event-time window, deduplicates or applies idempotent updates, then writes queryable aggregates. Dashboard reads the aggregate store. Watermarks and an allowed-lateness policy determine when old windows may be revised.

## Why these components exist

Processing time is when an event arrives; event time is when the order happened. Checkpoint/replay semantics must agree with sink idempotency to avoid double-counting.

## Failure walkthrough

A delayed phone connection can deliver yesterday’s event today. Define correction or side-output policy. Watch consumer lag, backlog and dashboard freshness separately.

## Capacity worked example

At 5,000 events/second and 500 bytes/event, raw ingestion is 2.5 MB/second or about 216 GB/day before replicas and indexes.

## Explain it back

If the processor replays a batch after a crash, how do totals avoid doubling?

[Beginner glossary and learning order](visual-learning-guide.md) · [All case studies](README.md)
