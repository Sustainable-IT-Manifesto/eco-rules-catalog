#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import jsonschema
except ImportError:
    print('ERROR: jsonschema is required. Install with: pip install jsonschema')
    sys.exit(2)

ID_RE = re.compile(r'^ECO-([A-Z0-9]+)-([A-Z0-9]+)-([0-9]{3})$')
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = 'catalog/registry.json'
DEFAULT_SCHEMA = 'catalog/schema/schema-rule.json'

@dataclass
class ValidationMessage:
    level: str
    rule_id: str
    message: str


def load_json(path: Path) -> Any:
    with path.open('r', encoding='utf-8') as fh:
        return json.load(fh)


def iter_rules(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get('rules'), list):
        return payload['rules']
    raise ValueError("Unsupported catalog shape. Expected list or {'rules': [...]}.")


def normalize_text(value: str | None) -> str | None:
    return value.strip().lower() if isinstance(value, str) else None

class Registry:
    def __init__(self, data: dict[str, Any]) -> None:
        self.data = data
        self.categories_by_code = data.get('categories', {})
        self.families_by_code = data.get('families', {})
        self.allowed_layers = set(data.get('system_layers', []))
        self.allowed_statuses = set(data.get('statuses', []))
        self.allowed_lifecycle = set(data.get('lifecycle_stages', []))
        self.allowed_resource_impacts = set(data.get('resource_impacts', []))
        self.allowed_detection_methods = set(data.get('detection_methods', []))
        self.allowed_remediation_patterns = set(data.get('remediation_patterns', []))
        self.category_name_to_code: dict[str, str] = {}
        self.family_name_to_code: dict[str, str] = {}
        for code, item in self.categories_by_code.items():
            for raw in [item.get('name'), *item.get('aliases', [])]:
                n = normalize_text(raw)
                if n: self.category_name_to_code[n] = code
        for code, item in self.families_by_code.items():
            for raw in [item.get('name'), *item.get('aliases', [])]:
                n = normalize_text(raw)
                if n: self.family_name_to_code[n] = code

    def resolve_category_code(self, raw: str | None) -> str | None:
        if raw in self.categories_by_code: return raw
        return self.category_name_to_code.get(normalize_text(raw))

    def resolve_family_code(self, raw: str | None) -> str | None:
        if raw in self.families_by_code: return raw
        return self.family_name_to_code.get(normalize_text(raw))


def derive_expected_id(rule: dict[str, Any], registry: Registry) -> tuple[str | None, list[str]]:
    problems = []
    category_code = registry.resolve_category_code(rule.get('category_code') or rule.get('ontology', {}).get('category_code') or rule.get('category'))
    family_code = registry.resolve_family_code(rule.get('family_code') or rule.get('ontology', {}).get('family_code') or rule.get('family'))
    sequence = rule.get('sequence')
    if sequence is None:
        m = ID_RE.match(str(rule.get('id', '')))
        if m: sequence = int(m.group(3))
        else: problems.append('Missing sequence and unable to infer from id')
    if category_code is None: problems.append('Could not resolve category_code')
    if family_code is None: problems.append('Could not resolve family_code')
    if category_code and family_code:
        expected_category = registry.families_by_code.get(family_code, {}).get('category_code')
        if expected_category != category_code:
            problems.append(f'family {family_code} belongs to category {expected_category}, not {category_code}')
    if problems: return None, problems
    return f'ECO-{category_code}-{family_code}-{int(sequence):03d}', []


def validate_level_map(rule_id: str, name: str, value: Any) -> list[ValidationMessage]:
    messages = []
    levels = {'none','low','medium','high','critical'}
    if value is None: return messages
    if not isinstance(value, dict):
        return [ValidationMessage('ERROR', rule_id, f'{name} must be an object')]
    for k, v in value.items():
        if v not in levels:
            messages.append(ValidationMessage('ERROR', rule_id, f'{name}.{k} must be one of {sorted(levels)}, found {v!r}'))
    return messages


