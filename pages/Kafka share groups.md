- **Blip:** [Kafka share groups](https://www.thoughtworks.com/radar/platforms/kafka-share-groups)
- **Time:** ~1 hour
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know how Kafka topics, partitions and consumer groups work.

---

## Current state (late 2026)

Kafka has always been a log, not a queue: in a consumer group, each partition goes to one consumer, so you can't have more active consumers than partitions, and one slow message holds up the rest of its partition. Teams that needed a work queue often ran a separate message broker next to Kafka. KIP-932, "Queues for Kafka", adds share groups: any consumer in the group can take any record, and acknowledges it individually. It arrived as early access in Kafka 4.0 (2025) and, according to the blip, has been production-ready since Kafka 4.2. Dead-letter queues aren't there yet.

## Level 1 — What it is (~10 min)

Queue-like consumption on Kafka: records go to any available consumer, each with its own lock and acknowledgement.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/kafka-share-groups) (~1 min) — note the trade-off: you lose ordering within a partition, and get at-least-once delivery, with possible duplicates.

## Level 2 — How it behaves (~50 min)

See share groups in action, including their rough edges.

- [ ] **~40 min** · Read: [Let's Take a Look at... KIP-932: Queues for Kafka!](https://morling.dev/blog/kip-932-queues-for-kafka) (Gunnar Morling, Mar 2025, ~13 min) — a hands-on look by a well-known Kafka practitioner: acknowledging, releasing and rejecting records, delivery limits, and where the state is stored. It was written for the 4.0 early access, so some of the rough edges he found may be fixed by now.
- [ ] **~10 min** · **Do:** Pick a workload you know that runs on a separate queue next to Kafka, or one that's limited by the number of partitions. Write down whether share groups could replace it, given the missing ordering and dead-letter queues.

## Wrap-up

This plan covers it. The original proposal, [KIP-932](https://cwiki.apache.org/confluence/display/KAFKA/KIP-932:+Queues+for+Kafka), is the reference if you'll implement it.

## Review the blip

- [ ] **~5 min** · Re-read [Kafka share groups](https://www.thoughtworks.com/radar/platforms/kafka-share-groups) now that you know the topic.
