---
name: hk-procurement-strategy
description: Activate for Hong Kong procurement route selection — traditional Design-Bid-Build, Design and Build, management contracting, construction management, NEC4 partnering and target cost — including contract form mapping, risk allocation, programme/BD interfaces, and typhoon EOT handling by route.
user-invocable: true
---

# HK Procurement Strategy

Strategic procurement advice for Hong Kong building projects (typically RIBA Stages 0–2 / brief freeze). For **tender documents, CA procedures, and contract administration**, use `hk-tender-contract-administration`. For **valuations and claim quantum**, use `hk-cost-consultancy`.

**Deep references** (load via dispatcher `references_available`):
- `references/hk-procurement-routes-comparison.md` — full narrative for all four routes
- `references/hk-typhoon-eot-by-procurement.md` — typhoon / weather delay entitlement by procurement route

---

## 1. When to Use This Skill

| Question type | Use this skill | Use instead |
|---|---|---|
| Traditional vs D&B vs management vs NEC — which route and why? | `hk-procurement-strategy` | — |
| Risk allocation (design, construction, statutory AP) by route | This skill + routes reference | — |
| NEC4 Option C pain/gain, early warning, DEVB public works | Routes reference + `hk-tender-contract-administration` §10–11 | — |
| Typhoon T8, inclement weather, EOT time vs money by contract type | Typhoon reference + §5 below | `hk-tender-contract-administration` §12.8 if acting as CA |
| Tender package, BoQ, CA certificates, variations | — | `hk-tender-contract-administration` |
| Record contract family code on tender register | Cross-link §4 below | `hk-tender-contract-administration` §4A |

---

## 2. Route Decision Guide

Answer these before locking procurement in the **Project Delivery Plan** (`hk-project-management` §4):

| Factor | Favours traditional (D-B-B) | Favours D&B | Favours management (MC/CM) | Favours NEC4 (often Option C) |
|---|---|---|---|---|
| Client type | Premium private residential; Grade A office with envelope control | Fast-track institutional; public hospitals/sports | Large phased / unpredictable programme | Major public works; MTR; Airport Authority |
| Architectural control | Strict (facade, spatial transitions, custom detail) | Only if Employer's Requirements (ER) are robust | Consultant-led design; packages integrate later | Defined in Works Information + risk register |
| Programme | Sequential design → tender → build acceptable | Overlap (e.g. foundations while superstructure designed) | Parallel trade packages (piling before tower detailed) | Depends on ECC option; EW/CE rhythm critical |
| Cost certainty at award | High at tender (BoQ); variation risk later | High fixed price if ER fixed | Lower initially; PC sums common | Shared target; pain/gain on outturn |
| Client admin capacity | Moderate | Lower design burden on client | **High** (many packages, interfaces) | **High** (registers, reply periods, CEs) |
| Statutory (BD) | Client AP manages submissions sequentially | Contractor AP; client checker | Client AP coordinates; packages tendered incrementally | Mapped in risk register; collaborative |

**Red flags**
- D&B without a mature ER → loss of finish quality and scope ambiguity.
- Management contracting with tight package handover dates → typhoon can trigger **compensable** downstream delays (see typhoon reference).
- NEC without resourcing for EW/CE/programme → contract fails operationally.

---

## 3. Summary Comparison Matrix

| Strategy | Design lead | Statutory submissions (AP role) | Cost certainty | Speed to market |
|---|---|---|---|---|
| **Traditional (Design-Bid-Build)** | Consultant architect | Managed by client's AP; high control over BD plans | High at tender; vulnerable to variations | Slower (sequential design then build) |
| **Design & Build** | Contractor's architect | AP shifts to contractor; client retains independent checking engineer | High fixed price early if ER unchanged | Fast (overlapped packages, fast-tracking) |
| **Management contracting** | Consultant architect | Client AP coordinates; trade packages integrated incrementally | Lower initially; prime cost sums | Fast (parallel execution) |
| **Construction management** | Consultant architect | Client AP coordinates; trade contractors contract with employer | Lower initially; employer bears package risk | Fast (flexible packages) |
| **NEC4 (e.g. Option C target cost)** | Variable (traditional or D&B delivery) | Coordinated collaboratively; statutory risks in risk register | Shared risk; outturn depends on target performance | Depends on option and programme |

---

## 4. Contract Form Map (HK)

Record the chosen route and **Contract Family Code** in the tender control register (`hk-tender-contract-administration` §4A).

