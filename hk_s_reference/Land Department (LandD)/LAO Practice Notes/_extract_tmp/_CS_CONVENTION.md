# LAO Practice Note CS convention (this batch)

Read `d:\Users\rico.kwok\PycharmProjects\Skills-Architects-HK\.cursor\skills\hk-critical-summary\SKILL.md` and follow it.

Match tone/structure of:
`d:\Users\rico.kwok\PycharmProjects\Skills-Architects-HK\hk_s_reference\Land Department (LandD)\LACO Circular Memorandum\summaries\LACO Circular Memorandum No. 1A (21-10-1994)_CS.md`

## Paths

- Extracts: `d:\Users\rico.kwok\PycharmProjects\Skills-Architects-HK\hk_s_reference\Land Department (LandD)\LAO Practice Notes\_extract_tmp\{stem}.txt` (spaces in PDF names become `_`)
- Write CS to: `d:\Users\rico.kwok\PycharmProjects\Skills-Architects-HK\hk_s_reference\Land Department (LandD)\LAO Practice Notes\summaries\`
- Do **not** move/rename original PDFs/DOC/RTF. Do **not** write into `source_reference/`. Do **not** create a combined Technical Summaries file.

## Filename

`LAO Practice Note No. {issue} ({Month YYYY})_CS.md`

- Issue from the document (e.g. `2/2000`, `3/2012B`, `1/2020A`, `APSRSE 2/94`).
- Parenthetical date = signature month/year in the source (e.g. `February 2000`). If only year is known, omit the parens or use the issue year only.
- Never put "Architect Critical Summary" in the filename.
- Never invent issue numbers.

H1 is the short title: `# LAO Practice Note No. 2/2000` with the PN subject on the same line after an em dash if short enough.

## Body (mandatory skeleton)

```markdown
# LAO Practice Note No. {issue} — {subject}
**Architect critical summary for schematic design**
{Month YYYY} | Lands Administration Office — Lands Department
Ref. {file ref if present}

> Scope note: {what this PN governs / is not}

## Regulatory Overview
{exactly 2 sentences}

## Critical main topics and subtopics

### 1. {topic} ({para refs})
{tables of hard rules}
**SD takeaway:** {one design lock}

### Source
{original filename} | companions named in the PN
```

## Rules

- Cite only what is in the extract. Do not invent clauses or remember LandsD policy from training.
- Skip legal preamble, “for general reference”, reservation-of-rights, office-move filler unless it is the whole PN.
- Prefer tables. Numbers, % , weeks, premium bases, GFA/SC locks, application windows, supersession.
- One `**SD takeaway:**` per `###` topic.
- OCR/extract noise: ignore garbled Chinese, page markers, Word OLE junk; use the English body.
- If the PN only amends another PN, say what changed — do not restated the whole parent unless the extract contains it.
- Scale depth to length: a 1-page supplement may be 1–2 topics; a 12-page PN may need more.
