# ECO-CMP-CPP-005

**Name:** Expensive logging or stream formatting

**Category:** Computation

**Family:** C++

**Primary layer:** `code`

**System layers:** `code`

## Description

Using iostream formatting, stringstream construction, or full object logging in hot paths.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `cpp`
- **parser:** cpp_ast_or_tree_sitter
- **notes:** Detect std::stringstream, operator<< logging, or full payload logs in loops and request paths.

## Remediation

- **guidance:** Use structured bounded logs, lazy log evaluation, sampling, and efficient formatting libraries.
- **tradeoffs:** Debuggability matters; retain targeted diagnostic fields.

## Cost Dimensions

- **compute:** medium
- **memory:** high
- **network:** low
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

- CPU profiles
- allocation profiles
- request traces
- benchmark results

## Pattern examples

### Expensive logging or stream formatting

Using iostream formatting, stringstream construction, or full object logging in hot paths.

## Remediation examples

### Reduce avoidable work

Use structured bounded logs, lazy log evaluation, sampling, and efficient formatting libraries.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to C++ family](categories/cmp/families/cpp/index.md)
- [Back to Rule Browser](../rule-browser.md)
