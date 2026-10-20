# Kafka — Interview Study Guide

65 questions. Java examples use Java 21 unless noted; Angular and SQL snippets are labeled by language.

> **Quality note:** Entries marked “Guided study” include the original answer cue and a production discussion exercise; they are not yet fully curated standalone explanations.

## #168 What is Kafka, and why use it instead of a traditional message broker?

**Priority:** High · **Status:** Expanded

### Concept
Apache Kafka is a distributed event-streaming platform. It stores ordered records in partitioned, replicated logs and lets multiple applications publish and consume events independently. It is especially useful for high-throughput event pipelines, replay, and decoupling services. Unlike many queue-only designs, Kafka retains events according to configured retention policies, so consumers can reread them.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #169 What are topics, partitions, brokers, and offsets?

**Priority:** High · **Status:** Expanded

### Concept
A topic is a named stream of records. A partition is an ordered log within a topic. A broker is a Kafka server that stores partition replicas and serves client requests. An offset is the position of a record within one partition; offsets are not globally unique across a topic.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #170 Can multiple producers publish to the same topic?

**Priority:** High · **Status:** Expanded

### Concept
Yes. Multiple producers can publish concurrently to the same topic. Records are routed to partitions according to the producer's partitioner, key, and configuration. Ordering is guaranteed within a partition, not across the whole topic.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #171 Can multiple consumer groups consume the same topic?

**Priority:** High · **Status:** Expanded

### Concept
Yes. Each consumer group tracks its own progress, so different applications can independently consume the same records. For example, one group can update an order database while another updates analytics.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #172 What is the difference between a consumer and a consumer group?

**Priority:** Medium · **Status:** Expanded

### Concept
A consumer is a client that reads records. A consumer group is a set of consumers that cooperate to consume subscribed partitions. Within one group, each partition is assigned to at most one consumer at a time; different groups can independently read the same partition.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #173 How are messages distributed across partitions?

**Priority:** Medium · **Status:** Expanded

### Concept
A producer can select a partition explicitly, use a key-based partitioner, or use a partitioning strategy for records without keys. With keyed records, records sharing a key are commonly routed to the same partition, preserving per-key ordering while the partition count and partitioning strategy remain stable.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #174 What is the difference between an offset and a message key?

**Priority:** Medium · **Status:** Expanded

### Concept
A key is application data used for partitioning or identifying related records. An offset is Kafka's position number for a record in a specific partition. Keys may repeat; offsets identify positions within a partition.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #175 Can Kafka guarantee message ordering?

**Priority:** Medium · **Status:** Expanded

### Concept
Kafka guarantees order within a single partition. It does not guarantee total ordering across multiple partitions. To preserve order for a particular entity, such as an orderId, publish its events with that entity as the key so they normally go to the same partition.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #176 How does Kafka assign partitions to consumers?

**Priority:** High · **Status:** Expanded

### Concept
The group coordinator manages group membership and offsets, while the group leader and configured assignor determine partition assignments. Assignment strategies include range, round-robin, sticky, and cooperative-sticky approaches, depending on client configuration and version.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #177 Can two consumers in the same group read the same partition simultaneously?

**Priority:** High · **Status:** Expanded

### Concept
Under normal group assignment, no: a partition is assigned to at most one consumer in that group at a time. Two consumers in different groups can read that same partition independently.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #178 What happens when consumers outnumber partitions?

**Priority:** High · **Status:** Expanded

### Concept
Some consumers in the group remain without partition assignments and cannot consume records from that topic. Adding consumers beyond the partition count does not increase parallel consumption of those partitions.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #179 How does a consumer group rebalance work?

**Priority:** High · **Status:** Expanded

### Concept
Kafka redistributes partition assignments when group membership or subscription changes, or when a consumer is considered unavailable. During reassignment, consumption can pause or be disrupted depending on the protocol and assignor. Cooperative rebalancing can reduce the amount of work that must be revoked.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #180 What triggers a rebalance?

**Priority:** Medium · **Status:** Expanded

### Concept
Common triggers include a consumer joining or leaving, a consumer failing heartbeats or exceeding poll limits, topic/partition changes, subscription changes, or group metadata changes.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #181 Who maintains consumer offsets?

**Priority:** Medium · **Status:** Expanded

### Concept
Kafka stores committed offsets in the internal __consumer_offsets topic. Progress is tracked per consumer group and topic-partition. The consumer application typically controls when to commit, either automatically or explicitly.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #182 What is the difference between auto-commit and manual commit?

**Priority:** Medium · **Status:** Expanded

