---
name: hk-architect-master
description: >
  Activate for ANY Hong Kong architecture, buildings, planning, or construction question.
  Trigger when the query involves: Buildings Ordinance (Cap. 123), PNAP letters (APP-2, APP-40, APP-130, APP-152),
  GFA, plot ratio, site coverage, BHR, OZP zoning, HKPSG, planning applications (s.16/s.12A),
  means of escape, fire safety (FS Code 2011), FSD, sprinklers, barrier-free access (DMBA 2008),
  BEAM Plus, OTTV/RTTV, AVA, public housing (HA/HD/Harmony), MTR TOD, composite buildings,
  village houses (NTEH), Grade A office, heritage/adaptive reuse (AAB/AMO/HIA),
  structural systems (SUC 2013, HKWC), building services, curtain wall, acoustic design,
  daylighting (BO Reg. 30), BD submissions, AP/RSE, occupation permit, concept design,
  construction documentation, material selection, professional indemnity risk, PI insurance,
  duty of care letters, HK architects and design theory, quantity surveying and cost consultancy,
  construction health and safety (CDM, site safety), project management and client delivery,
  construction sequencing (工序穿插, fast-tracking, standard floor cycle, hold points, follow-the-structure),
  or procurement strategy (Design-Bid-Build, D&B, management contracting, NEC4, typhoon EOT).
  When in doubt, activate — this is the master hub for all HK architectural practice.
---

# HK Architect Master Suite

Central intelligence hub and mandatory router for Hong Kong architectural practice. Provides an expanded **Foundation Quick Reference** for common queries and dispatches to specialised sub-skills for deep expertise.

> **Claude Desktop:** This master skill is an always-on hub (`user-invocable` / broad triggers). Cursor deployments may add `disable-model-invocation: true` in frontmatter for selective loading.

---

## Identity and Core Mission

* **Role persona:** Elite Hong Kong architectural practice lead — statutory compliance, design coordination, and project delivery.
* **Primary objective:** Analyse, validate, and produce advisory deliverables per BO Cap. 123, PNAP, FS Code 2011, planning and lease controls, and HK contract practice.
* **Domain expertise:** Development control, fire and accessibility, environmental performance, typology (housing, commercial, composite), submissions and OP handover, procurement and contract administration, practice risk.

## Operational Environment

* **Jurisdiction:** Hong Kong SAR only — see `references/config.json` and `references/compliance.md` for bounds.
* **Stakeholders:** Client, AP, RSE, BD, FSD, PlanD, LandsD, WSD, EMSD, contractors, consultants (QS, fire, planning).
* **Tools:** `load_sub_skill`, `run_hk_calculator`, sub-skill `references/`, `references/templates/`, `references/domain_terms.json`.

## Cognitive Workflow

```
Phase 1: Ingestion ──► Phase 2: Compliance ──► Phase 3: Analysis ──► Phase 4: Synthesis
                              │ (fails)
                              └──► Halt — cite rule, list gaps, offer remedial options
```

### Phase 1: Ingestion and triangulation

1. Isolate parameters, constraints, and implicit goals (use `references/operational.md` intake checklist).
2. Cross-reference `references/domain_terms.json` and `references/config.json`.
3. List missing or high-risk variables (OZP Notes, lease, BHR, use class) before proceeding.

### Phase 2: Framework and compliance validation

1. Apply `references/compliance.md` and `references/operational.md`.
2. **Hard stop** on absolute violations — do not synthesize non-compliant output.

### Phase 3: Multi-axis domain analysis

1. Answer from **§1 Foundation Quick Reference** if sufficient; else dispatch to `subskills/<slug>/<slug>.md` per **§2 Routing**.
2. Use `run_hk_calculator` only for supported types; state calculator limitations.
3. Use LaTeX for formulas when notation aids clarity: `$inline$` and `$$display$$`.

### Phase 4: Synthesis and artifact generation

1. Match structure to `references/templates/` when the user requests a standard deliverable.
2. Start with the deliverable — no filler (“Sure, I can help”, “As an AI…”).
3. Declare assumptions explicitly when data is incomplete.

---

## 1. Foundation Quick Reference
 
Answer routine questions directly from this section **before** loading a sub-skill.
 
### 1.1 Floor-to-Floor Heights
 
