---
name: hk-deliverables-workstages
description: HK deliverables by workstage — define who gets what (client/authorities/contractor/consultants), how to present issue packs clearly, include delivery reference tables, and suggest drawing scales.
disable-model-invocation: true
---

# HK Deliverables by Workstage

Use this sub-skill to ensure every project **workstage deliverable** is explicitly defined for each audience (client / government departments / contractors / other bodies), with a clear presentation format and (where applicable) suggested drawing scales.

For **Deliverables by workstage / transmittals**, use `hk-deliverables-workstages`. For other topics, see the routing table below.

Optional output template: `../.../../references/templates/deliverables.md`

## When to Use This Skill

Issue packs, transmittals, drawing scales, consultant RACI, stage freezes.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Deliverables by workstage / transmittals | `hk-deliverables-workstages` | `—` |
| RIBA stage task checklists | `—` | `hk-plan-of-work` |
| Client delivery plan / reporting | `—` | `hk-project-management` |
---

## 0. Deliverables Must Always Be “Issue-Pack Ready”

Every deliverable set should be packaged as an **Issue Pack** (even for internal/client-only issues):

- **Cover page**: project, stage, issue purpose, issue date, revision, recipients, confidentiality, and who prepared/checked/approved.
- **Deliverables register**: one table listing every file/sheet with revision + status (Draft / For Review / For Approval / For Tender / For Construction / As-Built).
- **Drawing register**: drawing list with title, sheet size, scale(s), revision, status.
- **Transmittal**: what is issued, why, and what action is required by each recipient (review/approval/price/build/record).
- **File naming + folder structure**: stable, predictable, sortable.
- **Revision discipline**: revision clouds on drawings (where applicable) + written change summary in the transmittal.

Presentation rule: **audience-first**. A contractor needs buildable packages; a client needs decision packs; authorities need compliance packs.

---

## 1. Stakeholder Groups and What “Good” Looks Like

| Recipient | What they need to decide/do | Deliverable emphasis |
|---|---|---|
| Client / Owner | Approve scope, budget, programme, quality | Options, implications, cost/time impacts, clear visuals, decision log |
| Authorities (BD / FSD / DSD / etc.) | Approve compliance; inspect | Code-compliant drawings, calculations, forms, schedules, clear annotation, referenced standards |
| Contractor / Tenderers | Price accurately; plan method | Coordinated scope, clear measurement, unambiguous specs, interfaces, exclusions stated |
| Specialist subcontractors | Detail, fabricate, install | Performance criteria, interfaces, key details, tolerances, sample requirements |
| Consultants (RSE / MEP / Façade / Acoustic / etc.) | Coordinate; certify | Model/drawing interfaces, responsibility matrix, coordination minutes, RFI tracking |
| Building management / FM | Operate and maintain | O&M structure, asset data, warranties, training records, as-builts, maintenance access notes |

---

## 2. Workstages (HK-typical) and Deliverable Definition

Workstages below are intentionally generic so they can map to HKIA/RIBA-like stages and to BD statutory milestones.

### Stage A — Brief / Feasibility (Pre-Design)

**Client deliverables**
- Brief confirmation pack: objectives, constraints, budget range, programme assumptions, risk register (early).
- Site / context findings: constraints map (lease controls, access, utilities, fire appliance access assumptions).

**Recommended drawing scales**
- Site/context diagrams: **1:2000 / 1:1000**
- Blocking/massing: **1:500 / 1:1000**

**How to present**
- 10–15 page PDF deck (decision-led), plus one-page “Brief Snapshot” for signing.

---

### Stage B — Concept Design

**Client deliverables**
- Concept options (2–3): plans/sections/massing, experience visuals, key risks.
- Preliminary area schedule and efficiency metrics (GFA/NFA assumptions).
- Outline cost plan input assumptions (if QS involved).

**Other bodies (if applicable)**
- Early consultation notes (e.g., planning/lease constraints), clearly labelled “non-statutory” unless confirmed.

**Recommended drawing scales**
- Site plan: **1:500 / 1:1000**
- Floor plans / sections: **1:200 / 1:100**
- Key concept diagrams: not-to-scale is OK, but include dimensions when claiming feasibility.

**How to present**
- Decision pack: each option includes **pros/cons + cost/time impacts + compliance risks** in a single page.

---

### Stage C — Schematic / Developed Design (Pre-Submission / Coordination)

**Client deliverables**
- Preferred scheme with coordinated plans/sections/elevations and key design intent.
- Updated area schedule and outline spec (performance requirements).

**Consultant deliverables (coordination)**
- Coordination set with clear interfaces (structural grids, plant room assumptions, shaft sizes).
- Design responsibility matrix (who owns what drawing/spec scope).

**Recommended drawing scales**
- GA plans/sections/elevations: **1:100**
- Core/typical unit / critical junctions: **1:50**

**How to present**
- “Single source of truth”: one drawing index, one model/drawing revision per issue.

---