### Concept
Auto-commit periodically commits offsets based on consumer configuration. Manual commits let the application choose when progress is committed, which can better align with successful processing. Incorrect commit timing can cause message loss from the application's perspective or duplicate processing.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #183 What happens if a consumer crashes after processing a message but before committing its
 offset?

**Priority:** Medium · **Status:** Expanded

### Concept
After restart or reassignment, Kafka may deliver that record again because the committed position did not advance. This is at-least-once behavior and can cause duplicate side effects unless processing is idempotent.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #184 How do you handle duplicate message processing?

**Priority:** Medium · **Status:** Expanded

### Concept
Use idempotent processing: for example, enforce a unique event ID in the database, use an upsert, or store processed-event IDs transactionally with the business update. Kafka producer idempotence helps prevent certain duplicate writes from producer retries, but it does not by itself make external database effects exactly once.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #185 What are leader and follower replicas?

**Priority:** High · **Status:** Expanded

### Concept
Each partition has a leader replica that handles normal reads and writes, and zero or more follower replicas that replicate the leader's log. Replicas are typically distributed across brokers for fault tolerance.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #186 What happens when a partition leader's broker crashes?

**Priority:** High · **Status:** Expanded

### Concept
If an eligible in-sync replica is available, Kafka can elect it as the new leader. The partition may be briefly unavailable during detection and election. If no eligible replica is available, availability depends on the configuration and recovery situation.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #187 What is the ISR (in-sync replica) list?

**Priority:** High · **Status:** Expanded

### Concept
ISR means in-sync replicas: replicas considered sufficiently caught up with the leader under Kafka's replication rules. The ISR is important for safe leader election and for interpreting acknowledgements such as acks=all.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #188 What do replication.

**Priority:** High · **Status:** Expanded

### Concept
factor, min.insync.replicas, and acks mean? replication.factor sets how many replicas are configured per partition. min.insync.replicas is the minimum ISR size required for writes with acks=all. Producer acks controls the acknowledgement level: 0 waits for none, 1 waits for the leader, and all waits for the in-sync replicas required by the protocol. These settings work together to balance durability and availability.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #189 What happens when all replicas are unavailable?

**Priority:** Medium · **Status:** Expanded

### Concept
The partition becomes unavailable until a suitable replica can serve as leader. If replicas later recover with their logs intact, data can become available again. If all copies are permanently lost, replication cannot recover the data.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #190 What is unclean leader election?

**Priority:** Medium · **Status:** Expanded

### Concept
Unclean leader election permits a replica outside the ISR to become leader when no ISR replica is available. This can restore availability but may lose records that existed only on the previous leader. Disabling it favors data safety over availability in that situation.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #191 Can Kafka lose messages even with replication factor 3?

**Priority:** Medium · **Status:** Expanded

### Concept
Yes. Possible causes include simultaneous permanent loss of all replicas, weak producer acknowledgements, unsafe leader election, misconfiguration, operator deletion, retention expiry, or an application committing offsets before processing is safely complete. Replication reduces risk but is not a backup against every failure.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #192 How do you design a highly available Kafka cluster?

**Priority:** Medium · **Status:** Expanded

### Concept
Use multiple brokers across independent failure domains, appropriate replication (often factor 3), a suitable min.insync.replicas with acks=all, safe leader-election settings, monitoring, capacity headroom, tested recovery procedures, and backups or replication to another cluster when required. Availability and durability requirements must be balanced explicitly.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #193 What are at-most-once, at-least-once, and exactly-once delivery?

**Priority:** High · **Status:** Expanded

### Concept
At-most-once means a record may be lost but is not intentionally retried after progress is committed. At-least-once means records are retried until processing succeeds, so duplicates are possible. Exactly-once means each intended effect is reflected once within a clearly defined transactional boundary; it should not be claimed for arbitrary external systems without additional coordination.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #194 Does Kafka guarantee exactly-once processing end to end?

**Priority:** High · **Status:** Expanded

### Concept
Kafka supports transactions and exactly-once processing patterns between Kafka topics when producers, consumers, offsets, and isolation settings are configured correctly. End-to-end exactly-once effects involving a relational database, email service, or other external system usually require idempotency, an outbox/inbox pattern, or a coordinated transaction strategy.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #195 What is idempotent production?

**Priority:** High · **Status:** Expanded

### Concept
An idempotent producer uses producer IDs and sequence numbers so Kafka can deduplicate retrying writes from the same producer session and preserve ordering under supported retry scenarios. It reduces duplicate records caused by producer retries, but it does not deduplicate arbitrary application-level repeated sends.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #196 How do Kafka transactions work?

