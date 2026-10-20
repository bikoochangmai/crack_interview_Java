# System Design — Uber / Ride Hailing

4 senior-level interview questions with architectural trade-offs, practical examples and follow-ups.

> Answers are original study material. Product capabilities and cloud SKUs should be checked against current vendor documentation before deployment.

## 255. Design an Uber-like ride-hailing system.

**Concept:** Match riders with nearby drivers in real time while tracking trip state and location updates.

**How and why:** Driver app sends periodic coordinates; geo-index nearby drivers; matching service offers trip with expiry; atomic acceptance; trip events stream; payment after completion.

**Real-world example:** Rider requests pickup at Bengaluru airport; nearby available drivers receive time-limited offers.

**Trade-offs / failure modes:** GPS is noisy; stale location and simultaneous acceptances require safeguards.

**Interview follow-up:** How do you ensure only one driver accepts a ride?

## 256. How do you find nearby drivers efficiently?

**Concept:** Full scans of all driver coordinates are too slow.

**How and why:** Use H3/S2/geohash spatial cells or geospatial index; search nearby cells, filter availability, then rank by ETA from routing service.

**Real-world example:** A rider query scans a handful of nearby spatial cells rather than every driver in a city.

**Trade-offs / failure modes:** Nearest straight-line driver may have longer road ETA.

**Interview follow-up:** How do you update driver location without write overload?

## 257. How do you design trip state and matching concurrency?

**Concept:** Trip lifecycle must prevent contradictory transitions.

**How and why:** Explicit states REQUESTED→OFFERED→ACCEPTED→IN_PROGRESS→COMPLETED/CANCELLED; compare-and-set version or unique assignment constraint.

**Real-world example:** Two drivers tap Accept at once; DB conditional update assigns only one.

**Trade-offs / failure modes:** Distributed locks without durable constraints can fail under lease expiry.

**Interview follow-up:** What happens when driver disconnects after acceptance?

## 258. How do surge pricing and ETA estimation work?

**Concept:** Demand/supply imbalance influences dispatch and pricing, but models need guardrails.

**How and why:** Aggregate available drivers and requests by geo cell; estimate ETA with map data; cap/smooth surge factors; audit pricing decisions.

**Real-world example:** Rain causes demand spike in one area; app shows updated fare estimate before confirmation.

**Trade-offs / failure modes:** Avoid unfair or opaque dynamic pricing and stale supply snapshots.

**Interview follow-up:** How do you test surge rules?
