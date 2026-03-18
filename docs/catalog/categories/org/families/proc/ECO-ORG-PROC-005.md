# ECO-ORG-PROC-005 — Feature shipped without load testing

- **Category:** Organizational (ORG)
- **Family:** Process (PROC)
- **Layer:** Process
- **Tier:** 4
- **Severity:** warning
- **Tags:** testing, slo
- **Legacy ID:** ECO-PROC-005

## Summary

Skipping load tests creates risk and often forces wasteful overprovisioning.

## Rationale

Without tests, teams overprovision “just in case.”

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Systemic.",
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
  "guidance": "Add load tests and regression gates tied to SLOs.",
  "tradeoffs": "More pipeline time."
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
