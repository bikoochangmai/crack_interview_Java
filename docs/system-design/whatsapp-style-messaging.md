# WhatsApp-style messaging: a worked design

**Real-world situation:** Alice sends Bob a message while he is offline.

This is an illustrative architecture, not a claim about a specific company’s implementation.

## What we need and why

Durable send, history, reconnect, per-conversation ordering and separate accepted/delivered/read states. This is an illustrative chat architecture, not WhatsApp internals.

## API and data ownership

POST /conversations/{id}/messages; GET messages?after=cursor. Message(conversation, sequence, sender, client_message_id unique within its scope, ciphertext). DeviceCursor tracks delivery.

## Component diagram

![WhatsApp-style messaging architecture](diagrams/whatsapp-style-messaging.svg)

Arrows show requests or emitted data. Responses generally return to callers and are omitted. Branches can be alternatives rather than steps that always run.

## Follow one request

Authenticate membership, deduplicate the send and commit message plus outbox. Acknowledge acceptance only after the durability contract is met. Worker delivers to connected devices. Bob fetches from durable history after reconnect even if a push notification was lost.

## Why these components exist

Use conversation sequences rather than phone clocks. Consumers deduplicate IDs. For end-to-end encryption, encrypt on the sender and decrypt on recipient devices with an established protocol.

## Failure walkthrough

If the worker crashes after push but before recording progress, retry can duplicate delivery. Devices deduplicate. Offline users cannot rely on socket memory.

## Capacity worked example

100,000 connected users sending one message/minute produce about 1,667 sends/second before group fan-out and multi-device copies.

## Explain it back

How does Bob recover if he receives sequence 42 before sequence 41?

[Beginner glossary and learning order](visual-learning-guide.md) · [All case studies](README.md)
