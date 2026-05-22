# ECO-CMP-JOOMLA-009

**Name:** Inefficient ACL checks repeated per item

**Category:** Computation

**Family:** Joomla

**Primary layer:** `code`

**System layers:** `code`

## Description

Extension code repeats authorization checks individually across large item lists.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `php`
- **parser:** php-ast

## Remediation

- **guidance:** Batch permission checks where safe, precompute effective access, and avoid repeated service construction.
- **tradeoffs:** Framework conventions, readability, caching correctness, and deployment topology should be considered before changing behavior.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
- **network:** low
- **storage:** medium
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

- request traces
- CPU profiles
- allocation profiles
- APM transaction timing

## Pattern examples

### Inefficient ACL checks repeated per item

Extension code repeats authorization checks individually across large item lists.

## Remediation examples

### Reduce repeated work

Batch permission checks where safe, precompute effective access, and avoid repeated service construction.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Joomla family](categories/cmp/families/joomla/index.md)
- [Back to Rule Browser](../rule-browser.md)
