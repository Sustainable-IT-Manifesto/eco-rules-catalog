PY ?= python3
CATALOG ?= master.json

CATEGORIES ?= ontology/categories.json
FAMILIES ?= ontology/families.json

SCHEMA_CATALOG ?= schema/schema-catalog.json
SCHEMA_RULE ?= schema/schema-rule.json
SCHEMA_CATEGORIES ?= schema/schema-categories.json
SCHEMA_FAMILIES ?= schema/schema-families.json

HUMAN_OUT ?= eco_catalog_human
EXAMPLES_DIR ?= examples
SITE_INDEX_OUT ?= docs-site/docs/catalog/_data/catalog_index.json

VENV_DIR ?= .venv
VENV_PY := $(VENV_DIR)/bin/python
VENV_PIP := $(VENV_DIR)/bin/pip

.PHONY: help \
	venv install install-dev clean clean-venv \
	validate-schema validate-schema-catalog validate-schema-categories validate-schema-families \
	validate validate-strict \
	validate-catalog validate-catalog-strict \
	normalize normalize-check \
	update-rules update-rules-check \
	examples-stubs \
	docs docs-html \
	build-site-assets \
	publish publish-strict publish-report \
	ci ci-strict check-all fix-all

help:
	@echo ""
	@echo "Eco Rules Catalog"
	@echo ""
	@echo "Bootstrap:"
	@echo "  make venv                    Create virtual environment"
	@echo "  make install                 Install runtime dependencies"
	@echo "  make install-dev             Install dev dependencies"
	@echo ""
	@echo "Validation:"
	@echo "  make validate-schema         Validate JSON files against JSON Schema"
	@echo "  make validate                Validate ontology blocks"
	@echo "  make validate-strict         Validate ontology strictly"
	@echo "  make validate-catalog        Validate catalog against registries"
	@echo "  make validate-catalog-strict Validate catalog strictly"
	@echo ""
	@echo "Normalization / updates:"
	@echo "  make normalize               Normalize ontology in-place"
	@echo "  make normalize-check         Fail if normalization would change catalog"
	@echo "  make update-rules            Backfill category/code/canonical_id fields"
	@echo "  make update-rules-check      Write updated catalog to temp file"
	@echo ""
	@echo "Docs:"
	@echo "  make examples-stubs          Create example stub files"
	@echo "  make docs                    Generate human-readable Markdown docs"
	@echo "  make docs-html               Generate Markdown + HTML docs"
	@echo "  make build-site-assets       Build search / ontology browser assets"
	@echo ""
	@echo "Publishing:"
	@echo "  make publish                 Run full publishing pipeline"
	@echo "  make publish-strict          Run strict publishing pipeline"
	@echo "  make publish-report          Run pipeline and write JSON report"
	@echo ""
	@echo "Convenience:"
	@echo "  make ci                      CI checks"
	@echo "  make ci-strict               Strict CI checks"
	@echo "  make check-all               Full local check sequence"
	@echo "  make fix-all                 Normalize, update, validate, docs"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean                   Remove generated docs"
	@echo "  make clean-venv              Remove virtual environment"
	@echo ""

venv:
	@$(PY) -m venv "$(VENV_DIR)"
	@echo "Created venv: $(VENV_DIR)"

install: venv
	@$(VENV_PIP) install -r requirements.txt
	@echo "Installed requirements.txt"

install-dev: venv
	@$(VENV_PIP) install -r requirements-dev.txt
	@echo "Installed requirements-dev.txt"

validate-schema-catalog:
	@$(VENV_PY) tools/validate_schema.py --schema "$(SCHEMA_CATALOG)" --data "$(CATALOG)"

validate-schema-categories:
	@$(VENV_PY) tools/validate_schema.py --schema "$(SCHEMA_CATEGORIES)" --data "$(CATEGORIES)"

validate-schema-families:
	@$(VENV_PY) tools/validate_schema.py --schema "$(SCHEMA_FAMILIES)" --data "$(FAMILIES)"

validate-schema: validate-schema-catalog validate-schema-categories validate-schema-families
	@echo "Schema validation passed."

validate:
	@$(VENV_PY) tools/validate_ontology.py --in "$(CATALOG)" --require-ontology

