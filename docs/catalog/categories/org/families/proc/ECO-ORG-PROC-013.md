# ECO-ORG-PROC-013 — No capacity planning cadence

- **Category:** Organizational (ORG)
- **Family:** Process (PROC)
- **Layer:** Process
- **Tier:** 4
- **Severity:** note
- **Tags:** capacity-planning
- **Legacy ID:** ECO-PROC-013

## Summary

Without planning, teams overbuy or get surprised and scramble.

## Rationale

Planning reduces panic-driven overprovisioning.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Varies by workload variability.",
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
  "guidance": "Add regular capacity review using trends and forecasts.",
  "tradeoffs": "Time investment."
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
