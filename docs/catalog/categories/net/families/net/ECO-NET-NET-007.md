# ECO-NET-NET-007 — Excessive retry storms

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 2
- **Severity:** error
- **Tags:** retries, circuit-breaker
- **Legacy ID:** ECO-NET-007

## Summary

Aggressive retries amplify failures and increase waste.

## Rationale

Retries without backoff turn a small outage into a system-wide incident.

## Impact

```json
{
  "confidence": 0.85,
  "notes": "High propagation risk.",
  "type": "reliability"
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
  "guidance": "Use exponential backoff + jitter; add circuit breakers; cap retries.",
  "tradeoffs": "May reduce immediate success rate during blips."
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