### Stage D — Statutory Submissions (BD / FSD / Others as Applicable)

**Authorities deliverables (typical)**
- Submission drawing sets (e.g., General Building Plans, drainage plans, structural plans, fire services plans), with schedules/calculations/forms as required.
- Compliance narrative: brief, cross-referenced to drawing sheet numbers and relevant code notes.

**Client deliverables**
- Submission summary: what is being lodged, what approvals are expected, timeline, and critical conditions.

**Recommended drawing scales (typical)**
- Site plans: **1:500 / 1:1000**
- Submission floor plans/sections/elevations: **1:100** (sometimes **1:200** for large buildings)
- Fire strategy diagrams: **1:200 / 1:100** (ensure legibility of egress widths and travel distances)

**How to present**
- Authorities pack should have **clean, consistent note conventions** and a sheet-by-sheet compliance checklist.

---

### Stage E — Detailed Design / Tender Documentation

**Tenderer/contractor deliverables**
- Tender drawings + coordinated outline specs sufficient for pricing.
- Scope clarity: inclusions/exclusions, provisional sums allowances, interface notes (by trade).
- Measurement-friendly information: typical details, room data sheets (if fit-out), key schedules.

**Client deliverables**
- Tender scope report and tender strategy notes (packages, preliminaries assumptions).

**Recommended drawing scales**
- Tender GA plans: **1:100**
- Enlarged plans (lobbies/toilets/kitchens): **1:50**
- Typical details: **1:20 / 1:10**

**How to present**
- Issue a “Tender Query Protocol” and make the drawing/spec package **internally consistent** (no contradictions).

---

### Stage F — Construction (For Construction / Site Information)

**Contractor deliverables**
- IFC issue packs: drawings/specs/schedules with explicit status “For Construction”.
- Site information: clarification sketches, SI/AI logs, RFI responses with references.

**Other bodies (if applicable)**
- Inspection-ready packs: method statements, test plans, mock-up approvals, material submissions logs.

**Recommended drawing scales**
- IFC GA plans: **1:50** where it materially reduces ambiguity (keep **1:100** for large repetitive layouts)
- Construction details: **1:20 / 1:10 / 1:5**
- Setting-out/control drawings: **1:50 / 1:20** (dimension-first)

**How to present**
- Maintain a **live drawing register + SI log** and issue only via controlled transmittals.

---

### Stage G — Completion / Testing / OP Readiness (as applicable)

**Client deliverables**
- Completion readiness checklist: inspections, testing, outstanding risks, target PC date.

**Authorities deliverables**
- Inspection/testing evidence packs as required (by discipline), clearly indexed for audit/visit day.

**Recommended drawing scales**
- Life safety plans for inspection walkthrough: **1:100 / 1:200** (legible on A3)

**How to present**
- One “Inspection Day Pack” PDF with bookmarks + an appendix folder of certificates/test records.

---

### Stage H — Handover (As-Built / O&M / FM)

**Client/FM deliverables**
- As-built drawings (record set), O&M manuals, warranties, training records.
- Asset register / equipment schedules aligned to O&M sections.

**Recommended drawing scales**
- As-built GA: match IFC issue scales (commonly **1:100 / 1:50**)
- Services schematics: NTS allowed, but ensure readability and tagging consistency.

**How to present**
- O&M should be structured by **system → sub-system → equipment** with a searchable index.

---

### Stage I — Defects Liability / Closeout

**Client/FM deliverables**
- Defects log with responsibility, target closure date, evidence of completion.

**How to present**
- One tracker (spreadsheet) + photo evidence folders referenced by defect ID.

---

## 3. Delivery Reference Table (Template)

Use this table for each issue pack. Add or remove columns to suit.

| Workstage | Recipient | Deliverable | Format | Status | Scale(s) | Revision | Owner | Due / Action required |
|---|---|---|---|---|---|---|---|---|
| Stage E | Tenderers | Architectural GA plans | PDF | For Tender | 1:100 / 1:50 | P1 | Architect | Price against drawings + return tender |

Minimum recommendation: keep this table in **both** the transmittal PDF and a **machine-editable** version (Excel/Sheets).

---

## 4. How to Clearly Present Deliverables (Practical Rules)

- **One pack = one purpose**: don’t mix “for approval” and “for construction” in the same transmittal.
- **Declare what is not included**: exclusions prevent disputes more than extra details do.
- **Use a stable sheet numbering system** early (don’t renumber midstream unless unavoidable).
- **Always include a scale bar** on drawings (prints get resized; scale bars survive).
- **Legibility test**: if issued for site use, print to A3 and confirm key notes/dimensions are readable.
- **Change summary**: list the top 5–15 changes since last issue in plain language.
- **Interface notes**: when two trades meet, explicitly state what is by whom (and where the boundary line sits).

---

## 5. Drawing Scale Guidance (Quick Reference)

