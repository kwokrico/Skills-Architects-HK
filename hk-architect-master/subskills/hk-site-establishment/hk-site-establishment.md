---
name: hk-site-establishment
description: Activate for Hong Kong pre-construction and site establishment (假設工程) — mobilisation checklist, hoarding design and permits, temporary works, utility diversion coordination, neighbour liaison, site logistics, PCI pack assembly, and interface to consent (s.14) and construction programme lane 1.
disable-model-invocation: true
---

# HK Site Establishment (假設工程)

Execution playbook for **lane 1** — site mobilisation before main excavation and structure. Distinct from statutory consent timing (`hk-consent-scheduling`), programme sequencing (`hk-construction-programme`), and client governance (`hk-project-management`).

**Deep references** (load via dispatcher `references_available`):
- `hk-site-establishment-checklist.md`
- `hk-construction-stakeholder-register.md`

For **site establishment and hoarding**, use `hk-site-establishment`. For other topics, see the routing table below.

## When to Use This Skill

Pre-construction, hoarding, temporary works, utility diversion, mobilisation.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Site establishment, hoarding, lane 1 mobilisation | `hk-site-establishment` | `—` |
| Consent BA8 timelines, fast-track | `—` | `hk-consent-scheduling` |
| Construction sequence / swimlanes | `—` | `hk-construction-programme` |
| TD / TMP / TIA | `—` | `hk-traffic-coordination` |
| OFCA / telecom diversion | `—` | `hk-telecom-coordination` |

---

## 1. Scope and Position

- **This skill:** What must be in place on the ground before excavation and bulk works — hoarding, utilities, permits, neighbours, PCI.
- **Not this skill:** AP site inspection hold points during superstructure (`hk-site-supervision`); OP/BA14 completion certification (`hk-op-submission-strategy`).
- **Stakeholder index:** Load `hk-construction-stakeholder-register.md` for the full party map by phase.

---

## 2. Pre-construction Readiness Gate

Before hoarding erection or bulk excavation, confirm:

| Gate | Requirement | Cross-reference |
|------|-------------|-----------------|
| Plans | Approved E&S / hoarding drawings | `hk-construction-documentation` |
| Consent | Form BA8 granted (or concurrent path active) | `hk-consent-scheduling` |
| Supervision | SSP accepted by BD | `hk-site-supervision` |
| Contractor | RGBC / RSC appointed | `hk-consent-scheduling` §2.1 |
| Insurance | CAR, third-party, PI as per contract | `hk-professional-indemnity` |
| Land | LandsD DLO conditions for hoarding on grant land | `hk-lease-compliance` |
| Utilities | Record search completed | §5 below |
| Traffic | TMP aligned with hoarding layout | `hk-traffic-coordination` |
| H&S | PCI issued | §7 below |

Use `hk-site-establishment-checklist.md` with N/A / Pending / Cleared status per row.

---

## 3. Hoarding Design and Permits

### 3.1 Design elements

| Element | Typical requirement |
|---------|-------------------|
| Height and setbacks | Lease, OZP, BD approved hoarding plan |
| Pedestrian route | Min width, barrier-free where required — `hk-accessibility-design` |
| Viewing panels | At key pedestrian conflict points |
| Lighting | Night safety along public interface |
| Signage | Project info, safety, emergency contact |
| Gates | Vehicle and pedestrian access; lockable |
| Typhoon securing | Contractor method statement; inspect after T8 |

### 3.2 Permits and approvals

- Hoarding/scaffolding approval is tied to **approved plans and land conditions**, not to **Form BA14** (completion certificate for finished works packages / OP pathway).
- Coordinate hoarding footprint with **TMP** before erection (`hk-traffic-coordination`).
- LandsD DLO may impose additional conditions on government grant sites.

---

## 4. Temporary Works

