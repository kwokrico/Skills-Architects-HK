---
name: hk-critical-summary
description: >-
  Produces an hk_s_reference Architect Critical Summary (_CS.md) from a
  user-provided HK statutory document, code of practice, circular, PNAP, or
  ordinance. Use when the user invokes this skill, asks for a Critical Summary,
  CS.md, or schematic-design constraints extracted from a named source file.
disable-model-invocation: true
---

# HK Critical Summary

Write a highly practical, scannable Architect Critical Summary from a **provided** statutory source. Role: senior code consultant highlighting the absolute critical items an architect needs before schematic design. Skip all legal preamble, boilerplate, and administrative filler. Get straight to the design constraints. Do not invent clauses.

## Workflow

1. **Halt if no source file.** Do not summarize from memory or a Cap/CoP name alone. Ask for the PDF, extract, or `@`-attached path.
2. **Read the provided file fully** (PDF, `.md` extract, or attached path). Cite only what is in that source.
3. **Derive the CS filename** from the source (rules below). Never put "Architect Critical Summary" in the filename.
4. **Write the CS file** in the same parent folder as the source document topic — **not** inside `source_reference/`.
5. **Place the English PDF** in `source_reference/` under that parent. Keep the PDF's existing filename; do not rename it to match the CS. If it is already there, leave it. If only a bilingual PDF exists, use the English consolidated version.
6. **Refresh the inventories.** After the CS file and the English PDF are in place, from the repo root run `python scripts/reorganize_hk_s_reference.py --report-only`. That rewrites `hk_s_reference/_CS_INVENTORY.md` and `hk_s_reference/DOCUMENTS_WITHOUT_CS.md`. Do not hand-edit either file. Do not pass `--execute`. Skip this command if step 1 halted because no source was provided.

---

## File naming and folder layout (mandatory)

Follow the hk_s_reference Critical Summary convention:

### Critical Summary (.md)
- Save in the **same parent folder** as the source document topic (NOT inside `source_reference/`).
- Filename format: `{Document Title}_CS.md`
- If the source has an edition or consolidation date in parentheses, keep it before `_CS`:
  - `{Document Title} (DD-MM-YYYY)_CS.md`
  - `{Document Title} (YYYY Edition)_CS.md`

**Do NOT** use "Architect Critical Summary" in the filename.

**Examples:**
| Source PDF | Critical Summary filename |
|------------|---------------------------|
| `Cap 123L Consolidated version for the Whole Chapter (13-05-2021) (English).pdf` | `Cap 123L (13-05-2021)_Building (Appeal) Regulation_CS.md` |
| `Code of Practice for Fire Safety in Buildings 2011 (2024 Edition).pdf` | `Code of Practice for Fire Safety in Buildings 2011 (2024 Edition)_CS.md` |
| `FSD Circular Letter No. 2-2025 Fire Safety Requirements for Data Centres.pdf` | `FSD Circular Letter No. 2-2025 Fire Safety Requirements for Data Centres_CS.md` |

**Derive the CS title from the source by:**
1. Using the document’s short title (Cap number, CoP name, circular title, etc.).
2. Stripping boilerplate suffixes: `Consolidated version for the Whole Chapter`, `(English)`, `(English and Traditional Chinese)`.
3. Keeping one parenthetical date or edition if present in the source.
4. For a Cap instrument, inserting the statutory short title after the date: `Cap 123L (13-05-2021)_Building (Appeal) Regulation_CS.md`.
5. Appending `_CS.md`.

### Source PDF
- Move (or save) the original English PDF into a `source_reference/` subfolder under the same parent folder.
- Keep the PDF’s existing descriptive filename; do not rename it to match the CS file.
- Example layout:

```text
Cap 123 Building Ordience/
 ├── Cap 123L (13-05-2021)_Building (Appeal) Regulation_CS.md
 └── source_reference/
     └── Cap 123L Consolidated version for the Whole Chapter (13-05-2021) (English).pdf
```

If only a bilingual PDF exists, use the English consolidated version and place it in `source_reference/`.

---

## Markdown structure

Use this skeleton:

```markdown
# {Short title}
**Architect critical summary for schematic design**
{edition / consolidation date} | {issuing authority}

> Scope note: {what this instrument is / is not}

## Regulatory Overview
{exactly 2 sentences: scope, occupancy types, or construction classes}

## Critical main topics and subtopics

### 1. {topic} ({clause refs})
{tables of hard rules}
**SD takeaway:** {one design lock}

### Source
{source filename + companion instruments to read with it}
```

### Heading and body rules

- **Title (`#`)**: short document title (Cap number, CoP name, circular title). Same short title used in the filename, without `_CS`.
- **Subtitle line**: always `**Architect critical summary for schematic design**` (in the body, never in the filename).
- **Metadata line**: edition or consolidation date, then issuing authority (e.g. `Consolidated version: 13 May 2021 | Cap. 123 sub. leg. L`).
- **Scope note**: one blockquote stating what the instrument governs and what it is **not**.
- **`## Regulatory Overview`**: exactly 2 sentences defining scope, occupancy types, or construction classes.
- **`## Critical main topics and subtopics`**: numbered `###` topics with clause/section refs. Prefer tables of hard rules. End each topic with `**SD takeaway:**` (one design lock for schematic design).
- **`### Source`**: original source filename plus parent/companion instruments to read with it. Do not dump the full statute.

Scale depth to the source: a short circular may be a few tables; a CoP or Cap may need many numbered topics. Every topic still gets an SD takeaway.

---

## Common mistakes

| Mistake | Do this instead |
|---------|-----------------|
| CS saved inside `source_reference/` | Save `_CS.md` as a sibling of `source_reference/`, in the topic parent folder |
| Filename contains "Architect Critical Summary" | `{Short title} (date or edition)_CS.md` only |
| PDF renamed to match the CS | Keep the PDF's existing descriptive filename |
| Summarizing without a provided file | Halt and ask for the source |
| Legal preamble, commencement history, or admin filler | Design constraints, numbers, and clause refs only |
| Topic with no SD takeaway | One `**SD takeaway:**` per `###` topic |
| Invented clauses or remembered Cap text | Read the provided file; cite only what is in it |
| Regulatory Overview longer than 2 sentences | Two sentences, then move on to topics |
| Hand-editing `_CS_INVENTORY.md` or `DOCUMENTS_WITHOUT_CS.md` | Run `python scripts/reorganize_hk_s_reference.py --report-only` after the CS is written |
