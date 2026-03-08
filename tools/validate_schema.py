#!/usr/bin/env python3
import argparse
import json
import sys
from jsonschema import Draft7Validator

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schema", required=True)
    ap.add_argument("--data", required=True)
    args = ap.parse_args()

    try:
        schema = load_json(args.schema)
        data = load_json(args.data)
        validator = Draft7Validator(schema)
        errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        if errors:
            print("Schema validation failed:")
            for err in errors:
                path = ".".join(str(x) for x in err.path)
                print("- {}: {}".format(path or "<root>", err.message))
            return 1
        print("Schema validation passed.")
        return 0
    except Exception as e:
        print("ERROR:", e)
        return 2

if __name__ == "__main__":
    sys.exit(main())
