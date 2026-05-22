# Resilience & Reliability rules

**Code:** `RES`

**Total rules:** 3

- [Back to Human Catalog](../index.md)

## Rules

### [ECO-RES-DEG-001 — No degraded mode for optional dependencies](../ECO-RES-DEG-001.md)

The system fails completely when optional dependencies such as recommendations, analytics, or enrichment are unavailable.

- Category: **Resilience & Reliability**
- Family: **Graceful Degradation**
- Layer: **architecture**

### [ECO-RES-DR-001 — Untested regional failover](../ECO-RES-DR-001.md)

A system claims regional resilience, but failover paths are not regularly tested under realistic conditions.

- Category: **Resilience & Reliability**
- Family: **Disaster Recovery**
- Layer: **process**

### [ECO-RES-FAIL-001 — Retry storm without backoff](../ECO-RES-FAIL-001.md)

Clients retry failures aggressively without exponential backoff, jitter, or circuit breaking.

- Category: **Resilience & Reliability**
- Family: **Failure Handling**
- Layer: **architecture**
