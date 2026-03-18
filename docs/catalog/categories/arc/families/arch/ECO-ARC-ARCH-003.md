# ECO-ARC-ARCH-003 — Long synchronous dependency chain

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** warning
- **Tags:** dependencies, latency
- **Legacy ID:** ECO-ARCH-003

## Summary

Synchronous call chains amplify latency and failure propagation.

## Rationale

Chains multiply tail latency and increase coupled failure modes.

## Impact

```json
{
  "confidence": 0.8,
  "notes": "Common microservice anti-pattern.",
  "type": "latency"
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
  "guidance": "Introduce async boundaries, caching, or collapse hops.",
  "tradeoffs": "Consistency and design tradeoffs."
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