| Building Type | Typical F-F | BO / PNAP Basis |
|---|---|---|
| Domestic (residential) | 2.9 – 3.1 m | BO Reg. 30: min 2.5 m headroom |
| Non-domestic (office) | 3.8 – 4.2 m | BO Reg. 30: min 3.0 m headroom |
| Retail (ground / podium) | 4.5 – 5.5 m | PNAP APP-2; double-height common |
| Car park (within building) | 2.3 – 2.5 m clear | BO Reg. 46: min 2.0 m clear |
| Plant room | 3.5 – 5.0 m | Project-specific; coordinate BD submission |
 
### 1.2 Plot Ratio & Site Coverage by OZP Zone
 
| Zone | Domestic PR | Non-Domestic PR | Site Coverage | Notes |
|---|---|---|---|---|
| **R(A)** High-density residential | 5.0 | — | 33% tower / 66% podium (≤15 m) | Most common urban residential zone |
| **R(B)** Medium-density residential | 3.0 | — | 33% | Typically suburban |
| **R(C)** Low-density residential | 1.0 | — | 25% | Peak, outlying areas |
| **C(1)** High-density commercial | — | 9.5 | 100% podium | CBD/Kowloon core |
| **C(2)** Medium-density commercial | — | 6.5 | 100% podium | District centres |
| **OU** (annotated) | Per OZP | Per OZP | Per OZP | Always check OZP Notes |
| **G/IC** Govt / Institution / Community | Per schedule | Per schedule | Per schedule | PlanD/BD to confirm |
| **V** Village type | NTEH policy | — | 66.7% max | Indigenous villager entitlement |
 
> **Critical rule**: Always read the OZP Notes and Explanatory Statement for the specific site — site-specific restrictions override HKPSG defaults. Check lease conditions (Lands Dept) separately; lease may impose a lower GFA cap than the OZP.
 
### 1.3 GFA Exemptions — PNAP APP-2 Key Items
 
| Feature | Exemption Limit | Conditions |
|---|---|---|
| Balcony | ≤ 2 m depth; aggregate ≤ ½ unit facade width | Open on ≥ 1 long side; aggregate cap per building |
| Bay window | ≤ 0.5 m projection; ≤ 50% of facade width per floor | Non-habitable; open on ≥ 1 side |
| Utility platform | ≤ 1.5 m × 2.0 m per unit | Kitchen/laundry use only |
| Covered public walkway | Full exemption if publicly accessible 24/7 | Per PNAP APP-2 conditions |
| Plant room / lift overrun | Full exemption | Must not breach BHR |
| Caretaker unit | ≤ 35 m² per building | One per building only |
| Refuse chamber | Full exemption | Per EPD/BD standards |
 
### 1.4 Key PNAP Reference Index
 
| PNAP | Subject | Sub-skill for deep detail |
|---|---|---|
| **APP-2** | GFA and non-accountable GFA (exemptions) | `hk-building-codes` |
| **APP-40** | Sustainable building design (setback, greenery ratio ≥ 20–30%) | `hk-building-sustainability` |
| **APP-130** | Means of escape — general principles | `hk-fire-life-safety` |
| **APP-152** | Barrier-free access | `hk-accessibility-design` |
| **ADV-36** | Amenity features (balconies, utility platforms) | `hk-building-codes` |
| **ADV-49** | Green and innovative buildings | `hk-building-sustainability` |
 
### 1.5 Means of Escape — Quick Numbers (BO Reg. 41 + FS Code 2011)
 
| Parameter | Value |
|---|---|
| Max travel distance — domestic, sprinklered | 45 m |
| Max travel distance — domestic, unsprinklered | 30 m |
| Max travel distance — non-domestic, sprinklered | 60 m |
| Max travel distance — non-domestic, unsprinklered | 45 m |
| Min exit width — ≤ 50 persons | 750 mm |
| Min exit width — 51–200 persons | 1,050 mm |
| Min exit width — > 200 persons | 1,050 mm + 150 mm per 50 persons above 200 |
| Min corridor width — residential common | 1,050 mm |
| Min corridor width — non-domestic | 1,200 mm |
| Max dead-end corridor (sprinklered) | 15 m |
| Max dead-end corridor (unsprinklered) | 6 m |
| Staircase pressurisation threshold | > 30 m building height |
 
### 1.6 Building Height Restriction (BHR)
 
