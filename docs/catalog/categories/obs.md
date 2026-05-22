# Observability & Telemetry rules

**Code:** `OBS`

**Total rules:** 4

- [Back to Human Catalog](../index.md)

## Rules

### [ECO-OBS-LOG-001 — Excessive production debug logging](../ECO-OBS-LOG-001.md)

Verbose debug logging remains enabled in production, increasing CPU, storage, network, and review cost.

- Category: **Observability & Telemetry**
- Family: **Logging**
- Layer: **process**

### [ECO-OBS-LOG-002 — Large payload logging](../ECO-OBS-LOG-002.md)

Application logs capture full request, response, or message bodies where summaries or identifiers would be sufficient.

- Category: **Observability & Telemetry**
- Family: **Logging**
- Layer: **data**

### [ECO-OBS-METRIC-001 — High-cardinality metric explosion](../ECO-OBS-METRIC-001.md)

Metrics include unbounded labels such as user IDs, request IDs, or raw paths, causing storage and query amplification.

- Category: **Observability & Telemetry**
- Family: **Metrics**
- Layer: **data**

### [ECO-OBS-TRACE-001 — Unsampled high-volume tracing](../ECO-OBS-TRACE-001.md)

Tracing is enabled for high-volume paths without sampling, retention limits, or cardinality controls.

- Category: **Observability & Telemetry**
- Family: **Tracing**
- Layer: **network**
