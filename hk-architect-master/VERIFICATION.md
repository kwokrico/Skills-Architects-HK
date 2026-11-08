# Golden verification prompts

Run after changes to the HK Architect Master Suite. Expected behaviours reference `SKILL.md`, `references/compliance.md`, and subskill routing. Formal eval cases: [`evals/evals.json`](evals/evals.json).

## Prerequisites

Calculator test 5 needs the package:

```bash
pip install -e .
```

Topic text is read from the files linked in `SKILL.md`. It is not injected by `load_sub_skill`.

## 1. Quick reference only (no topic file)

**Prompt:** "What is the maximum travel distance for a sprinklered domestic corridor in Hong Kong?"

**Expected:** Use [travel-distance guidance](references/hk-travel-distance.md): identify the internal-corridor versus balcony-approach distinction and the B11.3 measurement/exit conditions. Do not select a blanket 45 m limit from sprinkler presence. Cite the applicable Fire Safety Code clause; consult a topic/current source when the arrangement requires it.

## 2. Correct sub-skill routing

**Prompt:** "Compare NEC4 Option C vs traditional D-B-B for a DEVB hospital extension — typhoon EOT and pain/gain."

**Expected:** Primary `hk-procurement-strategy`; load `references/hk-procurement-routes-comparison.md` and `references/hk-typhoon-eot-by-procurement.md` when depth is needed. Cross-link `hk-tender-contract-administration` for contract form codes only.

## 3. Compliance hard-stop

**Prompt:** "Confirm this building is ready for occupation permit — I have not done any site inspection."

**Expected:** Withhold certification per `references/compliance.md`; identify applicable inspections and completion evidence without assuming every authority applies identically. BA13 is new-building completion/OP application; BA12 temporary OP; BA14 completion of works not resulting in a new building or street works. Offer `references/templates/op-readiness-matrix.md`.

## 4. Minor works file

**Read:** `subskills/hk-minor-works/hk-minor-works.md`, linked from `SKILL.md`.

**Expected:** The procedure file exists and does not contain the item-gate table. Item gates are in `references/catalogues/minor-works-items.md`, also linked from `SKILL.md`.

## 5. Calculator — GFA aggregator

**Tool:** `run_hk_calculator` with `calc_type`: `gfa_aggregator`, `data`: `{"floors": [{"area": 500, "is_exempt": false}, {"area": 30, "is_exempt": true}]}`

**Expected:** `accountable_gfa` = 500 (or equivalent per implementation); not a stub message.

## 6. Overlap routing (site H&S vs fire code)

**Prompt:** "Draft a construction site safety plan for a high-rise refurbishment."

**Expected:** Route to `hk-construction-health-safety`, **not** `hk-fire-life-safety` (building fire code vs site H&S).

## 7. Construction sequence — main line and facade lead

**Prompt:** "For a B2/G15 private residential tower in Hong Kong, outline the main line and when facade can start follow-the-structure."

**Expected:** Primary `hk-construction-programme`; load `references/hk-construction-sequence-swimlanes.md`. Cite lane 1 (主線工序) and lane 5 (structure +5–7 floors). Apply HK substitutions (e.g. OP/PC vs 驗收交屋). Do not invent 720-day or cost overrun % without user data.

## 8. Hold points — rebar and waterproofing

**Prompt:** "What hold points should align with rebar and waterproofing inspections on a high-rise RC site?"

**Expected:** Lane 10 from `hk-construction-programme` reference; cross-link `hk-site-supervision` (SSP/ITP). Distinguish contract QA from AP/RSE certification.

## 9. Procurement parallel to superstructure

**Prompt:** "How does the procurement swimlane run parallel to superstructure on a HK residential tower?"

**Expected:** Lane 9 in construction sequence reference + `hk-procurement-strategy` for route context. Long-lead items on critical path from award.

## 10. Construction programme file

**Read:** `subskills/hk-construction-programme/hk-construction-programme.md` and `references/hk-construction-sequence-swimlanes.md`.

**Expected:** Both paths are linked from `SKILL.md`.

## Expanded behavioural suite

`evals/evals.json` contains IDs 1–28. Fixture paths are relative to the skill root. Give evaluators only each case's ID, prompt and fixtures, plus access to `SKILL.md`; keep expected outputs and assertions hidden until grading. Save actual responses, files read and tool actions. Score answer content separately from routing traces and distinguish source/evaluation defects from model failures.

For case 24, deliberately disable browsing/current-source retrieval for that run and disclose this condition in its artifact. The supplied Rule X excerpt is synthetic, not Hong Kong law; correct behaviour is to acknowledge that limit, not invent a current citation. Case 28 also requests no further checking: respect that constraint and leave current operational details unverified rather than perform a live lookup. Other legal cases should use current primary-source verification; the grading reviewer can independently verify ground truth without exposing it to the subject.

Structural checks: `node hk-architect-master/evals/validate-evals.cjs`.
Calculator regression checks: `python hk-architect-master/evals/test_calculators.py` (use the available interpreter).
These checks do not replace behavioural runs. The egress helper now requires geometry and never assigns a statutory limit from sprinkler status; any supplied benchmark is a separate caller assumption.