| Deliverable type | Typical scale(s) | Notes |
|---|---|---|
| Location / context plan | 1:2000 / 1:1000 | Add north point, key access, constraints |
| Site plan | 1:500 / 1:200 | Show boundaries, levels, access, fire appliance assumptions if relevant |
| General arrangement (GA) plans | 1:200 / 1:100 | Use 1:100 when dimensioning matters |
| Enlarged plans (critical areas) | 1:50 | Toilets, kitchens, lobbies, plantrooms |
| Elevations / sections | 1:200 / 1:100 | Use 1:100 for coordination + key heights |
| Typical construction details | 1:20 / 1:10 | Junctions, waterproofing build-ups, facade interfaces |
| Large-scale details | 1:5 / 1:2 | Where tolerances and fixings are critical |
| Schedules (doors/finishes/equipment) | NTS | Ensure tags match drawings/models |

Rule of thumb: choose the **smallest scale that remains unambiguous** at the intended sheet size.

---

## 6. Lead Consultant Coordination

Use when acting as **Lead Designer / Lead Consultant** on a multi-disciplinary team. Cross-reference: `hk-project-management`, `hk-fee-proposal-strategy`, `hk-cost-consultancy`, `hk-tender-contract-administration`.

### 6.1 Consultant team RACI (template)

| Workstage / deliverable | Lead Consultant | Architect | QS | RSE/MEP | Specialists | Client |
|---|---|---|---|---|---|---|
| Brief confirmation | A/R | C | C | I | I | A |
| Concept issue | A/R | R | C | C | C | A |
| Statutory submission | A/R | R | I | R | C | A |
| Tender package | A/R | R | R | R | C | A |
| Site/closeout | A | R | C | C | C | A |

*A = Accountable, R = Responsible, C = Consulted, I = Informed — adjust per appointment.*

### 6.2 Meeting cadence and workstage planning
- **Project kick-off**: brief, programme, RACI, communication protocol.
- **Design coordination**: fortnightly (or weekly near submission/tender).
- **Tender stage**: tender query log review; addenda coordination.
- **Construction**: monthly coordination + ad hoc RFIs.

Maintain **Consultant Action Register** from every meeting.

### 6.3 Progress reports (lead consultant to client)
Monthly minimum contents:
1. Design status by discipline and workstage
2. Programme vs milestone (submission, tender, award)
3. Key decisions required from client
4. Risks and issues (coordination, authority, scope)
5. Change log since last report
6. Look-ahead (next period deliverables)

### 6.4 Client instructions
- Channel client instructions through PM or Lead Consultant per governance.
- Confirm impact on brief, programme, and fee before design team implements.
- Log in Brief Change Log linked to `hk-project-management` Client Instruction Log.

### 6.5 Stage-freeze change control
| Freeze gate | What is frozen | Change after freeze |
|---|---|---|
| Brief freeze | Function, area, quality tier | Formal change request; fee/programme impact |
| Schematic freeze | Massing, core, major systems | Coordinated change only |
| Tender issue freeze | Scope for pricing | Via variation or tender addendum only |
| Construction issue freeze | IFC baseline | Formal instruction + record |

### 6.6 Value management
- Plan VM workshops at concept and pre-tender (with QS).
- Present options with cost/time/quality/risk trade-offs.
- Record decisions in VM log; update deliverables register.

### 6.7 Procurement and contract advice
- Advise client on procurement route (traditional, D&B, NEC4, management contracting, construction management) — see `hk-procurement-strategy` (selection rationale, risk allocation, typhoon/interface implications).
- Advise on contract form and record Contract Family Code — see `hk-tender-contract-administration` Section 4A.
- Support PQ criteria and tender evaluation chairing (technical + commercial integration).

### 6.8 QS deliverables by workstage (coordination)

| Workstage | QS deliverable | Lead consultant review |
|---|---|---|
| Feasibility | OOM / feasibility cost | Budget realism |
| Concept | Elemental cost plan | Design-to-budget |
| Developed design | Cost plan revisions | Variance narrative |
| Tender | BoQ / pricing docs | Scope alignment |
| Construction | Valuations, cost reports | Client reporting integration |
| Closeout | Final account | Certificate sequence |

### 6.9 Designer duties index (cross-links)

| Designer duty | Primary sub-skill |
|---|---|
| Project set-up / definition | This skill Stage A; `hk-concept-design` |
| Design development & coordination | `hk-concept-design`, discipline skills |
| Production info & tender docs | Stage E; `hk-construction-documentation` |
| Contract administration (when appointed) | `hk-tender-contract-administration` |
| Check contractor/supplier work | `hk-site-supervision`, `hk-practical-completion-snagging` |

### 6.10 Plan of Work checklists (process vs deliverables)

- **Deliverables** (this skill): what to **issue** — drawings, registers, transmittals, scales.
- **Process checklists** (RIBA Stages 0–7): what to **do/verify** — use `hk-plan-of-work` and `../../references/hk-pow-stages-0-7.md`.
- At each stage gate, run PoW checklist then update deliverables register for any new issue packs.

