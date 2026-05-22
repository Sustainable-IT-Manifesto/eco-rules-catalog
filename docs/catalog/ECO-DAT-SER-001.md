# ECO-DAT-SER-001

**Name:** Repeated serialization/deserialization chain

**Category:** Data

**Family:** Serialization

**Primary layer:** `data`

**System layers:** `data`

## Description

Data is repeatedly converted between formats within the same request or processing path.

## Impact

- **type:** cpu
- **confidence:** 0.7
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Keep data in a canonical internal representation and serialize only at boundaries.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** high
- **memory:** high
- **network:** low
- **storage:** low
- **human_time:** low
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

- CPU profile
- allocation profile
- code review

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
- [Back to Data category](categories/dat/index.md)
- [Back to Serialization family](categories/dat/families/ser/index.md)
- [Back to Rule Browser](../rule-browser.md)