| Procurement route | Typical contract forms | Family code (internal) |
|---|---|---|
| Traditional — private | HKIA/HKIS/HKICM Standard Form of Building Contract (With or Without Quantities, 2005/2006 editions) | `SFBC-Private-WQ` / `SFBC-Private-WOQ` |
| Traditional — public | Government General Conditions of Contract (GCC) for Building Works | `GCC-Building` |
| Design & Build — public | ArchSD D&B Conditions; DEVB Standard D&B Form | `D&B-ArchSD` / `D&B-DEVB` |
| Design & Build — private | Bespoke or HKIA-aligned D&B (verify title page) | `D&B-HK` |
| Management contracting | Bespoke MC agreement + trade package subcontracts | `MC-HK` |
| Construction management | Bespoke CM appointment + employer–trade contracts | `CM-HK` |
| NEC4 collaborative | NEC4 ECC Options A–E (HK public: commonly **Option C** target cost + activity schedule) | `NEC-ECC` |

**NEC4 public sector note:** As of the mid-2020s, NEC4 is mandatory for major Hong Kong public works under Development Bureau policy. Also used by statutory bodies (e.g. MTR Corporation, Airport Authority). **Verify the current DEVB circular and contract data on each project.**

---

## 5. Typhoon / Weather Delay — Quick Reference

Hong Kong Observatory **Typhoon Signal No. 8 (T8) or higher** typically stops site work. Entitlement differs materially by procurement route.

| Procurement strategy | Time (EOT)? | Money (delay costs)? | Assessment metric |
|---|---|---|---|
| Traditional (SFBC / GCC) | Yes, if critical path affected | No (excusable, non-compensable) | Specified Event / exceptionally inclement weather; AP assesses programme |
| Design & Build | Yes for **physical site** stoppage only | No | Design/office delay during T8 generally **contractor risk** |
| Management contracting / CM | Yes for affected package; **downstream risk** | Risk of **yes** for next trade (site handover) | Package interface and handover claims |
| NEC4 Option C/D | Only if weather exceeds **1-in-10-year** threshold for that month | Shared via pain/gain if CE qualifies | HKO historical data vs storm metrics (CE 60.1(13) — verify clause) |

**Detail:** load `references/hk-typhoon-eot-by-procurement.md`. **CA process:** `hk-tender-contract-administration` §12.8.

---

## 6. Programme and Buildings Department Interface

| Route | BD / consent programming note |
|---|---|
| Traditional | No design–construction overlap; map **28-day statutory buffers** for BD plan approvals and consents **sequentially** in master programme (`hk-consent-scheduling`) |
| D&B | Fast-track: e.g. foundation package while contractor's team refines superstructure; contractor owns submission timing risk unless ER states otherwise |
| MC / CM | Early works (excavation, lateral support, piling) can start before upper floors detailed |
| NEC4 | Programme is contractually central; weather float and CE thresholds should be explicit in accepted programme |

---

## 7. Stage-Gate Outputs (Procurement)

Before tender issue (RIBA Stage 3–4 / `hk-plan-of-work`):

- [ ] Procurement route selected and recorded in Project Delivery Plan
- [ ] Contract family code and full form title verified from draft tender (`hk-tender-contract-administration` §4A)
- [ ] Risk allocation briefed to client (design vs construction vs statutory)
- [ ] ER quality gate (if D&B) or BoQ coordination gate (if traditional)
- [ ] Typhoon season interface matrix (if MC/CM or multi-package)
- [ ] NEC: EW/CE/programme/communications plan resourced (if applicable)

---

## 8. Cross-References

| Topic | Sub-skill |
|---|---|
| Tender set, BoQ, CA playbook, certificates | `hk-tender-contract-administration` |
| Delivery plan, client instruction, contractor selection | `hk-project-management` |
| Stage 1–2 procurement checklist items | `hk-plan-of-work` + `references/hk-pow-stages-0-7.md` |
| Lead consultant procurement advice | `hk-deliverables-workstages` §6.7 |
| Claims quantum, valuations | `hk-cost-consultancy` §7 |
| Consent and BD programme | `hk-consent-scheduling` |

---

## 9. How to Use the References

1. Load this skill for route selection and summary matrices.
2. Read `references/hk-procurement-routes-comparison.md` for mechanism, contract forms, risk, HK examples, and architect/AP implications per route.
3. Read `references/hk-typhoon-eot-by-procurement.md` when assessing T8, EOT notices, or NEC weather compensation events.
4. Switch to `hk-tender-contract-administration` for post-award administration.

---

*Clause numbers (e.g. SFBC delay events, NEC 60.1(13)) are illustrative. Verify the executed contract, edition, and particular conditions on every live project.*
