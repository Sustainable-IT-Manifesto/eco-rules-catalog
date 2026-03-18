# ECO-CMP-JAVA-008 — Excessive synchronization contention

- **Category:** Computation (CMP)
- **Family:** Java (JAVA)
- **Layer:** Code
- **Tier:** 2
- **Severity:** warning
- **Tags:** java, contention
- **Legacy ID:** ECO-JAVA-008

## Summary

Over-synchronization creates contention and wastes CPU.

## Rationale

Contention turns CPU into waiting; throughput collapses under load.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Often visible as lock wait.",
  "type": "cpu"
}
```

## Detection

```json
{
  "languages": [
    "java"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Reduce lock scope; use concurrent structures; redesign hotspots.",
  "tradeoffs": "Harder correctness work."
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
