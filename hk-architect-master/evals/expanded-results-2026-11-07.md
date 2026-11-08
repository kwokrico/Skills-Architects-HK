# Expanded behavioural evaluation — 7 November 2026

## Outcome

Implemented the approved plan: added scenarios 17–28 and three synthetic fixtures, evaluated the remaining existing scenarios 1–12, and regressed 13–16. The latest reviewed evidence passes **100/100 assertions across 28 scenarios**. Independent repeat runs of cases 9, 11, 19, 23 and 27 pass another **19/19 assertions**. These are repeat observations, not additional unique scenarios. [Assertion-level judgements and evidence hashes](expanded-results-2026-11-07.json).

## Coverage and grading

Evaluators received prompts, fixtures and the skill, without expected answers or assertions. They saved actual responses and recorded file reads, tool actions and source checks. The parent reviewed the responses against the assertions; the validator checks structure only and does not grade language.

| Cases | Coverage | Final evidence |
|---|---|---|
| 1–6 | Travel distance; OP readiness; NEC procurement; site start; crane traffic; telecom | Fresh verification; final 2/3/5 supersede intermediate checks |
| 7–8 | Wage defaults; overseas employment | Reviewed baselines; no relevant behaviour change |
| 9 | Injury reporting, access control and insurance | Two fresh final runs after an evidence omission |
| 10 | Occupational disease/OSHC | Reviewed baseline; no relevant behaviour change |
| 11 | Builders' lift | Two independent verification runs |
| 12 | Boiler and radiation plant | Reviewed baseline; no relevant behaviour change |
| 13–16 | Environmental controls, marine works, HFC/DG, transport/watercourse | Fresh regressions; final 16 supersedes an omitted road-opening check |
| 17–22 | Unknown OZP; lease conflict; wall removal; PC versus OP; night noise; restaurant licensing | New baselines and fresh verification; wall removal repeated independently |
| 23–28 | Conflicting exits; unavailable source; GFA; calculator limits; watercourse consent; archived sediment detail | New baselines and verification; 23/27 repeated independently; final 24/26 follow review fixes; final 28 honours no retrieval |

The 24 initial responses satisfy the **83 source-corrected assertions** applicable to them. This does not mean the original skill content was accurate: several subjects explicitly identified and rejected defective local guidance using official sources. The original rubric was preserved before correction rather than used to penalise accurate answers.

Two actual omissions appeared during verification and remain recorded:

- `verified-16.md`: **3/4** — omitted the explicit separate public-road excavation permission check. Added a conditional crossing/access-work check; `final-16.md` meets **4/4**, including the wholly private-route boundary.
- `repeat-9.md`: **3/4** — insurer notification was given without requesting insurance coverage records. Added that evidence distinction; `final-9-a.md` and `final-9-b.md` each meet **4/4**.

## Corrections made

