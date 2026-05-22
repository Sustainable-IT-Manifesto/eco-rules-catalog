# ECO-CMP-RB-001

**Name:** String concatenation in loops

**Category:** Computation

**Family:** Ruby

**Primary layer:** `code`

**System layers:** `code`

## Description

Repeated string concatenation in a loop can create avoidable object churn and CPU overhead.

## Impact

- **type:** cpu
- **confidence:** 0.75
- **notes:** Impact increases in hot paths, large collections, high-traffic Rails actions, background jobs, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `ruby`
- **parser:** ruby_parser_or_prism

## Remediation

- **guidance:** Use an array with join, StringIO, or append with a pre-sized/bounded strategy when constructing large strings repeatedly.
- **tradeoffs:** May require refactoring for readability, query shape, or framework conventions.

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
- **scales_with_data_volume:** Yes
- **scales_non_linearly:** No

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- CPU profiles
- allocation profiles
- request traces
- background job timing

## Pattern examples

### Building strings one item at a time

A loop repeatedly appends or interpolates into a string while processing many records.

## Remediation examples

### Use buffered construction

Accumulate fragments and join them once, or use StringIO for stream-like generation.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Ruby family](categories/cmp/families/rb/index.md)
- [Back to Rule Browser](../rule-browser.md)
