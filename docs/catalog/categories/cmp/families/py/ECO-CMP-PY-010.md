# ECO-CMP-PY-010 — Inefficient data structure choice

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 1
- **Severity:** note
- **Tags:** python, data-structures
- **Legacy ID:** ECO-PY-010

## Summary

Using lists for membership tests instead of sets/dicts increases CPU time.

## Rationale

O(n) lookups in loops are a common silent perf killer.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "High impact when lookups are frequent.",
  "type": "cpu"
}
```

## Detection

```json
{
  "languages": [
    "python"
  ],
  "method": "ast"
}
```

## Remediation

```json
{
  "guidance": "Use set/dict for membership-heavy operations.",
  "tradeoffs": "Memory tradeoff for speed."
}
```

## Ontology

```json
{
  "system_layers": [
    "code"
  ]
}
```