validate-strict:
	@$(VENV_PY) tools/validate_ontology.py --in "$(CATALOG)" --require-ontology --strict

validate-catalog:
	@$(VENV_PY) tools/validate_catalog.py --catalog "$(CATALOG)" --categories "$(CATEGORIES)" --families "$(FAMILIES)"

validate-catalog-strict:
	@$(VENV_PY) tools/validate_catalog.py --catalog "$(CATALOG)" --categories "$(CATEGORIES)" --families "$(FAMILIES)" --strict

normalize:
	@$(VENV_PY) tools/normalize_ontology.py --in "$(CATALOG)" --write --fill-system-layer

normalize-check:
	@$(VENV_PY) tools/normalize_ontology.py --in "$(CATALOG)" --check --fill-system-layer

update-rules:
update-rules:
	@$(VENV_PY) tools/update_rules.py \
		--catalog "$(CATALOG)" \
		--categories "$(CATEGORIES)" \
		--families "$(FAMILIES)" \
		--write \
		--fill-system-layer \
		--normalize-ontology

update-rules-check:
	@$(VENV_PY) tools/update_rules.py --catalog "$(CATALOG)" --categories "$(CATEGORIES)" --families "$(FAMILIES)" --out /tmp/master.updated.json --fill-system-layer --normalize-ontology

examples-stubs:
	@$(VENV_PY) generate_human_catalog.py --in "$(CATALOG)" --out "$(HUMAN_OUT)" --examples-template "$(EXAMPLES_DIR)"

docs:
	@if [ -d "$(EXAMPLES_DIR)" ]; then \
		$(VENV_PY) generate_human_catalog.py --in "$(CATALOG)" --out "$(HUMAN_OUT)" --examples-dir "$(EXAMPLES_DIR)"; \
	else \
		$(VENV_PY) generate_human_catalog.py --in "$(CATALOG)" --out "$(HUMAN_OUT)"; \
	fi

docs-html:
	@if [ -d "$(EXAMPLES_DIR)" ]; then \
		$(VENV_PY) generate_human_catalog.py --in "$(CATALOG)" --out "$(HUMAN_OUT)" --examples-dir "$(EXAMPLES_DIR)" --html; \
	else \
		$(VENV_PY) generate_human_catalog.py --in "$(CATALOG)" --out "$(HUMAN_OUT)" --html; \
	fi

build-site-assets:
	@$(VENV_PY) tools/build_site_assets.py --in "$(CATALOG)" --out "$(SITE_INDEX_OUT)"

publish:
	@$(VENV_PY) tools/publish_catalog.py --catalog "$(CATALOG)" --categories "$(CATEGORIES)" --families "$(FAMILIES)" --human-out "$(HUMAN_OUT)" --site-index-out "$(SITE_INDEX_OUT)" --examples-dir "$(EXAMPLES_DIR)" --write

publish-strict:
	@$(VENV_PY) tools/publish_catalog.py --catalog "$(CATALOG)" --categories "$(CATEGORIES)" --families "$(FAMILIES)" --human-out "$(HUMAN_OUT)" --site-index-out "$(SITE_INDEX_OUT)" --examples-dir "$(EXAMPLES_DIR)" --write --strict

publish-report:
	@$(VENV_PY) tools/publish_catalog.py --catalog "$(CATALOG)" --categories "$(CATEGORIES)" --families "$(FAMILIES)" --human-out "$(HUMAN_OUT)" --site-index-out "$(SITE_INDEX_OUT)" --examples-dir "$(EXAMPLES_DIR)" --write --report-out build/publish-report.json

ci: validate-schema normalize-check validate validate-catalog
	@echo "CI checks passed."

ci-strict: validate-schema normalize-check validate-strict validate-catalog-strict
	@echo "Strict CI checks passed."

check-all: validate-schema normalize-check validate-strict validate-catalog-strict
	@echo "All checks passed."

fix-all: normalize update-rules validate validate-catalog docs
	@echo "Catalog normalized, updated, validated, and docs generated."

clean:
	@rm -rf "$(HUMAN_OUT)"
	@echo "Removed: $(HUMAN_OUT)"

clean-venv:
	@rm -rf "$(VENV_DIR)"
	@echo "Removed venv: $(VENV_DIR)"
