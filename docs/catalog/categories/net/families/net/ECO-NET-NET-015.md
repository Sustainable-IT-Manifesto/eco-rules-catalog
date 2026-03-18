# ECO-NET-NET-015 — Missing circuit breaker patterns

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 3
- **Severity:** warning
- **Tags:** circuit-breaker, reliability
- **Legacy ID:** ECO-NET-015

## Summary

Without circuit breakers, failures propagate and waste resources.

## Rationale

Circuit breakers prevent repeated failing calls and protect upstream capacity.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "High in distributed systems.",
  "type": "reliability"
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
  "guidance": "Implement circuit breakers; define fallbacks and budgets.",
  "tradeoffs": "Requires clear SLO thinking."
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
