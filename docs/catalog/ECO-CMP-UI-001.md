# ECO-CMP-UI-001

**Name:** Oversized frontend bundle

**Category:** Computation

**Family:** Frontend/UI

**Primary layer:** `code`

**System layers:** `code`

## Description

A frontend ships excessive JavaScript or unused dependencies that increase transfer, parsing, and device energy cost.

## Impact

- **type:** network
- **confidence:** 0.75
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Remove unused dependencies, split code, tree-shake, lazy-load, and set performance budgets.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
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

- bundle analysis
- RUM
- Core Web Vitals

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
- [Back to Computation category](categories/cmp/index.md)
- [Back to Frontend/UI family](categories/cmp/families/ui/index.md)
- [Back to Rule Browser](../rule-browser.md)
