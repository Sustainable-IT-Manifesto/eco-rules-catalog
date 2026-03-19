# Start Here

Welcome to the **Eco Rules Catalog**.

This project is a SITM-owned standard for identifying, describing, and organizing software inefficiency.

If you are new to the catalog, this is the shortest path to understanding it.

## What this is

The Eco Rules Catalog provides:

- a shared language for software waste
- a canonical rule format
- controlled vocabulary through the registry
- validation and reproducibility
- a foundation for tooling, education, and certification

In plain English: it helps teams name waste, find waste, and fix waste more consistently.

Because waste is a bug.

## What to read first

1. [Standard](standard.md)  
   The governing document for the catalog.

2. [Ontology Overview](ontology/README.md)  
   Explains how rules are classified and described.

3. [Taxonomy](ontology/taxonomy.md)  
   Shows the canonical vocabulary used by the catalog.

4. [Human Catalog](catalog/index.md)  
   Browse the actual rules.

5. [Contributing](contributing.md)  
   How to propose changes safely and cleanly.

## How the system is organized

### Machine-readable source of truth
- `catalog/registry.json`
- `catalog/schema/schema-rule.json`
- `catalog/schema/schema-registry.json`
- `catalog/rules/...`

### Generated artifacts
- `catalog/master.json`
- generated human-readable catalog pages

### Public documentation
- `docs/...`

## The basic model

A rule describes a known inefficiency pattern.

A rule should answer:

- what is happening
- why it matters
- where it appears
- how it can be detected
- how it can be remediated

Every rule has:

- a canonical ID
- a category and family
- a primary `layer`
- `ontology.system_layers`
- impact, detection, remediation, and metadata

## Current canonical layers

- `ai`
- `architecture`
- `code`
- `data`
- `network`
- `process`

These values come from the registry and should be treated as canonical.

## What to use as the source of truth

If documents ever disagree:

- trust `catalog/registry.json` for controlled values
- trust `catalog/schema/...` for structure
- trust `catalog/rules/...` as the source of truth for individual rules
- treat `catalog/master.json` as generated

## What this enables

This catalog is meant to support:

- rule browsing
- validation
- tool integration
- reporting
- education
- certification alignment
- future benchmarking

## Suggested next steps

If you are:

### A contributor
Read:
- [Contributing](contributing.md)
- [Rule Checklist](rule-checklist.md)
- [Ontology Checklist](ontology/checklist.md)

### A tool builder
Read:
- [Standard](standard.md)
- [Ontology Model](ontology/model.md)
- the registry and schemas in `catalog/`

### A reader
Start with:
- [Human Catalog](catalog/index.md)
- [Releases](releases/v0.2.0.md)

## Final note

The Eco Rules Catalog is not just a repository of patterns.

It is an effort to make software waste visible, discussable, and actionable.

That is the point.

Because waste is a bug.
