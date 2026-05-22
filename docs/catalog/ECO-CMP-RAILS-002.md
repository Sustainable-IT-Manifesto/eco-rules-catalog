# ECO-CMP-RAILS-002

**Name:** Callback performs heavy side effects

**Category:** Computation

**Family:** Ruby on Rails

**Primary layer:** `code`

**System layers:** `code`

## Description

ActiveRecord callbacks perform network calls, file work, or expensive computation during save/update flows.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `ruby`
- **parser:** ruby_parser_or_prism

## Remediation

- **guidance:** Move side effects to explicit services or background jobs with idempotency and failure handling.
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

### Callback performs heavy side effects

ActiveRecord callbacks perform network calls, file work, or expensive computation during save/update flows.

## Remediation examples

### Reduce repeated work

Move side effects to explicit services or background jobs with idempotency and failure handling.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Ruby on Rails family](categories/cmp/families/rails/index.md)
- [Back to Rule Browser](../rule-browser.md)
