# ECO-DAT-DATA-006 — Excessive replication factor

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 3
- **Severity:** note
- **Tags:** replication
- **Legacy ID:** ECO-DATA-006

## Summary

High replication increases storage and write amplification.

## Rationale

Replication should match durability needs, not fear.

## Impact

```json
{
  "confidence": 0.55,
  "notes": "Context-dependent; validate requirements.",
  "type": "storage"
}
```

## Detection

```json
{
  "languages": [
    "infra"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Right-size replication; use tiered durability patterns.",
  "tradeoffs": "Risk if requirements misunderstood."
}
```

## Ontology

```json
{
  "system_layers": [
    "data"
  ]
}
```
