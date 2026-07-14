---
name: hk-tender-contract-administration
description: Activate for tender documentation strategy, Bills of Quantities coordination, Standard Form of Building Contract guidance, tender assessment support, post-contract architect administration, variation management, and progress/certification workflows.
disable-model-invocation: true
---

# HK Tender and Contract Administration
Covers pre-tender package preparation, procurement interface, contract formation, and post-contract architect duties in Hong Kong practice.

---

For **Tender / CA / post-contract admin**, use `hk-tender-contract-administration`. For other topics, see the routing table below.

## When to Use This Skill

Tender docs, BoQ coordination, CA duties, variations, certificates, EOT.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Tender / CA / post-contract admin | `hk-tender-contract-administration` | `—` |
| Procurement route choice | `—` | `hk-procurement-strategy` |
| Cost plan / valuation quantum | `—` | `hk-cost-consultancy` |
| Typhoon EOT by route (strategy) | `—` | `hk-procurement-strategy` |
## 1. Scope and Role
- Manage tender and contract administration as a risk-control workflow, not a paperwork exercise.
- Coordinate among client, quantity surveyor, engineers, and legal/commercial advisers.
- Keep procurement, contract clauses, and construction administration aligned to project objectives.

---

## 2. Pre-Tender Documentation
Typical tender set should include:
1. Architect's drawings and specifications at suitable tender detail.
2. Bills of Quantities (BoQ) prepared by QS, with architect-led design coordination inputs.
3. Employer requirements, preliminaries, and particular conditions.
4. Form of tender, return schedules, and tender instructions.
5. Proposed form of contract and appendices.

Quality checks before issue:
- Scope completeness and consistency between drawings, specs, and BoQ.
- Clear assumptions and exclusions to reduce post-award dispute risk.
- Practical tender period and bidder query protocol.

---

## 3. BoQ Coordination (Architect Interface)
- Architect defines design intent, scope boundaries, and quality requirements.
- QS leads measurement and pricing structure; architect verifies technical alignment.
- Resolve inconsistencies early (dimensions, material descriptions, interface items).

BoQ coordination principles:
- One design intent, one description language across all documents.
- Avoid "double counting" or scope gaps across trades.
- Record all clarifications with auditable issue history.

---

## 4. Contract Form Strategy
Common approach:
- Use the Standard Form of Building Contract (or project-approved equivalent) with project-specific amendments where required.
- Ensure contract particulars reflect actual project constraints (time, liquidated damages, insurance, sectional completion, defects period).

Architect review focus:
- Certifier role neutrality and procedural clarity.
- Clause consistency with tender drawings/specification obligations.
- Administration practicality: notices, timelines, substantiation, and evidence standards.

If NEC (New Engineering Contract) is used (common in public/infrastructure-style procurement):
- **DEVB policy:** NEC4 is mandatory for major Hong Kong public works (mid-2020s onward — verify current Development Bureau circular on each project). Also used by statutory bodies (e.g. MTR Corporation, Airport Authority).
- Treat the contract as an **active project management system** with defined response times and mandatory communications.
- Confirm the project has the capability and resourcing to run NEC properly (named roles, meeting cadence, programme controls, compensation event administration).
- Identify notice/time-bar requirements early and set up registers from day 1 (communications, early warnings, compensation events, programme submissions, payment assessments).

---

## 4A. Hong Kong standard architect-administered contract types (quick identification)
Use this section to clearly identify the contract family before tender issue and before post-award administration starts.

