# ECO-RES-DEG-001

**Name:** No degraded mode for optional dependencies

**Category:** Resilience & Reliability

**Family:** Graceful Degradation

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

The system fails completely when optional dependencies such as recommendations, analytics, or enrichment are unavailable.

## Impact

- **type:** resilience
- **confidence:** 0.75
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Classify dependencies by criticality and provide fallback, cached, or reduced-function behavior for non-critical services.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** medium
- **memory:** low
- **network:** medium
- **storage:** low
- **human_time:** high
- **carbon:** medium
- **water:** low

## Amplification

- **scales_with_users:** Yes
- **scales_with_data_volume:** No
- **scales_non_linearly:** Yes

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- architecture review
- dependency traces
- incident reports

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
- [Back to Resilience & Reliability category](categories/res/index.md)
- [Back to Graceful Degradation family](categories/res/families/deg/index.md)
- [Back to Rule Browser](../rule-browser.md)
