# ECO-RES-DR-001

**Name:** Untested regional failover

**Category:** Resilience & Reliability

**Family:** Disaster Recovery

**Primary layer:** `process`

**System layers:** `process`

## Description

A system claims regional resilience, but failover paths are not regularly tested under realistic conditions.

## Impact

- **type:** resilience
- **confidence:** 0.7
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Schedule failover exercises, validate runbooks, measure recovery behavior, and retire false redundancy.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** medium
- **memory:** low
- **network:** medium
- **storage:** medium
- **human_time:** high
- **carbon:** medium
- **water:** low

## Amplification

- **scales_with_users:** No
- **scales_with_data_volume:** No
- **scales_non_linearly:** Yes

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- DR test records
- runbooks
- incident history

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
- [Back to Disaster Recovery family](categories/res/families/dr/index.md)
- [Back to Rule Browser](../rule-browser.md)
