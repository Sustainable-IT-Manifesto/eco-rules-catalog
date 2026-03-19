# ECO-INF-COMPOSE-001

**Name:** Overprovisioned default Compose stack

**Category:** Infrastructure

**Family:** Docker Compose

**Primary layer:** `process`

**System layers:** `process`, `architecture`

## Description

Compose files that always start optional databases, observability services, caches, and workers even when they are not needed consume developer resources and energy for little value.

## Impact

- **cost:** Wastes local and CI resources.
- **performance:** Consumes memory and CPU that could be used elsewhere.
- **carbon:** Runs more services than needed for the task at hand.

## Detection

- **method:** yaml-compose
- **selector:** compose_default_stack_overprovisioned

## Remediation

- **guidance:** Use profiles or separate compose overlays so services start only when needed.
- **examples:**
  - Make observability and auxiliary services opt-in rather than default.

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
