#!/usr/bin/env python3
import importlib.util
import json
import sys
from pathlib import Path

if importlib.util.find_spec("jsonschema") is None:
    print(
        "jsonschema is not installed. Install it with "
        "`python3 -m pip install jsonschema` before running this script.",
        file=sys.stderr,
    )
    raise SystemExit(0)

from jsonschema import Draft202012Validator

schema_path = Path('semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.schema.json')
data_path = Path('semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.json')

schema = json.loads(schema_path.read_bytes().decode('utf-8-sig'))
data = json.loads(data_path.read_bytes().decode('utf-8-sig'))

Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema)
errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
if errors:
    for err in errors:
        path = '.'.join([str(p) for p in err.path])
        print(f"Validation error at {path}: {err.message}")
    raise SystemExit(1)

print('Schema validation passed.')
