# ECO-OPS-SEC-002

**Name:** Secrets retrieval on every request

**Category:** Operations

**Family:** Identity & Security Efficiency

**Primary layer:** `code`

**System layers:** `code`

## Description

Application code fetches secrets from a remote secret store on each request instead of caching with rotation-aware controls.

## Impact

- **type:** network
- **confidence:** 0.7
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Cache secrets safely in process with TTLs, rotation hooks, and least-privilege access.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** medium
- **memory:** low
- **network:** high
- **storage:** low
- **human_time:** medium
- **carbon:** medium
- **water:** low

## Amplification

- **scales_with_users:** Yes
- **scales_with_data_volume:** No
- **scales_non_linearly:** No

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- secret manager metrics
- request traces
- code review

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0
- **status:** draft
- **source:** catalog expansion recommendations applied 2026-05-21

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Operations category](categories/ops/index.md)
- [Back to Identity & Security Efficiency family](categories/ops/families/sec/index.md)
- [Back to Rule Browser](../rule-browser.md)
