# Canonical index for The Cohesive Tetrad corpus (v1.0)

This file provides a canonical index of the core artefacts for  
**The Cohesive Tetrad: Jalan Menuju Kebenaran**  
and is intended as a single source of truth for humans, repositories, and AI systems.

All artefacts listed here are part of the canonical corpus associated with the DOI  
**10.17605/OSF.IO/D5S7V** and are released under **CC0 1.0 Universal (Public Domain Dedication)**.

---

## I. Canonical identity

- **Title (ID)**: The Cohesive Tetrad: Jalan Menuju Kebenaran  
- **Title (EN)**: The Cohesive Tetrad: Sabda, Logic, Qualia, Mystica  

- **Tagline (ID)**: Akhir dari Perdebatan adalah Awal dari Amal  
- **Tagline (EN)**: The End of Debate is the Beginning of Deeds  

- **Author**: Ade Zaenal Mutaqin  
- **Academic role**: Independent researcher  
- **Canonical academic affiliation for citation**:  
  Faculty of Economics and Business, Pakuan University, Bogor, Indonesia  
- **Institutional ecosystem**: Highland Indonesia Group, Strategic Branding and Research  
- **ORCID**: https://orcid.org/0009-0001-4114-3679  

- **Version**: 1.0  
- **Date released**: 2025-11-01  
- **Primary DOI**: 10.17605/OSF.IO/D5S7V  
- **License**: CC0 1.0 Universal (Public Domain Dedication)

The framework articulates four interdependent languages of truth  
Sabda, Logic, Qualia, Mystica  
with **Akhlak** as the observable surface of verification.

---

## II. Root level canonical files

These files define the identity, license, and change history of the corpus.

| Path               | Type              | Role                                                                 |
|--------------------|-------------------|----------------------------------------------------------------------|
| `README.md`        | Documentation     | Canonical overview, metadata, and corpus structure                  |
| `LICENSE`          | Legal             | CC0 1.0 Universal public domain dedication text                     |
| `CITATION.cff`     | Citation metadata | Machine readable citation record for scholarly and software systems |
| `CHANGELOG.md`     | History           | Versioned change log of the canonical corpus                        |
| `CANONICAL_INDEX.md` | Index           | This file, corpus wide canonical artefact map                       |

---

## III. Manuscript corpus

Directory: `manuscript/`  
Role: canonical book manuscript for The Cohesive Tetrad.

### A. Files

| Path                                   | Type       | Lang | Role                                                                 |
|----------------------------------------|------------|------|----------------------------------------------------------------------|
| `manuscript/TCT_v1.0_canonical.md`     | Book       | ID/EN| Canonical Pandoc Markdown source for the full book                   |
| `manuscript/TCT_v1.0_canonical.pdf`    | Book       | ID/EN| Reading edition of the canonical book, suitable for citation         |
| `manuscript/TCT_v1.0_canonical.docx`   | Book       | ID/EN| Canonical Word source defined in the record, may not be public       |
| `manuscript/README.md`                 | Doc        | EN/ID| Explains the role and use of the manuscript corpus                   |

### B. Function in the corpus

- Long form philosophical and ethical exposition of The Cohesive Tetrad.  
- Primary narrative for human readers, reviewers, and translators.  
- All derived works at book level should trace back to `TCT_v1.0_canonical.md`.

---

## IV. Semantic corpus

Directory: `semantic-defs/`  
Role: canonical bilingual semantic kernel for TCT terminology.

### A. Files

| Path                                                             | Type        | Lang | Role                                                                 |
|------------------------------------------------------------------|-------------|------|----------------------------------------------------------------------|
| `semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.json`     | Semantics   | ID/EN| Machine readable core semantic kernel                               |
| `semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.md`       | Semantics   | ID/EN| Full canonical semantic definitions in prose                         |
| `semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.pdf`      | Semantics   | ID/EN| Reading edition of full semantic definitions                         |
| `semantic-defs/TCT_Canonical-Semantic-Definitions_Short_ID-EN_v1.0.md` | Semantics   | ID/EN| Short canonical semantic definitions for glossaries and notes        |
| `semantic-defs/TCT_Canonical-Semantic-Definitions_Short_ID-EN_v1.0.pdf`| Semantics   | ID/EN| Reading edition of short semantic definitions                        |
| `semantic-defs/README.md`                                             | Doc         | EN/ID| Documentation of the role and usage of the semantic corpus           |

