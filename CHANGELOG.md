# Changelog

All notable changes to this canonical repository are documented in this file.

The versioning scheme follows a corpus oriented semantic versioning:
- 1.x.y = corpus version 1, x level feature additions, y level maintenance and metadata updates.

## [1.0.2] - 2026-02-04

### Added
- `llms.txt` and `llms-full.txt` to provide LLM friendly corpus summaries and canonical pointers.
- `checksums.sha256` with SHA-256 integrity hashes for canonical text artefacts.
- JSON Schema for the semantic kernel (`semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.schema.json`) to normalize and validate the canonical structure.
- GitHub Actions workflow (`.github/workflows/ci.yml`) to validate checksum integrity on pushes and pull requests.
- GitHub community health files (`.github/SECURITY.md`, `.github/SUPPORT.md`, issue templates, and PR template) plus `AUDIT_REPORT.md` for forensic documentation.
- `scripts/update_checksums.sh` to regenerate the checksum manifest consistently across environments.
- `scripts/check_links.py` and a manual GitHub Actions workflow (`.github/workflows/link_check.yml`) for on-demand link validation.

### Changed
- Added `$schema` reference to the semantic kernel JSON for validation support.
- Normalized cross platform metadata filename to `META_LINKS.md`.
- Documented indexing and LLM metadata guidance across corpus READMEs and updated canonical index listings.
- Added merge conflict guidance to canonical metadata files for consistency.
- Enforced LF normalization via `.gitattributes` to stabilize checksum validation across platforms.
- Updated checksum workflow to use the shared manifest script for consistent CI results.
- Added a manual link check workflow to avoid breaking CI while enabling periodic validation.

## [1.0.1] - 2025-11-23

### Added
- `semantic-defs/` directory with canonical bilingual semantic definitions for Sabda, Logic, Qualia, Mystica, and Akhlak (`TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.*` and short versions).
- `journal/` directory with bilingual truth governance journal manuscripts and PDF editions  
  (`TCT_Journal_TruthGovernance_EN_v1.0*`, `TCT_Jurnal_TataKelolaKebenaran_ID_v1.0*`).
- Local `README.md` files in `semantic-defs/` and `journal/` that describe the canonical role of each corpus.

### Changed
- Root `README.md` aligned with the canonical semantic field of The Cohesive Tetrad: Sabda, Logic, Qualia, Mystica, with Akhlak as the observable surface of verification.
- `CITATION.cff` updated with the primary DOI `10.17605/OSF.IO/D5S7V`, ORCID, canonical academic affiliation for citation, structured abstract, and keywords for machine readable citation.
- Documentation of repository structure clarified so that manuscripts, semantic definitions, and journal articles are explicitly marked as canonical sources.

## [1.0.0] - 2025-11-01

- Initial canonical setup based on OSF record `10.17605/OSF.IO/D5S7V`.
- Added root `README.md`, `LICENSE` (CC0 1.0), `CITATION.cff`, and canonical PDF manuscript `manuscript/TCT_v1.0_canonical.pdf`.
