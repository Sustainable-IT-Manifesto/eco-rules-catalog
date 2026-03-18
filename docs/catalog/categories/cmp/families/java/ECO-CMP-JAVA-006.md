# ECO-CMP-JAVA-006 — Missing connection pooling

- **Category:** Computation (CMP)
- **Family:** Java (JAVA)
- **Layer:** Architecture
- **Tier:** 2
- **Severity:** error
- **Tags:** java, db, pooling
- **Legacy ID:** ECO-JAVA-006

## Summary

No pooling increases connection churn and DB overhead.

## Rationale

Connection setup is expensive; pooling stabilizes and reduces waste.

## Impact

```json
{
  "confidence": 0.85,
  "notes": "High propagation under load.",
  "type": "latency"
}
```

## Detection

```json
{
  "languages": [
    "java"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Use and tune a pool (e.g., HikariCP).",
  "tradeoffs": "Must manage max connections."
}
```

## Ontology

```json
{
  "system_layers": [
    "architecture"
  ]
}
```
