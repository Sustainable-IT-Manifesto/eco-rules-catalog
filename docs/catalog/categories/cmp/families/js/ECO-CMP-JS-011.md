# ECO-CMP-JS-011 — Inefficient array transformations (multi-pass)

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Code
- **Tier:** 1
- **Severity:** note
- **Tags:** javascript, cpu
- **Legacy ID:** ECO-JS-011

## Summary

Multiple passes over arrays increases CPU and GC overhead.

## Rationale

Map/filter/reduce chains can be fine, but in hot paths they add overhead.

## Impact

```json
{
  "confidence": 0.55,
  "notes": "Context-dependent.",
  "type": "cpu"
}
```

## Detection

```json
{
  "languages": [
    "javascript"
  ],
  "method": "ast"
}
```

## Remediation

```json
{
  "guidance": "Combine passes in hot paths; keep readability elsewhere.",
  "tradeoffs": "Potential readability loss."
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
