# ECO-CMP-JAVA-002 — Unbounded cache growth

- **Category:** Computation (CMP)
- **Family:** Java (JAVA)
- **Layer:** Code
- **Tier:** 2
- **Severity:** error
- **Tags:** java, cache, memory
- **Legacy ID:** ECO-JAVA-002

## Summary

Caches without limits grow until they become the problem.

## Rationale

Unbounded caches create memory bloat and instability.

## Impact

```json
{
  "confidence": 0.85,
  "notes": "High outage risk.",
  "type": "memory"
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
  "guidance": "Use bounded caches with eviction policies and TTL.",
  "tradeoffs": "Possible cache misses; tune properly."
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
