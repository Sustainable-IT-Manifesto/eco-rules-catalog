# ECO-CMP-CPP-009

**Name:** Per-item remote calls

**Category:** Computation

**Family:** C++

**Primary layer:** `code`

**System layers:** `code`

## Description

Making database, RPC, or HTTP calls inside loops over collections.

## Impact

- **type:** network
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `cpp`
- **parser:** cpp_ast_or_tree_sitter
- **notes:** Detect client/database calls inside loops over IDs, rows, messages, or entities.

## Remediation

- **guidance:** Batch, join, prefetch, pipeline, or use bounded parallelism with explicit backpressure.
- **tradeoffs:** Batching changes failure semantics and may need partial retry handling.

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

### Per-item remote calls

Making database, RPC, or HTTP calls inside loops over collections.

## Remediation examples

### Reduce avoidable work

Batch, join, prefetch, pipeline, or use bounded parallelism with explicit backpressure.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to C++ family](categories/cmp/families/cpp/index.md)
- [Back to Rule Browser](../rule-browser.md)
