# ECO-INF-COMPOSE-002

**Name:** Unbounded restart loops for noncritical services

**Category:** Infrastructure

**Family:** Docker Compose

**Primary layer:** `process`

**System layers:** `process`, `architecture`

## Description

Compose configurations that restart transient or low-value services indefinitely can waste local resources and hide operational problems instead of surfacing them.

## Impact

- **cost:** Consumes unnecessary local or CI resources.
- **performance:** Repeated restarts create churn and noise.
- **carbon:** Repeated failed restarts waste compute cycles.

## Detection

- **method:** yaml-compose
- **selector:** compose_unbounded_restart_loops

## Remediation

- **guidance:** Use restart policies intentionally and avoid infinite restart churn for services that should fail fast during development.
- **examples:**
  - Prefer clearer failure behavior for optional tooling containers.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **status:** draft
- **severity:** medium
- **version:** 0.3.0-draft

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
