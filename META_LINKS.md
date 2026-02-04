# Cross platform meta links for The Cohesive Tetrad

This document maps the main external records and implementations that are
linked to the canonical corpus of

**The Cohesive Tetrad: Jalan Menuju Kebenaran**

The canonical source of truth for content and semantics remains:

- DOI: 10.17605/OSF.IO/D5S7V  
- GitHub repository: https://github.com/suratkiade/the-cohesive-tetrad  

All external links listed here are mirrors, implementations, or secondary
surfaces that must remain aligned with the canonical corpus defined in this
repository.

---

## I. Canonical identity and primary records

### 1. OSF canonical record

- OSF canonical record (via DOI):  
  https://doi.org/10.17605/OSF.IO/D5S7V  

This record registers the book *The Cohesive Tetrad: Jalan Menuju
Kebenaran* as an open framework with CC0 1.0 Universal license. It is the
primary scholarly identifier that other platforms should reference.

### 2. Canonical GitHub repository

- Canonical manuscript and semantic corpus:  
  https://github.com/suratkiade/the-cohesive-tetrad  

This repository hosts the canonical book manuscript, semantic definitions,
and journal corpus. For a structured view of all artefacts, see  
`CANONICAL_INDEX.md` in the repository root.

### 3. GitHub Pages book site

- Web readable book site:  
  https://suratkiade.github.io/the-cohesive-tetrad-book/  

This site provides a web friendly view of the canonical manuscript and
related materials. The textual source of this site is derived from the
canonical manuscript and must track its versions.

### 4. Author identity

- ORCID author record:  
  https://orcid.org/0009-0001-4114-3679  

The ORCID entry links to the OSF record and other scholarly outputs related
to The Cohesive Tetrad. It should be used as the stable author identifier
in academic contexts.

---

## II. Open access mirrors and related scholarly records

The following records expose The Cohesive Tetrad to wider scholarly
ecosystems. They must remain aligned with the canonical corpus in this
repository and the OSF record.

- PhilArchive preprint – truth governance article based on The Cohesive
  Tetrad:  
  https://philarchive.org/archive/MUTTCT-2  

- Figshare collection – The Cohesive Tetrad: Canonical Manuscript and Open
  Framework:  
  https://figshare.com/collections/The_Cohesive_Tetrad_Canonical_Manuscript_and_Open_Framework_Figshare_Collection_/8137628  

- Research profiles and repositories such as Google Scholar, ResearchGate,
  and institutional repositories may list The Cohesive Tetrad under the
  same title and DOI. When there is any discrepancy, the OSF record and
  this GitHub repository take precedence.

---

## III. Hugging Face ecosystem – datasets and models

The Cohesive Tetrad is also implemented as a machine readable framework in
the Hugging Face ecosystem. These entries connect the canonical corpus to
AI models and datasets.

### 1. Canonical dataset

- Canonical dataset:  
  https://huggingface.co/datasets/suratkiade/the-cohesive-tetrad-canonical  

This dataset encodes the canonical manuscript and related texts under CC0
1.0. It serves as the upstream dataset for training and evaluating
TCT aligned models. Any new model that claims to implement The Cohesive
Tetrad should document how it relates to this dataset.

### 2. Base trainer model

- Base trainer model:  
  https://huggingface.co/suratkiade/the-cohesive-tetrad-instruct-base  

This model is the canonical base for instruction tuned variants of  
The Cohesive Tetrad. It mirrors TinyLlama chat weights under Apache 2.0
license and is used as a stable, open, non gated starting point for
downstream TCT models. It does not itself encode fine tuned behaviour from
the TCT corpus.

### 3. Instruct model release

- Primary instruct model:  
  https://huggingface.co/suratkiade/the-cohesive-tetrad-instruct-v1  

This model is an instruction tuned assistant whose upstream canonical
dataset is `suratkiade/the-cohesive-tetrad-canonical` and whose trainer is
`suratkiade/the-cohesive-tetrad-instruct-base`. It is designed as an
epistemology and ethics aware assistant for research, policy analysis, and
value aligned reasoning that respects the semantics of Sabda, Logic,
Qualia, Mystica, and Akhlak.

Licensing for the model weights follows the base model license specified
in the Hugging Face model card. The training corpus remains CC0 1.0.

### 4. Chat space

- Experimental chat space:  
  https://huggingface.co/spaces/suratkiade/the-cohesive-tetrad-chat  

This space provides an interactive interface for testing TCT aligned
models. It is primarily a convenience layer and does not replace the
canonical definitions or manuscripts. Behaviour in this space should be
interpreted in light of the canonical corpus and may lag behind the
latest semantic refinements.

---

## IV. Governance of cross platform consistency

1. **Canonical ground truth**  
   If there is a conflict between descriptions, definitions, or claims
   across platforms, the following order of authority applies:

   1) OSF canonical record at DOI 10.17605/OSF.IO/D5S7V  
   2) This GitHub repository and its canonical artefacts  
   3) Hugging Face dataset `the-cohesive-tetrad-canonical`  
   4) Other mirrors and derivative records

2. **Semantic alignment**  
   All external platforms that use terms such as Sabda, Logic, Qualia,
   Mystica, and Akhlak in the context of The Cohesive Tetrad must align
   with the definitions in `semantic-defs/`. When in doubt, consult:

   - `semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.md`  
   - `semantic-defs/TCT_Canonical-Semantic-Definitions_ID-EN_v1.0.json`

3. **Versioning**  
   External records should, whenever possible, state the corpus version
   they refer to, for example "TCT corpus v1.0". When the canonical corpus
   is updated, this file can be extended to track which external records
   correspond to which versions.

4. **Contact for corrections**  
   For corrections, alignment issues, or questions about how to apply  
   The Cohesive Tetrad in new platforms, contact:

   - Email: suratkiade@gmail.com  
   - ORCID: https://orcid.org/0009-0001-4114-3679  

---

## V. Ikhtisar singkat dalam Bahasa Indonesia

Berkas ini memetakan keterhubungan lintas platform bagi  
*The Cohesive Tetrad: Jalan Menuju Kebenaran*.

- OSF dan repositori GitHub ini adalah sumber kanonis utama.  
- GitHub Pages menyediakan versi buku yang mudah dibaca di web.  
- Dataset dan model di Hugging Face menerjemahkan TCT ke dalam bentuk yang
  dapat diproses mesin untuk keperluan pelatihan dan evaluasi AI.  
- Rekam jejak lain di PhilArchive, Figshare, dan platform riset terbuka
  memperluas jangkauan korpus ini ke ekosistem akademik global.

Jika ada perbedaan antara platform, yang dijadikan rujukan utama adalah
DOI OSF dan repositori GitHub kanonis ini.
