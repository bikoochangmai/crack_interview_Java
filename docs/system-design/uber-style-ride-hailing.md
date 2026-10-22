# Uber-style ride hailing: a worked design

**Real-world situation:** A rider at a railway station needs an available driver who can reach them soon.

This is an illustrative architecture, not a claim about a specific company’s implementation.

## What we need and why

Location freshness, nearby search, one driver per active assignment and durable trip lifecycle. Illustrative design, not Uber internals.

## API and data ownership

POST /rides; POST /offers/{id}/accept with expected state/version. DriverPosition(timestamp, coordinates), Trip(state, rider, driver, version), Assignment.

## Component diagram

![Uber-style ride hailing architecture](diagrams/uber-style-ride-hailing.svg)

Arrows show requests or emitted data. Responses generally return to callers and are omitted. Branches can be alternatives rather than steps that always run.

## Follow one request

Find drivers in nearby cells including neighbors, discard stale positions, rank a shortlist by road ETA and send expiring offers. On acceptance, atomically claim available driver and pending trip within the authoritative boundary. Only committed assignment is confirmed to clients.

## Why these components exist

Geographic index is a candidate view, not proof of availability. Use guarded state transitions. Separate-shard ownership requires a recoverable assignment protocol.

## Failure walkthrough

Reject late acceptances. On reconnect, fetch durable trip status. Fence stale owners so an expired lock cannot authorize a conflicting write.

## Capacity worked example

50,000 drivers updating every five seconds create 10,000 location writes/second; coalesce updates and expire old positions.

## Explain it back

Why might the nearest driver in straight-line distance not have the shortest pickup ETA?

[Beginner glossary and learning order](visual-learning-guide.md) · [All case studies](README.md)
