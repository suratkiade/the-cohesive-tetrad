# Scripts in this repository

This folder contains the small, auditable scripts used by CI and manual
maintenance tasks.

## `update_checksums.py`
- Purpose: regenerate `checksums.sha256` for canonical text artefacts.
- Usage: `python3 scripts/update_checksums.py`
- Behavior: reads files from git blobs when the worktree is clean and normalizes
  line endings to LF before hashing.

## `validate_schema.py`
- Purpose: validate `semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.json`
  against its JSON Schema.
- Usage: `python3 scripts/validate_schema.py`
- Dependency: requires the `jsonschema` package (install with
  `python3 -m pip install jsonschema` if missing).

## `check_links.py`
- Purpose: validate external links in canonical documentation.
- Usage: `python3 scripts/check_links.py`
- Allowlist: `scripts/link_check_allowlist.json` records URLs that block
  automated checks (403/robots). These entries require periodic manual
  verification and are treated as documented exceptions.
