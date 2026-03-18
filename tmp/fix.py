from pathlib import Path
import json

ROOT = Path(".")
RULES = ROOT / "catalog" / "rules"

MAP = {
    "AI/ML": "ai",
    "Architecture": "architecture",
    "Code": "code",
    "Data": "data",
    "Network": "network",
    "Process": "process",
    "ai": "ai",
    "architecture": "architecture",
    "code": "code",
    "data": "data",
    "network": "network",
    "process": "process",
}

changed = 0

for path in RULES.rglob("*.json"):
    print(path)
    with path.open("r", encoding="utf-8") as f:
        rule = json.load(f)

    layer = rule.get("layer")
    ontology = rule.setdefault("ontology", {})
    system_layers = ontology.get("system_layers")

    if not system_layers:
        if layer:
            ontology["system_layers"] = [layer]
            changed += 1
    else:
        normalized = []
        for item in system_layers:
            normalized.append(MAP.get(item, item.lower()))
        ontology["system_layers"] = sorted(set(normalized))
        changed += 1

    if layer and layer not in ontology["system_layers"]:
        ontology["system_layers"].insert(0, layer)
        ontology["system_layers"] = sorted(set(ontology["system_layers"]))
        changed += 1

    with path.open("w", encoding="utf-8") as f:
        json.dump(rule, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Updated rules: {changed}")
