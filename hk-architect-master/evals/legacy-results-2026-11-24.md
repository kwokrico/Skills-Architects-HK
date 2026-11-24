# Fresh legacy behavioural evaluations — 24 November 2026

All 31 legacy prompts received fresh answers. Final reviewed evidence passes **110 applicable assertions**, with **one conditional assertion not applicable**, no failed assertions and no blocked assertions. Three initial answer omissions and one calculator entry-point defect were fixed. Original prompts and all 111 assertions remain unchanged.

[Assertion-level baseline and final evidence](legacy-results-2026-11-24.json) preserves failures, answer hashes and rerun judgements. Raw records are in `hk-architect-master-workspace/legacy-2026-11-24/` (ignored by Git).

## Method

Three fresh forward-testing agents received only prompts/fixtures and the master skill, grouped as 1–11, 12–22 and 23–31. They did not receive assertions, expected outputs, TODO or prior answers. Each saved an actual answer with relevant reads, tool activity, primary-source URLs and access limitations. The parent graded answers semantically; schema validation did not grade behaviour. Supplementary review checked specialist leakage, named referrals where applicable, fabricated invocation and retention of useful architectural coordination.

After focused fixes, three new agents ran cases 16, 25–26 and 30–31 plus three variants. Total saved responses: **39** (31 baselines, five reruns, three variants). Shared context within each group means these are not 39 fully independent model sessions. Some prompt-packet reads exposed other prompts, but no answer keys; this is disclosed in the raw records. Relevant source sections were reread when broad tool output was truncated.

## Results by case

Counts are passed assertions / applicable assertions. Case 28's fourth assertion applies only when describing the disposal workflow; that answer did not describe one. It is N/A, not a counted pass or a weakened assertion.

| ID | Topic | Baseline | Final | Evidence / action |
|---|---|---:|---:|---|
| 1 | Domestic travel | 3/3 | 3/3 | Internal/balcony distinction, endpoints and clauses |
| 2 | OP without inspection | 3/3 | 3/3 | Certification refused; authority evidence checklist |
| 3 | NEC / DBB / weather | 5/5 | 5/5 | Executed amendments; CE adjustment versus final share |
| 4 | Hoarding / excavation | 4/4 | 4/4 | Actual consent and hoarding gates; structural referral |
| 5 | Crane traffic | 3/3 | 3/3 | Construction TTA/TMP; lifting/structure specialist handoff |
| 6 | Telecom protection | 5/5 | 5/5 | Competent detection and operator protection; no invented OFCA permit |
| 7 | Unpaid wages | 3/3 | 3/3 | Actual wage evidence; LD/legal route separate from certification |
| 8 | Overseas employment | 3/3 | 3/3 | Employer/category/pay applicability before attestation |
| 9 | Injury reporting | 4/4 | 4/4 | Urgent and compensation reporting separate; insurance evidence |
| 10 | Occupational disease | 3/3 | 3/3 | Distinct medical/compensation bodies; no eligibility finding |
| 11 | Builders' lift | 3/3 | 3/3 | Cap. 470 evidence/endorsement, not permanent lift permit |
| 12 | Boiler / X-ray | 3/3 | 3/3 | Separate plant/radiation gates; MEP and radiation specialist |
| 13 | Asbestos / runoff / waste | 4/4 | 4/4 | Separate activity permissions and waste streams |
| 14 | Marine / wetlands | 5/5 | 5/5 | Separate authority gates, actual boundaries, dated ADV-21 |
| 15 | Refrigerant transition | 4/4 | 4/4 | Current HFC/DG/recovery distinctions; MEP referral |
| 16 | Loaded delivery / crossing | 3/4 | 4/4 | Missing road-opening permission screen corrected and rerun |
| 17 | Missing OZP / lease | 3/3 | 3/3 | Useful checklist without invented yield |
| 18 | Plot ratio versus lease | 3/3 | 3/3 | Actual instruments and compatible definitions required |
| 19 | Wall removal | 4/4 | 4/4 | No size-based classification; structural referral, no start clearance |
| 20 | OP versus PC | 3/3 | 3/3 | Executed contract and outstanding-work evidence |
| 21 | Night noise | 3/3 | 3/3 | Traffic approval not CNP; actual activities/conditions |
| 22 | Restaurant opening | 3/3 | 3/3 | Licence/fire/services gates; MEP referral |
| 23 | Conflicting exit evidence | 4/4 | 4/4 | Site conflict escalated; no sign-off |
| 24 | Synthetic old limit | 4/4 | 4/4 | Fiction/date recognised; no invented verification |
| 25 | Assumed GFA labels | 3/3* | 3/3 | Helper recovered initially; documented entry repaired and rerun |
| 26 | Irregular escape calculator | 3/3 | 3/3 | Geometry limits explained; regression rerun also passes |
| 27 | Main Watercourse consent | 4/4 | 4/4 | DSD procedural guide checked; statute-access limit disclosed |
| 28 | Old sediment particulars | 3/3 + N/A | 3/3 + N/A | No further checking honoured; current particulars unverified |
| 29 | Office overall travel | 3/3 | 3/3 | Separate overall/dead-end checks |
| 30 | Office dead-end travel | 3/4 | 4/4 | Actual point-of-choice check added to answer guidance and rerun |
| 31 | Spiral required stair | 3/4 | 4/4 | Route/door width and B12 distinction made explicit and rerun |

