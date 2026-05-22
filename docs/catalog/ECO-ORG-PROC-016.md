# ECO-ORG-PROC-016

**Name:** No performance or sustainability budget

**Category:** Organizational

**Family:** Process

**Primary layer:** `process`

**System layers:** `process`

## Description

Teams ship features without explicit performance, cost, carbon, or resource budgets.

## Impact

- **type:** process
- **confidence:** 0.75
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Define lightweight budgets for latency, compute, data transfer, storage, cost, and sustainability-sensitive workloads.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
- **network:** medium
- **storage:** medium
- **human_time:** high
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

- architecture review
- SLOs
- team standards

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
- [Back to Organizational category](categories/org/index.md)
- [Back to Process family](categories/org/families/proc/index.md)
- [Back to Rule Browser](../rule-browser.md)
