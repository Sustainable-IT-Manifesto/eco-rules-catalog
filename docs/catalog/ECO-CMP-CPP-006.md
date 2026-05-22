# ECO-CMP-CPP-006

**Name:** Inefficient string concatenation

**Category:** Computation

**Family:** C++

**Primary layer:** `code`

**System layers:** `code`

## Description

Repeated std::string concatenation without capacity planning for large outputs.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `cpp`
- **parser:** cpp_ast_or_tree_sitter
- **notes:** Find += or append patterns in loops where output size grows substantially.

## Remediation

- **guidance:** Reserve capacity, use append with known sizes, fmt buffers, ostreams carefully, or streaming writers.
- **tradeoffs:** Small strings may be optimized; avoid premature rewrites outside hot paths.

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

### Inefficient string concatenation

Repeated std::string concatenation without capacity planning for large outputs.

## Remediation examples

### Reduce avoidable work

Reserve capacity, use append with known sizes, fmt buffers, ostreams carefully, or streaming writers.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to C++ family](categories/cmp/families/cpp/index.md)
- [Back to Rule Browser](../rule-browser.md)
