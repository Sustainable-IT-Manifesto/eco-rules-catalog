#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import jsonschema
except ImportError:
    print("ERROR: jsonschema is required. Install with: pip install jsonschema")
    sys.exit(2)

ID_RE = re.compile(r"^ECO-([A-Z0-9]+)-([A-Z0-9]+)-([0-9]{3})$")
ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "catalog" / "registry.json"
SCHEMA_PATH = ROOT / "catalog" / "schema" / "schema-rule.json"


@dataclass
class ValidationMessage:
    level: str
    rule_id: str
    message: str


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def normalize_text(value: str | None) -> str | None:
    if value is None:
        return None
    return value.strip().lower()


class Registry:
    def __init__(self, data: dict[str, Any]) -> None:
        self.data = data
        self.categories_by_code = data["categories"]
        self.families_by_code = data["families"]
        self.allowed_layers = set(data.get("system_layers", []))
        self.allowed_statuses = set(data.get("statuses", []))
        self.allowed_lifecycle = set(data.get("lifecycle_stages", []))
        self.allowed_resource_impacts = set(data.get("resource_impacts", []))
        self.allowed_detection_methods = set(data.get("detection_methods", []))
        self.allowed_remediation_patterns = set(data.get("remediation_patterns", []))

        self.category_name_to_code = {}
        self.family_name_to_code = {}
        for code, item in self.categories_by_code.items():
            self.category_name_to_code[normalize_text(item["name"])] = code
            for alias in item.get("aliases", []):
                self.category_name_to_code[normalize_text(alias)] = code
        for code, item in self.families_by_code.items():
            self.family_name_to_code[normalize_text(item["name"])] = code
            for alias in item.get("aliases", []):
                self.family_name_to_code[normalize_text(alias)] = code

    def resolve_category_code(self, raw: str | None) -> str | None:
        if raw is None:
            return None
        if raw in self.categories_by_code:
            return raw
        return self.category_name_to_code.get(normalize_text(raw))

    def resolve_family_code(self, raw: str | None) -> str | None:
        if raw is None:
            return None
        if raw in self.families_by_code:
            return raw
        return self.family_name_to_code.get(normalize_text(raw))


def derive_expected_id(rule: dict[str, Any], registry: Registry) -> tuple[str | None, list[str]]:
    problems = []
    category_code = registry.resolve_category_code(rule.get("category_code") or rule.get("ontology", {}).get("category_code") or rule.get("category"))
    family_code = registry.resolve_family_code(rule.get("family_code") or rule.get("ontology", {}).get("family_code") or rule.get("family"))
    sequence = rule.get("sequence")

    if category_code is None:
        problems.append("Could not resolve category_code")
    if family_code is None:
        problems.append("Could not resolve family_code")

    if category_code and family_code:
        expected_category = registry.families_by_code[family_code]["category_code"]
        if expected_category != category_code:
            problems.append(f"family {family_code} belongs to category {expected_category}, not {category_code}")

    if sequence is None:
        existing_id = rule.get("id", "")
        m = ID_RE.match(existing_id)
        if m:
            sequence = int(m.group(3))
        else:
            problems.append("Missing sequence and unable to infer from id")

    if problems:
        return None, problems
    return f"ECO-{category_code}-{family_code}-{int(sequence):03d}", []


