# Notification platform: a worked design

**Real-world situation:** A confirmed order triggers an email, an app notification and optionally SMS.

This is an illustrative architecture, not a claim about a specific company’s implementation.

## What we need and why

Durable intent, preferences, deduplication, retries, scheduling and provider delivery-status tracking.

## API and data ownership

POST /notifications with stable event key. Intent(tenant, recipient, template, channel), Preference, DeliveryAttempt(provider ID/status), DedupKey.

## Component diagram

![Notification platform architecture](diagrams/notification-platform.svg)

Arrows show requests or emitted data. Responses generally return to callers and are omitted. Branches can be alternatives rather than steps that always run.

## Follow one request

Persist the intent before acknowledging acceptance. Fan out by allowed channel using current preferences and templates. Workers rate-limit providers and record attempts. Delivery callbacks update status; accepted by a provider is not proof that a person read it.

## Why these components exist

A stable event/recipient/channel key prevents duplicate local scheduling. External send needs provider idempotency where available or a documented duplicate-risk policy.

## Failure walkthrough

Retry transient failures with backoff and jitter; isolate permanent failures for review. Cancellation, unsubscribe and sensitive-message redaction need explicit policies.

## Capacity worked example

One million notifications/hour is about 278/second before channel fan-out; a promotion can create a much larger short burst.

## Explain it back

If the provider accepted an SMS but the acknowledgement was lost, what duplicate risk remains?

[Beginner glossary and learning order](visual-learning-guide.md) · [All case studies](README.md)