Office naming convention (use in reports, tender queries, and registers):
- **SFBC-Private-WQ**: HKIA/HKIS/HKICM Standard Form of Building Contract (Private Edition), **With Quantities**.
- **SFBC-Private-WOQ**: HKIA/HKIS/HKICM Standard Form of Building Contract (Private Edition), **Without Quantities**.
- **GCC-Building**: HKSAR Government General Conditions of Contract for building works (or approved project-specific government equivalent).
- **D&B-HK**: design-and-build form used for the project (where contractor design responsibility is substantial).
- **D&B-ArchSD**: Administrative Services Department (ArchSD) Design and Build Conditions of Contract (public sector).
- **D&B-DEVB**: Development Bureau (DEVB) Standard Design and Build Form (public sector).
- **MC-HK**: management contracting — bespoke MC agreement plus trade package subcontracts (Works Contractors).
- **CM-HK**: construction management — bespoke CM appointment; trade contractors contract directly with Employer.

Common Hong Kong building contract forms used in architect-led procurement:
- **SFBC-Private-WQ / SFBC-Private-WOQ**: typical private-sector architect-administered route; valuation/procedural workflow differs depending on quantities basis.
- **GCC-Building**: public works route with government procedures and amendments; confirm delegated powers, notices, and certification workflow.
- **D&B-HK / D&B-ArchSD / D&B-DEVB**: contractor design route; check Employer's Requirements, design submission/acceptance process, novation interfaces, and liability split. Confirm ArchSD vs DEVB form on public projects.
- **MC-HK / CM-HK**: multiple trade packages; confirm handover interfaces, EOT chains per package, and who holds head contract (MC vs Employer). See `hk-procurement-strategy` and `../../references/hk-typhoon-eot-by-procurement.md` for interface risk.

How to identify the exact form quickly (no assumptions):
1. Check the Form of Tender and Articles/Agreement title page.
2. Check Contract Particulars / Appendix for the named form and edition.
3. Check Particular Conditions / Special Conditions / Additional Conditions for amendments.
4. Record the chosen form, edition/year, and amendment set in the tender control sheet.

Internal tender control register - minimum fields:
- `Project Code`
- `Tender Package ID`
- `Contract Family Code` (use: SFBC-Private-WQ / SFBC-Private-WOQ / GCC-Building / D&B-HK / D&B-ArchSD / D&B-DEVB / MC-HK / CM-HK / NEC-ECC)
- `Form Full Title (as per signed docs)`
- `Edition / Revision / Issue Date`
- `Quantities Basis` (With Quantities / Without Quantities / Activity Schedule / BoQ / Other)
- `Particular Conditions Reference`
- `Special/Additional Conditions Reference`
- `Z Clause or Bespoke Amendment Register Ref` (if applicable)
- `Key Notice Time-bars Summary Ref`
- `Contract Administrator / PM Role Mapping Ref`
- `Last Verification Date`
- `Verified By`

Sample row (filled example, copy into tender tracker):
- `Project Code: PRJ-2026-014 | Tender Package ID: TND-ARC-01 | Contract Family Code: SFBC-Private-WQ | Form Full Title (as per signed docs): HKIA/HKIS/HKICM Standard Form of Building Contract (Private Edition) With Quantities | Edition / Revision / Issue Date: 2005 Edition, Rev. 2018, 2026-03-15 | Quantities Basis: With Quantities (BoQ) | Particular Conditions Reference: PC-RevB Clauses 1-24 | Special/Additional Conditions Reference: SC-RevA Clauses A1-A12 | Z Clause or Bespoke Amendment Register Ref: N/A | Key Notice Time-bars Summary Ref: NTS-PRJ-2026-014-v1 | Contract Administrator / PM Role Mapping Ref: RAM-CA-PM-2026-014 | Last Verification Date: 2026-05-09 | Verified By: A. Chan (Project Architect)` 

Minimum admin implications to flag by form type:
- **With quantities (BoQ route)**: measurement/valuation interfaces and BoQ consistency controls become critical.
- **Without quantities / lump-sum route**: scope-definition quality and variation causation records become critical.
- **Design-and-build route**: design responsibility matrix, submission/acceptance gates, and PI/fitness obligations must be explicit.
- **Government GCC route**: strict compliance with government circulars/procedures and delegated authority limits.