**Priority:** High · **Status:** Expanded

### Concept
A transactional producer can write records to multiple partitions and commit or abort them as a unit. Consumers configured with isolation.level=read_committed read only committed transactional records. Transactions can also include consumed offsets, enabling atomic consume-process-produce flows within Kafka.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #197 What is the difference between producer idempotence and consumer idempotency?

**Priority:** Medium · **Status:** Expanded

### Concept
Producer idempotence prevents certain duplicate log writes caused by producer retries. Consumer idempotency makes repeated processing of the same event safe, such as by using a unique event ID and a database uniqueness constraint. They protect different boundaries.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #198 How do you atomically write output records and commit consumed offsets?

**Priority:** Medium · **Status:** Expanded

### Concept
Use a transactional producer: begin a transaction, produce output records, add the consumed offsets to the transaction using the consumer group metadata, and commit. If the transaction aborts, output records and offsets are not committed as a successful unit. Exact APIs depend on the Kafka client version.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #199 How would you prevent duplicate database updates?

**Priority:** Medium · **Status:** Expanded

### Concept
Make the handler idempotent. A common pattern is to assign each event a stable ID and, in one database transaction, insert that ID into a processed-events table with a unique constraint and apply the business update. If the ID already exists, skip the duplicate. Carefully coordinate offset commits with successful database commits.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #200 How do you implement a retry and dead-letter topic strategy?

**Priority:** Medium · **Status:** Expanded

### Concept
Retry transient failures with bounded attempts and backoff, then route poison or exhausted messages to a dead-letter topic with the original topic, partition, offset, key, error, and timestamp in headers or metadata. Define replay procedures and alerting. Avoid blocking a partition indefinitely, and preserve ordering where the business requires it.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #201 How do producer acknowledgments work?

**Priority:** High · **Status:** Expanded

### Concept
acks=0 means no broker acknowledgement is awaited; acks=1 waits for the leader's local write; acks=all waits for acknowledgement from the in-sync replicas according to Kafka's replication protocol and min.insync.replicas constraints. Higher durability can increase latency or reduce write availability.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #202 What are batching, linger.

**Priority:** High · **Status:** Expanded

### Concept
ms, and compression? The producer batches records per partition. linger.ms allows a short wait to build larger batches; batch.size limits batch size. Compression (such as gzip, lz4, or zstd, depending on client support) reduces network and disk traffic, trading some CPU for throughput.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #203 How do keys affect partition selection and ordering?

**Priority:** High · **Status:** Expanded

### Concept
A key commonly determines the partition, keeping events with the same key together and ordered within that partition. If the partition count or partitioner changes, key-to-partition mapping may change, so strict long-term ordering for a key needs careful topic and migration design.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #204 What happens when a hot key overloads one partition?

**Priority:** High · **Status:** Expanded

### Concept
A high-volume key can concentrate traffic on one partition while others are underused. Options include changing the key strategy, sharding the key, increasing partitions where appropriate, or splitting the workload. Sharding can weaken per-entity ordering and must be designed around business requirements.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #205 How do you tune producer throughput and latency?

**Priority:** Medium · **Status:** Expanded

### Concept
Measure first. Tune batch.size, linger.ms, compression.type, buffer.memory, request limits, acknowledgements, and partition count based on throughput, latency, durability, and broker capacity. Monitor retries, request latency, record errors, and buffer exhaustion.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #206 What are backpressure and consumer lag?

**Priority:** Medium · **Status:** Expanded

### Concept
Backpressure is the mechanism by which a slower downstream system limits upstream intake. Consumer lag describes how far a consumer group's position is behind the log end, commonly measured in records or offsets. Lag can grow because of slow processing, insufficient consumers/partitions, broker issues, or traffic spikes.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #207 How do you investigate increasing consumer lag?

**Priority:** Medium · **Status:** Expanded

### Concept
Check lag by partition, input rate versus processing rate, consumer errors and latency, rebalance frequency, poll/heartbeat settings, downstream database/API latency, GC and CPU, broker/network health, and partition skew. Scale consumers only when there are unassigned partitions or partition parallelism can be increased safely.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #208 How do you choose the number of partitions?

**Priority:** Medium · **Status:** Expanded

### Concept
Estimate throughput per partition, required consumer parallelism, message ordering needs, retention and storage, and broker capacity. More partitions can improve parallelism but increase metadata, file handles, recovery work, and operational overhead. Load-test and leave room for growth.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #209 How does Kafka store records on disk?

