# ECO-CMP-JOOMLA-006

**Name:** Manifest or update checks in request path

**Category:** Computation

**Family:** Joomla

**Primary layer:** `code`

**System layers:** `code`

## Description

Extension code performs remote update checks or manifest reads during normal page rendering.

## Impact

- **type:** latency
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `php`
- **parser:** php-ast

## Remediation

- **guidance:** Run update checks on schedule or admin-only flows, and cache results with sane TTLs.
- **tradeoffs:** Framework conventions, readability, caching correctness, and deployment topology should be considered before changing behavior.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
- **network:** medium
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

- request traces
- CPU profiles
- allocation profiles
- APM transaction timing

## Pattern examples

### Manifest or update checks in request path

Extension code performs remote update checks or manifest reads during normal page rendering.

## Remediation examples

### Reduce repeated work

Run update checks on schedule or admin-only flows, and cache results with sane TTLs.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Joomla family](categories/cmp/families/joomla/index.md)
- [Back to Rule Browser](../rule-browser.md)
