# Azure — Services & Architecture

10 senior-level interview questions with architectural trade-offs, practical examples and follow-ups.

> Answers are original study material. Product capabilities and cloud SKUs should be checked against current vendor documentation before deployment.

## 274. Azure App Service vs Azure VM vs AKS vs Container Apps?

**Concept:** Deployment target depends on operational control, workload and orchestration needs.

**How and why:** App Service for managed web/API; VM for OS control/custom dependencies; Container Apps for serverless containers and event scaling; AKS for Kubernetes control.

**Real-world example:** Spring Boot REST API on App Service, worker on Container Apps, complex multi-service platform on AKS.

**Trade-offs / failure modes:** AKS has high ops overhead; VM demands patching and capacity management.

**Interview follow-up:** Where would you host Ollama or a self-managed LLM?

## 275. Azure Functions vs Logic Apps vs Durable Functions?

**Concept:** They serve different event-driven and workflow needs.

**How and why:** Functions runs code triggered by events; Durable Functions coordinates stateful code workflows; Logic Apps orchestrates SaaS/business integrations visually.

**Real-world example:** Blob upload triggers Functions to extract document text; Durable workflow waits for human approval.

**Trade-offs / failure modes:** Long-running work needs retry and idempotency design.

**Interview follow-up:** What is cold start?

## 276. Azure API Management vs Front Door vs Application Gateway?

**Concept:** These services operate at different layers of ingress and policy.

**How and why:** Front Door global edge/CDN/WAF; Application Gateway regional L7 load balancing/WAF; API Management API policy, products and developer portal.

**Real-world example:** Global Angular app via Front Door; partner APIs via API Management; regional private ingress via Application Gateway.

**Trade-offs / failure modes:** Overlapping WAF and routing policies can add cost and complexity.

**Interview follow-up:** Where should OAuth token validation happen?

## 277. Azure SQL vs Azure Database for PostgreSQL vs Cosmos DB?

**Concept:** Choose based on SQL ecosystem, extension needs and global distribution.

**How and why:** Azure SQL for SQL Server ecosystem; PostgreSQL Flexible Server for Postgres and supported extensions; Cosmos DB for globally distributed NoSQL access patterns.

**Real-world example:** Compliance RAG stores metadata and vectors using PostgreSQL with pgvector where supported.

**Trade-offs / failure modes:** Cosmos partition-key choice affects RU cost and hot partitions.

**Interview follow-up:** How do you design tenant isolation?

## 278. Azure Service Bus vs Event Hubs vs Event Grid?

**Concept:** Messaging services have distinct semantics.

**How and why:** Service Bus for enterprise queues/topics, DLQ and workflows; Event Hubs for high-throughput telemetry streams; Event Grid for event notifications/routing.

**Real-world example:** Order workflow uses Service Bus; device telemetry streams into Event Hubs; blob-created event via Event Grid.

**Trade-offs / failure modes:** Do not assume Event Grid replaces a durable work queue.

**Interview follow-up:** Where does Apache Kafka fit?

## 279. Azure Blob Storage vs Azure Files vs managed disks?

**Concept:** Object, file and block storage solve different workloads.

**How and why:** Blob for unstructured objects and lifecycle policies; Files for SMB/NFS shares; disks for VM block devices.

**Real-world example:** Store uploaded compliance PDFs in Blob Storage with metadata in PostgreSQL.

**Trade-offs / failure modes:** Choose retention, encryption and access tiers carefully.

**Interview follow-up:** How do you implement short-lived download URLs?

## 280. Azure Key Vault, Managed Identity and Microsoft Entra ID?

**Concept:** Avoid hard-coded credentials and centralize identity and secret handling.

**How and why:** Entra authenticates principals; Managed Identity obtains workload tokens; Key Vault stores secrets/keys/certs; RBAC limits access.

**Real-world example:** Spring Boot App Service uses Managed Identity to access Key Vault and Azure resources.

**Trade-offs / failure modes:** Secret rotation and least privilege still need operations.

**Interview follow-up:** Managed Identity vs service principal?

## 281. Azure Monitor, Application Insights and OpenTelemetry?

**Concept:** Observability combines metrics, logs and traces.

**How and why:** Instrument Java service with OpenTelemetry; export telemetry to Azure Monitor/Application Insights; define alerts and SLO dashboards.

**Real-world example:** Trace 95th percentile checkout latency across API, DB and messaging.

**Trade-offs / failure modes:** High-cardinality labels and verbose traces can increase costs.

**Interview follow-up:** How do you detect silent failures?

## 282. Azure OpenAI vs self-hosted open-weight model?

**Concept:** Managed APIs reduce infrastructure operations; self-hosting increases control but adds GPU/serving burden.

**How and why:** Compare residency, data policies, model quality, latency, throughput, cost and governance; deploy behind an abstraction.

**Real-world example:** Prototype with Ollama locally; use approved managed model endpoint for production compliance assistant if requirements fit.

**Trade-offs / failure modes:** Do not assume an App Service CPU plan can efficiently serve a large LLM.

**Interview follow-up:** When choose Azure ML managed endpoints or GPU VMs?

## 283. Azure networking: VNet, private endpoint, NSG and VPN?

**Concept:** Private networking reduces exposure of data services and model endpoints.

**How and why:** Use VNet segmentation, private endpoints to PaaS, NSG traffic rules, private DNS and VPN/ExpressRoute where required.

**Real-world example:** Private PostgreSQL and Blob endpoints accessible only to compliance services.

**Trade-offs / failure modes:** Private endpoints require correct DNS and routing.

**Interview follow-up:** How do you troubleshoot a private DNS issue?