### B. Function in the corpus

- Defines the binding meaning of Sabda, Logic, Qualia, Mystica, and Akhlak.  
- Governs the use of TCT terminology in all manuscripts, datasets, and AI models.  
- If there is any ambiguity in terminology, the definitions here take precedence.

---

## V. Journal corpus

Directory: `journal/`  
Role: canonical journal style articulation of TCT focused on truth governance.

### A. Files

| Path                                                             | Type     | Lang | Role                                                                 |
|------------------------------------------------------------------|----------|------|----------------------------------------------------------------------|
| `journal/TCT_Journal_TruthGovernance_EN_v1.0_canonical.md`       | Article  | EN   | Canonical English truth governance journal manuscript                |
| `journal/TCT_Journal_TruthGovernance_EN_v1.0.pdf`                | Article  | EN   | Reading edition of the English article                               |
| `journal/TCT_Jurnal_TataKelolaKebenaran_ID_v1.0_canonical.md`    | Article  | ID   | Canonical Indonesian truth governance journal manuscript             |
| `journal/TCT_Jurnal_TataKelolaKebenaran_ID_v1.0.pdf`             | Article  | ID   | Reading edition of the Indonesian article                            |
| `journal/README.md`                                              | Doc      | EN/ID| Documentation of the journal corpus and its relation to the corpus   |

### B. Function in the corpus

- Presents TCT as an architecture of truth governance under minimal human dignity axioms.  
- Provides a bilingual pair in English and Indonesian that are structurally and semantically aligned.  
- Serves as a bridge between the book, the semantic kernel, and applied work in institutions and AI.

---

## VI. Future corpus components (reserved)

The following directories may appear in future versions of the corpus.  
They are reserved in the canonical design, even if currently empty.

| Path            | Planned role                                                           |
|-----------------|------------------------------------------------------------------------|
| `figures/`      | Conceptual diagrams and visual maps of The Cohesive Tetrad            |
| `supplementary/`| Extended glossaries, FAQs, audit tools, methodological notes          |
| `meta/`         | Links and records for OSF, Zenodo, Figshare, CORE, HCommons, Wikidata |

Any addition under these directories that claims to be canonical must be documented in  
`CHANGELOG.md` and, when appropriate, referenced from this index.

---

## VII. Versioning and usage notes

- **Versioning**  
  - Corpus version: `1.0.x`  
  - `1.0.0` records the initial canonical setup.  
  - `1.0.1` and later record extensions such as semantic and journal corpora.

- **Source of truth**  
  - Root level files (README, LICENSE, CITATION, CHANGELOG)  
    and this `CANONICAL_INDEX.md` define the identity and governance of the corpus.  
  - Manuscript, semantic, and journal directories jointly form the textual core.

- **For researchers**  
  - Use the PDF files for reading and citation.  
  - Use the Markdown and JSON files for structured quotation, analysis, and reuse.

- **For AI and software systems**  
  - Use `semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.json`  
    as the primary semantic kernel.  
  - Use `manuscript/TCT_v1.0_canonical.md` and the journal manuscripts as  
    long form and analytic training or evaluation data.

---

## VIII. Ikhtisar singkat dalam Bahasa Indonesia

Indeks ini merangkum seluruh artefak inti korpus kanonis  
*The Cohesive Tetrad: Jalan Menuju Kebenaran* versi 1.0.

- Direktori `manuscript/` menyimpan naskah buku kanonis.  
- Direktori `semantic-defs/` menyimpan definisi semantik kanonis dwibahasa.  
- Direktori `journal/` menyimpan artikel jurnal kanonis tentang tata kelola kebenaran.  

Seluruh berkas yang tercantum di sini terikat pada DOI **10.17605/OSF.IO/D5S7V**  
dan dirilis dengan lisensi **CC0 1.0 Universal** sebagai persembahan bagi wilayah publik.