| Item | Notes |
|------|-------|
| Site offices / welfare | Contractor layout; fire precautions |
| Tower cranes / mobile cranes | Lifting plans; exclusion zones; TD if over carriageway |
| Shoring / ELS interface | Align with geotechnical design — `hk-structural-systems` |
| Survey control | Primary benchmarks before bulk dig |
| Dewatering | Licence and discharge consent where applicable |
| Temporary power / water | CLP/HKE, WSD temporary supplies |

---

## 5. Utility and Undertaker Liaison

| Undertaker | Lane 1 actions | Skill |
|------------|----------------|-------|
| WSD | Temporary supply, mains diversion, fire main route | `hk-building-services` |
| DSD | Drainage diversion, connection sequencing | `hk-building-services` |
| CLP / HKE | Cable protection, temporary supply, substation access | `hk-building-services` |
| Towngas | Mains protection/diversion if gas serves site | This skill |
| Telecom (OFCA undertakers) | Protection, diversion, trial holes | `hk-telecom-coordination` |

**Rule:** Undertaker field approval is separate from BD plan approval. Programme float for diversion lead times (often 8–16+ weeks).

---

## 6. Authority, Undertaker, and Neighbour Interfaces

| Party | Lane 1 focus |
|-------|--------------|
| **LandsD DLO** | Hoarding on grant land, site formation obligations |
| **EPD** | **Construction Noise Permit** (Cap. 400) before prescribed activities (e.g. piling, night works) — `hk-acoustic-design` |
| **MTR Corp** | Railway protection zone, settlement monitoring if within influence |
| **CEDD / GEO** | Slope and retaining wall maintenance responsibility |
| **Adjoining owners / OC** | Access, vibration, noise notification; agreements for A&A — `hk-alterations-additions` |
| **LD** | Contractor safety plan; architect reviews PCI — `hk-construction-health-safety` |
| **BD referral** | FSD/WSD/DSD comments on E&S consent package — `hk-consent-scheduling` |

Loading/unloading bays and haul routes must match TMP and lease servicing strategy.

---

## 7. PCI and Mobilisation Pack

Pre-construction information (PCI) supports contractor safety planning (`hk-construction-health-safety` §7):

- Existing utilities and buried services (including telecom search results).
- Ground conditions summary, adjacent structures, overhead hazards.
- Design residual risks (temporary works, deep excavation).
- Site access, restrictions, and neighbour interfaces.
- Emergency and environmental constraints (CNP conditions).

Contractor mobilisation documents (review, not duplicate): safety plan, method statements, insurance, organogram, programme baseline.

---

## 8. Programme Hooks

- Align with swimlane **lane 1** (`hk-construction-sequence-swimlanes.md`).
- Typical lane 1 duration: **4–12 weeks** depending on diversions and permits (verify per site).
- Critical path candidates: telecom/power diversion, TD TMP approval, EPD CNP, LandsD hoarding clearance.
- Do not start lane 2 (excavation) until gate checklist cleared or client accepts documented residual risk.

---

## 9. Cross-references

| Topic | Skill |
|-------|-------|
| Consent BA8 | `hk-consent-scheduling` |
| TMP / TD | `hk-traffic-coordination` |
| Telecom | `hk-telecom-coordination` |
| SSP / AP duties | `hk-site-supervision` |
| PCI / CDM | `hk-construction-health-safety` |
| Master programme | `hk-construction-programme`, `hk-project-management` |

---

## 10. Output Checklist

- [ ] `hk-site-establishment-checklist.md` completed (Pending → Cleared)
- [ ] Hoarding erected per approved plan and TMP
- [ ] Utility diversions / protections signed off by undertakers
- [ ] EPD CNP obtained where required
- [ ] PCI issued and contractor mobilised
- [ ] Neighbour / MTR / LandsD interfaces documented
- [ ] Ready for lane 2 excavation sign-off

---

*Advisory only — not AP/BD/undertaker sign-off. Verify live PNAP, lease, and authority circulars per project.*
