# ECO-CMP-PY-007 — Loading entire file into memory

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 2
- **Severity:** warning
- **Tags:** python, memory, io
- **Legacy ID:** ECO-PY-007

## Summary

Reading large files fully into memory increases peak RAM and risk of OOM.

## Rationale

Streaming reduces peak memory and improves stability.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Common in file processing / ETL.",
  "type": "memory"
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
  "guidance": "Stream/chunk reads; process iteratively.",
  "tradeoffs": "May change downstream logic."
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
