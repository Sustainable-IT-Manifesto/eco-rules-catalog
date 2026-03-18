# ECO-CMP-JS-009 — Unbounded promise chains

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Code
- **Tier:** 2
- **Severity:** note
- **Tags:** javascript, promises
- **Legacy ID:** ECO-JS-009

## Summary

Long or recursive promise chains can leak work and increase memory usage.

## Rationale

Unbounded async chains may create retention and scheduling overhead.

## Impact

```json
{
  "confidence": 0.55,
  "notes": "Depends on implementation.",
  "type": "memory"
}
```

## Detection

```json
{
  "languages": [
    "javascript"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Bound retries; avoid recursion; use iterative loops with limits.",
  "tradeoffs": "Logic changes."
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
