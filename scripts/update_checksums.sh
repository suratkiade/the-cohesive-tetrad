#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root_dir"

python3 - <<'PY'
import hashlib
from pathlib import Path

files = [
    "README.md",
    "CANONICAL_INDEX.md",
    "CHANGELOG.md",
    "AUDIT_REPORT.md",
    "CITATION.cff",
    "META_LINKS.md",
    "llms.txt",
    "llms-full.txt",
    "meta/metadata.jsonld",
    "manuscript/README.md",
    "manuscript/TCT_v1.0_canonical.md",
    "journal/README.md",
    "journal/TCT_Journal_TruthGovernance_EN_v1.0_canonical.md",
    "journal/TCT_Jurnal_TataKelolaKebenaran_ID_v1.0_canonical.md",
    "semantic-defs/README.md",
    "semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.json",
    "semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.schema.json",
    "semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.md",
    "semantic-defs/TCT_Canonical-Semantic-Definitions_Short_ID-EN_v1.0.md",
]

with open("checksums.sha256", "w", newline="\n") as handle:
    handle.write("# SHA-256 checksums for canonical text artefacts\n")
    handle.write("# Regenerate with: scripts/update_checksums.sh\n")

    for path in files:
        data = Path(path).read_bytes()
        normalized = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        digest = hashlib.sha256(normalized).hexdigest()
        handle.write(f"{digest}  {path}\n")
PY
