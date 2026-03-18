# ECO-ARC-ARCH-013 — No caching layer for high-read workloads

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** warning
- **Tags:** caching
- **Legacy ID:** ECO-ARCH-013

## Summary

High-read systems without caching waste CPU and DB capacity.

## Rationale

Caching reduces repeated work and improves latency.

## Impact

```json
{
  "confidence": 0.65,
  "notes": "Be careful with invalidation.",
  "type": "cpu"
}
```

## Detection

```json
{
  "languages": [
    "infra"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Introduce caching at appropriate boundaries.",
  "tradeoffs": "Invalidation complexity."
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