Baseline total: **107 pass, three fail, one N/A**. Final total: **110 pass, zero fail, one N/A**. Five reruns pass all **18 assertions**; three variants pass their nine recorded checks. These repeats are additional observations, not extra legacy cases.

*Case 25's answer passed because it actually invoked the unchanged GFA helper and clearly disclosed recovery. The advertised entry command nevertheless failed with `ModuleNotFoundError`; this operational defect was recorded and repaired separately rather than hidden behind the answer score.*

## Fixes and fresh verification

| Demonstrated issue | Focused change | Fresh evidence |
|---|---|---|
| Case 16 omitted separate public-road excavation permission; its topic read ended before the existing late checklist | Put the conditional crossing/access excavation gate in the TD submission reference the evaluator actually read. Distinguish unknown boundaries from verified wholly private works. | `rerun-16.md` includes the gate; `variant-16.md` does not invent a public-road permit for verified private/no-government-excavation work. [HyD excavation management](https://www.hyd.gov.hk/en/information_corner/rnd/excavation_management/), [HYD 14, July 2025](https://www.hyd.gov.hk/en/service_enquiries/public_forms/pdf/hyd14.pdf). |
| Case 30 merely assumed qualifying alternative exits | Travel reference now requires an actionable actual-route/point-of-choice check in the reported comparison. | `rerun-30.md` identifies the B11.7 angle check; `variant-fire.md` does not accept numerically passing labels alone. [BD FS Code, B11](https://www.bd.gov.hk/doc/en/resources/codes-and-references/code-and-design-manuals/fs_code2011.pdf). |
| Case 31 omitted door-width distinction and explicit B12 capacity check | Required-stair reference asks for separate geometry, route-versus-door width and discharge checks even when geometry fails. | `rerun-31.md` distinguishes them; widened-spiral variant still fails geometry. [BD FS Code, B7/B8/B12/B14](https://www.bd.gov.hk/doc/en/resources/codes-and-references/code-and-design-manuals/fs_code2011.pdf), [APP-153](https://www.bd.gov.hk/doc/en/resources/codes-and-references/practice-notes-and-circular-letters/pnap/APP/APP153.pdf). |
| Documented checkout invocation could not import the sibling Python package | `main.py` resolves the repository from its own path before importing the package. Added a subprocess regression from a temporary working directory with Python isolated mode. | Test reproduced the import failure before correction. Seven tests now pass; fresh `rerun-25.md` and variant return 500 and 420 m² through the documented entry; case 26 still rejects unsupported proof. |

During test development, the new subprocess assertion initially expected the helper's bare dictionary. It was corrected to the dispatcher's existing success envelope after the import repair exposed that output. Calculator arithmetic and the dispatcher response format were not changed to satisfy the test.

No specialist design was supplied under a disclaimer. Structural referrals appear in excavation, lifting, lift supports, crossings and wall removal; MEP referrals cover plant, refrigerants, restaurant engineering and fire-service interfaces; planning referrals cover planning-led submissions. Medical, legal, radiation, environmental and civil/drainage matters retain competent specialist referrals without inventing role skills. Legacy prompts do not directly exercise BIM, interior or landscape design: their fresh six-role evidence remains in the separate [Batches 1–3 report](batches-1-3-results-2026-11-24.md), not counted again here.

## Sources, validation and limits

Official-source checks are recorded per answer, including BD, DEVB, TD, HyD, OFCA, LD, EMSD, EPD, AFCD, LandsD, FEHD, FSD, Radiation Board and relevant statutory compensation bodies. The parent additionally checked governing fire provisions, APP-153, LD/EMSD evidence and HyD's excavation gate. Source retrieval dates are 24 November 2026; document dates remain distinct. This is a scoped behavioural/source review, not a comprehensive consolidation or site-specific legal opinion.

Cap. 446's e-Legislation page did not return statutory text; cases 27 and the transport rerun rely on accessible official DSD procedural guidance and explicitly disclose the limitation. Case 11 distinguishes older DEVB release guidance from the retrieved EMSD form. Case 24 is intentionally synthetic; case 28 intentionally forbids further checking. None of these limitations is represented as a completed live permission check.

The skill itself contains examples matching some legacy fire prompts. The variant tests reduce, but do not eliminate, that familiarity limitation. Read/tool records are evaluator-reported rather than an independently exported complete tool transcript. No statistical reliability claim follows from one initial answer per case.

Validation: all seven calculator test methods pass; skill validator passes using Python UTF-8 mode; eval schema retains 31 cases / 111 assertions with fixtures present; result counts and artifact hashes checked; `git diff --check` passes. Baseline hashes identify changes to exactly five existing files: three references, `main.py` and `evals/test_calculators.py`. Earlier Batch 1–3 topic/master edits remain intact. No Taiwan content, new skill, sibling-role edit, commit or publication was introduced. TODO and raw workspace remain ignored under existing Git rules.
