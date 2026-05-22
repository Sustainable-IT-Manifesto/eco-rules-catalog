# Logging (LOG)

- [Back to Observability & Telemetry (OBS)](../../index.md)

**Total rules:** 2

## Rules

### [ECO-OBS-LOG-001 — Excessive production debug logging](../../../../ECO-OBS-LOG-001.md)

Verbose debug logging remains enabled in production, increasing CPU, storage, network, and review cost.

- Layer: **process**

### [ECO-OBS-LOG-002 — Large payload logging](../../../../ECO-OBS-LOG-002.md)

Application logs capture full request, response, or message bodies where summaries or identifiers would be sufficient.

- Layer: **data**
