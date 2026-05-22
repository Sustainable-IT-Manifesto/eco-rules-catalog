# ECO-OBS-LOG-001

**Name:** Excessive production debug logging

**Category:** Observability & Telemetry

**Family:** Logging

**Primary layer:** `process`

**System layers:** `process`

## Description

Verbose debug logging remains enabled in production, increasing CPU, storage, network, and review cost.

## Impact

- **type:** storage
- **confidence:** 0.85
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Set environment-specific log levels, sample noisy events, and apply retention controls.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** medium
- **memory:** low
- **network:** medium
- **storage:** high
- **human_time:** medium
- **carbon:** medium
- **water:** low

## Amplification

- **scales_with_users:** Yes
- **scales_with_data_volume:** Yes
- **scales_non_linearly:** No

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- log volume metrics
- logging config
- storage billing

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
