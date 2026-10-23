"""Narrative case-study sources: each follows one concrete user operation end to end."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
JOURNEYS={
'whatsapp-style-messaging':[
('Start with Alice and Bob, not a broker','Alice types “Meet at 6” and presses Send. Bob has no mobile connection. Alice should learn that the service accepted the message, while Bob must receive it after reconnecting. Accepted, delivered and read are different facts. We will build that sequence first. A live socket alone cannot satisfy it because disconnecting would lose the only delivery path.'),
('How the apps find the service','The operator configures an owned hostname such as chat.learn.example in DNS, binds it to an HTTPS/WebSocket edge and provisions its certificate. The app has this approved service origin in configuration. The domain of Bob’s email address does not decide which server owns the chat. DNS locates the service; conversation and recipient IDs select application records after connection. A mobile reconnect can reach another server, so required state must not exist only on the old socket node.'),
('Log in and send one message','Alice authenticates and establishes an authorized connection. A WebSocket handshake must validate the credential and permitted browser origins where applicable; being connected is not permission to post to every conversation. Alice sends {conversationId: c7, clientMessageId: m81, ciphertext: ...}. The service derives the sender from the session, verifies membership and checks that m81 has not already been accepted for that sender/conversation.'),
('Commit before showing accepted','Within the chosen database boundary, insert the message, assign its conversation sequence and store a delivery outbox event. Return accepted only after the promised durability level is met. If the response disappears, Alice retries m81 and receives the original sequence rather than creating another message. A single partition owner or transactional sequencer can order one conversation; phone clocks cannot reliably do so. An outbox relay can publish twice, so workers and recipients must tolerate duplicates.'),
('Deliver now or recover later','A delivery worker looks up Bob’s connected devices in a session directory. When Bob is offline, a notification can wake his app but is not the message database. On reconnect Bob authenticates, proves membership again and requests messages after cursor 40. If he gets 42 before 41, he fetches the missing range. Devices deduplicate IDs, acknowledge delivered state and later explicitly report read state. History retention and tombstones determine what an old cursor can recover.'),
('Keep privacy rules on every path','Check membership for send, history reads, attachment access and socket subscriptions, not just conversation creation. Revocation must reach live sessions or be enforced at each operation. End-to-end encryption happens on authorized devices using an established protocol; TLS alone only encrypts the connection to the service. Store encrypted envelopes and explicit metadata. Multi-device keys, attachments, backup recovery and joining/leaving groups require deliberate policies.'),
('Rehearse the failures','Kill the socket server after database commit: the message remains and reconnect recovers it. Kill the worker after push: redelivery is possible and Bob deduplicates. Lose database access: do not acknowledge durable acceptance. Lose the membership service: deny protected reads/sends temporarily rather than bypass membership. Expire a device session: require reauthentication. For groups, choose a fan-out model that does not block acceptance on every recipient; huge groups may fetch shared history. Measure accepted-message latency, reconnect gaps and delivery lag separately.'),
('Prove the first version before scaling','Begin with one authenticated API/socket service and durable conversation storage. Test two devices, an offline recipient, retry of the same client ID, forbidden conversation reads and history after reconnect. Then add multiple connection nodes, a shared session directory and background delivery workers for measured connection count and fan-out needs. Do not claim global ordering or exactly-once external effects merely because a broker exists.')],
'e-commerce-checkout':[
('Follow one purchase of the last mug','Alice adds mug-42 to her cart, then clicks Pay. At the same moment Bob buys the last available mug. Our task is to produce one correct order and one intended payment effect per purchase, while giving the losing buyer an honest sold-out result. Cached product pages are discovery views, not inventory reservations. Start by choosing where the stock decision is authoritative.'),
('Where the browser sends requests','The shop operator owns shop.learn.example and configures DNS, edge routing and TLS for the web/API origin. A separate payment provider owns its own API/domain. The shop calls that approved provider endpoint from trusted configuration. A return URL shown to a browser is not proof of payment; a customer can visit or modify a browser URL. Confirm outcomes using authenticated server-to-server responses, signed callbacks and reconciliation.'),
('Create a trusted checkout request','Alice signs in or receives a deliberately scoped guest-checkout session. POST /checkout contains item IDs, quantities, delivery choices and an idempotency key purchase-81, not a trusted total or owner ID. The server derives cart ownership from the verified session and recomputes price, currency, tax and eligibility. Cookie-based writes need CSRF protection. Card details should use the provider’s appropriate hosted/tokenized integration rather than passing raw card data through an interview toy API.'),
('Make the stock decision atomic','Inside a short local transaction, claim the purchase key, conditionally decrement available stock and create a pending order, reservation and payment outbox intent. UPDATE inventory SET available=available-1 WHERE sku=:sku AND available>=1 RETURNING available lets one buyer win the last unit. Check the affected row; an earlier SELECT is not a guarantee. If any required change fails, roll back all local changes. Do not hold this transaction open while a remote payment call runs.'),
('Move from pending to a known payment result','A worker reads the committed intent and calls the provider with a stable provider idempotency key. A timeout means unknown: the card may already be charged. Query/retry using the same reference according to the provider contract. Verify webhook authenticity and deduplicate its event ID. A guarded order transition marks payment confirmed and records fulfillment intent. A duplicated callback cannot create a second shipment. A local transaction cannot magically include the remote provider.'),
('Handle cancellation, expiry and refunds','Reserve stock for a defined interval. Expiry and payment success can race, so reservation states and version guards must decide exactly which action wins. A late successful charge after release needs policy: reacquire stock or refund. Refund is compensation recorded as a new business event, not rollback of time. Customers can only view/cancel their own orders; staff refund permissions and audit trails are separate from ordinary customer rights.'),
('Search and browse without weakening checkout','Product changes flow to a derived search index; search can filter/rank and recommendations can fail independently. Cart entries carry item identity/quantity, not permanent price promises. A stale search result may show a sold-out mug; checkout revalidates authoritative state. Begin with transactional order/stock ownership, then split services only with a defined reservation protocol and recovery for partial success.'),
('Test what the buyer sees under failure','Retry purchase-81 after losing its response and assert one order. Race two buyers for stock=1 and assert only one reservation. Delay payment success until after expiry and verify compensation. Submit someone else’s order ID and deny it. Simulate database outage before commit: do not report success. Stop analytics/email workers: the paid order remains durable. Track pending-payment age, reservation leaks, reconciliation backlog and duplicate-effect attempts, not only HTTP 200 counts.')],
'uber-style-ride-hailing':[
('Follow a station pickup','Alice requests a car at a railway station. Driver D7 appears closest, but another rider is also trying to book D7. We need to find likely candidates quickly and then confirm exactly one valid assignment. Fresh-looking coordinates are a search hint; authoritative trip/driver state decides whether the assignment exists. A diagram that treats those as the same fact misses the core race.'),
('How rider and driver apps connect','Both apps use the operator’s configured HTTPS origin, for example rides.learn.example, backed by owned DNS, edge bindings and TLS. Authenticated APIs carry durable requests; sockets or push carry timely updates. GPS selects a geographic search area inside the application, not a different DNS domain for every driver. Region routing can reduce latency, but ownership of a trip/driver must remain explicit during handoff.'),
('Authenticate roles and validate a ride request','POST /rides includes pickup, destination, quote ID and an idempotency key. Derive rider identity from credentials. Validate supported area and quote terms. A driver session may update only its own authorized vehicle/location and accept offers addressed to that driver. Rider and driver permissions differ; guessing a trip ID must not reveal another passenger’s route or permit cancellation.'),
('Find candidates then send expiring offers','Drivers publish timestamped positions. A geographic index searches the pickup cell plus neighbors, expanding radius if needed. Discard stale/ineligible candidates and compute road ETAs for a bounded shortlist: distance across a river can be misleading. Send offers containing trip, driver, expiry and expected state/version. Choosing one candidate is not yet a successful booking.'),
('Confirm one driver with guarded state','On acceptance, recheck expiry and availability. If trip and driver share a database boundary, conditionally reserve the available driver and move the pending trip to accepted in one transaction, with an outbox update. Roll back if either condition fails. If separately owned shards/services are involved, use an assignment owner or recoverable reservation protocol with fencing. Do not pretend a short Redis lock supplies a cross-service transaction.'),
('Run the trip and price contract','Persist allowed transitions: accepted, arrived, started, completed or a permitted cancellation. Late acceptances and old client versions cannot rewind state. A quote has stored currency, terms, pricing-policy version and expiry. ETA is a prediction based on route/traffic and should communicate uncertainty. Local demand/supply can inform bounded, smoothed surge policy; the rider accepts recorded terms rather than an undocumented moving price.'),
('Recover when phones and workers fail','If Alice loses connection after assignment commit, a retry/reconnect fetches the same durable trip. Duplicate offers cannot assign D7 twice. An expired offer is rejected even if the phone shows it. If the position store fails, avoid inventing nearby drivers; use a documented temporary-unavailable policy. Stop status-push delivery: clients can refresh durable state. A payment timeout after trip completion requires separate payment reconciliation, not changing the trip back to started.'),
('Build and verify in stages','First test one region with a few drivers, neighbor-cell search, two competing riders, late acceptance, stale coordinates and forbidden trip reads. Then measure position write volume, candidate-search time, assignment conflicts and notification lag. Add geographic partitioning for fleet size and load, while retaining a clear owner for assignments and tested recovery during region failure.')],
'ai-compliance-auditing-rag':[
('Start with a question requiring evidence','An employee asks: “How long may our team retain customer call records?” A useful answer must cite the applicable approved policy version. A fluent guess is a failure. The first design question is where approved evidence lives and which documents this employee is allowed to read. A vector database is only a candidate-search tool; it does not know corporate authorization by itself.'),
('Connect the user and trusted model endpoints','The organization owns an internal HTTPS portal such as audit.learn.example, configured with DNS, TLS and identity-aware access. The application calls approved model/embedding endpoints using server-held credentials. A link printed in an uploaded document is evidence text, not authority to make a network/tool request. Define data-residency and provider-retention requirements before sending sensitive chunks to a hosted model.'),
('Ingest approved policy versions','An authorized policy owner uploads a document. Store its immutable version, checksum, source location, tenant and ACL. Extract text, create chunks with page/section provenance and compute embeddings in an asynchronous job. Keep ingestion status explicit: uploaded is not yet searchable. Deleting/restricting a document requires removal or filtering of derived chunks and caches, not merely hiding its filename in the UI.'),
('Retrieve for one authenticated question','The query API derives tenant/user from verified credentials. Apply tenant/ACL and approved-version filters before selecting candidate evidence, then rank/retrieve a bounded set. Validate authorization again where needed at source access. Retrieval must not first expose forbidden snippets to the model and hope the final response hides them. Log query/evidence IDs safely without indiscriminately logging confidential text.'),
('Construct and verify the answer','Pass the user question and authorized evidence to a constrained answer builder. Instruct it to cite actual source chunks and abstain when evidence is insufficient. Separate system instructions from retrieved content; a malicious paragraph saying ignore previous instructions does not change tool permissions. Verify citation linkage and surface applicable version/date. A confident answer citing an obsolete policy is still wrong.'),
('Work through failure and evaluation','If extraction fails, retain an explicit failed-ingestion state for retry, not an empty policy treated as valid. If retrieval finds no permitted evidence, return an evidence-not-found/abstention response. If the model times out, report temporary answer unavailability without inventing text. If identity is unavailable, deny protected retrieval. Evaluate retrieval recall, correct ACL exclusion, citation faithfulness and version selection separately; one aggregate accuracy score hides different faults.'),
('Make the first release reviewable','Start with a small approved policy collection and manually curated questions with expected evidence. Test the same question as two users with different permissions, a superseded policy, an injected document and deleted source chunks. Only after that measure chunk count, vector index overhead, model latency/cost and ingestion lag. Add caching only with tenant/permission/version-aware keys and a revocation policy.')],
}
JOURNEYS.update({
'video-streaming-platform':[
('Follow a teacher’s upload to a student’s playback','A teacher uploads a one-hour lecture. A student later presses Play on a slow mobile network. The upload file, encoded playback segments and metadata are different assets with different lifetimes. We first need to accept the source durably, produce playable versions and authorize a student to request them. Adding a CDN before defining those states does not explain how video becomes playable.'),
('Set up the domains and delivery origins','The operator configures its web/API origin, for example video.learn.example, with owned DNS and TLS. A media hostname such as media.learn.example binds to a CDN whose origin is the rendition object store. DNS selects the service/edge; the video ID and segment path select data. Keep the source store private, lock down origin access and avoid a public bucket that bypasses playback authorization.'),
('Authenticate and authorize the upload','The teacher signs in and requests POST /uploads with expected media metadata. The API checks upload permission and quota and issues short-lived upload authorization scoped to the teacher’s specific object key, method and limits. The client uploads directly to storage if appropriate, then the service verifies completion. Never accept arbitrary client claims that any object key belongs to that teacher. Store owner, course, source checksum and processing status.'),
('Turn a source file into playable media','After durable upload, write a recoverable transcode intent. Workers probe/validate the source and create supported renditions at several bitrates. Split them into segments and produce a manifest describing those segments. Use versioned outputs and idempotent jobs; publish READY only after the required manifest/segments exist. Failed encoding stays PROCESSING/FAILED with retry status, not a broken public manifest.'),
('Trace the student’s Play request','GET /videos/{id}/playback checks the student’s identity and current course entitlement. If permitted and READY, return an appropriately protected manifest/playback credential. The player fetches the manifest and media segments through the CDN and switches rendition based on measured bandwidth. The application API handles metadata/permission; the CDN carries most bytes. Every protected segment path must enforce the chosen credential/origin policy, not just the initial Play button.'),
('Define authorization and revocation honestly','Playback credentials must be limited to permitted paths and time windows. A shareable signed media URL can be used by whoever possesses it until expiry; define acceptable revocation delay and stronger controls where needed. Expiring a credential mid-playback needs a refresh policy. Protect manifests as well as segments. A CDN HIT must not accidentally turn private content into anonymously reusable content.'),
('Recover the student experience','Duplicate storage/job events should not create competing READY versions. Kill a worker halfway through: temporary outputs remain unpublished and retry safely resumes/replaces them. If a rendition is missing, avoid advertising it. If bandwidth drops, select a lower rendition instead of treating every stall as API failure. If auth is unavailable, fail closed for private videos. Track startup delay, buffering ratio, encode backlog and CDN errors separately.'),
('Scale the right part','Start with a source store, metadata/permission API, worker and a tested player. Test unauthorized segment access, expired credentials, failed encoding and partial uploads. At 2 Mbit/second and 10,000 concurrent viewers, media delivery is about 20 Gbit/second before overhead. That points to CDN/object-storage delivery and encoding capacity, not sharding the small metadata table first.')],
'notification-platform':[
('Follow one order confirmation','Order 81 is confirmed and Alice expects an email plus an app notification. The order must remain confirmed even if the email provider is down. “Accepted for sending”, “provider accepted”, “delivered” and “read” are different facts. We therefore record durable notification intent and process delivery asynchronously instead of holding checkout open while every provider responds.'),
('Know which domains and credentials do what','The operator configures an HTTPS notification-management API with DNS/TLS. Its workers call approved provider APIs with server-managed credentials. Email also uses an owned sender domain with the provider’s required authentication records such as SPF/DKIM/DMARC configuration; those concern email sender verification, not HTTP user authorization. SMS and mobile push have their own provider credentials and registration rules.'),
('Record the business event once','Checkout commits order confirmation and an outbox event together. A relay delivers event e81 to the notification service. The service authenticates the producing workload, checks allowed tenant/event types and records a stable event-recipient-channel identity. A random public caller must not be able to send arbitrary branded messages to arbitrary recipients. Templates and recipient selection belong to trusted business rules.'),
('Choose channels from preferences','Resolve Alice’s verified contact destinations and current preferences, including necessary transactional versus optional promotional policy. Create channel work with the chosen template version and safe data fields. Do not place full secrets or unnecessary payment/customer details in message bodies or logs. A change of contact address needs verification; a request parameter must not silently redirect sensitive notifications to an attacker.'),
('Send and track a delivery attempt','A worker consumes channel work, observes provider rate limits and creates an attempt record. It calls the provider with a stable idempotency key where supported, stores the returned provider reference and handles authenticated status callbacks. Provider accepted means the provider took responsibility under its contract, not proof Alice read the message. Push tokens identify device registrations and can expire.'),
('Handle the lost-acknowledgement problem','If the provider accepted an SMS but the worker timed out, retrying may duplicate it. Prefer provider idempotency/status lookup; when unavailable, document the duplicate-versus-loss policy for that channel. Local deduplication cannot make a remote non-idempotent send exactly once. Retry transient errors with bounded backoff and jitter, quarantine permanent failures, and monitor oldest pending intent. A crash after send can cause reprocessing.'),
('Expose only authorized status and controls','Alice can inspect her own notification preferences and permitted delivery history. Tenant operators can manage only their authorized templates/recipients; privileged overrides need audit. Unsubscribe/cancellation and queued work must have a defined interaction. If the preference service is unavailable for optional marketing, do not guess consent; apply a safe documented policy.'),
('Prove correctness before promotion traffic','Test duplicate e81, a provider timeout, invalid contact, revoked push token, consent change and an unauthorized caller. Preserve order success while workers stop. Then estimate fan-out: one million notifications/hour is about 278/second before channels and retries, but scheduled campaigns produce much larger bursts. Separate channel queues and worker budgets so one failing SMS provider cannot starve all email.')],
'distributed-rate-limiter':[
('Follow two requests competing for one token','A paid tenant may sustain 10 requests/second with a burst of 20. After previous traffic only one token remains. Two API instances receive requests simultaneously. Both must not read one token and independently accept it. That race, plus how we identify the tenant and handle store failure, is the problem the limiter design must solve.'),
('Put the check on the real request path','Clients resolve api.learn.example through the operator’s DNS/TLS edge and reach an API gateway or middleware. The limiter is usually an internal check on this path, not a public database endpoint. Prevent bypass through direct backend access using appropriate network and workload authentication controls. DNS balancing alone does not coordinate quota across instances.'),
('Determine the policy key from trusted identity','Authenticate an access token/API credential and map it to tenant, subject and allowed plan. Construct the quota key from those verified attributes plus route/cost class. Do not trust a client-supplied X-Tenant header. Anonymous endpoints may use an abuse budget with carefully interpreted source information; shared NAT and proxies make an IP address an imperfect user identity.'),
('Execute the atomic decision','For a bucket with current tokens T, elapsed seconds d, refill rate r and capacity C, compute min(C,T+d*r), then consume request cost only if sufficient. Refill, comparison and subtraction must be atomic at the chosen store/owner. With one remaining token, one caller consumes it and the next is rejected. Define time source and how to handle clock movement rather than mixing arbitrary app-server clocks.'),
('Return a useful outcome','An allowed request proceeds to the backend, which still enforces its own business authorization and in-flight resource bounds. A rejected request gets HTTP 429 and suitable retry guidance; do not silently enqueue unlimited waiting work. Rate permission is not permission to read another tenant’s order. A token may reasonably be charged for an attempted request even if its later backend operation fails; document the policy.'),
('Handle distribution and outages','A single atomic shared bucket provides a clearer global decision but can be a hot dependency. Local/regional token allocations reduce coordination with an explicit overshoot/fairness budget. If the store fails, choose fail-open or fail-closed by endpoint risk and expose metrics. Fail-open can protect availability but weakens quota; fail-closed can reject legitimate traffic. Neither should happen accidentally because a timeout was caught as true.'),
('Bound the limiter itself','Expire inactive keys, constrain attacker-controlled key cardinality, bound decision timeouts and avoid retry storms against an unavailable store. A malicious tenant can use many subjects/paths unless hierarchical budgets exist. The limiter protects request arrival rate; a slow backend still needs connection-pool/in-flight/queue limits and backpressure.'),
('Verify the budget with concurrent traffic','Test a full burst, steady refill, two callers racing for the final token, stale time and datastore outage policies. Repeat across API instances, not only within one thread. At one million requests/minute, the check runs about 16,667 times/second; measure contention and added latency. Confirm direct backend traffic cannot bypass both gateway policy and application authorization.')],
'multi-tenant-saas':[
('Follow Alice opening her company’s project','Company A and Company B use the same project tracker. Alice belongs to A and requests project 42. A guessed project ID from B must never return B’s tasks, attachments or cached results. This must remain true in APIs, workers, search and exports, not only on the first database query.'),
('Decide how domains map to tenants','The operator owns app.learn.example. A customer may use team-a.learn.example under that owned zone, or a verified custom domain. Configure DNS/TLS/edge bindings and a trusted hostname-to-tenant directory; verify ownership before accepting custom domains. A hostname selects a tenant context, not a user identity. A visitor typing team-b into a Host/header cannot thereby gain membership in B.'),
('Authenticate then establish membership','Alice logs in through the chosen identity provider. The API validates her session/token and resolves which tenant memberships/roles she currently has. If a route selects company A, verify she is authorized there. Do not assume the user controls a tenant just because their email suffix resembles its name. Workload/service credentials also need tenant/purpose scoping for internal calls.'),
('Execute one tenant-scoped request','GET /projects/42 derives tenant context from the verified session and route policy. Query by tenant_id AND project_id, check project permissions and return an API value rather than leaking an ORM graph. Store tenant ID in appropriate composite unique constraints and foreign keys so cross-tenant relationships cannot be inserted casually. Row-level security can add defense but must be configured and tested with real connection/session behavior.'),
('Carry context beyond the database','Cache keys include tenant and relevant permission/version context. Search queries apply tenant/ACL filters before results leave the service. Blob downloads use scoped, expiring authorization. A background export job stores trusted tenant/user purpose and rechecks access as required; workers cannot infer tenant solely from an arbitrary payload field. Audit records identify actor, tenant, operation and result without exposing unnecessary data.'),
('Handle a support user and membership removal','Tenant admins act within their own organization. Platform support access is a separate explicit privileged flow with approval/audit rules appropriate to the product. Removing Alice’s membership must affect new requests and live subscriptions, caches and long-running exports according to a documented revocation window. Authentication succeeding does not mean an old tenant permission remains valid forever.'),
('Recover without leaking or starving neighbors','On tenant-directory/authorization failure, deny protected access rather than choose a default tenant. On cache outage, use bounded tenant-scoped DB fallback. Enforce per-tenant quotas and workload isolation so one large tenant does not exhaust every shared pool. Backups/restores and exports need tenant-aware procedures; a full shared-database restore is not automatically a safe single-tenant restore.'),
('Choose isolation after defining the invariant','Begin with a clear shared-table model and deliberate cross-tenant negative tests. Database-per-tenant gives different isolation/operating trade-offs; it does not remove authentication or routing requirements. Test colliding project IDs, unscoped cache keys, forbidden exports, custom-host spoofing and membership removal. Measure both total traffic and the largest tenant rather than assuming tenants are equal.')],
'real-time-analytics':[
('Follow a late order event into a minute chart','Order 81 happened at 10:01:58 but its event arrives at 10:03 after a connection failure. The sales dashboard should place it according to the chosen event-time policy, not blindly count it as a new 10:03 sale. If the processor crashes and replays it, the total should not double. These two questions determine storage and processing rules.'),
('Set up ingestion and dashboard access','The operator configures separate approved HTTPS endpoints such as events.learn.example and dashboard.learn.example with DNS/TLS. Producers authenticate as authorized workloads/clients and can publish only their permitted tenant/event classes. Dashboard viewers authenticate separately and can see only entitled aggregates. A broker topic name or a client-provided tenant field is not an access-control boundary by itself.'),
('Record a trustworthy event','Emit stable event ID e81, order/tenant identity, event timestamp, schema version and amount/currency under a defined business contract. For transactional order events, use a committed outbox rather than publishing before the order exists. Validate schema, timestamp bounds and producer permission. Avoid mixing currencies into one meaningless summed number. Append to a durable log before acknowledging the chosen ingestion guarantee.'),
('Calculate a window','A processor reads partitioned events and groups them by tenant and event-time minute. Watermarks estimate progress; an allowed-lateness policy determines which old windows can be revised. For e81, update the 10:01 window if still permitted, or send it to an explicit correction/late-event path. A watermark is a processing policy, not proof no late event can ever arrive.'),
('Commit output without duplicate counting','Keep processor progress/checkpoint and sink behavior compatible. If a crash occurs after aggregate output but before input progress is recorded, replay is possible. Use a transactional/idempotent sink strategy or event-ID deduplication with retention matching replay policy. A raw increment on every delivery can double totals. Published aggregate versions let downstream reads distinguish revisions.'),
('Show freshness honestly','The dashboard API reads precomputed tenant-scoped aggregates and returns their window/version and freshness/progress information. Polling or streaming can update the browser. A last-updated label should distinguish no new sales from a stalled processor. If processing is behind, keep the last valid view with an explicit stale indication where permitted rather than displaying invented zero sales.'),
('Recover and correct deliberately','Replay from durable input after processor failure and verify stable totals. Quarantine malformed events instead of blocking every partition indefinitely. Handle duplicate IDs, clock-skewed timestamps and late cancellation/correction events. On authorization failure deny the dashboard read. Monitor ingest errors, consumer lag, watermark delay, sink failures and user-visible freshness as separate signals.'),
('Test the chart before adding streaming products','Start with a handful of timestamped events and write down the expected windows. Replay e81 twice, delay it across the lateness boundary, crash before/after sink commit and test another tenant’s dashboard query. At 5,000 events/second and 500 bytes/event, raw data is about 2.5 MB/second or 216 GB/day before replicas/indexes; that motivates retention and replay budgets rather than an unbounded log.')]
})
# Illustrative HTTP contracts, not requests to live services.
EXCHANGES={
'whatsapp-style-messaging':"""POST /conversations/c7/messages
Authorization: Bearer <chat-access-token>
Content-Type: application/json

