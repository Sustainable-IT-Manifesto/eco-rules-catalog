# Operations rules

**Code:** `OPS`

**Total rules:** 2

- [Back to Human Catalog](../index.md)

## Rules

### [ECO-OPS-SEC-001 — Repeated token introspection on hot path](../ECO-OPS-SEC-001.md)

Every request performs remote token introspection or identity lookup without safe caching or local validation.

- Category: **Operations**
- Family: **Identity & Security Efficiency**
- Layer: **network**

### [ECO-OPS-SEC-002 — Secrets retrieval on every request](../ECO-OPS-SEC-002.md)

Application code fetches secrets from a remote secret store on each request instead of caching with rotation-aware controls.

- Category: **Operations**
- Family: **Identity & Security Efficiency**
- Layer: **code**