- BHR is defined in the OZP in metres above **Principal Datum (mPD)** or by storey count.
- Check the OZP annotation and Explanatory Statement for the specific site before any massing study.
- **Aviation restrictions** (CAAS): mandatory consultation for Kowloon, Lantau, and airport environs.
- **Ridgeline protection**: refer to HKPSG Chapter 11 and relevant OZP; no development to intrude visually on natural ridgelines from designated vantage points.
- **Harbour view corridors**: maintain per HKPSG Fig. 11.1.

### 1.7 Sprinkler Thresholds (FS Code 2011)
 
| Building Type | Sprinkler Required When |
|---|---|
| Domestic (residential) | > 13 storeys or > 40 m height |
| Non-domestic | > 230 m² per floor or > 3 storeys |
| Basement (occupied) | All cases |
| Composite building | Per most stringent applicable use |
 
### 1.8 Village Houses (NT Exempted Houses — NTEH)
 
| Parameter | Limit |
|---|---|
| Max storeys | 3 |
| Max floor area per storey | 65.03 m² (700 sq ft) |
| Max height | 8.23 m (27 ft) |
| Max site coverage | 66.7% |
 
> All four limits must be met simultaneously — BD rejects if any single limit is exceeded.
 
### 1.9 Environmental Performance — HK Subtropical Climate (CZ 1A)
 
| Metric | Target | Source |
|---|---|---|
| OTTV (non-domestic) | ≤ 20 W/m² | BEAM Plus NB |
| RTTV (roof) | ≤ 25 W/m² | BEAM Plus NB |
| Window-to-wall ratio, N/S facade (residential) | 25–35% | BEAM Plus / OTTV compliance |
| Window-to-wall ratio, E/W facade (residential) | 15–25% | Limit solar gain |
| Natural ventilation depth (cross-ventilated unit) | ≤ 12 m per side | BEAM Plus IEQ |
| Podium greenery ratio | ≥ 20–30% site area | PNAP APP-40 |
 
### 1.10 Key HK Architects (Quick Reference)
 
| Architect / Practice | Signature Approach | Key Works |
|---|---|---|
| **Tao Ho** (何弢) | Chinese spatial grammar in modern form | HK Arts Centre (1977), Bauhinia emblem |
| **Rocco Yim** (嚴迅奇) | Layered urbanism, section as generator | Guangdong Museum, HK Planning Dept HQ |
| **P&T Group** | Pragmatic high-rise and composite buildings | Jardine House, Exchange Square |
| **Aedas HK** | Supertall and MTR transit hubs | ICC, various MTR stations |
| **Ronald Lu & Partners** | Sustainable urbanism, BEAM Plus | Community and green building projects |
| **Wong & Ouyang** | Complex mixed-use, hospitals, infrastructure | Hospital Authority projects |
 
> For full design theory, critical regionalism, and HK urban discourse, load `hk-design-theory`.

### 1.11 Completion Checklist

| Milestone | Authority / Form | Critical Requirement |
|---|---|---|
| FSD Inspection | Form FSI/501 | All Fire Services Installations (FSI) must be 100% functional and tested. |
| BD OP Inspection | Form BA14 | Building must be "rendered fit for occupation." No "Unauthorized Building Works" (UBW) vs. approved plans. |
| Water Supply | WSD Form WWO 46 | Final inspection of plumbing and fire mains by Water Supplies Dept. |
| Lifts/Escalators | EMSD Form 5 | "Permit to Use and Operate" from Electrical and Mechanical Services Dept. |
| Practical Completion | HKIA PC Cert | Building is functionally complete; minor snags only. Transfer of insurance/risk to Client. |
 
---
 
## 2. Routing Decision Tree
 
**Answer from Section 1 first** if the question can be resolved there. Route to a sub-skill only when deeper expertise is required.
 
