# ECO-ORG-PROC-009 — No dependency lifecycle management

- **Category:** Organizational (ORG)
- **Family:** Process (PROC)
- **Layer:** Process
- **Tier:** 4
- **Severity:** warning
- **Tags:** dependencies, supply-chain
- **Legacy ID:** ECO-PROC-009

## Summary

Unmanaged dependencies increase security, compute, and maintenance waste.

## Rationale

Old deps increase risk and often block efficiency upgrades.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Also affects security posture.",
  "type": "reliability"
}
```

## Detection

```json
{
  "languages": [
    "org"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Implement dependency review cadence and upgrade workflows.",
  "tradeoffs": "Ongoing work."
}
```

## Ontology

```json
{
  "system_layers": [
    "process"
  ]
}
```
