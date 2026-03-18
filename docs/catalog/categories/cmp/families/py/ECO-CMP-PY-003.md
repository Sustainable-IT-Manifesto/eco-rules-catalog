# ECO-CMP-PY-003 — Repeated invariant computation inside loop

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 1
- **Severity:** note
- **Tags:** python, cpu
- **Legacy ID:** ECO-PY-003

## Summary

Recomputing values that do not change inside a loop wastes CPU cycles.

## Rationale

Small wasted work per iteration can become significant in hot loops.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Best targeted when loop counts are high.",
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
  "guidance": "Move invariant work outside the loop.",
  "tradeoffs": "Minimal."
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
