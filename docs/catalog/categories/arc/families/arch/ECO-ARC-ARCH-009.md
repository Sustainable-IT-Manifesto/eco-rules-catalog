# ECO-ARC-ARCH-009 — Duplicate services performing the same work

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** warning
- **Tags:** duplication, complexity
- **Legacy ID:** ECO-ARCH-009

## Summary

Duplicate services increase operational load and waste compute.

## Rationale

Duplication multiplies deploy, run, monitor, and patch overhead.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Often found during audits.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "org",
    "infra"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Consolidate responsibilities; retire redundant services.",
  "tradeoffs": "Migration effort."
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
