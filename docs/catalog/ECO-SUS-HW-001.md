# ECO-SUS-HW-001

**Name:** Premature hardware refresh policy

**Category:** Sustainability & Environmental Impact

**Family:** Hardware Lifecycle

**Primary layer:** `process`

**System layers:** `process`

## Description

Hardware is refreshed on a fixed schedule without utilization, repairability, reuse, or embodied-impact review.

## Impact

- **type:** embodied-impact
- **confidence:** 0.6
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Base refresh decisions on reliability, security, workload fit, repairability, reuse, and embodied impact.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** low
- **memory:** low
- **network:** low
- **storage:** low
- **human_time:** medium
- **carbon:** high
- **water:** medium

## Amplification

- **scales_with_users:** No
- **scales_with_data_volume:** No
- **scales_non_linearly:** No

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- asset inventory
- procurement policy
- utilization data

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
