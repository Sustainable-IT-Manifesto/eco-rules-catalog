# Scanner model for Eco Rules Catalog and MSG

This document describes the recommended routing model for the MSG scanner.

## Principle

Family-level scanner profiles define the default routing contract.

Rules remain focused on the pattern itself. They only add `scanner_override` when a rule needs behavior that differs from the family default.

This keeps rule authoring lighter and reduces drift.

## Model

### Category
Broad concern domain.

Example:
- `INF` = Infrastructure

### Family
Concrete ecosystem or technical context.

Examples:
- `DOCKER`
- `COMPOSE`
- `K8S`
- `PY`
- `JS`
- `JAVA`

### Family `scanner_profile`
Describes where and how a family is normally scanned.

Typical fields:
- `technologies`
- `targets`
- `default_scope`
- `file_globs`
- `file_names`
- `path_hints`
- `repo_signals`
- `manifest_kinds`
- `parser`

### Rule `scanner_override`
Optional. Only present when the rule needs narrower or broader routing than the family default.

### Rule `detection`
Keeps the dispatch hint for the actual detector implementation.

Example:
```json
"detection": {
  "method": "dockerfile-lint",
  "selector": "multi_stage_build"
}
```

## Effective scanner profile

The scanner should resolve effective applicability like this:

1. Load the family scanner profile
2. Merge the optional rule `scanner_override`
3. Dispatch the detector identified by `detection.selector`

Conceptually:

```python
effective_profile = deep_merge(family.scanner_profile, rule.get("scanner_override", {}))
```

## Why this design

This avoids repeating the same Docker / Compose / Kubernetes routing hints on every rule.

It also keeps existing families consistent with new infrastructure families.