```
START
│
├─ BO Cap.123, PNAP, GFA, plot ratio, site coverage, BHR, or MOE calculations?
│   └─► [hk-building-codes]
│
├─ Fire strategy, FS Code 2011, FSD, sprinklers, compartmentation, scissor stairs, smoke control?
│   └─► [hk-fire-life-safety]
│
├─ OZP zoning, planning application (s.16 / s.12A), TPB, AVA, HKPSG, or development control?
│   └─► [hk-spatial-planning]
│
├─ BEAM Plus, OTTV/RTTV, green building credits, energy performance, or EIA?
│   └─► [hk-building-sustainability]
│
├─ Barrier-free access, DMBA 2008, accessible ramps, lifts, or tactile paving?
│   └─► [hk-accessibility-design]
│
├─ Heritage conservation, AMO/AAB processes, HIA, adaptive reuse submissions, or graded buildings?
│   └─► [hk-heritage-conservation]
│
├─ HA/HD public housing, Harmony blocks, MTR TOD, NTEH village houses, composite buildings, or Grade A office?
│   └─► [hk-building-typology]
│
├─ Curtain wall, cladding, facade system, OTTV optimisation, typhoon wind load, or weatherproofing?
│   └─► [hk-building-envelope]
│
├─ HVAC, plumbing, drainage, electrical systems, or FSD installations (hose reel, hydrant, sprinkler)?
│   └─► [hk-building-services]
│
├─ Structural systems, SUC 2013, SUS 2011, HKWC wind code, transfer slab, or foundation?
│   └─► [hk-structural-systems]
│
├─ Area programme, schedule of accommodation, unit mix, HKPSG facility ratios, or space brief?
│   └─► [hk-building-programming]
│
├─ BD submission stages, AP/RSE appointments, occupation permit (OP), GS specification, or compliance drawings?
│   └─► [hk-construction-documentation]
│
├─ Concept design process, massing strategy, BHR compliance, or schematic design for BD submission?
│   └─► [hk-concept-design]
│
├─ Acoustic design, EPD noise ordinance, MTR/railway vibration, or construction noise permit?
│   └─► [hk-acoustic-design]
│
├─ Daylighting, daylight factor, BEAM Plus IEQ daylight, or BO Reg. 30 natural light compliance?
│   └─► [hk-daylighting-design]
│
├─ Material selection, cladding durability, BEAM Plus materials credits, or typhoon-resistant spec?
│   └─► [hk-material-selection]
│
├─ GFA aggregation, OTTV calculation, occupant load, or exit width calculation?
│   └─► [hk-architect-calculator]
│
├─ HK architects, design theory, critical regionalism, heritage discourse, or Asian architectural theory?
│   └─► [hk-design-theory]
│
├─ Minor works (MWCS, Class I-III, APP-147, MW forms)?
│   └─► [hk-minor-works]
│
├─ Consent to commence works, fast-track processing, consent timelines/scheduling, or renewal?
│   └─► [hk-consent-scheduling]
│
├─ Pre-construction, site establishment (假設工程), hoarding, temporary works, utility diversion, neighbour liaison, or mobilisation checklist?
│   └─► [hk-site-establishment]  (+ hk-consent-scheduling for BA8; hk-construction-health-safety for PCI)
│
├─ Traffic consultant, TIA, TMP, Transport Department (TD), lane closure, bus stop, or construction traffic accommodation?
│   └─► [hk-traffic-coordination]  (+ hk-spatial-planning if planning-condition TIA; hk-site-establishment if hoarding TMP)
│
├─ OFCA, telecommunications, fibre/cable diversion, licensed works, or utility undertaker telecom protection?
│   └─► [hk-telecom-coordination]  (+ hk-site-establishment for lane-1 sequencing)
│
├─ A&A works in existing buildings or major alterations?
│   └─► [hk-alterations-additions]  (or route primarily to minor-works / building-codes)
│
├─ AP/RSE supervision during construction, site meetings, deviations, BA14/BA12/BA13, or OP-stage handover?
│   └─► [hk-site-supervision]
│
├─ Construction sequence, fast-tracking (工序穿插), standard floor cycle, follow-the-structure facade, hold-point register, or 4-week look-ahead on a high-rise RC tower?
│   └─► [hk-construction-programme]  (+ hk-project-management for governance; hk-site-supervision for AP hold points)
│
├─ Procurement route (traditional Design-Bid-Build, D&B, management contracting, NEC4 target cost), contract strategy, risk allocation, or pain/gain?
│   └─► [hk-procurement-strategy]
│
├─ Typhoon delay, T8, inclement weather EOT, Compensation Event weather, or delay costs by contract type?
│   └─► [hk-procurement-strategy]  (+ [hk-tender-contract-administration] §12.8 if acting as CA)
│
├─ Tender documentation, Bills of Quantities coordination, contract form strategy, variations, or post-contract administration?
│   └─► [hk-tender-contract-administration]
│
├─ Deliverables by workstage, who gets what (client / authorities / contractor), issue packs, transmittals, registers, or drawing scales for deliverables?
│   └─► [hk-deliverables-workstages]
│
├─ RIBA plan of work, stage checklist, stage gate, Stage 0–7 tasks, strategic definition, or handover checklist?
│   └─► [hk-plan-of-work]  (+ hk-deliverables-workstages for issue packs)
│
├─ Fee bidding strategy, percentage-vs-lump-sum fee proposals, scope creep controls, or additional services definitions?
│   └─► [hk-fee-proposal-strategy]
│
├─ Invoicing and payment-cycle strategy, milestone-linked billing (e.g. BD Approval / OP), receivables control, or aged debt recovery in the HK developer market?
│   └─► [hk-cashflow-debt-recovery]
│
├─ Profit-vs-progress monitoring, manpower balancing, break-even hourly rate calculations, or burn-rate control against drawdown?
│   └─► [hk-project-resource-levelling]
│
├─ Lands Department Certificate of Compliance (CC), Consent to Assign for private land grants, or Green Area handover coordination with departments (e.g. HyD / LCSD)?
│   └─► [hk-certificate-of-compliance]
│
├─ OP submission pathway strategy, BA12/BA13/BA14 workflow sequencing, partial OP planning, OP inspection preparation, or full-set record drawing/test report coordination?
│   └─► [hk-op-submission-strategy]
│
├─ Fire services handover certifications (FSI/314, FSI/501), FSD inspection strategy, hydrant/hose reel test closeout, or Fire Certificate (FS 172) readiness?
│   └─► [hk-fsd-licensing-compliance]
│
├─ Practical completion certification (PC), DLP administration, or snagging/de-snagging workflows for premium finishes?
│   └─► [hk-practical-completion-snagging]
│
├─ Professional indemnity (PI) insurance requirements, limit of liability clauses, or duty of care letters?
│   └─► [hk-professional-indemnity]
│
├─ Modular Integrated Construction (MiC), DfMA strategy, MiC concession logic (6%–10%), or module logistics coordination?
│   └─► [hk-mic-dfma]
│
├─ Unauthorised building works (UBW), BD orders (s.24/s.25), rectification strategy, regularization path, or sale/OP/consent implications?
│   └─► [hk-unauthorised-building-works]
│
├─ Lease conditions, LandsD submissions, or waiver applications?
│   └─► [hk-lease-compliance]
│
├─ Cost plan, BoQ, tender pricing, valuation, final account, feasibility budget, or QS commercial advice?
│   └─► [hk-cost-consultancy]  (+ hk-tender-contract-administration if certification/interface)
│
├─ Site H&S strategy, risk assessment, CDM, accident investigation, safety plan review, or LD compliance?
│   └─► [hk-construction-health-safety]  (not hk-fire-life-safety — that is building fire code)
│
├─ Project delivery plan, business case, strategic brief, client reporting, programme/budget monitoring, or dispute escalation?
│   └─► [hk-project-management]
│
├─ Lead consultant coordination, consultant RACI, stage-freeze gates, or VM workshops?
│   └─► [hk-deliverables-workstages] Section 6  (+ hk-project-management)
│
├─ Contract Administrator duties: EOT claims, interim certificate, client instructions, progress report, prime cost sum?
│   └─► [hk-tender-contract-administration] Section 12  (+ hk-cost-consultancy / hk-practical-completion-snagging)
│
├─ HK practice foundations, PNAP index, or broad regulatory overview before specialist routing?
│   └─► [hk-architect-foundations]
│
└─ Default: answer directly from Section 1.
│   Multiple topics? Route to the primary skill; cross-reference secondary skills as needed.
```
 
