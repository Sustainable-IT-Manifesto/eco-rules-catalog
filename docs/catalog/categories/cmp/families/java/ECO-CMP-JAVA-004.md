# ECO-CMP-JAVA-004 — Reflection in hot path

- **Category:** Computation (CMP)
- **Family:** Java (JAVA)
- **Layer:** Code
- **Tier:** 1
- **Severity:** note
- **Tags:** java, cpu
- **Legacy ID:** ECO-JAVA-004

## Summary

Reflection adds overhead and can inflate latency and CPU usage.

## Rationale

Reflection is flexible, but expensive in tight loops.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Context-dependent.",
  "type": "cpu"
}
```

## Detection

```json
{
  "languages": [
    "java"
  ],
  "method": "ast"
}
```

## Remediation

```json
{
  "guidance": "Avoid reflection in hot paths; precompute accessors.",
  "tradeoffs": "Reduced dynamism."
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
