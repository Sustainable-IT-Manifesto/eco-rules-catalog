# ECO-CMP-FLASK-004

**Name:** Session payload bloat

**Category:** Computation

**Family:** Flask

**Primary layer:** `code`

**System layers:** `code`

## Description

Flask session data stores large objects or repeated state in client-side cookies or backing stores.

## Impact

- **type:** network
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `python`
- **parser:** python-ast

## Remediation

- **guidance:** Store only compact identifiers in the session and keep larger state server-side with lifecycle controls.
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

### Session payload bloat

Flask session data stores large objects or repeated state in client-side cookies or backing stores.

## Remediation examples

### Reduce repeated work

Store only compact identifiers in the session and keep larger state server-side with lifecycle controls.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Flask family](categories/cmp/families/flask/index.md)
- [Back to Rule Browser](../rule-browser.md)
