# ECO-CMP-FLASK-010

**Name:** Per-request object allocation in middleware

**Category:** Computation

**Family:** Flask

**Primary layer:** `code`

**System layers:** `code`

## Description

Flask before/after request hooks allocate expensive objects or clients on every request.

## Impact

- **type:** memory
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `python`
- **parser:** python-ast

## Remediation

- **guidance:** Reuse clients safely, move expensive construction outside hot hooks, and limit middleware scope.
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

### Per-request object allocation in middleware

Flask before/after request hooks allocate expensive objects or clients on every request.

## Remediation examples

### Reduce repeated work

Reuse clients safely, move expensive construction outside hot hooks, and limit middleware scope.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Flask family](categories/cmp/families/flask/index.md)
- [Back to Rule Browser](../rule-browser.md)