**Priority:** High · **Status:** Expanded

### Concept
Kafka stores partition data as an append-only log split into segment files. Records are written sequentially, which supports efficient disk and network use. The operating system page cache often plays an important role in read performance.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #210 What are segments, indexes, and log retention?

**Priority:** High · **Status:** Expanded

### Concept
A partition log is divided into segments. Indexes help locate offsets and timestamps efficiently. Retention policies remove old or excess log segments based on time or size; deleting old data is separate from consumer offset commits.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #211 What is log compaction?

**Priority:** High · **Status:** Expanded

### Concept
Compaction retains the latest known value for each key over time, while allowing older values for the same key to be removed. It is useful for changelog or state-reconstruction topics. It is asynchronous, and tombstone records mark deleted keys for removal during compaction.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #212 What are retention by time, size, and compaction?

**Priority:** High · **Status:** Expanded

### Concept
Time retention removes segments after a configured age; size retention removes older segments to stay within a configured log-size limit; compaction keeps the latest value per key rather than preserving every historical value indefinitely. A topic can be configured with policies appropriate to its use case.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #213 What is the role of the controller?

**Priority:** Medium · **Status:** Expanded

### Concept
The controller manages cluster metadata and coordination tasks such as partition leadership and broker state changes. In modern Kafka using KRaft, controller nodes use the metadata quorum rather than ZooKeeper to manage cluster metadata.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #214 What is KRaft, and how does it differ from ZooKeeper-based Kafka?

**Priority:** Medium · **Status:** Expanded

### Concept
KRaft is Kafka's built-in consensus-based metadata management mode. Older Kafka deployments used ZooKeeper for cluster metadata and controller coordination. KRaft removes the separate ZooKeeper dependency and uses a Kafka metadata log and controller quorum.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #215 How does replication work internally?

**Priority:** Medium · **Status:** Expanded

### Concept
Followers fetch records from the leader and append them to their own logs. Replica progress is tracked, and leader election uses replica eligibility and ISR state. Replication is asynchronous in typical operation, so acknowledgement settings matter for durability.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #216 What is the high-watermark concept?

**Priority:** Medium · **Status:** Expanded

### Concept
The high watermark is the offset boundary up to which records are considered replicated sufficiently for normal consumer visibility. It helps distinguish records that are safe to expose from records that may not yet be safely replicated. Exact behavior depends on Kafka's replication protocol and version.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #217 How do you configure Kafka producers and consumers in Spring Boot?

**Priority:** High · **Status:** Expanded

### Concept
Set bootstrap servers, serializers/deserializers, group ID, offset policy, and security settings in application configuration. Use KafkaTemplate for producing and @KafkaListener for consuming. Configure error handling, retry policy, transactions, and observability explicitly for production.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #218 What are @KafkaListener and ConsumerRecord?

**Priority:** High · **Status:** Expanded

### Concept
@KafkaListener marks a Spring-managed method that receives records from Kafka. ConsumerRecord provides record metadata such as topic, partition, offset, key, value, timestamp, and headers. Listener signatures can also receive just the value or other supported metadata types.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #219 How do you configure retries and error handlers?

**Priority:** High · **Status:** Expanded

### Concept
Use Spring Kafka's error-handling facilities, such as DefaultErrorHandler and configured backoff, and a dead-letter publishing recoverer when appropriate. Decide which exceptions are retryable, bound attempts, and ensure DLT publishing failures are handled.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #220 How do you handle deserialization errors?

**Priority:** High · **Status:** Expanded

### Concept
Use appropriate serializers/deserializers and validation. Spring Kafka can use error-handling deserializers to capture deserialization failures and route or recover those records. Record enough metadata for investigation without exposing sensitive payload data.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #221 How do you manage database transactions with Kafka consumers?

**Priority:** Medium · **Status:** Expanded

### Concept
A Kafka transaction does not automatically include an ordinary database transaction. A robust approach is often database idempotency plus carefully ordered commits, or an outbox/inbox pattern. If using Spring transaction support, understand exactly which resources are coordinated and what failure windows remain.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #222 How do you test Kafka integrations?

**Priority:** Medium · **Status:** Expanded

### Concept
Unit-test business logic separately. For integration tests, use an embedded broker or a containerized Kafka test environment, publish test records, verify outputs and error behavior, and test retry, serialization, and restart scenarios. Avoid tests that depend on arbitrary sleeps when a deterministic condition can be used.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #223 How do you manage schemas and backward compatibility?

