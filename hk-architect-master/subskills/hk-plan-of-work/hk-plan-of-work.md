---
name: hk-plan-of-work
description: Activate for RIBA Plan of Work Stages 0–7 task checklists adapted for Hong Kong — stage gates, client/design/construction team duties, cost and BIM sections, with HK statutory and contractual substitutions. Use for "RIBA stage", "plan of work", stage checklist, or strategic definition through in-use.
disable-model-invocation: true
---

# HK Plan of Work (RIBA Stages 0–7)

Process **checklists** for Hong Kong building projects aligned to the RIBA Plan of Work. For **what to issue** at each stage (drawings, transmittals, scales), use `hk-deliverables-workstages`. For **client PM governance**, use `hk-project-management`.

**Full checklists:** read [hk-pow-stages-0-7.md](../../references/hk-pow-stages-0-7.md). The master router links this file directly.

---

## When to Use This Skill

Use section 9 for a scoped post-occupancy evaluation/aftercare brief, occupant questionnaire and findings report. Apply the [master role-referral rule](../../SKILL.md#specialist-role-referrals) before any specialist investigation.

| Question type | Use this skill | Use instead |
|---|---|---|
| Stage 0–7 task checklist, stage gate, "what should be done at Stage 4?" | `hk-plan-of-work` | — |
| Issue pack contents, drawing scales, transmittal | `hk-deliverables-workstages` | — |
| EOT, interim certificate, CA duties on site | `hk-tender-contract-administration` §12 | `hk-procurement-strategy` (typhoon EOT by route) |
| Procurement route, D&B vs traditional, NEC target cost | `hk-procurement-strategy` | `hk-tender-contract-administration` §4A |
| Cost plan, BoQ, valuation | `hk-cost-consultancy` | — |
| Business case, delivery plan, client reporting | `hk-project-management` | — |

## Halt criteria

- Stage checklists are advisory — confirm project-specific appointments and contract duties before treating tasks as mandatory.

---

## 2. Stage Mapping (RIBA ↔ HK ↔ Deliverables)

| RIBA | HK label | Statutory / contract anchor | Deliverables §2 |
|------|----------|-----------------------------|-----------------|
| **0** Strategic Definition | Feasibility / commission | OZP, lease, site constraints | Stage A |
| **1** Preparation and Briefing | Brief and team setup | Appointments, brief sign-off | Stage A–B |
| **2** Concept Design | Concept | Massing, PA optional, BEAM target | Stage B |
| **3** Spatial Coordination | Developed / coordinated design | GBP coordination, s.16 if needed | Stage C |
| **4** Technical Design | Tender / detailed design | Tender set, BoQ, specs | Stage E |
| **5** Manufacturing and Construction | Construction | Consent, CA, site | Stage F–G |
| **6** Handover | PC, DLP, OP | BA14, OP, O&M | Stage H–I |
| **7** Use | In-use / POE | BEAM Plus EB, FM | Post–Stage I |

---

## 3. HK Substitution Guide (UK → Hong Kong)

| RIBA / UK | Hong Kong practice |
|-----------|-------------------|
| ARB / RIBA requirements | **HKIA** Code of Conduct; **AR/AP/RSE** under Buildings Ordinance — `hk-construction-documentation` |
| RIBA Professional Services Contract | **HKIA/HKIS appointment** (Archi-SOR, consultant agreement) — `hk-fee-proposal-strategy` |
| CDM / Principal Designer | **Site H&S coordination** (FIU Cap. 59, Construction Sites (Safety) Regs, OSH Cap. 509) — `hk-construction-health-safety` |
| Party Wall Act | **Adjoining owner / DMC / common wall**; LandsD — not UK Party Wall |
| Planning + building approvals | **TPO** (s.16/s.12A, OZP) + **BO** (GBP, consent, OP) — `hk-spatial-planning`, `hk-construction-documentation` |
| BREEAM | **BEAM Plus** (NB/EB) — `hk-building-sustainability` |
| UK EPC / DEC | **BEEO**, mandatory **energy audit** (commercial), project-specific disclosure |
| CIBSE TM31 log book | Contract **O&M manuals**, as-builts, FM handover |
| Generic building contract | **SFBC** (WQ/WOQ), **GCC-Building**, **D&B**, **NEC** — `hk-tender-contract-administration` §4A |
| Clerk of works | **Site inspector** under CA; distinct from **AP/RSE** — `hk-site-supervision` |

---

## 4. Stage Gate Procedure (All Stages)

Before proceeding to the next RIBA stage:

1. **Accounts** — client has settled fees to agreed milestones (`hk-cashflow-debt-recovery`).
2. **Written approval** — client sign-off on brief, design stage, or proceed instruction (log in Client Instruction Register — `hk-project-management`).
3. **Stage report** — issue stage report summarising status, risks, cost, programme.
4. **Change control** — no unapproved scope drift; formal change if post-freeze (`hk-deliverables-workstages` §6.5).
5. **Team readiness** — consultants appointed and scoped for next stage.

Typical gate references in checklists: Stage 1 → 2 (1.1.12), Stage 2 → 3 (2.1.10), Stage 3 → 4 (3.5.6–3.5.8).

---

## 5. Role Routing (Checklist Sections)

| Professional role | Primary checklist sections | Sub-skill |
|---|---|---|
| **Project Lead / PM** | Client Team (all stages); stage gates; delivery plan | `hk-project-management` |
| **Lead Designer / Lead Consultant** | Design Team; coordination; stage reports | `hk-deliverables-workstages` §6 |
| **Designer / Architect** | Design Team; Other Activities (design); statutory submissions | `hk-concept-design`, `hk-construction-documentation` |
| **Cost Consultant (QS)** | Cost (all stages) | `hk-cost-consultancy` |
| **Contract Administrator** | Construction Team Stage 5; certificates; progress meetings | `hk-tender-contract-administration` §12 |
| **Health & Safety Advisor** | H&S strategy items (2.5.4, 4.5.8, 5.1.13–5.1.17, 5.5.22) | `hk-construction-health-safety` |

---

## 6. Per-Stage HK Reminders (Before Opening Full Checklist)

| Stage | HK focus |
|-------|----------|
| **0** | PI insurance; fee proposal; conflict of interest; commission feasibility |
| **1** | RACI; statutory list (BD, PlanD, LandsD, EPD, FSD); procurement advice (`hk-procurement-strategy`) |
| **2** | OZP/BHR/massing; BEAM Plus target; elemental cost plan |
| **3** | Design coordination freeze; s.16 planning if required; contract form in writing |
| **4** | Tender package; SFBC form ID; specialist tenders; materials sign-off |
| **5** | Consent to commence; CA playbook; valuations; EOT register; AP supervision; **construction swimlanes** — load `hk-construction-programme` + `../../references/hk-construction-sequence-swimlanes.md` |
| **6** | PC → Making Good Defects → Final; OP pathway; commissioning |
| **7** | POE / soft landings; BEAM Plus In-Use; **separate appointment** for Stage 7 services |

---

## 7. How to Use the Reference Checklists

1. Load this skill for mapping and gates.
2. Read `../../references/hk-pow-stages-0-7.md` for the full bilingual checklist (`- [ ]` items).
3. Apply Section 3 substitutions where an item still references UK practice.
4. Cross-load specialist sub-skills when an **HK note** or gate requires deep detail.
5. Pair with `hk-deliverables-workstages` to define issue packs for the same stage.

---

## 8. Practical Output Checklist

- [ ] Correct RIBA stage identified and HK mapping confirmed
- [ ] Stage gate criteria met before proceed instruction
- [ ] Applicable Client / Design / Construction / Cost / BIM sections reviewed
- [ ] UK-specific items interpreted via Section 3
- [ ] Stage report issued and filed
- [ ] Deliverable register updated if issue packs released (`hk-deliverables-workstages`)

---

*Checklists follow RIBA Plan of Work structure localised for Hong Kong. Verify live project appointments, contract form, and authority requirements.*

## 9. Post-occupancy evaluation and aftercare service

Use for an agreed Stage 7 service on a Hong Kong project. Confirm appointment, fee, access, reporting recipients and duration before undertaking extra work. POE does not replace statutory inspections, contract defect procedures or professional certification. Apply the [role-referral rule](../../SKILL.md#specialist-role-referrals): retain architectural usability and coordination; refer specialist investigations rather than supplying their conclusions.

### 9.1 Agree the service brief

Record project/occupied areas, decision to inform, baseline brief/design revisions, occupancy dates and actual uses/hours, participant groups, survey methods, monitoring scope, review dates, responsible people and outputs. Agree early-use and follow-up reviews suited to actual occupancy and seasonal conditions; do not impose a universal review interval. Distinguish a representative review from an exhaustive survey.

Request as-built information, handover/commissioning evidence, operational instructions, complaint/defect logs and available performance data. Mark missing or unreliable records. Agree accessible participation and appropriate languages, explain the purpose/use of responses, collect only necessary data and report without exposing identifiable occupants or sensitive tenant information. Obtain permissions for access, photographs and monitoring; do not enter occupied premises or change systems through this workflow.

### 9.2 Conduct and interpret the review

1. Compare the agreed brief with actual use, occupancy, layout and operating hours. Note changes since design/handover before attributing outcomes to the building.
2. Conduct a scoped walk-through with users and FM; record location, date, conditions, observed facts and reported experiences separately. Flag immediate safety concerns promptly through the responsible site/FM/emergency channels rather than waiting for the POE report.
3. Use the questionnaire below and relevant records. Record invited/responding groups and non-response; do not present a small convenience sample as representative of every occupant.
4. Compare feedback and observations with the original criteria. A satisfaction response is not a statutory, medical or technical performance finding. Refer measurement/diagnosis to the competent role or specialist.
5. Classify each issue provisionally using section 9.4; do not assign liability or label every complaint a contractor defect.
6. Agree actions, owners and evidence for review. Recheck under stated conditions after an authorised change; record unresolved issues and scope limits.
7. Feed anonymised lessons into the [brief-validation record](../hk-building-programming/hk-building-programming.md#7-user-research-and-functional-brief-validation), distinguishing project-specific findings from proposals for future briefs. Do not automatically change another project's requirements.

### 9.3 Short occupant questionnaire

Record room/zone, typical activity and time of use without requiring a person's name. Offer `Not applicable` and `Not experienced` responses. Suggested satisfaction scale: very dissatisfied / dissatisfied / neutral / satisfied / very satisfied; this is a survey convention, not a compliance threshold.

- Can you reach, find and use the spaces you need? Where do routes, doors or shared facilities cause difficulty?
- Does the layout support your activities, privacy and storage needs? Describe an example and when it occurs.
- How do you experience light/glare, noise, temperature, draughts, stuffiness or odours? Identify location/time and frequency; avoid asking for medical diagnoses.
- Can you understand and use the controls available to you? What happens outside normal hours?
- Have leakage, cleaning, maintenance or closures affected use? What was observed and what action was reported?
- What works well and should be retained? What single change would most improve use?

### 9.4 Findings report and follow-up register

| Finding type | Evidence needed before conclusion | Action owner / referral |
|---|---|---|
| Architectural design/usability mismatch | Brief, drawings, user journey and observed conditions | Architect; refer interior-led layout/detail design to **Skills-Interior-Designer-HK** |
| Suspected construction defect | Installed condition versus contract/design baseline and inspection evidence | Contract administrator and relevant designer; use [PC/defects handoff](../hk-practical-completion-snagging/hk-practical-completion-snagging.md#11-operational-readiness-and-aftercare-handoff) |
| Operating/maintenance issue | Actual schedules, instructions, maintenance/commissioning records | FM; refer technical services diagnosis to **Skills-MEP-Engineer-HK** |
| Changed use or unmet new requirement | Original versus current activity/occupancy and authorised changes | Client/architect for revised brief; specialist feasibility referrals as needed |
| Cause not established | Missing/conflicting records or measurements | Assign investigation; retain `Unresolved`, not presumed blame |

**Report:** purpose/appointment; methods, participants and limitations; design-versus-use baseline; observations and reported feedback; specialist evidence/status; findings with confidence and alternative causes; prioritised actions; follow-up and lessons.

**Action record:** finding ID/location; evidence/date/conditions; original requirement; provisional category; potential consequence; role referral; action/owner/date; verification method; status; lesson for future briefs. Multiple causes may apply. A closed complaint is not necessarily a repaired defect or corrected design.

**Hypothetical review:** office users report afternoon glare and stuffiness after more desks were added. Record changed occupancy and blind/window operating patterns, compare the brief and layout, and refer ventilation diagnosis to **Skills-MEP-Engineer-HK**. If a revised interior layout is requested, refer **Skills-Interior-Designer-HK**. Do not prescribe airflow rates or assume either contractor fault or occupant misuse. Issue a conditional findings/action record and plan a repeat review after authorised changes.

**HK context:** [ArchSD's POE teaching material](https://www.archsd.gov.hk/en/teachingkits/TK1/post_occupancy_evaluation.html) describes post-occupancy review of performance, design intent and user needs. Checked 24 November 2026. The service brief and questionnaire above are independently authored practice tools, not a mandatory scheme or rating-system assessment.
