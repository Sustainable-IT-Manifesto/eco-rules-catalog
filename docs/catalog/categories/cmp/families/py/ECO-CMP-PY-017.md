# ECO-CMP-PY-017 — Large object retained in global scope

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 2
- **Severity:** warning
- **Tags:** python, memory
- **Legacy ID:** ECO-PY-017

## Summary

Long-lived globals can cause persistent memory bloat.

## Rationale

Accidental retention prevents GC and inflates baseline memory footprint.

## Impact

```json
{
  "confidence": 0.65,
  "notes": "Often invisible until scale.",
  "type": "memory"
}
```

## Detection

```json
{
  "languages": [
    "python"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Avoid storing large payloads globally; use caching with eviction.",
  "tradeoffs": "May require new cache strategy."
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
