# ECO-SUS-WATER-001

**Name:** Water-stress-blind AI inference placement

**Category:** Sustainability & Environmental Impact

**Family:** Water-Aware Computing

**Primary layer:** `ai`

**System layers:** `ai`

## Description

AI inference workloads are placed without considering regional water stress or cooling impact.

## Impact

- **type:** water
- **confidence:** 0.65
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Consider region, model size, caching, batching, and workload scheduling to reduce water-stress-weighted impact.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** high
- **memory:** medium
- **network:** medium
- **storage:** low
- **human_time:** medium
- **carbon:** high
- **water:** high

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

- region inventory
- AI usage metrics
- water stress factors

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
- [Back to Water-Aware Computing family](categories/sus/families/water/index.md)
- [Back to Rule Browser](../rule-browser.md)
