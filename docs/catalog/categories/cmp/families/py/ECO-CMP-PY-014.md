# ECO-CMP-PY-014 — Redundant environment variable lookups

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 1
- **Severity:** note
- **Tags:** python, config
- **Legacy ID:** ECO-PY-014

## Summary

Repeated env lookups in hot code paths add overhead and noise.

## Rationale

Load config once; don’t pay the lookup tax repeatedly.

## Impact

```json
{
  "confidence": 0.5,
  "notes": "Small individually; measurable in hot loops.",
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
  "guidance": "Read env/config once during startup; pass config explicitly.",
  "tradeoffs": "Slight architecture changes."
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
