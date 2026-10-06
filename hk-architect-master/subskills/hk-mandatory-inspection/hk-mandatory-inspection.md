---
name: hk-mandatory-inspection
description: Activate for Hong Kong Mandatory Building Inspection Scheme (MBIS) and Mandatory Window Inspection Scheme (MWIS), including Cap. 123P, the 2023 code of practice, and PNBI appointment, projection, and report rules.
disable-model-invocation: true
---

# HK Mandatory Building and Window Inspection

Lifecycle inspection and prescribed repair for existing buildings. This is not plan approval, not plot-ratio control, and not the minor-works classification schedule.

For **MBIS / MWIS**, use `hk-mandatory-inspection`. For other topics, see the routing table below.

## When to Use This Skill

Cap. 123P, MBIS, MWIS, PNBI, prescribed inspection of external walls, projections, and windows.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| MBIS / MWIS inspection and prescribed repair | `hk-mandatory-inspection` | `—` |
| New alteration submission under s.14 | `—` | `hk-alterations-additions` |
| Class I–III minor works items | `—` | `hk-minor-works` |
| Removal orders for unauthorised works | `—` | `hk-unauthorised-building-works` |

## Halt criteria

- Cap. 123P does not start a cycle. Confirm Cap. 123 ss.30B–30E (notice, impending cycle, or voluntary early survey) before treating inspection as live.
- Prescribed repair is measured against the latest legal fabric, not an automatic upgrade to the current FS Code, barrier-free manual, or planning regulations.

---

## 1. What the regulation covers (Cap. 123P)

Cap. 123P is the inspection-scope, repair-standard, registered inspector (RI) / qualified person (QP) document, detailed-investigation, and handover rulebook under Cap. 123 ss.30B–30E.

| Point | Rule |
|---|---|
| Who is named | Name the contractor company, its authorized signatory, and the RI / QP individuals. Independence is a person-and-office test |
| Inspection content | Photos without defect identification and a repair proposal, where defects exist, do not satisfy the regulation |
| Standard of repair | “Rendered safe” is not “brought to the current FS Code, barrier-free manual, or Cap. 123F”. A current-code upgrade is a parallel A&A path |
| Tagging | Tag each external-wall item as a projection, a scheduled appendage, a scheduled fixture, or a window (QP). The wrong tag selects the wrong professional |
| Future access | Anything placed on the external wall is likely a later inspection target. Budget reachable maintenance access and demountable detailing |
| Appointment | The owner or owners’ corporation signature on the appointment notice is mandatory |

Treat MBIS/MWIS as a lifecycle constraint on common parts, external walls, projections, signboards, and windows, including on a building still at design stage (PNBI-1).

---

## 2. Two regimes on one facade (PNBI-10)

Mixed curtain wall, punched windows, and window wall are two regimes, two professionals, and two repair tracks.

- Curtain wall stays on the MBIS / RI track.
- Punched windows and window walls are the MWIS / QP track.
- Specify windows so hinges, fixings, and locks remain inspectable and replaceable from inside. The code expects inspection from the interior as far as practicable. Prefer details that accept 4-bar stainless hinges and stainless rivets or screws on a later MWIS repair.

---

## 3. Projections (PNBI-6)

Notices under Cap. 123 s.30B(3), (4), and (5) attach to projections. The same physical object (canopy versus balcony) can land on different notice parties. Freeze the deed of mutual covenant and the ownership of the external wall and of each projection before assigning repair liability.

Enclosing a balcony for kitchen or living expansion does not remove it from s.30B(5) projection inspection. Do not treat an illegal enclosure as a way out of projection liability.

---

## 4. Appointment continuity (PNBI-2 to PNBI-5)

| Note | Practice point |
|---|---|
| PNBI-2 | Fee, appointment, and independence of RI / QP / registered contractor are locked. The RI must be independent of the contractor |
| PNBI-3 | Use the specified forms. If the inspection RI is not the repair-supervising RI, budget the split appointment. Split QP appointments compress the inspection certificate to a 7-day clock |
| PNBI-4 | If the RI or QP cannot continue at inspection stage, the owners must replace that person. A nominee does not cover the absence |
| PNBI-5 | Where the MWIS qualified person is a company, the individual who must personally inspect the windows is fixed by the note. Do not leave the Form field blank |

---

## 5. Reports

| Report | Use at design or tender |
|---|---|
| Building inspection report (PNBI-7) | Defect, inspectability, and unauthorised-works map for common parts, external walls, curtain walls, canopies, and balconies. Checklists are for the RI; they are not submitted to the Building Authority |
| Building completion report (PNBI-8) | Close-out evidence after prescribed repair for facade, structure, drainage, fire-resisting construction, and removal of unauthorised works |
| Window inspection report (PNBI-9) | Component list for punched windows and window walls |

---

## 6. Coordination

- Fire-safety upgrade of pre-1987 stock is `hk-fire-life-safety` (Cap. 502, Cap. 572, Cap. 636), not a substitute for prescribed repair.
- Common-part access and exclusive-use repair duties under the Building Management Ordinance are `hk-alterations-additions`.
- Signboard validation is `hk-minor-works`.

---

*Sources: Building (Inspection and Repair) Regulation Cap. 123P (31 March 2022), Code of Practice for MBIS and MWIS (2023 Edition), PNBI-1 to PNBI-10.*
