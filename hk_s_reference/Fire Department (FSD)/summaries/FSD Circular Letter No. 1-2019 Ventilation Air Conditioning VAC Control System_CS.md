# FSD Circular Letter No. 1/2019 — Ventilation/Air Conditioning (V/AC) Control System
**Architect critical summary for schematic design**  
15 January 2019 | Fire Services Department — Licensing & Certification Command  
Immediate effect; supersedes FSD Circular Letter No. 2/2005. No change to CoP §5.27 requirements — updated schematic cases only.

---

## Regulatory Overview

This circular re-issues V/AC control system schematic guidance aligned with Section 5.27 of the FSI Code, updating Cases 12/1–12/3 and 12/5 and making Case 12/4 obsolete. It does not alter the underlying shutdown logic but gives designers operational response tables for PAU, EAF, FCU and kitchen exhaust arrangements.

---

## Critical main topics and subtopics

### 1. Drawing updates (Annex cases)

| Case | Topic | SD note |
|---|---|---|
| 12/1 | Typical kitchen ventilating system | Updated drawing FS-VEN-128A |
| 12/2 | Kitchen with fans at kitchen side + fire & smoke damper | FS-VEN-129A |
| 12/3 | Kitchen with fans at kitchen side without F&SD | FS-VEN-130A |
| 12/4 | Fans at non-kitchen side without F&SD | **Obsolete** — do not detail |
| 12/5 | Kitchen with booster fans and central system | FS-VEN-132A |

**SD takeaway:** Cross-check kitchen MVAC schematics against updated Annex cases before FSI submission; retire Case 12/4 details.

### 2. PAU / FCU shutdown logic (general cases)

| Equipment flow | PAU ≤ 1,000 l/s | PAU > 1,000 l/s | FCU > 1,000 l/s |
|---|---|---|---|
| Multi-compartment PAU (Cases 1/2, 1/3) | No PAU shutdown | Shutdown PAU | Shutdown FCU |
| Single-compartment PAU ≤ 1,000 l/s (Case 3/1) | No shutdown | Shutdown PAU | — |

### 3. PAU + EAF interlock cases

| Condition | Response |
|---|---|
| PAU may run only when linked EAF is running | Interlock mandatory |
| Probe smoke detector at EAF inlet | Trips system on smoke |
| EAF ≤ 1,000 l/s with PAU ≤ 1,000 l/s | Generally no shutdown |
| EAF or PAU > 1,000 l/s | Shutdown per scenario table |

### 4. Kitchen and commercial exhaust (Cases 12/1–12/5)

| Design feature | Requirement |
|---|---|
| Fire & smoke dampers at compartment boundaries | Coordinate with kitchen exhaust fan location (kitchen-side vs remote fan) |
| Booster fan + central system (12/5) | Follow FS-VEN-132A shutdown matrix |
| Shop-front duct entries (Cases 11.x in Annex) | Fire/smoke damper waivers only where partition has no FRR requirement |

**SD takeaway:** At SD, tabulate every PAU/EAF/FCU capacity against 1,000 l/s thresholds and assign Case numbers from the Annex — V/AC control is a submission deliverable, not a note on the MEP drawing margin.
