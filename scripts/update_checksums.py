#!/usr/bin/env python3
import hashlib
import subprocess
from pathlib import Path

FILES = [
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


def main() -> None:
    with open("checksums.sha256", "w", newline="\n") as handle:
        handle.write("# SHA-256 checksums for canonical text artefacts\n")
        handle.write("# Regenerate with: scripts/update_checksums.py\n")

        for path in FILES:
            data = read_from_worktree(path) if is_dirty(path) else read_from_git(path)
            normalized = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            digest = hashlib.sha256(normalized).hexdigest()
            handle.write(f"{digest}  {path}\n")


if __name__ == "__main__":
    main()
