# ECO-CMP-PY-001 — String concatenation in loops

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 1
- **Severity:** warning
- **Tags:** python, allocations, hot-path
- **Legacy ID:** ECO-PY-001

## Summary

Repeated string concatenation in a loop increases allocations and CPU.

## Rationale

Avoids unnecessary intermediate string objects that compound under load.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Most visible in tight loops / hot paths.",
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
  "guidance": "Use list accumulation + join(), or StringIO.",
  "tradeoffs": "Slightly more verbose."
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
