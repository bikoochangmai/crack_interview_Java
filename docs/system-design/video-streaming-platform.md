# Video streaming platform: a worked design

**Real-world situation:** A teacher uploads a lecture; students watch it on mobile connections.

This is an illustrative architecture, not a claim about a specific company’s implementation.

## What we need and why

Durable upload, asynchronous transcoding, access-controlled playback and adaptive bitrate quality.

## API and data ownership

POST /uploads issues scoped upload authorization; GET /videos/{id}/playback authorizes a manifest. Video(owner, status), Rendition(codec, bitrate, segments), Job.

## Component diagram

![Video streaming platform architecture](diagrams/video-streaming-platform.svg)

Arrows show requests or emitted data. Responses generally return to callers and are omitted. Branches can be alternatives rather than steps that always run.

## Follow one request

Store the source first and mark processing. Queue a job to produce multiple bitrates and segment manifests. Publish a playable version only when required outputs exist. The player requests segments through the CDN and adapts quality to observed bandwidth.

## Why these components exist

Object storage holds large immutable media; metadata DB tracks ownership/status. Encode asynchronously because it is CPU-heavy and slow relative to an upload acknowledgement.

## Failure walkthrough

Retries must not publish partial manifests or overwrite a newer version. CDN cache policy and signed/scoped playback access must protect private lectures.

## Capacity worked example

At 2 Mbit/second × 10,000 simultaneous viewers, delivery is about 20 Gbit/second before overhead. CDN bandwidth dominates, not metadata QPS.

## Explain it back

Why should an upload succeed before every video rendition is ready?

[Beginner glossary and learning order](visual-learning-guide.md) · [All case studies](README.md)
