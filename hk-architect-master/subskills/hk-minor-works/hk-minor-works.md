---
name: hk-minor-works
description: >
  Covers the Minor Works Control System (MWCS) under the Buildings Ordinance (Cap. 123). 
  Includes classification of Class I, II, and III works, simplified reporting 
  procedures, professional roles (AP/RSE/RMWC), and PNAP APP-147 compliance.
disable-model-invocation: true
---

# HK Minor Works Control System (MWCS)

The MWCS provides a simplified legal pathway for carrying out small-scale building works without seeking prior approval and consent from the Buildings Department (BD) under the full Section 14 process.

For **Minor works classification and MW forms**, use `hk-minor-works`. For other topics, see the routing table below.

## When to Use This Skill

MWCS Class I–III, PNAP APP-147, MW forms — not full s.14 approval.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Minor works classification and MW forms | `hk-minor-works` | `—` |
| Major A&A requiring full approval | `—` | `hk-alterations-additions` |
| UBW enforcement | `—` | `hk-unauthorised-building-works` |
---

## 1. Classification & Professional Requirements
Minor works are divided into three classes based on scale and risk.

| Class | Complexity | Required Professionals | Notification Requirement |
|---|---|---|---|
| **Class I** | High | AP, RSE (if structural), Registered Contractor | 7 days before; 14 days after |
| **Class II** | Medium | Registered Contractor (Company) | 7 days before; 14 days after |
| **Class III** | Low | Registered Contractor (Company/Individual) | 14 days after completion only |

### 1.1 Types of Minor Works (A to G)
Contractors must be registered for specific types:
* **Type A:** Alteration & Addition Works
* **Type B:** Repair Works
* **Type C:** Works relating to Signboards
* **Type D:** Drainage Works
* **Type E:** Works relating to Structures for Amenities
* **Type F:** Finishes Works
* **Type G:** Demolition Works

---

## 2. Common Minor Works Items (PNAP APP-147)
Selection of frequently used items in Hong Kong commercial and residential projects:

| Item ID | Class | Description | Key Technical Constraint |
|---|---|---|---|
| **1.1** | I | Internal staircase | Linking 2 floors only; non-structural slab opening |
| **1.23** | I | Removal of load-bearing wall | Max 10% of total length of wall on that floor |
| **2.1** | II | External wall rendering/wall tiles | Repairing area > 40m² |
| **2.16** | II | Ventilation ductwork | Max 1.2m diameter; projection < 600mm from wall |
| **3.1** | III | External wall rendering/wall tiles | Repairing area ≤ 40m² |
| **3.6** | III | Window / Glass block | Replacement of existing window in original opening |
| **3.27** | III | AC supporting frame | Max 100kg load; projection < 600mm from wall |

---

## 3. Statutory Submission Workflow

### 3.1 Class I & II Procedure
1. **Appointment:** Appoint AP (for Class I) and a Registered Minor Works Contractor (RMWC).
2. **Notification (Stage 1):** Submit **Form MW01** (Class I) or **MW03** (Class II) with prescribed plans/photos at least **7 days before** commencement.
3. **Execution:** Works must comply with the Building (Minor Works) Regulation.
4. **Completion (Stage 2):** Submit **Form MW02** (Class I) or **MW04** (Class II) with record photos/plans within **14 days after** completion.

### 3.2 Class III Procedure
1. **Execution:** Appoint an RMWC to carry out the works.
2. **Completion:** Submit **Form MW05** with record photos/descriptions within **14 days after** completion. No prior notice is required.

---

## 4. Technical Guidelines & Compliance
* **GFA Accountability:** Minor works generally should not result in an increase in Gross Floor Area (GFA) unless explicitly permitted (e.g., small plant rooms).
* **Fire Safety:** All minor works must maintain the integrity of Fire Resisting Construction (FRC) and Means of Escape (MOE) per FS Code 2011.
* **Unauthorized Building Works (UBW):** Works not following the MWCS or full BD submission are considered UBWs and subject to Section 24 enforcement orders.
* **Validation Scheme:** Allows for the "legalization" of certain pre-existing UBWs (e.g., AC brackets, canopies) through inspection and certification by an AP/RSE (PNAP APP-148).

---

## 5. Signboard Control System

Erection of a signboard is building works. Unless it falls inside the minor-works specifications, approval of plans and consent are required before it is erected or altered. The Buildings Department’s fast-track processing service may give approval and consent within **30 days**. A very small signboard fixed to an external wall needs neither prior approval nor appointment of a building professional or registered contractor only where the published page’s conditions are all met, including no additional load to any cantilevered slab and no alteration of any other structural element.

| Type | Positional rule printed on the BD page |
|---|---|
| Wall signboard | Fixed to the external wall; no part projects more than **600 mm** |
| Projecting signboard | Fixed to the external wall and projects **more than 600 mm** |
| Roof signboard | No portion within **1.5 m** of the inside face of the roof parapet or curb |

Unauthorised signboards can be the subject of a section 24(2)(c) removal order. Failure to comply is an offence (maximum imprisonment of one year, maximum fine of HK$200,000, and a daily fine of HK$20,000).

### 5.1 Validation of an existing unauthorised signboard

Validation is a way to retain an existing unauthorised signboard. It is not a consent path for a new signboard. Date the signboard before **2 September 2013** and match it to a row of the eligible-items table before offering validation. Class I validation needs an authorized person and, unless the signboard is a specified construction, a registered structural engineer. Strengthening of a Class I or Class II signboard is notified at least **7 days** before it starts. File the inspection certificate within **14 days**. The inspection date on the form, where no strengthening is involved, starts the **5-year** validation period. The owner undertakes to keep the signboard structurally safe and to remove it and notify the Buildings Department when the business ceases. A signboard on common parts needs liaison with the co-owners, the owners’ corporation, or the manager about the right to use those parts.

Keep projecting signboards within the published diagram: **4.2 m** projection, **2.4 m** lateral spacing, **3 m** opposite-side spacing, **3.5 m** over the footway, and **5.8 m** over the carriageway. A spread footing eligible for validation is display area ≤ 1 m², thickness ≤ 300 mm, height ≤ 3 m, and footing excavation ≤ 500 mm. Leave a face for a **35 mm** validation number.

Abandoned or dangerous signboards (a blank panel, a sign for a shop no longer in the building, rust, a loose anchor, a crack at the fixing, or a torn face) are identified for a dangerous-structure removal notice. That notice is not a sizing guide for a new signboard.

## 6. Reference Materials
* **PNAP APP-147:** Technical Guidelines on Minor Works Control System (The primary reference).
* **PNAP APP-148:** Validation Scheme for Unauthorised Minor Works.
* **PNAP APP-110:** Requirements for Windows and Glass Walls.
* **Building (Minor Works) Regulation (Cap. 123N)** and the fees regulation (Cap. 123O).
* **PNRC-75** and the signboard-validation addendum for the five-year validation procedure.

Catalogue detail for this topic is in `references/catalogues/minor-works-items.md`, `references/catalogues/minor-works-categories.md`, `references/catalogues/minor-works-designated-exempted.md`, `references/catalogues/pnap-hk-minor-works.md`, `references/catalogues/pnrc-hk-minor-works.md`. The master router links these files directly.
