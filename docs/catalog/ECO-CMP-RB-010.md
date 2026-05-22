# ECO-CMP-RB-010

**Name:** Per-record writes instead of batched operations

**Category:** Computation

**Family:** Ruby

**Primary layer:** `code`

**System layers:** `code`

## Description

Saving or updating records one at a time can create excessive database round trips and transaction overhead.

## Impact

- **type:** latency
- **confidence:** 0.85
- **notes:** Impact increases in hot paths, large collections, high-traffic Rails actions, background jobs, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `ruby`
- **parser:** ruby_parser_or_prism

## Remediation

- **guidance:** Use insert_all, upsert_all, update_all, transactions, batching, or database-native bulk operations when callbacks/validations are not required per record.
- **tradeoffs:** May require refactoring for readability, query shape, or framework conventions.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
- **network:** high
- **storage:** medium
- **human_time:** medium
- **carbon:** high
- **water:** low

## Amplification

- **scales_with_users:** No
- **scales_with_data_volume:** Yes
- **scales_non_linearly:** Yes

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- SQL logs
- transaction timing
- database write throughput
- background job duration

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
