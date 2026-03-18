# ECO-ARC-ARCH-010 — No observability on utilization

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 4
- **Severity:** warning
- **Tags:** observability, metrics
- **Legacy ID:** ECO-ARCH-010

## Summary

Without utilization metrics, waste is invisible and persistent.

## Rationale

You can’t reduce what you don’t see.

## Impact

```json
{
  "confidence": 0.85,
  "notes": "Systemic maturity issue.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "infra",
    "org"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Instrument CPU/mem/QPS/latency; add dashboards and alerts.",
  "tradeoffs": "Telemetry cost; requires curation."
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
