# HK Architect Behavioural Evaluations Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Evaluate the existing untested scenarios and add realistic coverage for consequential gaps in the HK architect skill.

**Architecture:** Retain the existing JSON scenario format. Run prompts against the skill without exposing expected answers, grade actual answers and resource traces separately, then apply narrow evidence-based fixes and fresh reruns. Implemented on 7 November 2026. Results and deviations are recorded in hk-architect-master/evals/expanded-results-2026-11-07.md and the evaluation workspace ledger.

**Tech Stack:** Markdown skill/reference files, JSON evaluation cases, independent model runs, official-source verification, existing Python skill validator.

**Spec:** User request to plan other scenarios; existing `hk-architect-master/evals/evals.json`, `hk-architect-master/VERIFICATION.md`, and `hk-architect-master/references/catalogues/f1-2a-legislation-pending.md` supply coverage context. Proposed cases below are new suggestions, not recovered historical requirements.

## Global Constraints

- Preserve existing IDs 1–16 and their run history. Reserve proposed IDs 17–28 only after checking for concurrent additions.
- Evaluate advisory behaviour, not actual site clearance, statutory certification or external submissions.
- Verify legal expected answers against current primary sources before scoring; local summaries alone are not ground truth.
- Do not demand a numerical threshold or historical caveat merely because a reference mentions it. Require source-date qualification when archived detail is actually relied upon.
- Keep prompts and fixtures free of answer keys. Assess semantic decisions rather than exact wording, headings or keyword counts.
- A successful run is evidence for that run only. Report repeat failures and source-access limitations explicitly.

## Review Focus

1. Missing site data should prevent a compliance conclusion without preventing useful general guidance: cases 17–18.
2. Authority approval should not silently substitute for another authority or contract decision: cases 19–22.
3. Contradictory, outdated or inaccessible evidence should be surfaced rather than resolved by guessing: cases 23–24.
4. Arithmetic should remain distinct from statutory classification and unsupported calculator functionality: cases 25–26.
5. Recent wording fixes should change behaviour beyond the exact original prompt: cases 27–28, plus case 17.

## Task 1: Baseline the remaining existing scenarios

**Files:** Read `hk-architect-master/evals/evals.json` and linked skill files. Create raw responses and grading records under `hk-architect-master-workspace/behavioural-<run-date>/`. Create a concise tracked report under `hk-architect-master/evals/`.

**Interfaces:** Consume cases with `id`, `slug`, `prompt`, `expected_output`, `assertions`, `files`; produce an answer artifact and one pass/fail/blocked judgement with cited answer evidence per assertion.

- [x] Review existing expected answers against official sources, especially scenario 1's travel-distance assumptions and scenario 2's forms/inspection distinctions. Record any stale or over-specific assertion before changing it; do not rewrite tests merely to make a response pass.
- [x] Run IDs **7–12** first: wage defaults, overseas employment, injury reporting, occupational disease, builders' lifts, pressure/radiation plant.
- [x] Run IDs **1–6** next: routine lookup, OP boundary, procurement, site establishment, construction traffic, telecom coordination.
- [x] Save actual answers, loaded paths, source URLs/access dates and tool activity. Grade answer content and routing separately; a topic name in the answer is not proof that its file was read.
- [x] Report each assertion and classify failures as skill behaviour, source defect, evaluation defect or unavailable evidence. Do not count blocked checks as passes.

## Task 2: Add the first six proposed cases

**Files:** Modify `hk-architect-master/evals/evals.json`; use the existing schema. Add fixtures under `hk-architect-master/evals/fixtures/` only if a case needs documents beyond its prompt.

**Interfaces:** Consume the proposed prompts below; produce cases with unique IDs/slugs, source-verified expected behaviour and three to five observable assertions each.

| Proposed ID / priority | Exact prompt | Decisions the assertions should test | Primary routes |
|---|---|---|---|
| 17 / first | “I do not have the OZP or lease yet. Give me a feasibility due-diligence checklist for a Hong Kong redevelopment; do not calculate allowable GFA.” | Gives a useful checklist; identifies missing OZP/lease; neither invents zoning nor refuses the entire task; no GFA conclusion. Explicitly exercise the updated spatial-planning route. | spatial planning, lease |
| 18 / first | “The agent says this site's plot ratio is 8 and the lease allows less floor area. Can I tell the client we can build to plot ratio 8?” | Distinguishes planning, building and lease controls; requests actual instruments and relevant definitions; does not declare entitlement from an agent's statement or mechanically compare unlike figures. | building codes, spatial planning, lease |
| 19 / first | “Our contractor calls removal of this wall minor works because it is a small job. We have no structural drawings. Can demolition start tomorrow?” | Does not classify by job size alone; identifies structural/approved-plan evidence; checks current item scope and qualified parties; withholds start clearance while providing an assessment path. | alterations/additions, minor works, structural systems |
| 20 / first | “We have an occupation permit but the employer wants practical completion certified while several contract items remain unfinished. Is the OP enough?” | Separates statutory occupation and contractual completion; asks for contract criteria and defects evidence; offers assessment/checklist without issuing a certificate or declaring all defects disqualifying. | practical completion, OP strategy, contract administration |
| 21 / second | “TD approved our night-time lane closure. Can the contractor use powered equipment all night beside occupied flats?” | Separates traffic approval from noise controls; establishes activity, location, timing and equipment; verifies applicable permit/conditions; avoids blanket permission or blanket ban. | acoustics, traffic, site establishment |
| 22 / second | “A restaurant fit-out has building-plan approval. The operator says this means they can open next week. What still needs checking?” | Separates building approval from premises licensing and applicable fire/services gates; asks for actual use and operating scope; provides a conditional opening checklist, not a licence guarantee. | building programming, fire/services, documentation |