**Priority:** Medium · **Status:** Expanded

### Concept
Use a schema format and registry where appropriate, define compatibility rules, and evolve schemas additively where possible. Ensure old and new consumers can handle deployed versions, and test producer/consumer compatibility before rollout.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #224 How do you monitor consumer lag and broker health?

**Priority:** Medium · **Status:** Expanded

### Concept
Monitor lag by group and partition, throughput, request latency, under-replicated partitions, offline partitions, ISR changes, disk usage, CPU, network, produce/fetch errors, rebalances, and consumer processing latency. Alert on sustained symptoms tied to service-level objectives.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #225 Design an event-driven order processing system using Kafka.

**Priority:** High · **Status:** Expanded

### Concept
Publish an OrderCreated event keyed by orderId. Separate consumers handle inventory, payment, shipping, and notifications through their own groups. Use schema versioning, idempotent handlers, bounded retries, DLTs, tracing, and an outbox pattern to reliably publish events from a database transaction. Define compensation for cross-service failures rather than assuming one global transaction.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #226 Design a multi-channel notification platform using Kafka.

**Priority:** High · **Status:** Expanded

### Concept
An API validates requests and persists accepted notification jobs, preferably with an outbox. Kafka distributes events to channel-specific workers for push, email, SMS, or in-app delivery. Use per-channel consumer groups, provider rate limits, retry topics, DLTs, idempotency keys, preference/consent checks, delivery-status events, metrics, and prioritization. Partition by a suitable key and size capacity for peak traffic.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #227 Design a payment event pipeline with strong durability guarantees.

**Priority:** High · **Status:** Expanded

### Concept
Use durable replicated topics, acks=all, suitable min.insync.replicas, idempotent producers, strict schema governance, and idempotent consumers. Persist payment state transactionally and use unique transaction/event IDs. Keep an audit trail, reconcile with the payment provider, monitor lag and replication health, and define recovery and replay procedures.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #228 How would you process 1 million events per second?

**Priority:** High · **Status:** Expanded

### Concept
Start by measuring record size, key distribution, latency target, and downstream capacity. Partition enough to parallelize producers and consumers, scale brokers and consumers horizontally, batch and compress, use efficient serialization, and avoid hot keys. Load-test end-to-end and monitor disk/network throughput, replication, lag, and failure recovery. No fixed partition count guarantees a target rate.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #229 How do you handle poison messages without blocking a partition?

**Priority:** Medium · **Status:** Expanded

### Concept
Classify failures. Retry transient issues with bounded backoff; route repeatedly failing records to a DLT or retry topic with diagnostic metadata. Ensure offset handling does not skip records unintentionally. If strict ordering is required, decide whether later records for that key must wait until the failed event is repaired.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #230 How would you migrate a live system to Kafka without losing events?

**Priority:** Medium · **Status:** Expanded

### Concept
Use a controlled dual-write or transactional outbox approach, define an authoritative source, and reconcile counts or event IDs. If replaying from a database or old broker, establish a consistent cutover point, make consumers idempotent, monitor duplicates and gaps, and perform a staged cutover with rollback criteria.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #231 How do you replay historical events safely?

**Priority:** Medium · **Status:** Expanded

### Concept
Choose a replay strategy such as a dedicated consumer group, a new topic, or resetting offsets in a controlled group. Make side effects idempotent, throttle replay to protect downstream systems, preserve event versions, and separate replay traffic from live traffic if needed. Understand retention and compaction before relying on historical records.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---

## #232 How would you evolve topic schemas without breaking consumers?

**Priority:** Medium · **Status:** Expanded

### Concept
Use backward/forward compatibility rules, add optional fields with safe defaults, and deploy consumers that tolerate old and new versions before producers begin emitting new fields. Avoid changing field meaning or types in place. Test compatibility and use versioned events or topics for breaking changes.

### Why / when
Use this Kafka capability when independently deployed services must process events at different rates while preserving the delivery and ordering guarantees required by the business.

### Production example
A retail order service emits OrderPlaced events to Kafka. Inventory, billing and notifications use separate consumer groups. Test broker failover, duplicate delivery and consumer restarts against the specific behavior in this question.

### Trade-offs and failure modes
Kafka orders events only within a partition, not globally. Delivery retries can produce duplicate processing; use idempotent consumers, suitable retention, schema evolution and lag alerts. Do not assume Kafka transactions include an external database.

### Follow-up questions
- How would you test this during a broker restart?
- What happens when the consumer retries the same record?
- Which metrics and alerts would you deploy?

---
