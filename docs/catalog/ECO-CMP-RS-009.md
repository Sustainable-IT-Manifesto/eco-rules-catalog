# ECO-CMP-RS-009

**Name:** Per-item database or network calls

**Category:** Computation

**Family:** Rust

**Primary layer:** `code`

**System layers:** `code`

## Description

Issuing database or HTTP calls inside collection loops instead of batching or joining.

## Impact

- **type:** network
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `rust`
- **parser:** rust_ast_or_tree_sitter
- **notes:** Detect reqwest/sqlx/diesel calls inside loops over records or IDs.

## Remediation

- **guidance:** Batch requests, prefetch associations, use joins, or apply concurrency limits with backpressure.
- **tradeoffs:** Batching can complicate error handling and partial retries.

## Cost Dimensions

- **compute:** high
- **memory:** medium
- **network:** medium
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
- benchmark results

## Pattern examples

### Per-item database or network calls

Issuing database or HTTP calls inside collection loops instead of batching or joining.

## Remediation examples

### Reduce avoidable work

Batch requests, prefetch associations, use joins, or apply concurrency limits with backpressure.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Rust family](categories/cmp/families/rs/index.md)
- [Back to Rule Browser](../rule-browser.md)
