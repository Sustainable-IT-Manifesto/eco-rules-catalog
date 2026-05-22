# ECO-OBS-METRIC-001

**Name:** High-cardinality metric explosion

**Category:** Observability & Telemetry

**Family:** Metrics

**Primary layer:** `data`

**System layers:** `data`

## Description

Metrics include unbounded labels such as user IDs, request IDs, or raw paths, causing storage and query amplification.

## Impact

- **type:** storage
- **confidence:** 0.8
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Bound label values, aggregate dimensions, normalize paths, and reject unbounded labels in review.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
- **network:** medium
- **storage:** high
- **human_time:** medium
- **carbon:** medium
- **water:** low

## Amplification

- **scales_with_users:** Yes
- **scales_with_data_volume:** Yes
- **scales_non_linearly:** Yes

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- metrics backend cardinality
- query latency
- observability billing

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
- [Back to Observability & Telemetry category](categories/obs/index.md)
- [Back to Metrics family](categories/obs/families/metric/index.md)
- [Back to Rule Browser](../rule-browser.md)
