# Eco Rules Catalog

The Eco Rules Catalog is a SITM-owned standard for identifying, describing, and organizing software inefficiency.

## v0.4.0 - 2026-05-21

### Added

- Formal schema definitions for `cost_dimensions`, `amplification`, `temporal_behavior`, `runtime_evidence`, and `sustainability_priority`.
- Documentation for the new systems-level metadata fields.
- Migration entry documenting the 0.4.0 schema formalization.

### Changed

- Updated catalog registry version from `0.3.0` to `0.4.0`.
- Updated rule metadata catalog versions to `0.4.0`.
- Promoted the 0.3.0 expansion into a more explicit systems intelligence release.

### Compatibility

- Existing 0.3.x rules remain structurally compatible.
- Additional rule properties are still allowed so experimental metadata can continue to evolve.

### Why it matters

Waste doesn’t stop at code.

It lives in:
- images
- manifests
- scaling behavior
- defaults

Making it visible is the first step to reducing it.

---


## What this is

The catalog provides:

- a shared language for software waste
- a canonical rule model
- controlled vocabulary through the registry
- validation and reproducibility
- a foundation for tools, education, and certification

In plain English: it helps teams name waste, find waste, and fix waste more consistently.

Because waste is a bug.

## Why this matters

Software waste often hides in plain sight.

A little extra polling here. A little oversized payload there. A little retry loop that no one revisits.

At small scale, these things can look harmless.

At real scale, they become:

- cost
- latency
- energy use
- environmental impact
- fragility

The Eco Rules Catalog exists to make those patterns visible and actionable.

## Start here

New to the catalog?

Read [Start Here](start-here.md) for the fastest path into the standard.

## Core documents

- [Standard](standard.md)
- [Start Here](start-here.md)
- [Ontology Overview](ontology/README.md)
- [Taxonomy](ontology/taxonomy.md)
- [Human Catalog](catalog/index.md)
- [Rule Browser](rule-browser.md)
- [Contributing](contributing.md)

## Source of truth

The machine-readable source of truth is:

- `catalog/rules/...`
- `catalog/registry.json`
- `catalog/schema/...`

Generated artifacts include:

- `catalog/master.json`
- `docs/catalog/...`

`catalog/master.json` and `docs/catalog/...` are generated and should not be edited manually.

## For contributors

If you want to contribute safely, start with:

- [Contributing](contributing.md)
- [Rule Checklist](rule-checklist.md)
- [Ontology Checklist](ontology/checklist.md)

## For tool builders

If you want to integrate against the catalog, start with:

- [Standard](standard.md)
- [Ontology Model](ontology/model.md)
- `catalog/registry.json`
- `catalog/schema/schema-rule.json`

## Releases

- See [v0.3.0](releases/v0.3.0.md) for the current release
- See [v0.2.0](releases/v0.2.0.md) for the first validated standard release.

Because waste is a bug.