def validate_rule(rule: dict[str, Any], registry: Registry, schema: dict[str, Any]) -> list[ValidationMessage]:
    messages: list[ValidationMessage] = []
    rule_id = rule.get("id", "<missing-id>")

    try:
        jsonschema.validate(rule, schema)
    except jsonschema.ValidationError as exc:
        messages.append(ValidationMessage("ERROR", rule_id, f"schema validation failed: {exc.message}"))
        return messages

    category_code = registry.resolve_category_code(rule.get("category_code") or rule.get("category"))
    family_code = registry.resolve_family_code(rule.get("family_code") or rule.get("family"))

    if category_code is None:
        messages.append(ValidationMessage("ERROR", rule_id, f"unknown category_code/category: {rule.get('category_code') or rule.get('category')!r}"))
    if family_code is None:
        messages.append(ValidationMessage("ERROR", rule_id, f"unknown family_code/family: {rule.get('family_code') or rule.get('family')!r}"))

    if category_code and family_code:
        expected_category = registry.families_by_code[family_code]["category_code"]
        if expected_category != category_code:
            messages.append(ValidationMessage("ERROR", rule_id, f"family {family_code} is registered under {expected_category}, not {category_code}"))

    expected_id, id_problems = derive_expected_id(rule, registry)
    for problem in id_problems:
        messages.append(ValidationMessage("ERROR", rule_id, problem))
    if expected_id and rule.get("id") != expected_id:
        messages.append(ValidationMessage("ERROR", rule_id, f"id mismatch: expected {expected_id}, found {rule.get('id')}"))
    if expected_id and rule.get("canonical_id") and rule.get("canonical_id") != expected_id:
        messages.append(ValidationMessage("ERROR", rule_id, f"canonical_id mismatch: expected {expected_id}, found {rule.get('canonical_id')}"))

    if rule.get("category") and category_code:
        canonical_name = registry.categories_by_code[category_code]["name"]
        if rule["category"] != canonical_name:
            messages.append(ValidationMessage("WARN", rule_id, f"category should be normalized to {canonical_name!r}"))
    if rule.get("family") and family_code:
        canonical_name = registry.families_by_code[family_code]["name"]
        if rule["family"] != canonical_name:
            messages.append(ValidationMessage("WARN", rule_id, f"family should be normalized to {canonical_name!r}"))

    layer = rule.get("layer")
    if layer not in registry.allowed_layers:
        messages.append(ValidationMessage("ERROR", rule_id, f"invalid layer {layer!r}"))

    metadata = rule.get("metadata", {})
    status = metadata.get("status", "active")
    if status not in registry.allowed_statuses:
        messages.append(ValidationMessage("ERROR", rule_id, f"invalid metadata.status {status!r}"))

    ontology = rule.get("ontology", {})
    for item in ontology.get("system_layers", []):
        if item not in registry.allowed_layers:
            messages.append(ValidationMessage("ERROR", rule_id, f"invalid ontology.system_layers item {item!r}"))
    lifecycle = ontology.get("lifecycle_stage")
    if lifecycle and lifecycle not in registry.allowed_lifecycle:
        messages.append(ValidationMessage("ERROR", rule_id, f"invalid ontology.lifecycle_stage {lifecycle!r}"))
    for item in ontology.get("resource_impacts", []):
        if item not in registry.allowed_resource_impacts:
            messages.append(ValidationMessage("ERROR", rule_id, f"invalid ontology.resource_impacts item {item!r}"))
    for item in ontology.get("detection_methods", []):
        if item not in registry.allowed_detection_methods:
            messages.append(ValidationMessage("ERROR", rule_id, f"invalid ontology.detection_methods item {item!r}"))
    for item in ontology.get("remediation_patterns", []):
        if item not in registry.allowed_remediation_patterns:
            messages.append(ValidationMessage("ERROR", rule_id, f"invalid ontology.remediation_patterns item {item!r}"))

    remediation = rule.get("remediation", {})
    if not remediation.get("guidance"):
        messages.append(ValidationMessage("WARN", rule_id, "missing remediation.guidance"))
    if not remediation.get("examples"):
        messages.append(ValidationMessage("WARN", rule_id, "missing remediation.examples"))

    return messages


def iter_rules(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and "rules" in payload and isinstance(payload["rules"], list):
        return payload["rules"]
    raise ValueError("Unsupported catalog shape. Expected list or {'rules': [...]}.")


def summarize(messages: list[ValidationMessage]) -> int:
    errors = 0
    warns = 0
    for msg in messages:
        print(f"{msg.level}: {msg.rule_id}: {msg.message}")
        if msg.level == "ERROR":
            errors += 1
        elif msg.level == "WARN":
            warns += 1
    print()
    print(f"Summary: {errors} error(s), {warns} warning(s)")
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("catalog", help="Path to master.json or a rules file")
    args = parser.parse_args()

    payload = load_json(Path(args.catalog))
    rules = iter_rules(payload)
    registry = Registry(load_json(REGISTRY_PATH))
    schema = load_json(SCHEMA_PATH)

    messages: list[ValidationMessage] = []
    seen_ids: set[str] = set()
    for rule in rules:
        rid = rule.get("id", "<missing-id>")
        if rid in seen_ids:
            messages.append(ValidationMessage("ERROR", rid, "duplicate rule id"))
        seen_ids.add(rid)
        messages.extend(validate_rule(rule, registry, schema))

    return summarize(messages)


if __name__ == "__main__":
    raise SystemExit(main())
