# ECO-CMP-RB-005

**Name:** Inefficient ActiveRecord count usage

**Category:** Computation

**Family:** Ruby

**Primary layer:** `code`

**System layers:** `code`

## Description

Using count, length, or size without understanding query/materialization behavior can create unnecessary database work or memory usage.

## Impact

- **type:** latency
- **confidence:** 0.75
- **notes:** Impact increases in hot paths, large collections, high-traffic Rails actions, background jobs, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `ruby`
- **parser:** ruby_parser_or_prism

## Remediation

- **guidance:** Use exists? for existence checks, count for database-side counts, and size only when the loaded/unloaded behavior is intentional.
- **tradeoffs:** May require refactoring for readability, query shape, or framework conventions.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
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
- query plans
- APM traces

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
