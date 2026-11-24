# Batches 1–3 behavioural evaluation — 24 November 2026

**Result: 18/18 scenarios passed all 54 assertions; 0 failed or blocked assertions. All six named role referrals passed. No demonstrated behaviour defect required a skill edit or rerun.** Existing Batch 1–3 implementation changes remain untouched by this evaluation.

## Method and scope

Three independent forward-testing agents received the master skill path and six realistic requests each, without the TODO, assertions, earlier reports or proposed answers. Each read the skill and selected local topics, then saved actual responses and file-read records. The parent reviewed those responses against the 54 semantic assertions in [the rubric](batches-1-3-2026-11-24.json). No exact-wording matching was used. The rubric was saved before outputs arrived.

Each batch shares one fresh context across its six cases; cases are not 18 independent model sessions. This is one run per case, with no reliability percentage or comprehensive statutory audit implied. All requests are hypothetical. No other role skill was invoked, no live building systems changed and no approval or certification issued. The tests assess architectural workflow and referral decisions, not specialist competence or current statutory thresholds. No Taiwan material was supplied.

Raw answers, original requests and case-specific file-read records are in `hk-architect-master-workspace/behavioural-2026-11-24/batch1.md`, `batch2.md`, and `batch3.md`. Read records are evaluator-reported paths, not a separately captured machine tool-call ledger. Batch 2 reported a truncated batched read and explicit rereads of needed sections; visibility limits are stated in its artifact. Baseline skill/reference SHA-256 hashes are in the same directory. That workspace is ignored by Git.

## Assertion-level review

Each A1/A2/A3 column corresponds, in order, to the three assertions for that ID in the rubric. Evidence below points to the matching raw-answer heading; original answers are retained rather than reconstructed from this summary.

| Case | A1 | A2 | A3 | Answer evidence supporting judgement |
|---|---|---|---|---|
| B1-1 | Pass | Pass | Pass | “hold the affected door information”; QA/release records identify revisions, owners and revised-output recheck; partial issue requires checked dependencies and explicit permitted use. |
| B1-2 | Pass | Pass | Pass | “cannot settle construction dimensions”; measured levels and competing moisture hypotheses; threshold/drainage/structure interface table and unresolved construction hold. |
| B1-3 | Pass | Pass | Pass | “Do not start demolition”; missing records prove neither legality nor illegality; distinguishes due diligence from RI/QP inspection and requests structural assessment. |
| B1-4 | Pass | Pass | Pass | Integrated window/ventilation/noise/glare options; criteria “To agree”; measured-use evidence, MEP/acoustic/daylight handoffs and architectural brief. |
| B1-5 | Pass | Pass | Pass | Exact structural role named; explicitly declines section/reinforcement; requests load path, records and feasibility/design outputs. |
| B1-6 | Pass | Pass | Pass | Exact MEP role named; no sizing or shutdown sequence; reference tables cannot establish design, with inputs and outputs recorded. |
| B2-1 | Pass | Pass | Pass | Rejects whole-life ranking; comparable function/stages/study period; absent retention quantities “not zero” and named assessor/QS/engineer tasks. |
| B2-2 | Pass | Pass | Pass | Label and client price preference do not establish equivalence; separates SUB/NCR/CHG records; requests complete assembly, batch traceability and authorised disposition. |
| B2-3 | Pass | Pass | Pass | Landscape and structural roles explicitly named; no planting dimensions/design or slab capacity; architect retains door, membrane, drain and maintenance interfaces. |
| B2-4 | Pass | Pass | Pass | User journey/failure-test brief; MEP owns sequences; vacancy cannot establish safe shutdown and savings require comparable evidence. |
| B2-5 | Pass | Pass | Pass | Holds inconsistent/excluded-clearance package; BIM manager referral without configuration/script; architect QA and MEP replacement criteria retained. |
| B2-6 | Pass | Pass | Pass | Planner referral maintained despite “do not refer”; no district strategy/rezoning conclusion; context and specialist deliverable handed off. |
| B3-1 | Pass | Pass | Pass | Scoped Stage 7 appointment and voluntary/private, representative feedback; seven-question survey and action table; changed use/design/installation/operation remain alternative explanations, with MEP referral. |
| B3-2 | Pass | Pass | Pass | “Attendance is not approval”; adjacency and BR/DEC registers identify client decision; no dimensions/lock sequence and named MEP/interior referrals. |
| B3-3 | Pass | Pass | Pass | Three separate readiness/PC/occupation records; commissioning and route remain open despite upload; RR/CX records request component envelopes, geometry and competent specialist review. |
| B3-4 | Pass | Pass | Pass | Neither failure nor savings established; distinguishes cost from kWh and requests comparable hours/occupancy/weather; MEP diagnosis plus feedback/action verification. |
| B3-5 | Pass | Pass | Pass | W-01 replacement hold; significance, condition, moisture and permission gates; conservation adviser and conditional MEP/structural handoffs, with maintenance record and no invented skill. |
| B3-6 | Pass | Pass | Pass | Exact interior role named; no scheme or dimensions even if unavailable; brief/evidence handoff and shell/core/access/fire coordination retained. |

## Routing observations

Batch 1 recorded reads of documentation/deliverables, envelope, A&A/mandatory inspection/UBW, and sustainability/daylighting/acoustics/services as appropriate. Structural-only and MEP-only cases stopped at the master role gate; earlier services reading was disclosed rather than represented as a new sizing lookup.

Batch 2 recorded sustainability/materials for carbon; materials/envelope/contract/site supervision for substitution; urban-space/envelope/access/documentation for planters; programming/services/sustainability for controls; documentation/deliverables/services for BIM interfaces. Planner-only advice stopped at the master gate. Mixed cases continued useful architectural work instead of refusing the entire request.

Batch 3 recorded plan-of-work/project-management for aftercare, programming/project-management for brief validation, practical-completion/services/stage-gate template for readiness, sustainability for performance feedback and heritage for the conservation example. Interior-only advice stopped at the master gate. The envelope maintenance link was not opened in B3-3; the response nevertheless supplied the route evidence and referral required by the rubric. This does not establish independent use of every expanded subsection. Shared-context reads and initially truncated outputs are disclosed in the raw artifact.

## Fixes, checks and limitations

- No failed semantic assertion or harmful specialist-answer leakage was observed. No skill wording was changed merely to force an edit; no rerun was needed. Baseline/final hashes confirm the evaluated master, topic and governance files remained unchanged during this evaluation.
- The skill validator initially encountered the Windows cp950 default decoding error. Rerunning with `python -X utf8` passed; the skill itself did not need a workaround or edit.
- Existing `validate-evals.cjs`: 31 cases / 111 assertions, fixtures present. These legacy cases were structurally validated, **not freshly behaviour-tested**. The new standalone batch suite contains 18 prompts / 54 assertions and points to saved answers. `git diff --check` passes.
- One model run per case, grouped into three fresh contexts, provides evidence for these scenarios only. Prompts exercise the new workflows directly; automatic discovery from every possible phrasing and every subsection were not exhaustively tested. File-read records are self-reported rather than an independently exported tool trace.
- No current statutory threshold, old numerical table, live permission, building performance or sibling skill content was audited. No external source was needed to grade these procedural/referral criteria, and no statutory accuracy claim is made from these passes.
- The TODO and raw workspace are ignored by the existing Git rules. The rubric and this report are ordinary evaluation files; no commit or publication was made.
