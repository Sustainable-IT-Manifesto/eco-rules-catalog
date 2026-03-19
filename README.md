<p align="center">
  <h1 align="center">Eco Rules Catalog</h1>
  <p align="center">
    A standard for identifying software inefficiency.
  </p>
  <p align="center">
    <strong>Because waste is a bug.</strong>
  </p>
</p>

<p align="center">
  <a href="https://sustainable-it-manifesto.github.io/eco-rules-catalog/">
    📖 Documentation
  </a>
  ·
  <a href="https://github.com/sustainable-it-manifesto/eco-rules-catalog/actions">
    ⚙️ CI
  </a>
  ·
  <a href="https://github.com/sustainable-it-manifesto/eco-rules-catalog/releases">
    📦 Releases
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/sustainable-it-manifesto/eco-rules-catalog/validate.yml?label=validate&style=flat-square" />
  <img src="https://img.shields.io/github/actions/workflow/status/sustainable-it-manifesto/eco-rules-catalog/deploy-docs.yml?label=docs&style=flat-square" />
  <img src="https://img.shields.io/github/v/release/sustainable-it-manifesto/eco-rules-catalog?style=flat-square" />
</p>

A structured catalog of **software inefficiency patterns** that waste compute, energy, network bandwidth, memory, and engineering time.

The Eco Rules Catalog is a **SITM-owned standard** for identifying, describing, and organizing software waste.

> Because waste is a bug.

---

# What this provides

The catalog includes:

- **Machine-readable rules** for tools and automation
- **Human-readable documentation** for understanding and learning
- **Remediation guidance** for improving systems
- **A canonical taxonomy and registry** for consistency
- **Validation and reproducibility** for governance

---

# Why this matters

Modern systems accumulate inefficiency in small ways:

- repeated string concatenation  
- unbounded retries  
- oversized payloads  
- inefficient queries  
- unnecessary serialization  
- excessive polling or logging  

Individually, these look harmless.

At scale, they become:

- higher cloud costs  
- increased latency  
- wasted energy  
- larger environmental footprint  
- system fragility  

The Eco Rules Catalog makes these patterns **visible and actionable**.

---

# Repository structure

```

catalog/
rules/              ← source of truth (per-rule files)
master.json         ← generated catalog
registry.json       ← canonical vocabulary
schema/             ← JSON schemas

docs/
...                 ← MkDocs site content

tools/
build_catalog.py
validate_rules_v2.py
generate_human_catalog_v2.py

````

## Note

* `docs/catalog/` is generated. Do not edit files there manually.
* `catalog/master.json` is generated. Do not edit it manually.

---

# Source of truth

The system is intentionally structured:

### Authoritative sources
- `catalog/rules/...` → rule definitions  
- `catalog/registry.json` → controlled vocabulary  
- `catalog/schema/...` → structure  

### Generated artifacts
- `catalog/master.json`  
- `docs/catalog/...` (human-readable pages)

> `catalog/master.json` is generated and should not be edited manually.

---

# Rule model

Each rule describes a specific inefficiency pattern.

Example:

```json
{
  "id": "ECO-AIM-AI-001",
  "name": "Example rule",
  "category_code": "AIM",
  "family_code": "AI",
  "layer": "ai",
  "ontology": {
    "system_layers": ["ai", "data"]
  }
}
````

Rules also include:

* rationale
* impact
* detection guidance
* remediation guidance

---

# Canonical layers

The catalog uses a controlled vocabulary:

* `ai`
* `architecture`
* `code`
* `data`
* `network`
* `process`

These values are defined in:

```
catalog/registry.json
```

---

# Build and validate

## Build catalog

```
make build
```

## Validate

```
make validate
```

## Generate docs

```
make docs
```

## Serve locally

```
make serve
```

---

# Documentation site

The catalog is published as a documentation site using MkDocs.

It includes:

* the standard
* ontology explanation
* rule catalog
* contributor guidance

---

# Intended uses

The catalog can power:

* static analysis tools
* CI/CD enforcement
* sustainability audits
* performance optimization
* engineering education
* certification programs

---

# Relationship to Sustainable IT

This catalog supports the **Sustainable IT Manifesto** by helping organizations move through:

**Aware → Conscious → Enabled → Empowered**

---

# Contributing

See:

* `CONTRIBUTING.md`
* `docs/rule-checklist.md`
* `docs/ontology/checklist.md`

---

# License

MIT License

Copyright (c) 2026 Sustainable IT Manifesto

