# ECO-CMP-FLASK-008

**Name:** Synchronous external calls in hot routes

**Category:** Computation

**Family:** Flask

**Primary layer:** `code`

**System layers:** `code`

## Description

Flask routes synchronously call external APIs for data that could be cached or pre-fetched.

## Impact

- **type:** latency
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `python`
- **parser:** python-ast

## Remediation

- **guidance:** Cache stable external responses, batch calls, or move slow enrichment to async/background flows.
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

### Synchronous external calls in hot routes

Flask routes synchronously call external APIs for data that could be cached or pre-fetched.

## Remediation examples

### Reduce repeated work

Cache stable external responses, batch calls, or move slow enrichment to async/background flows.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Flask family](categories/cmp/families/flask/index.md)
- [Back to Rule Browser](../rule-browser.md)