Reference note for this sub-skill:
- Always verify the **exact named form and edition adopted by the client**. Do not rely on memory or prior project habits.
- Where this sub-skill refers to "Standard Form of Building Contract", read it as the specific named HK form in the signed tender documents.
- In internal outputs, always include both the **Contract Family Code** and the **Form Full Title** to avoid ambiguity.

---

## 5. Tender Queries, Addenda, and Assessment
During tender period:
1. Receive and log tender queries.
2. Coordinate technical responses with consultants/QS.
3. Issue addenda in controlled revisions to all tenderers.

Assessment support:
- Check compliance against mandatory technical requirements.
- Flag exclusions, qualifications, and departures.
- Support tender report drafting with clear recommendation rationale.

---

## 5A. Architect role during tender stage (explicit duties)
Architect is not only a document author; architect is an active tender-stage evaluator and risk gatekeeper.

Architect duties before tender return:
- Attend and lead tender briefing / pre-tender meeting for design-intent clarification (with full tenderer parity).
- Confirm drawing/specification issue status, revision control, and addendum boundaries.
- Coordinate with QS/engineers so technical responses are contract-consistent and non-contradictory.

Architect duties at tender receipt and assessment:
- Attend tender opening / return review meeting where required by client procedure.
- Perform technical compliance check against mandatory design/specification requirements.
- Review tender qualifications/exclusions and identify any scope transfer or quality dilution risk.
- Assess alternative proposals (if permitted) for statutory compliance, buildability, maintainability, and whole-life impact.
- Record all technical clarifications in an auditable tender clarification log.

Architect duties for recommendation and award interface:
- Provide written technical assessment input to the tender report (compliance matrix, key risks, recommendation basis).
- Identify items requiring post-tender clarification and confirm the "no material change of tender" boundary.
- Support final tender interview / clarification meetings with clear minute-taking and action closure.
- Confirm that accepted tender assumptions are carried into contract documents before award.

Tender-stage control principles for architect:
- Equal treatment: same information to all tenderers through formal addenda/clarifications only.
- Audit trail: no off-record technical advice; all decisions traceable to issued documents.
- Role discipline: architect leads technical/design assessment, QS leads commercial arithmetic, client approves award decision.

---

## 6. Post-Contract Architect Duties
Core duties after award:
- Administer contract procedures in accordance with the agreed form.
- Issue architect instructions with clear scope, basis, and revision control.
- Monitor progress and quality through regular meetings and records.
- Coordinate with QS for interim valuation/certification inputs.

Deliverables baseline:
- Site instruction logs.
- Drawing and document revision tracker.
- Progress and issue registers tied to contractual milestones.

---

## 7. Variations and Change Control
Variation workflow:
1. Identify and define change scope.
2. Confirm reason (client change, statutory requirement, coordination issue, unforeseen condition).
3. Issue formal instruction/change record.
4. Obtain valuation input (typically QS-led) and track time/cost effect.
5. Update contract sum/time records and maintain audit trail.

Risk controls:
- No verbal-only scope changes.
- Keep causation and chronology evidence.
- Distinguish provisional design development from instructed change.

---

## 8. Certification and Payment Interfaces
- Architect and QS roles must stay coordinated and procedurally correct.
- Keep interim certification records consistent with measured/proven progress.
- Track withheld items, defects-related deductions, and adjustment events transparently.

Good practice:
- Maintain a single source register for certificates, dates, and associated backups.
- Confirm contractual notice periods are met for entitlement-related events.

---

## 9. Practical Compliance Checklist
- Tender package internally coordinated and issue-controlled.
- BoQ and design information technically aligned.
- Contract particulars and amendments reviewed for operability.
- Contract family and edition clearly identified (e.g., HKIA private form with/without quantities, GCC, or design-and-build form) and recorded in tender controls.
- Tender clarifications/addenda fully logged.
- Architect tender-stage actions are evidenced (briefing attendance, technical compliance review, qualification risk assessment, written recommendation input).
- Variation and instruction records auditable from instruction to valuation.
- Payment/certification timeline maintained with supporting evidence.
- If NEC is used: Early Warning + Compensation Event + Programme + Communications registers are established and response times are tracked.

