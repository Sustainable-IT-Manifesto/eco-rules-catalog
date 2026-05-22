# ECO-ARC-ARCH-010

**Name:** No observability on utilization

**Category:** Architecture

**Family:** Architecture

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Without utilization metrics, waste is invisible and persistent.

## Impact

- **confidence:** 0.85
- **notes:** Systemic maturity issue.
- **type:** cost

## Detection

- **languages:** `infra`, `org`
- **method:** config

## Remediation

- **guidance:** Instrument CPU/mem/QPS/latency; add dashboards and alerts.
- **tradeoffs:** Telemetry cost; requires curation.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
