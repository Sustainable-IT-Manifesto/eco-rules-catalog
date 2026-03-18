# ECO-NET-NET-014 — Synchronous cross-region calls

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 3
- **Severity:** warning
- **Tags:** cross-region, latency
- **Legacy ID:** ECO-NET-014

## Summary

Cross-region synchronous calls increase latency and cost.

## Rationale

Distance multiplies latency and increases transfer cost.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Often a structural design issue.",
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
  "guidance": "Co-locate dependencies; async replicate; cache at edges.",
  "tradeoffs": "Consistency tradeoffs."
}
```

## Ontology

```json
{
  "system_layers": [
    "network"
  ]
}
```