---

## 10. NEC (New Engineering Contract) — Tender + Contract Administration Essentials
Use this when the project adopts NEC4/NEC3 (e.g., NEC Engineering and Construction Contract) or NEC-aligned practices.

Core NEC concepts to include in tender review and post-award administration:
- **Roles and authority**: Employer/Client, Project Manager (PM), Supervisor, Contractor (and Designer where applicable). Confirm who issues instructions, who accepts the programme, and who carries out tests/inspections and defect processes.
- **Communication discipline**: NEC relies on formal “communications” with defined reply periods. Set up a single controlled channel and a communications register.
- **Early Warning (EW)**: A proactive risk system. Ensure the team runs EW notifications, EW register, and risk reduction meetings; treat EW as an operational rhythm (not informal emails).
- **Compensation Events (CEs)**: NEC’s change/entitlement mechanism (broader than “variations”). Track:
  - CE triggers per contract,
  - Who notifies (PM/Contractor) and when,
  - Quotation / assessment deadlines,
  - The impact on **Prices** and **Completion Date / Key Dates** (and in NEC4, “implemented” events).
- **Programme management**: The accepted programme is central. Confirm tender requirements for baseline programme quality and submission/acceptance cycles; after award, track programme submissions, reasons for non-acceptance, and revised programme timelines.
- **Risk allocation and cost mechanisms**: Identify whether it’s activity schedule/BoQ/target cost/reimbursable/management. Align QS cost control, design administration, and change control to the chosen mechanism.
- **Quality management under NEC**: Supervisor tests/inspections, defects, and acceptance criteria. Ensure the Works Information/specs are complete enough to avoid scope ambiguity and testing/commissioning disputes.
- **Payment**: NEC uses assessment-based payment with defined assessment dates and supporting information requirements; coordinate PM/QS workflows so assessments are timely and evidence-backed.
- **Dispute avoidance and resolution**: NEC expects issues to be surfaced early (EW/CE/programme). Check adjudication/dispute steps and ensure notices and records support fast resolution.

Tender-stage NEC checks (high-impact):
- **Works Information quality**: scope, standards, interfaces, constraints, commissioning/testing, temporary works responsibilities, and design responsibilities (if any) are explicit.
- **Contract Data completeness**: key dates, access dates, reply periods, defects correction period, delay damages (if applicable), insurances, and any bespoke amendments.
- **Option structure awareness**: identify main option (A/B/C/D/E/F) and secondary options (X), then tailor tender return schedules and the admin plan accordingly.

---

## 11. NEC reference list — Contract types and option details to check
Use this as a quick index during tender review and when setting up the project’s administration registers.

Common Hong Kong NEC templates (especially Government / public works and quasi-government clients) most often use:
- **ECC (Engineering and Construction Contract)**: main works contract; PM/Supervisor roles; CEs + programme are central.
- **PSC (Professional Service Contract)**: commonly used for consultancy/PM-type appointments; confirm deliverables, acceptance, service change (CEs), and PI/insurance alignment.
- **TSC (Term Service Contract)**: used for term/maintenance-style services; focus on task orders, performance measures, and payment mechanism.

Sometimes encountered (project-dependent):
- **ECSC (Engineering and Construction Subcontract)**: where the client drives NEC-down-the-chain; confirm whether “back-to-back” is intended and operationally realistic.

ECC main options most commonly seen in Hong Kong practice:
- **Option A**: priced contract with activity schedule. Manage scope definition tightly; CEs adjust prices/activity schedule and time.
- **Option B**: priced contract with BoQ. Strong BoQ/measurement interface; ensure measurement rules and substantiation are clear.
- **Option C**: target cost. Requires defined cost procedures, forecasting, and pain/gain; cost control cadence becomes critical.
- **Option D**: target cost with BoQ. Combines target cost controls with measurement/BoQ discipline.

