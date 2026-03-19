PYTHON ?= python3

CATALOG_DIR := catalog
RULES_DIR := $(CATALOG_DIR)/rules
MASTER_CATALOG := $(CATALOG_DIR)/master.json
REGISTRY := $(CATALOG_DIR)/registry.json
SCHEMA_DIR := $(CATALOG_DIR)/schema
RULE_SCHEMA := $(SCHEMA_DIR)/schema-rule.json
REGISTRY_SCHEMA := $(SCHEMA_DIR)/schema-registry.json

DOCS_DIR := docs
CATALOG_DOCS_DIR := $(DOCS_DIR)/catalog
MKDOCS_CONFIG := mkdocs.yml

TOOLS_DIR := tools
BUILD_CATALOG := $(TOOLS_DIR)/build_catalog.py
VALIDATE_REGISTRY := $(TOOLS_DIR)/validate_registry.py
VALIDATE_RULES := $(TOOLS_DIR)/validate_rules_v2.py
GENERATE_HUMAN := $(TOOLS_DIR)/generate_human_catalog_v2.py
MIGRATE_RULES := $(TOOLS_DIR)/migrate_rules.py
SPLIT_CATALOG := $(TOOLS_DIR)/split_catalog.py

.PHONY: help
help:
	@echo "Available targets:"
	@echo "  make build           Build catalog/master.json from catalog/rules/"
	@echo "  make validate        Run registry + rules validation"
	@echo "  make docs            Generate human-readable catalog pages"
	@echo "  make site            Build the MkDocs site"
	@echo "  make serve           Serve the MkDocs site locally"
	@echo "  make check           Build + validate + docs"
	@echo "  make clean           Remove generated site artifacts"
	@echo "  make rebuild         Cleanly rebuild catalog and docs"
	@echo "  make split           Split catalog/master.json into per-rule files"
	@echo "  make migrate         Run migration tooling"
	@echo "  make ci              CI-style full verification"
	@echo "  make print-config    Show key paths"

.PHONY: print-config
print-config:
	@echo "PYTHON=$(PYTHON)"
	@echo "RULES_DIR=$(RULES_DIR)"
	@echo "MASTER_CATALOG=$(MASTER_CATALOG)"
	@echo "REGISTRY=$(REGISTRY)"
	@echo "RULE_SCHEMA=$(RULE_SCHEMA)"
	@echo "REGISTRY_SCHEMA=$(REGISTRY_SCHEMA)"
	@echo "DOCS_DIR=$(DOCS_DIR)"
	@echo "CATALOG_DOCS_DIR=$(CATALOG_DOCS_DIR)"
	@echo "MKDOCS_CONFIG=$(MKDOCS_CONFIG)"

.PHONY: build
build:
	$(PYTHON) $(BUILD_CATALOG)

.PHONY: validate-registry
validate-registry:
	$(PYTHON) $(VALIDATE_REGISTRY)

.PHONY: validate-rules
validate-rules: build
	$(PYTHON) $(VALIDATE_RULES) $(MASTER_CATALOG)

.PHONY: validate
validate: validate-registry validate-rules

.PHONY: docs
docs: build
	$(PYTHON) $(GENERATE_HUMAN)

.PHONY: site
site: docs
	mkdocs build -f $(MKDOCS_CONFIG)

.PHONY: serve
serve: docs
	mkdocs serve -f $(MKDOCS_CONFIG)

.PHONY: check
check: build validate docs

.PHONY: ci
ci: build validate docs
	mkdocs build -f $(MKDOCS_CONFIG) --strict

.PHONY: rebuild
rebuild: clean check

.PHONY: clean
clean:
	rm -rf site
	find . -type d -name "__pycache__" -prune -exec rm -rf {} \;
	find . -type f -name "*.pyc" -delete

.PHONY: split
split:
	$(PYTHON) $(SPLIT_CATALOG)

.PHONY: migrate
migrate:
	$(PYTHON) $(MIGRATE_RULES)

.PHONY: new-baseline
new-baseline: build validate docs
	@echo "New baseline generated and validated."

.PHONY: guard-master
guard-master: build
	@git diff --exit-code -- $(MASTER_CATALOG) || \
	( echo "ERROR: $(MASTER_CATALOG) is out of sync. Run 'make build' and commit the result."; exit 1 )

.PHONY: guard-docs
guard-docs: docs
	@git diff --exit-code -- $(CATALOG_DOCS_DIR) || \
	( echo "ERROR: generated docs are out of sync. Run 'make docs' and commit the result."; exit 1 )
