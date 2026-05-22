# ECO-OBS-TRACE-001

**Name:** Unsampled high-volume tracing

**Category:** Observability & Telemetry

**Family:** Tracing

**Primary layer:** `network`

**System layers:** `network`

## Description

Tracing is enabled for high-volume paths without sampling, retention limits, or cardinality controls.

## Impact

- **type:** network
- **confidence:** 0.75
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Apply adaptive sampling, route-specific sampling, shorter retention, and cardinality controls.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
- **network:** high
- **storage:** high
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

- trace volume
- collector CPU
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
- [Back to Rule Browser](../rule-browser.md)
