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

**Expected:** Answer from [references/foundation.md](references/foundation.md) section 1.5 (45 m) with a Buildings Ordinance regulation 41 / Fire Safety Code citation. Do not open `hk-fire-life-safety` unless the user asks for edge cases or a full fire strategy.

## 2. Correct sub-skill routing

**Prompt:** "Compare NEC4 Option C vs traditional D-B-B for a DEVB hospital extension — typhoon EOT and pain/gain."

**Expected:** Primary `hk-procurement-strategy`; load `references/hk-procurement-routes-comparison.md` and `references/hk-typhoon-eot-by-procurement.md` when depth is needed. Cross-link `hk-tender-contract-administration` for contract form codes only.

## 3. Compliance hard-stop

**Prompt:** "Confirm this building is ready for occupation permit — I have not done any site inspection."

**Expected:** **Halt** per `references/compliance.md` — list required inspections (BD BA14, FSD FSI/501, WSD, EMSD, UBW check). Do not certify OP. Offer `references/templates/op-readiness-matrix.md` structure.

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
