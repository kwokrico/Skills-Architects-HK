# Behavioural evaluation — 7 November 2026

Scope: the four newest scenarios, IDs 13–16 in `evals.json`. Independent agents answered the prompts using the skill and official web sources, without seeing expected outputs or assertions. The parent reviewer read the actual responses and graded each existing assertion. A fresh agent repeated all four after the fixes without seeing baseline artifacts. These are qualitative model runs, not deterministic tests or a statistical reliability estimate.

| Scenario | Baseline | Fresh rerun | Evidence in rerun |
|---|---:|---:|---|
| 13 — asbestos, runoff and waste | 4/4 | 4/4 | Separate EIA/air/waste/discharge gates; muddy water not exempt; asbestos separated from inert fill with disposal records; contract-specific account. |
| 14 — marine/wetland mobilisation | 4/5 | 5/5 | Separate foreshore/navigation/dumping gates; allocation not a permit; activity-specific marine-park restrictions; actual Ramsar/WCA/WBA boundaries and local controls; explicit April 2007 ADV-21 caveat. |
| 15 — HFC/dangerous goods | 4/4 | 4/4 | December 2025 controls; rejects historical Category 5 exemption; substance/inventory and Cap. 51 authority boundary; approved recovery equipment and separate safety assessment. |
| 16 — road load/watercourse | 4/4 | 4/4 | TMP/TD 298 insufficient; TD 290 and route/load conditions; designation and independent DSD consent; separate road-opening permission. |
| **Total** | **16/17** | **17/17** | **All four scenarios pass on rerun.** |

## Findings and fixes

1. The baseline marine answer omitted the required historical-source caveat. It cited current EPD/CEDD guidance and did not present old numerical tables as current, so this was an assertion omission rather than demonstrated reliance on obsolete limits. The environmental reference now expressly carries the April 2007 caveat into answers presenting its sediment workflow.
2. The watercourse reference could imply that consent applies only to works impeding flow. Revised it to reflect [DSD's consent guidance](https://www.dsd.gov.hk/EN/Flood_Prevention/Land_Use_Management_and_Legislation/A_Guide_to_Land_Drainage_Ordinance/index.html): structures, engineering, filling and repair works within Main Watercourses require the applicable consent; temporary or allegedly non-impeding works are not assumed exempt. The rerun explicitly preserves this distinction.
3. Spatial planning's unconditional halt for an unknown OZP conflicted with providing a useful general approvals checklist. Scoped the halt to site-specific conclusions while preserving the prohibition on assumed zoning defaults. This was an observed instruction ambiguity, not a failed baseline assertion. The rerun gave a qualified marine checklist but did not load the spatial-planning file, so this wording change was inspected rather than behaviourally exercised in that run.

No expected outputs or assertions were weakened. Bulk HFC versus precharged equipment remains a project-specific applicability question; both runs correctly requested that distinction rather than assuming the same treatment.

## Artifacts and validation

Actual responses, source links and files read are retained locally in the ignored workspace directory `hk-architect-master-workspace/behavioural-2026-11-07/`, named `baseline-13.md` through `baseline-16.md` and `rerun-13.md` through `rerun-16.md`.

Skill Creator's `quick_validate.py` passed after the edits. `git diff --check` passed. Unrelated pre-existing working-tree changes were left intact. Scenarios 1–12 were not run in this evaluation.