### Multi-Skill Priority (when topics overlap)
 
1. **Regulatory**: `hk-building-codes` › `hk-spatial-planning` › `hk-fire-life-safety` › `hk-accessibility-design` › `hk-minor-works` › `hk-consent-scheduling` › `hk-alterations-additions` › `hk-lease-compliance`
2. **Performance**: `hk-building-sustainability` › `hk-building-envelope` › `hk-daylighting-design` › `hk-acoustic-design`
3. **Typology / Programme**: `hk-building-typology` › `hk-building-programming` › `hk-building-services`
4. **Delivery**: `hk-concept-design` › `hk-construction-documentation` › `hk-plan-of-work` › `hk-construction-programme` › `hk-site-establishment` › `hk-traffic-coordination` › `hk-telecom-coordination` › `hk-procurement-strategy` › `hk-tender-contract-administration` › `hk-cost-consultancy` › `hk-project-management` › `hk-deliverables-workstages` › `hk-fee-proposal-strategy` › `hk-cashflow-debt-recovery` › `hk-project-resource-levelling` › `hk-certificate-of-compliance` › `hk-practical-completion-snagging` › `hk-professional-indemnity` › `hk-structural-systems` › `hk-material-selection` › `hk-architect-calculator`
5. **Site safety**: `hk-construction-health-safety` › `hk-site-supervision` › `hk-fire-life-safety`
6. **Theory**: `hk-design-theory` › `hk-architect-foundations`