Secondary options and amendments typically seen in Hong Kong templates (confirm the actual contract data and amendments used):
- **X1 Price adjustment for inflation**: set up how indices, base dates and calculations will be evidenced/checked.
- **X5 Sectional Completion** (where phased handover is required): align Key Dates/Completion sections with programme logic and certification/testing sequences.
- **X7 Delay damages**: check trigger wording, caps, and interaction with programme acceptance and Completion/Key Dates.
- **X13 Performance bond**: confirm bond form, conditions for calling, and administration/expiry mechanics.
- **X15 Limitation of the Contractor’s liability for design** (where Contractor design is involved): verify it matches the project’s design responsibility split and PI insurance strategy.
- **X16 Retention**: confirm retention percentages, retention-free amount, and release rules; coordinate with subcontract retention logic (avoid double deductions and cashflow surprises).
- **X20 Key Performance Indicators (KPIs)**: define measurable KPIs, data sources, and consequences (payment adjustments / performance regimes).
- **X2 Changes in the law**: in some Hong Kong public-works templates this may be handled via **Z/additional conditions** instead of using X2—confirm which approach is adopted and ensure the CE trigger is correctly provided.

Always treat bespoke amendments as high-risk:
- **Z clauses / additional conditions**: can override standard NEC time-bars, CE/EW mechanics, payment checks, and subcontracting rules. Log all Z clauses and test “operability” against the intended admin process.

---

## 12. Employer's Agent / Contract Administrator Playbook

Use when acting as **Contract Administrator (CA)** or **Employer's Agent** under SFBC, GCC, D&B, or NEC. Cross-reference: `hk-cost-consultancy` (valuations), `hk-practical-completion-snagging` (PC/DLP), `hk-project-management` (client instructions).

### 12.1 Role clarity
| Function | CA / Employer's Agent | QS | PM (client) |
|---|---|---|---|
| Issue architect/PM instructions | Yes | No | Client instruction to CA |
| Certify payment (interim/final) | Yes (per contract) | Prepares valuation | Validates for client |
| Chair progress meetings | Yes | Attends | May attend |
| Determine EOT entitlement | Recommends/certifies per contract | Quantum support | Client decision on disputes |

### 12.2 Client instructions
- Obtain written client instructions before material scope, time, or cost commitments.
- Log in **Client Instruction Register**: ref, date, instruction summary, contract impact, issued CA instruction ref.
- Do not issue contractor instructions beyond client authority.

### 12.3 Contract documents for execution
Pre-award checklist:
1. Signed agreement, articles, contract particulars/appendix.
2. Drawings and specifications at award revision.
3. BoQ or pricing document (if applicable).
4. Particular/special conditions and amendment register.
5. Bonds, insurances, programme baseline (if contract requires at signing).
6. Named sub-contractor approvals and novation list (if any).

### 12.4 Issuing instructions
| Instruction type | Typical trigger | Controls |
|---|---|---|
| Variation / change | Client change, statutory, coordination | Formal instruction; QS valuation; time impact |
| Prime cost sum / provisional sum | Expenditure against PC/PS allowance | Instruction before commitment; substantiation; cap check |
| Defect rectification | Defects during works or DLP | Separate from variation unless scope change |
| Architect's instruction (general) | Clarification, opening up, sequencing | Logged; no scope creep without valuation |

**Prime cost sums / provisional sums**
- Confirm allowance remaining before authorising expenditure.
- Require quotes/invoices and scope match to description in contract.
- Record committed vs expended vs balance in PC/PS register.

### 12.5 Progress meetings and reports
**Meeting cadence (typical)**
- Monthly progress meeting with contractor (chair: CA).
- Technical coordination as required (design, samples, interfaces).

