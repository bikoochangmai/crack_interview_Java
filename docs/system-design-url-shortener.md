# System Design — URL Shortener

3 senior-level interview questions with architectural trade-offs, practical examples and follow-ups.

> Answers are original study material. Product capabilities and cloud SKUs should be checked against current vendor documentation before deployment.

## 243. Design a TinyURL/ShortURL service end to end.

**Concept:** Users create short links and expect low-latency, highly available redirects.

**How and why:** POST /links validates URL and allocates unique Base62 code; GET /{code} looks up cache then DB and returns 302; use abuse checks, TTL and analytics events.

**Real-world example:** Campaign marketing sends millions of redirect requests while link creation is comparatively rare.

**Trade-offs / failure modes:** 301 may be cached aggressively; 302 offers more control over mutable destinations.

**Interview follow-up:** How do you avoid code collisions and malicious destinations?

## 244. How would you generate globally unique short codes?

**Concept:** Short codes need uniqueness, compactness and predictable capacity.

**How and why:** Use database-generated IDs encoded Base62, a distributed ID service, or random tokens with unique constraint and retry.

**Real-world example:** Encode a 64-bit unique ID as Base62 to get compact tokens without collisions in the ID space.

**Trade-offs / failure modes:** Sequential codes are guessable; obfuscation is not authorization.

**Interview follow-up:** How do you support custom aliases?

## 245. How do you scale ShortURL redirects to millions of requests?

**Concept:** Read-heavy traffic benefits from cache, CDN and partition-aware storage.

**How and why:** Cache hot code→URL mappings with TTL, replicate reads, rate-limit abuse, publish asynchronous click analytics.

**Real-world example:** A viral link is served from edge/Redis rather than hitting PostgreSQL for every redirect.

**Trade-offs / failure modes:** Cache invalidation matters for deleted or malicious URLs.

**Interview follow-up:** What is the strategy for a cache miss during DB outage?
