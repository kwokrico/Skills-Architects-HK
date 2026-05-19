---
name: hk-plan-of-work
description: Activate for RIBA Plan of Work Stages 0–7 task checklists adapted for Hong Kong — stage gates, client/design/construction team duties, cost and BIM sections, with HK statutory and contractual substitutions. Use for "RIBA stage", "plan of work", stage checklist, or strategic definition through in-use.
user-invocable: true
---

# HK Plan of Work (RIBA Stages 0–7)

Process **checklists** for Hong Kong building projects aligned to the RIBA Plan of Work. For **what to issue** at each stage (drawings, transmittals, scales), use `hk-deliverables-workstages`. For **client PM governance**, use `hk-project-management`.

**Full checklists:** load `references/hk-pow-stages-0-7.md` (available via dispatcher `references_available`).

---

## 1. When to Use This Skill

| Question type | Use this skill | Use instead |
|---|---|---|
| Stage 0–7 task checklist, stage gate, "what should be done at Stage 4?" | `hk-plan-of-work` | — |
| Issue pack contents, drawing scales, transmittal | `hk-deliverables-workstages` | — |
| EOT, interim certificate, CA duties on site | `hk-tender-contract-administration` §12 | `hk-procurement-strategy` (typhoon EOT by route) |
| Procurement route, D&B vs traditional, NEC target cost | `hk-procurement-strategy` | `hk-tender-contract-administration` §4A |
| Cost plan, BoQ, valuation | `hk-cost-consultancy` | — |
| Business case, delivery plan, client reporting | `hk-project-management` | — |

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
| **5** | Consent to commence; CA playbook; valuations; EOT register; AP supervision |
| **6** | PC → Making Good Defects → Final; OP pathway; commissioning |
| **7** | POE / soft landings; BEAM Plus In-Use; **separate appointment** for Stage 7 services |

---

## 7. How to Use the Reference Checklists

1. Load this skill for mapping and gates.
2. Read `references/hk-pow-stages-0-7.md` for the full bilingual checklist (`- [ ]` items).
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
