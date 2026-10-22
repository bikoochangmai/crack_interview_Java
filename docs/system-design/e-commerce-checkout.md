# E-commerce checkout: a worked design

**Real-world situation:** Two buyers request the last mug; one payment response is lost.

This is an illustrative architecture, not a claim about a specific company’s implementation.

## What we need and why

Create one order per purchase, prevent overselling, reconcile payment uncertainty and fulfill only confirmed orders.

## API and data ownership

POST /checkout with idempotency key. Order, OrderLine, Reservation(state, expiry), PaymentAttempt(provider key/status), Outbox. Calculate price on the server.

## Component diagram

![E-commerce checkout architecture](diagrams/e-commerce-checkout.svg)

Arrows show requests or emitted data. Responses generally return to callers and are omitted. Branches can be alternatives rather than steps that always run.

## Follow one request

Reserve stock with a conditional update and commit pending order plus outbox in one local transaction. The relay publishes payment work. A worker calls the provider outside that transaction. Verified callbacks/reconciliation update guarded order state, then schedule fulfillment.

## Why these components exist

The provider charge and local database commit are not one ACID transaction. A saga persists progress and compensates with stock release/refund when required.

## Failure walkthrough

Treat a charge timeout as unknown. Query/retry with the same provider key. Define policy for late success after reservation expiry; never blindly release or fulfill twice.

## Capacity worked example

For 60,000 checkouts/hour, average is 16.7/second. Flash-sale concentration on a single SKU may matter more than total average.

## Explain it back

Which local records must commit together to stop an order existing without a recoverable payment request?

[Beginner glossary and learning order](visual-learning-guide.md) · [All case studies](README.md)