{"clientMessageId":"m81","ciphertext":"<encrypted-envelope>"}

HTTP/1.1 201 Created
{"messageId":"m81","sequence":41,"state":"ACCEPTED"}

GET /conversations/c7/messages?after=40
Authorization: Bearer <bob-access-token>

HTTP/1.1 200 OK
{"messages":[{"messageId":"m81","sequence":41,"ciphertext":"<encrypted-envelope>"}],"cursor":41}""",
'e-commerce-checkout':"""POST /checkout
Authorization: Bearer <buyer-access-token>
Idempotency-Key: purchase-81
Content-Type: application/json

{"items":[{"sku":"mug-42","quantity":1}],"paymentMethodRef":"<provider-token>"}

HTTP/1.1 202 Accepted
{"orderId":81,"state":"PAYMENT_PENDING","statusUrl":"/orders/81"}

GET /orders/81
Authorization: Bearer <same-buyers-access-token>

HTTP/1.1 200 OK
{"orderId":81,"state":"CONFIRMED"}""",
'uber-style-ride-hailing':"""POST /rides
Authorization: Bearer <rider-access-token>
Idempotency-Key: ride-81
Content-Type: application/json

{"pickup":{"lat":26.14,"lon":91.74},"destinationRef":"station-east-gate","quoteId":"q17"}

