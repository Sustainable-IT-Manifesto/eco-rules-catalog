# Eco Rules Catalog - Makefile
# Usage:
#   make help
#   make venv
#   make install
#   make validate
#   make normalize
#   make docs
#   make ci

PY ?= python3
CATALOG ?= master.json

HUMAN_OUT ?= eco_catalog_human
EXAMPLES_DIR ?= examples

VENV_DIR ?= .venv
VENV_PY := $(VENV_DIR)/bin/python
VENV_PIP := $(VENV_DIR)/bin/pip

.PHONY: help \
        venv install install-dev \
        validate validate-strict \
        normalize normalize-check \
        examples-stubs \
        docs docs-html \
        ci clean clean-venv

help:
	@echo ""
	@echo "Eco Rules Catalog"
	@echo ""
	@echo "Bootstrap:"
	@echo "  make venv               Create virtual environment in $(VENV_DIR)"
	@echo "  make install            Install runtime deps (requirements.txt)"
	@echo "  make install-dev        Install dev deps (requirements-dev.txt)"
	@echo ""
	@echo "Common targets:"
	@echo "  make validate            Validate ontology blocks (requires ontology)"
	@echo "  make validate-strict     Validate and treat warnings as errors"
	@echo "  make normalize           Normalize ontology in-place (stable diffs)"
	@echo "  make normalize-check     Fail if normalization would change files (CI)"
	@echo "  make docs                Generate human-readable catalog (md)"
	@echo "  make docs-html           Generate human-readable catalog (md + html)"
	@echo "  make examples-stubs      Create example stub files for all rules"
	@echo "  make ci                  Run normalization-check + validate"
	@echo "  make clean               Remove generated output"
	@echo "  make clean-venv          Remove virtual environment"
	@echo ""
	@echo "Variables (override like: make docs EXAMPLES_DIR=examples):"
	@echo "  PY=$(PY)"
	@echo "  CATALOG=$(CATALOG)"
	@echo "  HUMAN_OUT=$(HUMAN_OUT)"
	@echo "  EXAMPLES_DIR=$(EXAMPLES_DIR)"
	@echo "  VENV_DIR=$(VENV_DIR)"
	@echo ""

# ---- Bootstrap ----

venv:
	@$(PY) -m venv "$(VENV_DIR)"
	@echo "Created venv: $(VENV_DIR)"
	@echo "Activate with: source $(VENV_DIR)/bin/activate"

install: venv
	@$(VENV_PIP) install -r requirements.txt
	@echo "Installed requirements.txt into $(VENV_DIR)"

install-dev: venv
	@$(VENV_PIP) install -r requirements-dev.txt
	@echo "Installed requirements-dev.txt into $(VENV_DIR)"

# ---- Validation ----

validate:
	@$(VENV_PY) tools/validate_ontology.py --in "$(CATALOG)" --require-ontology

validate-strict:
	@$(VENV_PY) tools/validate_ontology.py --in "$(CATALOG)" --require-ontology --strict

# ---- Normalization ----

normalize:
	@$(VENV_PY) tools/normalize_ontology.py --in "$(CATALOG)" --write --fill-system-layer

normalize-check:
	@$(VENV_PY) tools/normalize_ontology.py --in "$(CATALOG)" --check --fill-system-layer

# ---- Docs generation ----

examples-stubs:
	@$(VENV_PY) generate_human_catalog.py --in "$(CATALOG)" --out "$(HUMAN_OUT)" --examples-template "$(EXAMPLES_DIR)"
	@echo "Created stub examples in: $(EXAMPLES_DIR)"

docs:
	@if [ -d "$(EXAMPLES_DIR)" ]; then \
		$(VENV_PY) generate_human_catalog.py --in "$(CATALOG)" --out "$(HUMAN_OUT)" --examples-dir "$(EXAMPLES_DIR)"; \
	else \
		$(VENV_PY) generate_human_catalog.py --in "$(CATALOG)" --out "$(HUMAN_OUT)"; \
	fi
	@echo "Wrote docs to: $(HUMAN_OUT)/"

docs-html:
	@if [ -d "$(EXAMPLES_DIR)" ]; then \
		$(VENV_PY) generate_human_catalog.py --in "$(CATALOG)" --out "$(HUMAN_OUT)" --examples-dir "$(EXAMPLES_DIR)" --html; \
	else \
		$(VENV_PY) generate_human_catalog.py --in "$(CATALOG)" --out "$(HUMAN_OUT)" --html; \
	fi
	@echo "Wrote docs to: $(HUMAN_OUT)/ (md + html)"

# ---- CI ----

ci: normalize-check validate
	@echo "CI checks passed."

# ---- Cleanup ----

clean:
	@rm -rf "$(HUMAN_OUT)"
	@echo "Removed: $(HUMAN_OUT)"

clean-venv:
	@rm -rf "$(VENV_DIR)"
	@echo "Removed venv: $(VENV_DIR)"