def validate_rule(rule: dict[str, Any], registry: Registry, schema: dict[str, Any]) -> list[ValidationMessage]:
    messages: list[ValidationMessage] = []
    rule_id = rule.get('id', '<missing-id>')
    try:
        jsonschema.validate(rule, schema)
    except jsonschema.ValidationError as exc:
        messages.append(ValidationMessage('ERROR', rule_id, f'schema validation failed: {exc.message}'))
        return messages

    expected_id, id_problems = derive_expected_id(rule, registry)
    messages.extend(ValidationMessage('ERROR', rule_id, p) for p in id_problems)
    if expected_id and rule.get('id') != expected_id:
        messages.append(ValidationMessage('ERROR', rule_id, f'id mismatch: expected {expected_id}, found {rule.get("id")}'))
    if expected_id and rule.get('canonical_id') and rule.get('canonical_id') != expected_id:
        messages.append(ValidationMessage('ERROR', rule_id, f'canonical_id mismatch: expected {expected_id}, found {rule.get("canonical_id")}'))

    category_code = registry.resolve_category_code(rule.get('category_code') or rule.get('category'))
    family_code = registry.resolve_family_code(rule.get('family_code') or rule.get('family'))
    if category_code is None: messages.append(ValidationMessage('ERROR', rule_id, f'unknown category_code/category: {rule.get("category_code") or rule.get("category")!r}'))
    if family_code is None: messages.append(ValidationMessage('ERROR', rule_id, f'unknown family_code/family: {rule.get("family_code") or rule.get("family")!r}'))

    layer = rule.get('layer')
    if layer not in registry.allowed_layers:
        messages.append(ValidationMessage('ERROR', rule_id, f'invalid layer {layer!r}'))
    status = rule.get('metadata', {}).get('status', 'active')
    if status not in registry.allowed_statuses:
        messages.append(ValidationMessage('ERROR', rule_id, f'invalid metadata.status {status!r}'))

    ontology = rule.get('ontology', {})
    for item in ontology.get('system_layers', []):
        if item not in registry.allowed_layers:
            messages.append(ValidationMessage('ERROR', rule_id, f'invalid ontology.system_layers item {item!r}'))
    lifecycle = ontology.get('lifecycle_stage')
    if lifecycle and lifecycle not in registry.allowed_lifecycle:
        messages.append(ValidationMessage('ERROR', rule_id, f'invalid ontology.lifecycle_stage {lifecycle!r}'))
    for item in ontology.get('resource_impacts', []):
        if item not in registry.allowed_resource_impacts:
            messages.append(ValidationMessage('ERROR', rule_id, f'invalid ontology.resource_impacts item {item!r}'))
    for item in ontology.get('detection_methods', []):
        if item not in registry.allowed_detection_methods:
            messages.append(ValidationMessage('ERROR', rule_id, f'invalid ontology.detection_methods item {item!r}'))
    for item in ontology.get('remediation_patterns', []):
        if item not in registry.allowed_remediation_patterns:
            messages.append(ValidationMessage('ERROR', rule_id, f'invalid ontology.remediation_patterns item {item!r}'))

    messages.extend(validate_level_map(rule_id, 'cost_dimensions', rule.get('cost_dimensions')))
    amp = rule.get('amplification')
    if amp is not None:
        for key in ('scales_with_users','scales_with_data_volume','scales_non_linearly'):
            if key in amp and not isinstance(amp[key], bool):
                messages.append(ValidationMessage('ERROR', rule_id, f'amplification.{key} must be boolean'))
    temporal = rule.get('temporal_behavior')
    if temporal is not None:
        for key in ('startup_only','steady_state','burst_sensitive','time_degradation'):
            if key in temporal and not isinstance(temporal[key], bool):
                messages.append(ValidationMessage('ERROR', rule_id, f'temporal_behavior.{key} must be boolean'))
    evidence = rule.get('runtime_evidence')
    if evidence is not None and not (isinstance(evidence, list) and all(isinstance(x, str) and x.strip() for x in evidence)):
        messages.append(ValidationMessage('ERROR', rule_id, 'runtime_evidence must be a list of non-empty strings'))
    priority = rule.get('sustainability_priority')
    if priority is not None and not (isinstance(priority, int) and 1 <= priority <= 5):
        messages.append(ValidationMessage('ERROR', rule_id, 'sustainability_priority must be an integer from 1 to 5'))

    remediation = rule.get('remediation', {})
    if not remediation.get('guidance'):
        messages.append(ValidationMessage('WARN', rule_id, 'missing remediation.guidance'))
    return messages


def summarize(messages: list[ValidationMessage], json_report: Path | None = None) -> int:
    errors = sum(1 for m in messages if m.level == 'ERROR')
    warns = sum(1 for m in messages if m.level == 'WARN')
    for msg in messages:
        print(f'{msg.level}: {msg.rule_id}: {msg.message}')
    print(f'\nSummary: {errors} error(s), {warns} warning(s)')
    if json_report:
        json_report.parent.mkdir(parents=True, exist_ok=True)
        json_report.write_text(json.dumps([m.__dict__ for m in messages], indent=2), encoding='utf-8')
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description='Validate Eco Rules against schema, registry, and v0.4.0 metadata conventions.')
    parser.add_argument('catalog', help='Path to master.json or a rules file')
    parser.add_argument('--registry', default=str(DEFAULT_REGISTRY))
    parser.add_argument('--schema', default=str(DEFAULT_SCHEMA))
    parser.add_argument('--json-report', default=None)
    args = parser.parse_args()
    schema_path = Path(args.schema)
    registry_path = Path(args.registry)
    print(f'Using schema: {schema_path}')
    print(f'Using registry: {registry_path}')
    registry = Registry(load_json(registry_path))
    schema = load_json(schema_path)
    rules = iter_rules(load_json(Path(args.catalog)))
    messages: list[ValidationMessage] = []
    seen = set()
    for rule in rules:
        rid = rule.get('id')
        if rid in seen:
            messages.append(ValidationMessage('ERROR', rid or '<missing-id>', 'duplicate rule id'))
        seen.add(rid)
        messages.extend(validate_rule(rule, registry, schema))
    print(f'Validated {len(rules)} rules')
    return summarize(messages, Path(args.json_report) if args.json_report else None)

if __name__ == '__main__':
    raise SystemExit(main())