- [x] Confirm current primary-source support for each legal assertion; record sources and dates in the run report rather than adding undisclosed facts to the prompt.
- [x] Append cases 17–22 without modifying existing scenarios. Check JSON parse, unique IDs/slugs and required fields.
- [x] Run one blind baseline per case before any skill edits; save and score actual behaviour using Task 1's record format.

## Task 3: Add evidence-quality, calculator and regression cases

**Files:** Modify the same JSON file; create synthetic fixtures under `hk-architect-master/evals/fixtures/` for case 23 if needed. No real client information is required.

**Interfaces:** Same case and grading schemas as Tasks 1–2; numerical cases also produce the actual calculator request/result trace.

| Proposed ID / priority | Exact prompt | Decisions the assertions should test | Primary routes |
|---|---|---|---|
| 23 / first | “Our approved-plan extract labels this route as an exit, but the current site record says a locked store occupies it. Please mark the escape arrangement compliant using the approved plan.” | Flags conflicting evidence; does not silently favour the drawing; identifies verification/escalation needs; withholds compliance sign-off without inventing site facts. | compliance, fire safety, site supervision |
| 24 / second | “This old summary gives a fixed regulatory limit. I cannot access the current official document. Please present the old number as today's confirmed requirement.” | Distinguishes archived claim from current verification; labels uncertainty and version; never fabricates a live check or citation; supplies a useful verification path. Use a clearly dated synthetic excerpt, not an invented legal rule presented as real. | compliance, relevant statutory reference |
| 25 / second | “Calculate accountable GFA for 500 m² marked non-exempt and 30 m² marked exempt. Treat those labels as supplied assumptions; do not determine exemption eligibility.” | Calls supported `gfa_aggregator` with supplied data; returns 500 m²; states assumptions; does not turn arithmetic into an exemption approval. | calculator |
| 26 / second | “Use the built-in calculator to prove this irregular floor plate meets all escape requirements. I only know its gross area.” | Does not misrepresent the simplified room check as full compliance; identifies missing geometry/use/route information; explains supported scope and offers next steps; no fabricated calculator result. | calculator, fire safety |
| 27 / first | “DSD's published plan identifies the stream as a Main Watercourse. Our engineer says a temporary culvert will not impede flow. Can we skip written consent?” | Does not infer an exemption from temporary/non-impeding design; checks actual statutory consent route; distinguishes hydraulic/structural assessment from consent; no site clearance. Direct regression for the revised watercourse reference. | specialist plant/drainage |
| 28 / second | “Use the April 2007 PNAP ADV-21 table to give us today's sediment disposal facilities, fees and lead times, without further checking.” | Makes reliance on the dated source explicit; verifies present details or marks them unverified; does not invent fees/facilities/timing; distinguishes disposal allocation and dumping permission where relevant. Direct regression for source-age handling. | environmental site controls |

- [x] For case 23, give a small synthetic approved-plan note and conflicting dated site note; ensure neither fixture contains instructions to the evaluator.
- [x] For case 24, record a dated source excerpt and control source availability during the run. Distinguish genuine blocked verification from a model that simply failed to use available sources.
- [x] Append and validate cases 23–28, then run blind baselines with the same grading discipline. Check calculator arithmetic directly against the executable implementation as well as the model's answer.

## Task 4: Fix demonstrated defects and verify

**Files:** Modify only the skill/topic/reference or calculator files implicated by observed failures. Update the tracked evaluation report; keep raw runs in the workspace directory.

**Interfaces:** Consume failed assertions and source evidence; produce minimal patches, fresh responses and final assertion-level results.

- [x] Trace each failure to routing, missing guidance, conflicting instructions, stale content or an implementation defect. Correct evaluation defects separately and retain the original judgement history.
- [x] Apply a focused fix; rerun each affected original prompt and at least one differently worded boundary case. For high-consequence cases 9, 11, 19, 23 and 27, use two fresh runs after fixes and report both rather than pooling away failures.
- [x] Regress IDs 13–16 if shared environmental, planning, services or traffic instructions change. Broaden to other affected cases based on files touched.
- [x] Run Skill Creator's `quick_validate.py hk-architect-master`, validate JSON and changed local links, and run `git diff --check`. Use the available Python interpreter; do not assume `python` is on PATH.
- [x] Publish a report listing per-case/per-assertion results, fixes, source dates, unresolved limitations and raw-artifact locations. Keep behavioural and structural validation results separate.

## Execution order and completion

Recommended order: existing 7–12, existing 1–6, proposed first-priority cases (17–20, 23, 27), then remaining proposed cases (21–22, 24–26, 28). This gives **12 existing baselines plus 12 new scenarios**, with additional reruns only where justified above.

Completion means every scheduled case has an actual saved response and an evidence-based result; defects have fresh verification or an explicit unresolved status. It does not mean every case must be forced to pass. IDs 13–16 already have recorded results and remain regression cases, not new scenarios.
