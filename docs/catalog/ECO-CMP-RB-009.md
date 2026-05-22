# ECO-CMP-RB-009

**Name:** Loading full ActiveRecord objects for scalar data

**Category:** Computation

**Family:** Ruby

**Primary layer:** `code`

**System layers:** `code`

## Description

Fetching complete model objects when only IDs or scalar fields are needed wastes memory, CPU, and database bandwidth.

## Impact

- **type:** memory
- **confidence:** 0.85
- **notes:** Impact increases in hot paths, large collections, high-traffic Rails actions, background jobs, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `ruby`
- **parser:** ruby_parser_or_prism

## Remediation

- **guidance:** Use pluck, pick, ids, select with limited columns, or database-side aggregation when full model behavior is not needed.
- **tradeoffs:** May require refactoring for readability, query shape, or framework conventions.

## Cost Dimensions

- **compute:** medium
- **memory:** high
- **network:** medium
- **storage:** low
- **human_time:** low
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

- SQL logs
- allocation profiles
- heap profiles
- query result sizes

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Ruby family](categories/cmp/families/rb/index.md)
- [Back to Rule Browser](../rule-browser.md)
