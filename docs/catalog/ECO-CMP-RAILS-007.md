# ECO-CMP-RAILS-007

**Name:** Large serialized JSON responses

**Category:** Computation

**Family:** Ruby on Rails

**Primary layer:** `code`

**System layers:** `code`

## Description

Rails endpoints serialize full ActiveRecord objects or large associations without field selection.

## Impact

- **type:** network
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `ruby`
- **parser:** ruby_parser_or_prism

## Remediation

- **guidance:** Use serializers with sparse fields, pagination, and explicit association loading.
- **tradeoffs:** Framework conventions, readability, caching correctness, and deployment topology should be considered before changing behavior.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
- **network:** medium
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

### Large serialized JSON responses

Rails endpoints serialize full ActiveRecord objects or large associations without field selection.

## Remediation examples

### Reduce repeated work

Use serializers with sparse fields, pagination, and explicit association loading.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Ruby on Rails family](categories/cmp/families/rails/index.md)
- [Back to Rule Browser](../rule-browser.md)
