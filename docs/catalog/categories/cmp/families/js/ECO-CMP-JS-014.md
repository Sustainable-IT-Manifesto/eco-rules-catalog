# ECO-CMP-JS-014 — Client-side heavy computation without workers

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Code
- **Tier:** 1
- **Severity:** warning
- **Tags:** javascript, web-workers
- **Legacy ID:** ECO-JS-014

## Summary

Heavy CPU work on main thread harms responsiveness and drains battery.

## Rationale

Main-thread CPU work directly impacts user experience and power use.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Visible as long tasks.",
  "type": "cpu"
}
```

## Detection

```json
{
  "languages": [
    "javascript"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Move heavy compute to web workers; optimize algorithms.",
  "tradeoffs": "More complexity."
}
```

## Ontology

```json
{
  "system_layers": [
    "code"
  ]
}
```
