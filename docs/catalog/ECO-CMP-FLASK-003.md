# ECO-CMP-FLASK-003

**Name:** Uncached template fragment rendering

**Category:** Computation

**Family:** Flask

**Primary layer:** `code`

**System layers:** `code`

## Description

Frequently rendered Flask templates recompute stable fragments on every request.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `python`
- **parser:** python-ast

## Remediation

- **guidance:** Cache stable fragments or precompute view models with clear invalidation boundaries.
- **tradeoffs:** Framework conventions, readability, caching correctness, and deployment topology should be considered before changing behavior.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
- **network:** low
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

### Uncached template fragment rendering

Frequently rendered Flask templates recompute stable fragments on every request.

## Remediation examples

### Reduce repeated work

Cache stable fragments or precompute view models with clear invalidation boundaries.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Flask family](categories/cmp/families/flask/index.md)
- [Back to Rule Browser](../rule-browser.md)