HTTP/1.1 202 Accepted
{"tripId":"T81","state":"SEARCHING"}

POST /offers/O17/accept
Authorization: Bearer <authorized-driver-access-token>
Content-Type: application/json

{"expectedVersion":3}

HTTP/1.1 200 OK
{"tripId":"T81","state":"ACCEPTED","driverId":"D7","version":4}""",
'ai-compliance-auditing-rag':"""POST /questions
Authorization: Bearer <auditor-access-token>
Content-Type: application/json

{"question":"How long may our team retain call records?"}

HTTP/1.1 200 OK
{"status":"INSUFFICIENT_AUTHORIZED_EVIDENCE","answer":null,"citations":[]}

This is a valid abstention, not an HTTP infrastructure error. When sufficient
approved evidence exists, return a grounded answer with real permitted source
IDs/pages/versions. Do not invent those citations to fill the response shape.""",
'video-streaming-platform':"""POST /uploads
Authorization: Bearer <teacher-access-token>
Content-Type: application/json

{"courseId":"C7","filename":"lecture.mp4","contentType":"video/mp4"}

HTTP/1.1 201 Created
{"videoId":"V81","state":"AWAITING_UPLOAD","uploadAuthorization":"<short-lived-object-scoped-value>"}

GET /videos/V81/playback
Authorization: Bearer <entitled-student-access-token>

