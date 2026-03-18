# ECO-ORG-PROC-008 — No architectural review gate

- **Category:** Organizational (ORG)
- **Family:** Process (PROC)
- **Layer:** Process
- **Tier:** 4
- **Severity:** note
- **Tags:** architecture, governance
- **Legacy ID:** ECO-PROC-008

## Summary

Without review gates, high-propagation waste slips in unnoticed.

## Rationale

High-impact decisions deserve lightweight review and documentation.

## Impact

```json
{
  "confidence": 0.65,
  "notes": "Prevents Tier-3 waste.",
  "type": "cost"
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
  "guidance": "Add a lightweight architecture review for high-tier changes.",
  "tradeoffs": "Process overhead if done poorly."
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
