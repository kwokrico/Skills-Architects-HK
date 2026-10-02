---
name: hk-ref-statutory-doc-crit-summary
description: >-
  Authors Hong Kong statutory Critical Summaries (*_CS.md) for hk_s_reference from
  Cap / CoP / PNAP / PNRC / PNBI / FSD Circular / JPN PDFs. Use when creating or
  updating Critical Summaries, _CS.md files, or summarizing attached BD/FSD/PlanD
  statutory documents for schematic design constraints.
---

# HK Statutory Document Critical Summary

## Mission

Please read the attached statutory document [document filename] and provide a highly practical, scannable detailed summary in Markdown format.

Imagine you are a senior code consultant highlighting the absolute critical items an architect needs to know before they begin schematic design. Skip all legal preamble, boilerplate language, and administrative filler. Get straight to the design constraints.

## Workflow

1. Identify the source PDF (or extract) and its parent topic folder under `hk_s_reference/`.
2. Ensure the English PDF is in `source_reference/` under that parent (move if needed; **do not rename** the PDF).
3. Derive the Critical Summary filename from the rules below.
4. Read the source thoroughly. Cite section / regulation / schedule numbers from the source — **do not invent clauses**.
5. Write `{Document Title}_CS.md` in the **same parent folder** as the topic (never inside `source_reference/`).
6. Prefer updating an existing `*_CS.md` in place when the user asks to refresh a summary for the same instrument.

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
| `Cap 123L Consolidated version for the Whole Chapter (13-05-2021) (English).pdf` | `Cap 123L (13-05-2021)_CS.md` |
| `Code of Practice for Fire Safety in Buildings 2011 (2024 Edition).pdf` | `Code of Practice for Fire Safety in Buildings 2011 (2024 Edition)_CS.md` |
| `FSD Circular Letter No. 2-2025 Fire Safety Requirements for Data Centres.pdf` | `FSD Circular Letter No. 2-2025 Fire Safety Requirements for Data Centres_CS.md` |

**Derive the CS title from the source by:**
1. Using the document’s short title (Cap number, CoP name, circular title, etc.).
2. Stripping boilerplate suffixes: `Consolidated version for the Whole Chapter`, `(English)`, `(English and Traditional Chinese)`.
3. Keeping one parenthetical date or edition if present in the source.
4. Appending `_CS.md`.

### Source PDF
- Move (or save) the original English PDF into a `source_reference/` subfolder under the same parent folder.
- Keep the PDF’s existing descriptive filename; do not rename it to match the CS file.
- Example layout:

```
Cap 123 Building Ordinance/
 ├── Cap 123L (13-05-2021)_CS.md
 └── source_reference/
     └── Cap 123L Consolidated version for the Whole Chapter (13-05-2021) (English).pdf
```

If only a bilingual PDF exists, use the English consolidated version and place it in `source_reference/`.

## Markdown structure

Use the following structure:

```markdown
# {Short Document Title}
**Architect critical summary for schematic design**
{Date / edition | Issuing authority | effective / supersession notes}

> Scope note: {1–3 sentences — what this instrument is / is not; sister regimes; SD gate}

## Regulatory Overview
{Exactly 2 sentences defining exact scope, occupancy types, construction classes, or trigger thresholds}

## Critical main topics and subtopics

### 1. {Topic that changes design or brief}
| Parameter | Requirement |
|---|---|
| ... | ... |

**SD takeaway:** {one line the architect must lock before schematic}

### 2. {Next topic}
...
```

### Authoring rules

- Prefer **tables** for numeric limits, thresholds, applicability gates, and split enforcement duties.
- **Bold** hard limits (heights, mm, W/m², dates, Cap numbers, mandatory verbs).
- Number topics as `### 1.`, `### 2.`, …; use `####` only when a topic splits cleanly.
- End major topics with **SD takeaway** when the rule changes massing, cores, programme, tenure, or brief.
- Cross-link sister instruments by Cap / CoP / PNAP / circular id — do not duplicate their full CS.
- Body subtitle may say “Architect critical summary”; the **filename** must not.

## Quality bar / anti-patterns

- No commencement history, gazette boilerplate, or admin process unless it changes **applicability** or **effective date**.
- Do not soften mandatory language (“shall” / “must” / absolute thresholds).
- Never put the CS file inside `source_reference/`.
- Never rename the PDF to match the CS stem.
- Never invent section numbers, dimensions, or exemptions not in the source.

## Legacy cleanup (optional)

Only when the user asks to rename inventory or clean legacy filenames: `scripts/reorganize_hk_s_reference.py`. Not required for normal CS authoring.