HTTP/1.1 200 OK
{"state":"READY","manifestUrl":"https://media.learn.example/V81/v3/master.m3u8?<scoped-credential>"}""",
'notification-platform':"""POST /notifications
Authorization: Bearer <trusted-order-service-credential>
Content-Type: application/json

{"eventId":"e81","orderId":81,"recipientRef":"customer-alice","template":"ORDER_CONFIRMED"}

HTTP/1.1 202 Accepted
{"intentId":"N81","state":"ACCEPTED_FOR_PROCESSING"}

The service resolves authorized tenant/customer contact data and preferences.
202 acknowledges the stored intent; it does not claim the email was delivered.
Repeated e81 for the same permitted recipient/channel resolves to the existing
intent under the documented deduplication policy.""",
'distributed-rate-limiter':"""GET /api/reports
Authorization: Bearer <verified-tenant-access-token>

HTTP/1.1 429 Too Many Requests
Retry-After: 1
Content-Type: application/json

{"error":"RATE_LIMITED","retryAfterSeconds":1}

This is the no-token branch. On the allowed branch, the gateway forwards to the
backend, which separately checks report authorization. A 200 backend response
is not generated merely because the limiter found a token.""",
'multi-tenant-saas':"""GET /projects/42
Authorization: Bearer <alice-access-token>

