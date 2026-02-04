#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root_dir"

python3 scripts/update_checksums.py
python3 - <<'PY'
import hashlib
import subprocess
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

def read_from_git(path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"HEAD:{path}"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout


def read_from_worktree(path: str) -> bytes:
    return Path(path).read_bytes()


def is_dirty(path: str) -> bool:
    result = subprocess.run(
        ["git", "status", "--porcelain", "--", path],
        check=True,
        stdout=subprocess.PIPE,
    )
    return bool(result.stdout.strip())

with open("checksums.sha256", "w", newline="\n") as handle:
    handle.write("# SHA-256 checksums for canonical text artefacts\n")
    handle.write("# Regenerate with: scripts/update_checksums.sh\n")

    for path in files:
        data = read_from_worktree(path) if is_dirty(path) else read_from_git(path)
        data = Path(path).read_bytes()
        normalized = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        digest = hashlib.sha256(normalized).hexdigest()
        handle.write(f"{digest}  {path}\n")
PY
files=(
  README.md
  CANONICAL_INDEX.md
  CHANGELOG.md
  AUDIT_REPORT.md
  CITATION.cff
  META_LINKS.md
  llms.txt
  llms-full.txt
  meta/metadata.jsonld
  manuscript/README.md
  manuscript/TCT_v1.0_canonical.md
  journal/README.md
  journal/TCT_Journal_TruthGovernance_EN_v1.0_canonical.md
  journal/TCT_Jurnal_TataKelolaKebenaran_ID_v1.0_canonical.md
  semantic-defs/README.md
  semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.json
  semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.schema.json
  semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.md
  semantic-defs/TCT_Canonical-Semantic-Definitions_Short_ID-EN_v1.0.md
)

for path in "${files[@]}"; do
  if [[ ! -f "$path" ]]; then
    echo "Missing file in checksum list: $path" >&2
    exit 1
  fi
done

echo "# SHA-256 checksums for canonical text artefacts" > checksums.sha256
echo "# Regenerate with: scripts/update_checksums.sh" >> checksums.sha256

LC_ALL=C sha256sum "${files[@]}" >> checksums.sha256
sha256sum "${files[@]}" >> checksums.sha256

echo "# SHA-256 checksums for canonical text artefacts" > checksums.sha256
echo "# Regenerate with: scripts/update_checksums.sh" >> checksums.sha256

sha256sum \
  README.md \
  CANONICAL_INDEX.md \
  CHANGELOG.md \
  CITATION.cff \
  META_LINKS.md \
  llms.txt \
  llms-full.txt \
  meta/metadata.jsonld \
  manuscript/README.md \
  manuscript/TCT_v1.0_canonical.md \
  journal/README.md \
  journal/TCT_Journal_TruthGovernance_EN_v1.0_canonical.md \
  journal/TCT_Jurnal_TataKelolaKebenaran_ID_v1.0_canonical.md \
  semantic-defs/README.md \
  semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.json \
  semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.schema.json \
  semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.md \
  semantic-defs/TCT_Canonical-Semantic-Definitions_Short_ID-EN_v1.0.md \
  >> checksums.sha256
