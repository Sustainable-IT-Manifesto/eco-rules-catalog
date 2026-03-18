# ECO-CMP-JAVA-005 — N+1 ORM query pattern

- **Category:** Computation (CMP)
- **Family:** Java (JAVA)
- **Layer:** Code
- **Tier:** 2
- **Severity:** warning
- **Tags:** java, orm, database
- **Legacy ID:** ECO-JAVA-005

## Summary

ORM queries inside loops multiply DB calls.

## Rationale

Hidden multiplicative cost for latency and DB load.

## Impact

```json
{
  "confidence": 0.8,
  "notes": "Often severe at scale.",
  "type": "network"
}
```

## Detection

```json
{
  "languages": [
    "java"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Use eager fetching, joins, or batch queries.",
  "tradeoffs": "Tune memory and query plans."
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
