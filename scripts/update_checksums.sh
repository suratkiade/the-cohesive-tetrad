#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root_dir"

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
