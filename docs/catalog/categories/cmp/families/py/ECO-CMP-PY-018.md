# ECO-CMP-PY-018 — Recursive algorithm without safeguards

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 1
- **Severity:** note
- **Tags:** python, cpu
- **Legacy ID:** ECO-PY-018

## Summary

Recursion without depth safeguards risks overhead and runtime errors.

## Rationale

Recursion adds call overhead; unbounded recursion risks failure.

## Impact

```json
{
  "confidence": 0.55,
  "notes": "Depends on input size.",
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
  "guidance": "Consider iterative approaches or enforce depth limits.",
  "tradeoffs": "Code rewrite."
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
