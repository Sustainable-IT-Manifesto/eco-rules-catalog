# ECO-CMP-JS-015 — Recreating large objects per render

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Code
- **Tier:** 1
- **Severity:** note
- **Tags:** javascript, allocations
- **Legacy ID:** ECO-JS-015

## Summary

Allocating large objects repeatedly increases GC churn and CPU.

## Rationale

Avoid unnecessary allocation churn in rendering loops.

## Impact

```json
{
  "confidence": 0.55,
  "notes": "Depends on render frequency.",
  "type": "cpu"
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
  "guidance": "Memoize stable objects; move creation outside render paths.",
  "tradeoffs": "Potential for stale data if misused."
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