| Finding | Correction and basis |
|---|---|
| Blanket travel distance and exit-width shortcuts | Replaced duplicated sprinkler-based travel tables with conditional B11 guidance; removed the generic 750 mm/50-person and width-formula shortcuts. Distinguish measurement endpoints, exit arrangements, individual and aggregate widths. [BD Fire Safety Code 2024, B11 and Table B2](https://www.bd.gov.hk/doc/en/resources/codes-and-references/code-and-design-manuals/fs_code2011.pdf). |
| OP forms treated as an approval chain | BA13 is new-building completion/OP application; BA12 temporary OP; BA14 non-new-building/street-work completion. Corrected templates, sequencing and programme milestone. [BD form list](https://www.bd.gov.hk/en/resources/forms/form_nbw.html). |
| DEVB weather treated as universally statistical | Read executed local amendments before choosing a weather trigger; separate target adjustment, eligible costs and final share. Removed unconditional route-level time/money conclusions. [DEVB NEC4 amendment library](https://www.devb.gov.hk/filemanager/en/content_1002/01_Library_of_Standard_Amendments_to_NEC4_ECC_9-5-2024_clean.pdf). |
| Pending consent/client risk acceptance could release excavation | Actual applicable permission and safety gates must be satisfied; concurrent application is not consent. [BD new-building process](https://www.bd.gov.hk/en/building-works/new-building-works/index.html). |
| Telecom detection optional on budget; invented blanket clearance | Require location/depth and competent-person detection evidence; distinguish protection/operator coordination from a universal OFCA permit. [OFCA guidance](https://www.ofca.gov.hk/en/industry_focus/infrastructures/ug_teles_lines_protection/index.html). |
| False wall-removal minor-works item | Removed duplicated item shortcuts, including the false 1.23/10%-wall claim; route to actual item catalogue and structural/fire assessment. [BD item 1.23](https://www.bd.gov.hk/en/building-works/minor-works/minor-works-items/index_mwcs_item1_23.html). |
| Universal night-CNP noise limit | Replaced blanket 75 dB(A) with applicable hours, activity, memorandum and permit conditions; distinguish percussive piling. [EPD guidance](https://www.epd.gov.hk/epd/noise_education/web/ENG_EPD_HTML/m3/ordinance_7.html). |
| New-building FSI sequence presented as general licensing | Distinguish FSI/501 inspection application, FSI/501a completion certificate and actual acceptance; restaurant licensing uses its own requirements. [FSD acceptance forms](https://www.hkfsd.gov.hk/eng/fire_protection/offa/), [FSD food-premises requirements](https://www.hkfsd.gov.hk/eng/fire_protection/licensing/premises_food.html). |
| Sediment summary contradicted its detailed table | Preserve the dated Category M biological-pass/Type 1 dedicated-site distinction; do not infer current allocation or permit. [BD PNAP ADV-21](https://www.bd.gov.hk/doc/en/resources/codes-and-references/practice-notes-and-circular-letters/pnap/ADV/ADV021.pdf). |
| Missing dimensions returned calculator “Pass” | Reject missing/nonpositive/nonfinite geometry. No sprinkler-derived limit; optional caller benchmark gives a geometric comparison only. The regression suite failed before the fix (11 failing subtests and one error); all six test methods pass afterwards. |

## Evaluation quality and review

- Added `validate-evals.cjs` for unique IDs/slugs, required fields, assertions and fixture existence, and `test_calculators.py` for executable boundary regressions.
- Corrected source-defective expected behaviour in cases 1/2/4/6 and strengthened cases 3/4/6 to catch weather, commencement and detection mistakes. Original IDs and prompts remain unchanged. The original JSON snapshot is retained locally.
- Independent final review accepted the calculator correction and identified the remaining exit-width shortcut and answer-leading fixture instruction. Both were fixed; fresh 24/26, a 40-occupant width boundary and an FSI/501 restaurant boundary were evaluated. No further code changes were needed after those checks.
- Case 24 remains explicitly synthetic. Removing its imperative improves the fixture, but it tests fiction recognition and refusal to invent verification, not retrieval of a real archived law.
- Early case 28 runs used the harness's general web-verification instruction, despite the prompt saying “without further checking.” Those observations cannot demonstrate compliance with that constraint; `final-28.md` honours the restriction and leaves current details unverified. This is a harness limitation, not concealed evidence of a pass.

## Validation and compatibility

Six calculator test methods pass; schema validation reports **28 cases / 100 assertions**, all fixtures present. Skill Creator `quick_validate.py` passes. Changed Markdown local links and `git diff --check` pass. Structural checks are separate from behavioural grading.

**Intentional API change:** `egress_1004_7` requires positive finite length and width. Without `distance_limit`, it returns `limit: null` and `status: "Not assessed"`; with a valid caller benchmark it reports `Within supplied limit` or `Exceeds supplied limit`. It no longer returns statutory-looking Pass/Fail or derives 45/30 from `sprinklered`. Existing callers relying on those old outputs must adapt. GFA aggregation remains unchanged and was exercised through `main.py`.

## Evidence and limits

Local artifacts are in `hk-architect-master-workspace/expanded-2026-11-07/`: `baseline-*`, `verified-*`, `repeat-*`, `final-*`, boundary responses, `source-audit.md`, `final-review.md`, `progress.md`, and `original-evals.json`. They are intentionally retained in the ignored workspace. The assertion record includes hashes of the exact reviewed final evidence.

Cases were grouped per evaluator, so some shared context; independent repeat runs use separate workers. Artifacts contain actual answers and recorded tool/read evidence, not complete immutable tool transcripts. Some official-source checks used indexed extracts after failed PDF retrieval; artifacts disclose this. This is bounded evaluation evidence, not a statistical reliability estimate or a comprehensive legal audit of every remaining topic/table.

No commit, push or deployment was performed. Unrelated pre-existing working-tree changes were preserved. Work stayed in the existing workspace to extend the earlier uncommitted fixes; the plan's evidence-retention requirement took precedence over deleting its workspace.
