# ECO-SUS-CARBON-001

**Name:** Carbon-insensitive workload placement

**Category:** Sustainability & Environmental Impact

**Family:** Carbon-Aware Computing

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Workloads are deployed without considering regional carbon intensity or cleaner available regions.

## Impact

- **type:** carbon
- **confidence:** 0.7
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Evaluate region placement against latency, compliance, resilience, carbon intensity, and water stress constraints.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** high
- **memory:** low
- **network:** medium
- **storage:** low
- **human_time:** medium
- **carbon:** high
- **water:** medium

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

- cloud region inventory
- carbon intensity data
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
- [Back to Carbon-Aware Computing family](categories/sus/families/carbon/index.md)
- [Back to Rule Browser](../rule-browser.md)
