# ECO-CMP-RAILS-009

**Name:** Verbose Rails logging in production

**Category:** Computation

**Family:** Ruby on Rails

**Primary layer:** `code`

**System layers:** `code`

## Description

Rails logs SQL binds, payloads, or debug details at high volume in production.

## Impact

- **type:** storage
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `ruby`
- **parser:** ruby_parser_or_prism

## Remediation

- **guidance:** Tune log levels, reduce payload logging, sample noisy events, and manage retention.
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

### Verbose Rails logging in production

Rails logs SQL binds, payloads, or debug details at high volume in production.

## Remediation examples

### Reduce repeated work

Tune log levels, reduce payload logging, sample noisy events, and manage retention.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Ruby on Rails family](categories/cmp/families/rails/index.md)
- [Back to Rule Browser](../rule-browser.md)
