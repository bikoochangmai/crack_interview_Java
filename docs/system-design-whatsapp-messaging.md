# System Design — WhatsApp & Messaging

4 senior-level interview questions with architectural trade-offs, practical examples and follow-ups.

> Answers are original study material. Product capabilities and cloud SKUs should be checked against current vendor documentation before deployment.

## 246. Design a WhatsApp-like one-to-one chat system.

**Concept:** Messaging needs real-time delivery, offline persistence, retries and ordering within conversations.

**How and why:** Use authenticated WebSockets to gateway; assign message IDs; persist messages; route through conversation-partitioned queue; ack delivered/read states; push notify offline devices.

**Real-world example:** Phone A sends a message while phone B is offline; server stores it and delivers on reconnect.

**Trade-offs / failure modes:** Exactly-once end-to-end delivery is hard; idempotent processing avoids duplicates.

**Interview follow-up:** What happens if sender reconnects after timeout?

## 247. How do you handle ordering and duplicates in chat?

**Concept:** Network delays and retries can reorder or duplicate messages.

**How and why:** Assign per-conversation monotonic sequence on authoritative write path; clients deduplicate by message ID and reconcile gaps.

**Real-world example:** Two phones in the same group reconnect after losing connectivity and merge by server sequence.

**Trade-offs / failure modes:** Global ordering is expensive and unnecessary; partition by conversation.

**Interview follow-up:** What about edits and deletes?

## 248. How would you design WhatsApp group messaging and presence?

**Concept:** Fan-out cost grows with group size, and presence updates are ephemeral.

**How and why:** Store membership, authorize sends, fan-out via queues; use Redis TTL for online presence; use push for offline clients.

**Real-world example:** Small groups use fan-out-on-write; massive broadcast channels may favor fan-out-on-read.

**Trade-offs / failure modes:** Presence is best-effort, not a financial consistency guarantee.

**Interview follow-up:** How would you support 100,000-member channels?

## 249. How does end-to-end encryption change messaging architecture?

**Concept:** The server transports ciphertext but should not possess plaintext decryption keys.

**How and why:** Use established audited cryptographic protocols and device key management; encrypt on sender and decrypt on recipients.

**Real-world example:** Attachments encrypted client-side; server stores encrypted blobs and metadata.

**Trade-offs / failure modes:** Server-side search, moderation and multi-device recovery become harder.

**Interview follow-up:** How do you handle key rotation and new devices?
