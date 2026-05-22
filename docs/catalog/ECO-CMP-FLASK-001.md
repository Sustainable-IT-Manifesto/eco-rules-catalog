# ECO-CMP-FLASK-001

**Name:** Database query in request loop

**Category:** Computation

**Family:** Flask

**Primary layer:** `code`

**System layers:** `code`

## Description

A Flask route performs repeated database queries while iterating over records.

## Impact

- **type:** latency
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `python`
- **parser:** python-ast

## Remediation

- **guidance:** Batch queries, eager load related data, or reshape the query so the route performs bounded database work.
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
- **scales_non_linearly:** Yes

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

### Database query in request loop

A Flask route performs repeated database queries while iterating over records.

## Remediation examples

### Reduce repeated work

Batch queries, eager load related data, or reshape the query so the route performs bounded database work.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Flask family](categories/cmp/families/flask/index.md)
- [Back to Rule Browser](../rule-browser.md)
