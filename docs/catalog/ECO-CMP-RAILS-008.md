# ECO-CMP-RAILS-008

**Name:** Per-request service/client construction

**Category:** Computation

**Family:** Ruby on Rails

**Primary layer:** `code`

**System layers:** `code`

## Description

Rails controllers or middleware construct expensive clients or configuration objects on every request.

## Impact

- **type:** memory
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `ruby`
- **parser:** ruby_parser_or_prism

## Remediation

- **guidance:** Reuse thread-safe clients, memoize stable configuration, and avoid global mutable state.
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

### Per-request service/client construction

Rails controllers or middleware construct expensive clients or configuration objects on every request.

## Remediation examples

### Reduce repeated work

Reuse thread-safe clients, memoize stable configuration, and avoid global mutable state.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Ruby on Rails family](categories/cmp/families/rails/index.md)
- [Back to Rule Browser](../rule-browser.md)
