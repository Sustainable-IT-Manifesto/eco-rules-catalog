# ECO-CMP-PY-009 — Repeated regex compilation

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 1
- **Severity:** note
- **Tags:** python, regex, cpu
- **Legacy ID:** ECO-PY-009

## Summary

Compiling regex repeatedly wastes CPU; compile once and reuse.

## Rationale

Regex compilation is non-trivial; repeated compilation is wasted work.

## Impact

```json
{
  "confidence": 0.65,
  "notes": "Common in parsing pipelines.",
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
  "guidance": "Precompile regex at module init or reuse compiled patterns.",
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
