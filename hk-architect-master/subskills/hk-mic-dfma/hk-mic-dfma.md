---
name: hk-mic-dfma
description: Hong Kong Modular Integrated Construction (MiC) and DfMA guidance, including PNAP ADV-36 links, mandatory land-sale MiC conditions, GFA concessions, and logistics coordination.
disable-model-invocation: true
---

# HK MiC and DfMA

Covers Modular Integrated Construction (MiC) and Design for Manufacture and Assembly (DfMA) implementation in Hong Kong projects, including policy triggers, GFA concession logic, and delivery logistics.

For **MiC / modular delivery strategy**, use `hk-mic-dfma`. For other topics, see the routing table below.

## When to Use This Skill

MiC, DfMA, BD concessions, module logistics.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| MiC / modular delivery strategy | `hk-mic-dfma` | `—` |
| Traditional construction procurement | `—` | `hk-procurement-strategy` |
| Structural module design | `—` | `hk-structural-systems` |
---

## 1. Policy and Approval Context

| Topic | Key Point |
|---|---|
| MiC policy driver | Government promotes MiC for productivity, safety, and quality uplift |
| Mandatory MiC cases | Certain land sale and public projects include mandatory MiC clauses |
| BD interface | Building plan submissions still require full compliance with BO Cap. 123 and related regulations |
| PNAP linkage | PNAP ADV-36 and related guidance may affect treatment of amenity features and accountable area strategy |
| Common authorities | BD, LandsD, PlanD, HyD (for transport interface), and utility undertakers |

---

## 2. MiC GFA Concession Logic (Project Screening)

Use this as early-stage feasibility logic before detailed BD/Lands submissions.

| Item | Typical Range | Notes |
|---|---|---|
| MiC-related GFA concession | 6% to 10% | Project-specific and authority-dependent; verify latest circulars and lease conditions |
| Concession basis | Added area attributable to modularization and associated plant/connection allowances | Must be clearly justified in submission schedules |
| Interaction with lease GFA cap | Lease cap can override planning assumptions | Always reconcile OZP potential vs lease ceiling |
| Interaction with PR/SC | Concession treatment must be mapped against accountable vs non-accountable area definitions | Keep one auditable GFA matrix from concept to submission |

### 2.1 Practical Decision Rule

1. Confirm whether site/brief imposes mandatory MiC.
2. Build two massing scenarios: `base conventional` and `MiC scenario`.
3. Apply preliminary concession band (6%, 8%, 10%) as sensitivity cases.
4. Test against lease GFA cap and BHR envelope.
5. Freeze a single submission narrative for BD/Lands consistency.

---

## 3. DfMA Design Coordination Checklist

| Discipline | DfMA Focus |
|---|---|
| Architecture | Module grid, facade rhythm, wet-core repetition, tolerance strategy |
| Structure | Module stacking logic, transfer zones, temporary and permanent stability |
| MEP | Vertical riser alignment, module interface connections, testing/commissioning sequence |
| Fire | Compartment continuity at module joints, fire-stopping details, inspection hold points |
| Acoustics | Junction detailing at module interfaces to control flanking transmission |
| Envelope | Water-tightness at inter-module joints, movement joints, sealant durability |

---

## 4. Logistics and Site Interface Planning

| Topic | Typical Requirement |
|---|---|
| Factory output planning | Align production lot size with site erection sequence |
| Transport route study | Check module dimensions/weight against road permits, turning radii, bridge limits |
| Lifting strategy | Crane reach, lifting windows, exclusion zones, weather constraints |
| Temporary storage | Minimize on-site buffer; prefer just-in-time delivery |
| Utility and road interface | Coordinate temporary traffic management (`hk-traffic-coordination`) and utility protection early (`hk-site-establishment`, `hk-telecom-coordination`) |
| Contingency | Plan fallback for weather delay, factory delay, or port/transport disruption |

### 4.1 Risk Hotspots

- Late freeze of module dimensions causing redesign across architecture, structure, and MEP.
- Interface tolerance mismatch between factory-built modules and in-situ works.
- Underestimated transport constraints causing permit delays and sequence breaks.
- Incomplete inspection/test plans at module joints leading to approval friction.

---

## 5. Submission Package Essentials (MiC-Focused)

- MiC design statement (why MiC, scope, and compliance path).
- GFA accountability table showing concession assumptions and reconciliation.
- Module interface drawings (architectural, structural, MEP, and fire stopping).
- Logistics and erection method statement with transport constraints.
- QA/QC and inspection test plan for factory and site interface works.

---

## 6. Joint Practice Note No. 8

JPN 8 is the MiC incentive note for new general building plans or major revisions submitted on or after **1 August 2022**. It supersedes the MiC content formerly in JPN 2 and in repealed PNAP APP-161. Plans the Building Authority approved before JPN 8 may still be read against the September 2019 JPN 2 and repealed APP-161, which disregarded **6%** of MiC floor area.

For a current submission, JPN 8 disregards **10%** of MiC floor area from gross floor area, and **10%** of MiC floor area at each floor from site coverage. That GFA disregard is **outside** the 10% overall cap in PNAP APP-151. The note also supports up to **4%** additional building height based on the total storey height of qualifying MiC floors, across the Buildings Ordinance, a section 16 minor-relaxation path, and a fast-track lease modification. Areas already exempt as green or amenity features (balcony, utility platform, common corridor or lobby, non-structural prefabricated external wall) may still be included in MiC floor area when working out the 10%.

The 6% to 10% sensitivity band in Section 2 remains a screening range for older approvals and for lease conditions that do not adopt JPN 8. Do not apply the 6% legacy figure to a general building plan submitted on or after 1 August 2022.

---

*Reference basis: Joint Practice Note No. 8 (submissions on or after 1 August 2022), PNAP APP-151, repealed PNAP APP-161 for pre-JPN 8 approvals, project-specific land-sale MiC conditions, and standard BD/Lands submission workflows.*

Catalogue detail for this topic is in `references/catalogues/pnap-hk-mic-dfma.md`. The master router links these files directly.
