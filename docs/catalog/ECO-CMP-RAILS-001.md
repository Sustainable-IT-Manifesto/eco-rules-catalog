# ECO-CMP-RAILS-001

**Name:** ActiveRecord N+1 query in controller or view

**Category:** Computation

**Family:** Ruby on Rails

**Primary layer:** `code`

**System layers:** `code`

## Description

Rails code loads associated records lazily while rendering a collection.

## Impact

- **type:** latency
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `ruby`
- **parser:** ruby_parser_or_prism

## Remediation

- **guidance:** Use includes, preload, eager_load, counter caches, or query reshaping as appropriate.
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

### ActiveRecord N+1 query in controller or view

Rails code loads associated records lazily while rendering a collection.

## Remediation examples

### Reduce repeated work

Use includes, preload, eager_load, counter caches, or query reshaping as appropriate.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Ruby on Rails family](categories/cmp/families/rails/index.md)
- [Back to Rule Browser](../rule-browser.md)