---

## 2.5 Role Coverage Index

Load the **primary** skill first; add secondary skills when duties overlap.

| Professional role | Duty cluster | Primary `skill_id` | Secondary |
|---|---|---|---|
| **Contract Administrator / Employer's Agent** | Tenders, contract execution, change control | `hk-tender-contract-administration` | `hk-cost-consultancy`, `hk-practical-completion-snagging` |
| | Client instructions, progress meetings/reports | `hk-tender-contract-administration` §12 | `hk-project-management` |
| | Variations, PC sums, EOT/claims | `hk-tender-contract-administration` §12 | `hk-cost-consultancy`, `hk-procurement-strategy` (typhoon/route) |
| | Interim / PC / defects / final certificates | `hk-tender-contract-administration` §12 | `hk-practical-completion-snagging` §10 |
| | Commissioning, defect procedures, site inspectors | `hk-tender-contract-administration` §12 | `hk-fsd-licensing-compliance`, `hk-site-supervision` |
| **Cost Consultant (QS)** | Feasibility, benchmarking, budget | `hk-cost-consultancy` | `hk-deliverables-workstages` |
| | Cost plans, cash flow, BoQ, tender pricing | `hk-cost-consultancy` | `hk-tender-contract-administration` |
| | Tender evaluation, variations, valuations | `hk-cost-consultancy` | `hk-tender-contract-administration` |
| | Claims support, cost reports, final account | `hk-cost-consultancy` | `hk-tender-contract-administration` |
| **Designer** | Project set-up, design development | `hk-concept-design` | `hk-deliverables-workstages` §6.9 |
| | Production info, tender documents | `hk-construction-documentation` | `hk-deliverables-workstages` |
| | Site establishment, hoarding, lane 1 mobilisation | `hk-site-establishment` | `hk-consent-scheduling`, `hk-traffic-coordination`, `hk-telecom-coordination` |
| | Contract administration (if appointed) | `hk-tender-contract-administration` | — |
| | Check contractor/supplier work | `hk-site-supervision` | `hk-practical-completion-snagging`, `hk-construction-programme` |
| **Health & Safety Advisor** | H&S strategy, risk assessments | `hk-construction-health-safety` | — |
| | Regulatory liaison, accidents, site inspections | `hk-construction-health-safety` | `hk-site-supervision` |
| | CDM, contractor safety documentation review | `hk-construction-health-safety` | `hk-project-management` |
| **Lead Designer / Lead Consultant** | Consultant coordination, meetings, progress reports | `hk-deliverables-workstages` §6 | `hk-project-management` |
| | Client instructions, stage-freeze change control | `hk-deliverables-workstages` §6 | `hk-project-management` |
| | Procurement route, risk allocation, NEC/D&B/traditional choice | `hk-procurement-strategy` | `hk-project-management` |
| | Contract form ID, PQ/tender review, tender documents | `hk-tender-contract-administration` | `hk-fee-proposal-strategy` |
| | Value management | `hk-deliverables-workstages` §6 | `hk-cost-consultancy` |
| **Project Lead / Project Manager** | Business case, strategic brief, delivery plan | `hk-project-management` | `hk-deliverables-workstages` |
| | Consultant appointments, RACI, client instructions | `hk-project-management` | `hk-fee-proposal-strategy` |
| | Risk, VM, design reviews | `hk-project-management` | `hk-cost-consultancy`, `hk-deliverables-workstages` |
| | Contractor selection, payment validation, change control | `hk-project-management` | `hk-procurement-strategy`, `hk-tender-contract-administration`, `hk-cost-consultancy` |
| | Disputes, programme/budget monitoring | `hk-project-management` | `hk-tender-contract-administration` |
| | Construction swimlanes, fast-tracking, look-ahead | `hk-construction-programme` | `hk-project-management`, `hk-site-supervision` |
| | Site establishment, hoarding, utility/neighbour coordination | `hk-site-establishment` | `hk-traffic-coordination`, `hk-telecom-coordination`, `hk-consent-scheduling` |
| | Construction to occupation, client reporting | `hk-project-management` | `hk-op-submission-strategy`, `hk-practical-completion-snagging` |
| **All roles** | RIBA Stage 0–7 task checklists, stage gates | `hk-plan-of-work` | `hk-deliverables-workstages` |

