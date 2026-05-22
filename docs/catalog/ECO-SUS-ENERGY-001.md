# ECO-SUS-ENERGY-001

**Name:** Always-on non-production environments

**Category:** Sustainability & Environmental Impact

**Family:** Energy Efficiency

**Primary layer:** `process`

**System layers:** `process`

## Description

Development, test, preview, or demo environments remain powered continuously without an operational need.

## Impact

- **type:** energy
- **confidence:** 0.8
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Add schedules, lifecycle policies, ephemeral environments, or automated shutdown for idle non-production resources.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** high
- **memory:** medium
- **network:** low
- **storage:** medium
- **human_time:** low
- **carbon:** high
- **water:** medium

## Amplification

- **scales_with_users:** No
- **scales_with_data_volume:** No
- **scales_non_linearly:** No

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** No
- **time_degradation:** Yes

## Runtime Evidence

- cloud inventory
- schedules
- billing data

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
- [Back to Sustainability & Environmental Impact category](categories/sus/index.md)
- [Back to Energy Efficiency family](categories/sus/families/energy/index.md)
- [Back to Rule Browser](../rule-browser.md)
