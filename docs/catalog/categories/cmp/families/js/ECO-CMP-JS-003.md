# ECO-CMP-JS-003 — Large unoptimized bundles

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Code
- **Tier:** 1
- **Severity:** warning
- **Tags:** javascript, bundling, frontend
- **Legacy ID:** ECO-JS-003

## Summary

Large bundles increase transfer size, parse time, and energy use.

## Rationale

Users pay for bytes and CPU; so do battery and emissions.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Affects every page view.",
  "type": "network"
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
  "guidance": "Enable tree-shaking, code splitting, and remove dead deps.",
  "tradeoffs": "Build config changes."
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