Derived server context: user=alice, tenant=A, role=member
Database intent: SELECT permitted fields WHERE tenant_id=A AND project_id=42

HTTP/1.1 200 OK
{"projectId":42,"name":"A onboarding","tenantId":"A"}

If project 42 belongs only to tenant B, this request must not return B's record.
Choose a documented forbidden/not-found policy and apply it consistently.
The client cannot grant itself B membership by sending tenantId=B.""",
'real-time-analytics':"""GET /metrics/orders?from=2026-10-23T10:01:00Z&to=2026-10-23T10:02:00Z
Authorization: Bearer <authorized-dashboard-access-token>

HTTP/1.1 200 OK
{"windowStart":"2026-10-23T10:01:00Z","orderCount":14,"aggregateVersion":8,"status":"PROVISIONAL"}

A late permitted event may revise this window to version 9. Replaying an
already-applied event must not increase the count again. Tenant and currency
filters are derived/validated by the API; freshness metadata must distinguish
an unfinished window from a fully final value under the chosen policy."""
}

FOUNDATIONS={
233:('Design the canteen before picking technology','Start with a student placing a lunch order, not with a list of cloud products. Ask what must happen on the screen: browse a menu, choose quantity, place an order, pay and collect. Then ask what may go wrong: duplicate clicks, no stock and a lost payment response. Each requirement should have a measurable or testable outcome. For example, one logical click with retries creates one order, and confirmed orders survive the promised failure model.', 'Work the numbers explicitly. Ten thousand students placing two orders in a ten-hour day means 20,000/36,000 = 0.56 order writes/second average. If 4,000 arrive in ten minutes, that interval is 6.7/second. Menu reads, payment calls, bytes stored and peak concentration are separate dimensions. Start with one API and database; test those assumptions. Use the checkout tutorial to see how an authoritative stock decision leads to API, schema and transaction choices. A design interview answer is an evolving argument, not a diagram chosen before the requirements.'),
234:('Watch one browser request and its response','Bob types https://go.learn.example/aB72xQ9. Split the URL into scheme, hostname and path. DNS resolves only the hostname; it does not translate the short code. Secure transport connects Bob to the shortener’s approved edge and certificate. An HTTP GET then carries the path and hostname to the application, which makes the mapping/access decision. Network setup can be reused across requests; HTTP/3 uses QUIC rather than assuming every request always starts a new TCP connection.', 'The application returns 302 Location: https://courses.example/lesson/42. Bob’s browser follows that instruction with a second request to the destination hostname, whose DNS/TLS and application are separate. If the first service returns 302 and the second returns 500, the two operations had different outcomes. Use a trace/request ID for the boundaries you control, and do not send shortener credentials to the destination. The full Short URL tutorial includes the actual request/response headers.'),
235:('Add an entry component only for its responsibility','Imagine a shop initially running one API behind HTTPS. Adding a second API instance creates a routing question: which healthy instance receives the next request? A load balancer solves that. A reverse proxy describes the role of accepting requests for upstream servers; load balancing may be one of its capabilities. A gateway can additionally enforce API token/quota policy. These roles can be implemented by one product; drawing four boxes is not mandatory.', 'Now serve a public product image repeatedly to distant users: a CDN cache can answer near them. That does not mean a private order response belongs in a public cache. The application must still authorize that the order belongs to the caller even if a gateway validated their identity token. DNS chooses the hostname’s route; API routing chooses the backend/path; object authorization chooses whether the operation is allowed. If a gateway fails, bypassing it is safe only if the alternate route preserves required controls, not merely because the backend is reachable.'),
236:('Design the data question before choosing SQL or NoSQL','Follow checkout: order 81 and its order lines must agree about ownership, totals and state. A relational transaction and constraints are a useful starting point. Now follow a search request for waterproof shoes in size 9: relevance and filtering may need a derived search index. These are two different read/write contracts, not a rule that SQL is old and NoSQL is fast.', 'Write the product change and an outbox event in the source database. An indexer applies versioned changes to the search view. A search result may briefly be stale; checkout still checks current authoritative price and stock. If the index is down, decide whether basic product browsing can use a simpler source lookup; do not make stock correctness depend on index availability. Evaluate a chosen document/key-value product by its actual transaction, query and consistency guarantees. Additional stores require rebuilds, version ordering and permission propagation.'),
237:('Trace a cache hit, a miss and a racing writer','Alice requests product 42. On a cache hit the API can return its permitted cached description without querying the database. On a miss it loads the authoritative row and stores a copy with a TTL. Only the miss branch calls the database; a straight arrow through both boxes can conceal that important choice. Coalesce simultaneous misses so 1,000 waiting readers do not all rebuild the same key.', 'Now a writer commits a new price and invalidates product:42. A reader that loaded the old row before commit may refill the old value afterward. TTL bounds staleness but does not make that race disappear; version-aware updates, ordering and a business-approved freshness policy may be needed. Checkout should revalidate authoritative terms. When Redis is down, cap database fallback concurrency rather than replacing every cache hit with unlimited DB traffic. Test hit, miss, stale refill, invalidation and outage as distinct paths.'),
238:('Recover an order service through three different disasters','First stop one API process: a load balancer can remove it and use a healthy replica if state was external. Next lose the database writer: promotion requires the chosen replication guarantee and fencing the old writer, not just another API process. Finally delete yesterday’s records accidentally: a live replica may copy the delete, so tested historical backup/point-in-time restore is required. These are different recovery mechanisms.', 'Set an example RTO of 30 minutes and RPO of five minutes, then run a drill. Measure time to restore usable user journeys and the actual committed-data gap, not merely time to start a VM. An asynchronous replica may not satisfy zero data loss. Authorization, DNS, certificates, secrets and dependent queues must also work in the recovery environment. Compare restored order/payment state and reconcile unknown external effects before opening full traffic. Availability architecture is incomplete without an executable ownership and recovery procedure.'),
239:('Follow the last-seat decision during a partition','Replicas A, B and C hold stock state. A and B can communicate, while C is isolated. If every side independently promises the last seat, two customers may get a success response for one seat. To preserve the required single-history decision, the isolated side may have to reject or delay. CAP concerns that partition-time trade-off between linearizable behavior and successful responses to every request; it is not a general instruction to pick any two database features.', 'With a fixed replica set N=3, a write quorum W=2 and read quorum R=2 overlap because R+W>N. Explain which replicas participate and how reads reconcile versions. Overlap alone is not a proof of linearizability under concurrent writers or alternative/sloppy replica sets. For booking, use the actual database/consensus transaction contract. For a social feed you might accept stale reads explicitly. Authentication and stock consistency are independent: an authorized caller can still be rejected because the service cannot safely decide during the partition.'),
240:('Spend the final token across two servers','A tenant’s bucket holds one token. Requests reach API instances A and B simultaneously. If both separately read one and later write zero, both enter. An atomic refill/compare/consume operation allows only one request at that boundary. Identify the tenant from verified credentials, not an arbitrary request header. A permitted quota decision still does not authorize access to someone else’s order.', 'For capacity 20 and refill 10 tokens/second, an idle tenant may burst 20, then sustain around the refill rate under the policy. If five nodes instead each maintain an independent full bucket, total allowed traffic can multiply. Decide on shared ownership or allocated local budgets and acceptable overshoot. On store outage, define fail-open/fail-closed per endpoint risk. HTTP 429 should communicate rejection and retry guidance. Backpressure and bounded in-flight work also matter: rate permission cannot create extra database connections or make a slow provider fast.'),
241:('Replay a lost order response without replaying its effect','Alice sends POST /orders with key purchase-81. The server commits order 81 but the response is lost. Alice does not know whether creation failed, so retrying with a fresh identity risks another order. Reuse purchase-81 for the same logical purchase. A tenant-scoped unique idempotency record plus payload fingerprint lets another API instance find the original result.', 'The idempotency claim, local business change and stored result need a defined transactional/concurrent protocol. Two simultaneous claims must not both execute the effect. Different payload reuse is rejected; key retention defines how long replay is recognized. A remote payment is a separate effect: use the provider’s stable key and reconcile unknown outcome. An in-memory cache is not a durable, cluster-wide solution. Test lost response, simultaneous retry, payload conflict, crash before commit and crash after a remote call separately.'),
242:('Scale the layer that is actually saturated','A single API process saturates CPU while the database is comfortable. Add stateless API instances behind routing: that is horizontal application scaling. If the writer database is now saturated, adding more callers may make it worse. Partitioning divides records; sharding distributes partitions across independently operated nodes; replication copies the same records. These actions solve different constraints.', 'For chat, conversation_id can keep one conversation’s messages on one partition for efficient ordered history reads. A routing map identifies the authoritative shard. A huge celebrity conversation is still a hot partition, even when most keys are balanced. Cross-shard queries, tenant authorization, migrations and ownership handoff become explicit design work. Rebalancing cannot let two nodes both act as current writer without a coordination rule. Measure CPU, write capacity, lock contention and hot-key distribution before choosing a shard key or claiming that more servers increase every form of capacity.')}

def content_blocks(source):
 """Safe structured content for portal; no HTML evaluation or remote renderer."""
 blocks=[];lines=source.splitlines();i=0
 while i<len(lines):
  line=lines[i]
  if line.startswith('## Reference documentation'):break
  if line.startswith('```'):
   i+=1;code=[]
   while i<len(lines) and not lines[i].startswith('```'):code.append(lines[i]);i+=1
   blocks.append({'type':'code','text':'\n'.join(code)});i+=1;continue
  if line.startswith('#'):
   blocks.append({'type':'heading','text':line.lstrip('# ').strip()});i+=1;continue
  m=re.fullmatch(r'!\[([^]]*)\]\(([^)]+)\)',line)
  if m:
   blocks.append({'type':'image','text':m[1],'path':'docs/system-design/'+m[2]});i+=1;continue
  if not line.strip():i+=1;continue
  paragraph=[]
  while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','```','![')):
   paragraph.append(lines[i]);i+=1
  if paragraph:blocks.append({'type':'text','text':'\n'.join(paragraph).replace('**','').replace('`','')})
  else:i+=1 # malformed standalone markup must not stall regeneration
 return blocks

def domain_diagrams():
 import html,textwrap
 diagrams={
 'short-url-domain':('Who owns the domain, and who handles the path?',[
 ('Operator chooses a domain','Register a real domain or use a subdomain you control. The destination domain does not choose the short hostname.'),
 ('DNS routes the hostname','go.learn.example aliases the approved hosting endpoint, or uses supported address/alias records. DNS does not inspect /aB72xQ9.'),
 ('Hosting binds the name and certificate','Configure the edge for the hostname and provision/renew a valid TLS certificate. DNS alone is insufficient.'),
 ('Browser sends an HTTP request','After resolving/connecting securely, the browser sends GET /aB72xQ9 with the short hostname.'),
 ('Application resolves domain plus code','Validate the host, find its domain ID, then check mapping, status, expiry and the access policy.')]),
 'short-url-redirect':('One click produces two separate browser requests',[
 ('Browser → shortener','GET https://go.learn.example/aB72xQ9. DNS/TLS reach the shortener, not the course site.'),
 ('Shortener → mapping database','Resolve the approved domain and code. Check status, expiry and public/restricted access before revealing the target.'),
 ('Shortener → browser','HTTP 302; Location: https://courses.example/lesson/42; Cache-Control: no-store in the tutorial baseline.'),
 ('Browser → destination website','The browser follows Location and establishes its own request to courses.example. Shortener credentials are not transferred.'),
 ('Destination → browser','The course site returns its page, its login requirement, or its own error. The shortener’s 302 is not proof the page loaded.')])}
 for slug,(title,steps) in diagrams.items():
  esc=html.escape;svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="1120" viewBox="0 0 960 1120" role="img" aria-labelledby="title desc"><title id="title">{esc(title)}</title><desc id="desc">Five sequential explanatory steps from domain ownership to browser behavior.</desc>','<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="#38bdf8"/></marker></defs>','<rect width="960" height="1120" rx="18" fill="#0f172a"/>',f'<text x="35" y="48" fill="#f8fafc" font-family="Arial,sans-serif" font-size="25">{esc(title)}</text>','<text x="35" y="80" fill="#cbd5e1" font-family="Arial,sans-serif" font-size="17">Reserved .example names illustrate configuration and request flow; these are not live URLs.</text>']
  for j,(label,body) in enumerate(steps):
   y=110+j*185;svg.extend([f'<rect x="35" y="{y}" width="890" height="155" rx="12" fill="#1e293b" stroke="#38bdf8"/>',f'<text x="55" y="{y+34}" fill="#7dd3fc" font-family="Arial,sans-serif" font-size="21">{j+1}. {esc(label)}</text>'])
   for k,line in enumerate(textwrap.wrap(body,91)):svg.append(f'<text x="55" y="{y+66+k*23}" fill="#f1f5f9" font-family="Arial,sans-serif" font-size="17">{esc(line)}</text>')
   if j<4:svg.append(f'<path d="M480,{y+157} L480,{y+181}" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>')
  svg+=['<text x="35" y="1080" fill="#fbbf24" font-family="Arial,sans-serif" font-size="17">Authentication establishes identity; authorization decides each protected operation.</text>','</svg>']
  (ROOT/f'docs/system-design/diagrams/{slug}.svg').write_text('\n'.join(svg),encoding='utf-8')

def references(slug):
 links=[('Authorization on protected operations','https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html')]
 if slug in ('multi-tenant-saas','ai-compliance-auditing-rag'):
  links.append(('Tenant isolation','https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html'))
 if slug in ('whatsapp-style-messaging','notification-platform','real-time-analytics'):
  links.append(('Event delivery semantics','https://kafka.apache.org/41/design/design/'))
 if slug in ('e-commerce-checkout','uber-style-ride-hailing'):
  links.append(('Database concurrency and row locking','https://www.postgresql.org/docs/18/explicit-locking.html'))
 if slug=='e-commerce-checkout':
  links.append(('Safe retries with idempotent APIs','https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/'))
 if slug=='video-streaming-platform':
  links.append(('HTTP Live Streaming','https://developer.apple.com/streaming/'))
 if slug=='ai-compliance-auditing-rag':
  links.append(('Secure multitenant retrieval architecture','https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/secure-multitenant-rag'))
 return '\n'.join('- ['+title+']('+url+')' for title,url in links)+'\n'

def build():
 from build_system_design_cases import CASES
 domain_diagrams()
 for case in CASES:
  slug,title,scenario,requirements,contract,nodes,edges,walk,decisions,failure,capacity,check=case
  if slug=='short-url':continue # Canonical hand-authored tutorial; never replace with a template.
  chapters=JOURNEYS[slug]
  chunks=[f'# Build {title}: follow the complete user journey\n','Read in order: each decision below follows from the same real-world situation. Domains ending in .example are reserved teaching names, not live services. These are illustrative designs, not descriptions of a company’s internal implementation.\n']
  for i,(heading,body) in enumerate(chapters,1):
   chunks.extend([f'## {i}. {heading}\n',body+'\n'])
   if i==3:chunks.extend(['The concrete API/data vocabulary used in this journey:\n',f'```text\n{contract}\n```\n','A concrete request and observable response for this journey (illustrative API contract):\n',f'```http\n{EXCHANGES[slug]}\n```\n',f'![{title} component overview](diagrams/{slug}.svg)\n','Use this diagram to locate the responsibilities just introduced. Arrows show selected requests/data; the paragraphs distinguish return responses, alternatives and transaction boundaries.\n'])
  chunks.extend(['## Work the capacity assumption\n',capacity+' These are illustrative assumptions; measure the chosen implementation and peak distribution before treating them as capacity.\n','## Explain the journey back\n',check+' Then explain the hostname, caller identity, object-level permission, authoritative record, success acknowledgement and crash/retry behavior for this same action.\n','## Reference documentation\n',references(slug),'[All tutorials](README.md) · [Foundation lessons](../system-design-foundations.md)\n'])
  (ROOT/f'docs/system-design/{slug}.md').write_text('\n'.join(chunks),encoding='utf-8')
 questions=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
 primary={243:'short-url',246:'whatsapp-style-messaging',250:'e-commerce-checkout',255:'uber-style-ride-hailing'}
 group={**{i:'short-url' for i in range(243,246)},**{i:'whatsapp-style-messaging' for i in range(246,250)},**{i:'e-commerce-checkout' for i in range(250,255)},**{i:'uber-style-ride-hailing' for i in range(255,259)}}
 for q in questions:
  ident=q['id']
  if ident in FOUNDATIONS:
   heading,part1,part2=FOUNDATIONS[ident]
   q['lessonSections']=[{'title':heading,'explanation':part1},{'title':'Work through the decision and failure','explanation':part2}]
   q['guidePath']='docs/system-design-foundations.md'
  if ident in group:
   slug=group[ident];q['guidePath']=f'docs/system-design/{slug}.md'
   if ident in primary:q['contentBlocks']=content_blocks((ROOT/q['guidePath']).read_text(encoding='utf-8-sig'))
   else:
    if slug=='short-url':
     source=(ROOT/q['guidePath']).read_text(encoding='utf-8-sig')
     target='## 6.' if ident==244 else '## 12.'
     section=next(p for p in re.split(r'(?=^## )',source,flags=re.M) if p.startswith(target))
     q['contentBlocks']=content_blocks('# '+q['question']+'\n\nFollow the same Alice/Bob short-link journey. The complete tutorial below explains domain setup, authentication, authorization and failure handling.\n\n'+section)
    else:
     chosen={'whatsapp-style-messaging':{247:[2,3,4,6],248:[4,5,6,7],249:[1,2,5,6]},'e-commerce-checkout':{251:[0,2,3,5,7],252:[2,3,4,5,7],253:[3,4,7],254:[0,2,6,7]},'uber-style-ride-hailing':{256:[0,1,3,6],257:[2,3,4,6],258:[0,3,5,7]}}[slug][ident]
     q['lessonSections']=[{'title':JOURNEYS[slug][i][0],'explanation':JOURNEYS[slug][i][1]} for i in chosen]
 (ROOT/'data/questions.json').write_text(json.dumps(questions,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 # Top-level topic links show the actual narrative rather than a second competing summary.
 for topic,slug in [('url-shortener','short-url'),('whatsapp-messaging','whatsapp-style-messaging'),('e-commerce-payments','e-commerce-checkout'),('uber-ride-hailing','uber-style-ride-hailing')]:
  source=(ROOT/f'docs/system-design/{slug}.md').read_text(encoding='utf-8-sig')
  source=source.replace('](diagrams/','](system-design/diagrams/').replace('](README.md)','](system-design/README.md)').replace('](../system-design-foundations.md)','](system-design-foundations.md)')
  (ROOT/f'docs/system-design-{topic}.md').write_text(source,encoding='utf-8')
 out=['# System design foundations: learn through worked requests\n','Read these ten lessons in sequence, then build [the Short URL service](system-design/short-url.md). Each lesson changes one part of a concrete request rather than introducing disconnected technology names.\n']
 for q in questions:
  if q['id'] not in FOUNDATIONS:continue
  out.extend([f'## {q["id"]}. {q["question"]}\n'])
  for section in q['lessonSections']:out.extend([f'### {section["title"]}\n',section['explanation']+'\n'])
  out.extend([f'![{q["learningTitle"]}](system-design/diagrams/topic-{q["id"]}.svg)\n','### Trace the steps\n'])
  out.extend(f'{i}. **{s["title"]}:** {s["explanation"]}\n' for i,s in enumerate(q['walkthroughSteps'],1))
  out.extend(['### Explain it back\n',q['knowledgeCheck']+'\n'])
 (ROOT/'docs/system-design-foundations.md').write_text('\n'.join(out),encoding='utf-8')
 print('Built all ten narrative case studies, ten foundation tutorials and all 26 portal lessons.')

if __name__=='__main__':build()