**Minimum progress report contents**
1. Works completed vs programme (summary)
2. Key events since last report
3. Instructions issued; variations status
4. Quality/safety highlights
5. Outstanding client decisions
6. Forecast completion and risks
7. Next period priorities

Issue report within agreed days after meeting; distribute to client, QS, consultants, contractor.

### 12.6 Site inspectors coordination
- Define who inspects what: CA/clerk of works, consultant inspectors, specialist testers.
- Issue written inspection instructions where contract requires.
- Consolidate reports into non-conformance and closeout registers.
- Distinguish statutory AP/RSE inspections (`hk-site-supervision`) from contract quality surveillance.

### 12.7 Commissioning, testing, and defect reporting
- Agree **Testing and Commissioning Plan** before PC (MEP, fire, lifts, drainage).
- Agree **Defect Reporting Procedure**: categories, response times, re-inspection, photo evidence.
- Cross-reference: `hk-fsd-licensing-compliance`, `hk-practical-completion-snagging`.

### 12.8 Claims — extension of time (EOT) and loss/expense
**SFBC-style process (verify contract clause numbers on project)**
1. Contractor serves notice of delay event within contractual period.
2. CA requests particulars and programme substantiation.
3. QS assesses cost effect if loss/expense claimed.
4. CA issues decision: grant EOT (with revision to completion date), reject, or grant in part.
5. Record reasons; maintain **EOT/Claim Register**.

**NEC**: use Compensation Event and Early Warning registers (see Section 10). Weather (including typhoon) may only be a CE if contract measurement rules exceed the **1-in-10-year** threshold for that month — see `hk-procurement-strategy` → `../../references/hk-typhoon-eot-by-procurement.md`.

**Typhoon / inclement weather — quick reference by procurement route**

| Route | Time (EOT)? | Money? | Notes |
|---|---|---|---|
| Traditional (SFBC / GCC) | Yes, if critical path | No (excusable, non-compensable) | AP assesses programme; verify Specified Event / inclement weather clauses |
| Design & Build | Yes, site stoppage only | No | Design or BD submission delay during T8 usually contractor risk |
| MC / CM | Yes per package; downstream risk | Risk of yes on handover delay | Interface claims between trade packages |
| NEC4 target cost | Only if > 1-in-10-year weather CE | Shared via pain/gain if CE qualifies | HKO data comparison per contract |

Full route-specific logic: load **`hk-procurement-strategy`** → `../../references/hk-typhoon-eot-by-procurement.md`.

**Controls**
- Monitor notice time-bars; late notices may be barred.
- Link EOT to programme logic; avoid retrospective approval without evidence.

### 12.9 Certificate sequence (SFBC private works — typical)

| Certificate | Purpose | Typical prerequisites |
|---|---|---|
| Interim Certificate | Payment for work done | QS valuation; CA satisfied with progress |
| Practical Completion (PC) | Works substantially complete | PC readiness gate; snag list |
| Certificate of Making Good Defects | Defects corrected at end of DLP | Final inspection; defects closed |
| Final Certificate | Release retention; close contract | Final account agreed; insurances/bonds released per terms |

Coordinate dates with QS valuations and client payment cycle. Cross-reference: `hk-practical-completion-snagging` Section 10.

### 12.10 Documentation to client
- Issue certified copies of drawings, instructions, certificates, and reports per client requirements.
- Maintain **Document Issue Log** for client transmittals.

### 12.11 CA output checklist
- [ ] Client Instruction Register current
- [ ] Progress meetings chaired; reports issued
- [ ] Instruction and variation registers auditable
- [ ] PC/PS register reconciled
- [ ] EOT/claim notices tracked to decision
- [ ] Interim certificates issued with QS valuations
- [ ] PC certificate issued with snag schedule
- [ ] Making Good Defects and Final Certificate sequence completed

---

*Reference framework to verify on live projects: project-specific contract conditions, Hong Kong standard procurement practices, consultant appointments, and client governance requirements.*
