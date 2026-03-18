# ECO-ARC-ARCH-011 — Excessive replica counts

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** warning
- **Tags:** replicas, rightsizing
- **Legacy ID:** ECO-ARCH-011

## Summary

Too many replicas increase baseline waste.

## Rationale

Replica counts often drift upward and never return.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Validate against SLOs.",
  "type": "cost"
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
  "guidance": "Reduce replicas and add autoscaling with guardrails.",
  "tradeoffs": "Risk if SLOs not defined."
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
