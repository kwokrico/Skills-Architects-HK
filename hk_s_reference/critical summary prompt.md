Please read the attached statutory document [file name] and provide a highly practical, scannable detailed summary in Markdown format.

Imagine you are a senior code consultant highlighting the absolute critical items an architect needs to know before they begin schematic design. Skip all legal preamble, boilerplate language, and administrative filler. Get straight to the design constraints.

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

Cap 123 Building Ordience/
 ├── Cap 123L (13-05-2021)_CS.md
 └── source_reference/
 └── Cap 123L Consolidated version for the Whole Chapter (13-05-2021) (English).pdf


If only a bilingual PDF exists, use the English consolidated version and place it in `source_reference/`.

---

## Markdown structure

Use the following structure:

## Regulatory Overview
A 2-sentence summary defining the exact scope, occupancy types, or construction classes this specific regulation applies to.

## Critical main topics and subtopics