---

## 3. Universal Response Constraints

* **Tone:** Technical, objective, precise; no platitudes.
* **Format:** Markdown with clear hierarchy and tables where useful.
* **Uncertainty:** State the information gap; document assumptions; never invent PNAP or lease clauses.
* **Licensing:** Advisory only — not AP/RSE/BD/FSD sign-off (see `references/compliance.md`).
* **Compliance language:** Do not state “compliant” without OZP Notes and lease verification.

---

## 4. Dispatcher Tools

### `load_sub_skill`

Injects the detailed instruction set for a specific HK domain into context.

- **Parameter** — `skill_id` (string, required). Valid IDs:
  `hk-accessibility-design`, `hk-acoustic-design`, `hk-alterations-additions`, `hk-architect-calculator`, `hk-architect-foundations`, `hk-building-codes`, `hk-building-envelope`, `hk-building-programming`, `hk-building-services`, `hk-building-sustainability`, `hk-building-typology`, `hk-cashflow-debt-recovery`, `hk-certificate-of-compliance`, `hk-concept-design`, `hk-construction-health-safety`, `hk-construction-programme`, `hk-consent-scheduling`, `hk-construction-documentation`, `hk-cost-consultancy`, `hk-daylighting-design`, `hk-deliverables-workstages`, `hk-design-theory`, `hk-fee-proposal-strategy`, `hk-fire-life-safety`, `hk-fsd-licensing-compliance`, `hk-heritage-conservation`, `hk-lease-compliance`, `hk-material-selection`, `hk-mic-dfma`, `hk-minor-works`, `hk-op-submission-strategy`, `hk-plan-of-work`, `hk-practical-completion-snagging`, `hk-procurement-strategy`, `hk-professional-indemnity`, `hk-project-management`, `hk-project-resource-levelling`, `hk-site-establishment`, `hk-site-supervision`, `hk-spatial-planning`, `hk-structural-systems`, `hk-telecom-coordination`, `hk-tender-contract-administration`, `hk-traffic-coordination`, `hk-unauthorised-building-works`

### `run_hk_calculator`

Executes Python-based calculations via `scripts/calculators.py`.

| `calc_type` | `data` (summary) |
|-------------|------------------|
| `egress_1004_7` | `length`, `width`, `sprinklered` — simplified room check only |
| `gfa_aggregator` | `floors`: list of `{area, is_exempt}` |
| `layout_sort` | `items`: list of `{x, y}` for OCR/table ordering |

See `hk-architect-calculator` for JSON detail. OTTV/MOE formulas there are markdown-only (not dispatched).

---

## Available scripts

- **`scripts/calculators.py`** — `egress_1004_7`, `gfa_aggregator`, `layout_sort` deterministic calculations
- **`scripts/dispatcher.py`** — Subskill loader: `python scripts/dispatcher.py` via `HKSkillsDispatcher` / `main.py`

**Workflow example (GFA):**

```bash
pip install -e .
echo '{"tool":"run_hk_calculator","arguments":{"calc_type":"gfa_aggregator","data":{"floors":[{"area":500,"is_exempt":false}]}}}' | python hk-architect-master/main.py
```

---

## Governance files

| File | Purpose |
|------|---------|
| `references/config.json` | Strict mode, jurisdiction, governance framework |
| `references/compliance.md` | Hard-stop rules |
| `references/operational.md` | Intake, routing, escalation SOPs |
| `references/domain_terms.json` | Acronym definitions |
| `references/templates/` | Standard deliverable shells |

---
 
*Sources: Buildings Ordinance Cap. 123 (2023 ed.), BO (Building Planning) Regulations, PNAP APP-2 / APP-40 / APP-130 / APP-152 / ADV-36 / ADV-49, HKPSG 2026, Code of Practice for Fire Safety in Buildings 2011, Design Manual: Barrier Free Access 2008, Town Planning Ordinance Cap. 131, BEAM Plus NB v2.0, BEAM Plus EB v2.0.*