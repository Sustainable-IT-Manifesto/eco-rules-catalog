# ECO-CMP-CPP-003

**Name:** Missing vector reserve before bulk insertion

**Category:** Computation

**Family:** C++

**Primary layer:** `code`

**System layers:** `code`

## Description

Growing std::vector or similar containers without reserving when size is known or bounded.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `cpp`
- **parser:** cpp_ast_or_tree_sitter
- **notes:** Detect push_back/emplace_back loops where count is known but reserve is absent.

## Remediation

- **guidance:** Call reserve with a realistic bound before bulk insertion.
- **tradeoffs:** Over-reserving can waste memory; use known or conservative bounds.

## Cost Dimensions

- **compute:** medium
- **memory:** high
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
- benchmark results

## Pattern examples

### Missing vector reserve before bulk insertion

Growing std::vector or similar containers without reserving when size is known or bounded.

## Remediation examples

### Reduce avoidable work

Call reserve with a realistic bound before bulk insertion.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to C++ family](categories/cmp/families/cpp/index.md)
- [Back to Rule Browser](../rule-browser.md)
