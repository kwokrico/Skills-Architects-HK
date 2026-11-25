---
name: hk-professional-assessment
description: Activate for the HKIA/ARB Professional Assessment, including the eight papers, the Professional Interview, eligibility and the eight-year pass window, and where a Paper 1 or Paper 2 question is answered in this suite.
disable-model-invocation: true
---

# HK Professional Assessment

Map of the HKIA/ARB Professional Assessment. This skill names the papers and the experience gates. It does not sit the exam, predict a pass, or replace the statute.

For **which paper, who may sit, or where a Paper 1 or Paper 2 topic lives**, use `hk-professional-assessment`, then open the linked skill for the statutory answer. For other topics, see the routing table below.

## When to Use This Skill

HKIA/ARB Professional Assessment, Paper 1, Paper 2, eligibility, pass validity.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Papers, eligibility, or which skill holds a Paper 1 or Paper 2 topic | `hk-professional-assessment` | the linked skill for the statutory answer |
| Registration, title, conduct, or Cap. 201 | `—` | `hk-professional-conduct` |
| Plot ratio, site coverage, or GFA under Cap. 123F | `—` | `hk-building-codes` |
| Contract administration or scale of charges | `—` | `hk-tender-contract-administration`, `hk-fee-proposal-strategy` |

## Halt criteria

- Do not predict a pass or write a model answer as a statutory sign-off.
- Do not reproduce lecture slides, handbook syllabi, fee tables, or forms.
- The Standard Form of Agreement between Client and Architect is not in this library. Do not invent its clauses.
- Papers 3 and 4 stay inside the specialist role referral in `SKILL.md`. Do not supply structural or services design from the unloaded study guides.
- Sharing sessions, past papers, and Paper 2 lectures other than Lecture 2 are not in this library.

---

## 1. What the assessment is

The HKIA/ARB Professional Assessment is jointly organised by the Hong Kong Institute of Architects and the Architects Registration Board. It is the route by which an applicant may qualify for HKIA membership and for registration under the Architects Registration Ordinance. Section 13 of that Ordinance still has to be met before the Board registers the person. Administration sits with the HKIA Professional Assessment Committee. Lectures are annual and not compulsory.

Handbook: `hk_s_reference/HKIA-ARB PA/PA Handbook_revised_2025 July.pdf` (July 2025). Non-local architectural professionals use section 3 of that handbook. This skill does not copy the recognised-body list.

## 2. Papers (handbook section 2.2 and Appendix D, July 2025)

Eight papers plus the Professional Interview. HKIA may vary the dates.

| Paper | Subject | Type | Duration |
|---|---|---|---|
| 1 | Statutory controls in building works | Multiple choice and essay, open book | 3 hours |
| 2 | Building contracts, professional practice, professional conduct, conditions of agreement and scale of charges | Multiple choice and essay, open book | 3 hours |
| 3 | Building structures | Multiple choice, open book | 1.5 hours |
| 4 | Building services and environmental controls | Multiple choice, open book | 1.5 hours |
| 5 | Building materials and technology | Multiple choice, open book | 1.5 hours |
| 6 | Site design | Drawing, open book | 4 hours |
| 7 | Building design | Drawing, open book | 6 hours |
| 8 | Case study | Written report, treated as a 6-hour paper | 6 hours |
| — | Professional Interview | — | 0.5 hour |

Papers 1, 2, 6 and 7 are held annually. Papers 3, 4 and 5 may be held two or three times a year. Case studies are accepted annually.

A passing score stays valid for 8 years (handbook section 2.8.1). The candidate must have passed, or been exempted from, all eight papers within the preceding 8 years before the Professional Interview (section 2.5.3).

Papers 3 and 4 test architectural awareness of structure and services. A specialist design or calculation goes to **Skills-Structural-Engineer-HK** or **Skills-MEP-Engineer-HK** under the master role referral. Papers 5, 6, 7 and 8 are named here only. Their study guides are not loaded.

## 3. Who may sit (handbook sections 1.3, 2.1 and 2.5)

Three entry routes: a graduate of an HKIA/ARB accredited or recognised programme (section 2); a graduate of a programme that is not accredited or recognised, after a positive Academic Qualification Assessment (Appendix A); a non-local architectural professional (section 3).

Recognised experience is full time and is counted up to the last day of the month before the paper. A spell shorter than 5 consecutive months in one office does not count.

| Gate | Rule as printed |
|---|---|
| Category A | At least 12 months post-professional-degree experience in a local architectural practice, under an Office Supervisor who is an HKIA Member or Fellow and a registered architect. Mandatory |
| Category B | Year-out experience after the first pre-professional degree, up to 12 months. Non-local post-professional-degree experience in an architectural practice, up to 12 months. A combination of those two is still capped at 12 months. Year-out or non-local experience in a non-local associated profession is not accepted |
| Category C | Experience in an associated profession under an HKIA Member or Fellow who is a registered architect, up to 12 months, at the Professional Assessment Committee’s discretion |
| Papers 3, 4 and 5 | Accredited or recognised professional programme, plus at least 12 months of recognised practical experience |
| Papers 1, 2, 6, 7 and 8 | That programme, plus at least 24 months of recognised practical experience, including at least 12 months of Category A, and guidance from an approved Adviser for that Category A period |
| Short degree | Less than 5 years of full-time pre-professional and professional study requires extra recognised experience before Papers 1, 2, 6, 7 and 8. The extra period does not exceed 3 years, so the maximum total recognised experience before those papers is 5 years. The Committee sets the extra period |

## 4. Paper 1 mark split (lecture of 4 August 2025)

This split is the 2025 lecture, not Appendix D. A later sitting can change it. The lecture says the course is a framework and does not cover every question.

| Part | 2025 lecture |
|---|---|
| I | 40 multiple-choice questions, 2 marks each |
| II | One mandatory essay, 30 marks, and three out of four electives, 15 marks each |

The paper is 3 hours and open book. The lecture’s point is to know where the answer is, not to rely on an unseen model answer.

Lecture files: `hk_s_reference/HKIA Exam/P1/`.

## 5. Where a Paper 1 question is answered

Reading list from Lecture 1, as routes into this suite. Do not open a new statute dump.

| Instrument or topic | Open |
|---|---|
| Cap. 123, subsidiary regulations, codes under the Ordinance, PNAP and JPN on development control, statutory forms | `hk-building-codes` |
| Cap. 121 | `hk-building-codes` section 7.2 |
| Cap. 131, TPB guidelines | `hk-spatial-planning` |
| Lease and LAO practice notes | `hk-lease-compliance` |
| Cap. 127 and Cap. 531 | `references/hk-coastal-wetland-controls.md` |
| Cap. 499 | `hk-building-sustainability` |
| Cap. 172 | `hk-building-programming` |
| Cap. 507 and Cap. 572, fire codes, FSD codes | `hk-fire-life-safety` |
| Cap. 610 and OTTV | `hk-building-sustainability` |
| Site supervision code and technical memorandum | `hk-site-supervision` |
| Barrier-free access manual | `hk-accessibility-design` |

Lecture map for the files that are in the library:

| Lecture | Subject | Open |
|---|---|---|
| 2 | Buildings Ordinance: objectives, appointments, approval and consent, occupation permit, exemptions | `hk-building-codes`, `hk-consent-scheduling`, `hk-op-submission-strategy`, `hk-site-supervision` |
| 3 | Development intensity, and control of existing buildings | `hk-building-codes` section 2.2; then `hk-alterations-additions`, `hk-minor-works`, `hk-unauthorised-building-works`, `hk-mandatory-inspection` |
| 4 | Planning and lease | `hk-spatial-planning`, `hk-lease-compliance` |
| 5 | Safety, health, environment | `hk-fire-life-safety`, `hk-building-codes`, `hk-building-sustainability`, `hk-construction-health-safety` |
| 6 | Fire safety and supervision | `hk-fire-life-safety`, `hk-site-supervision` |

New building versus existing building, from Lecture 1:

| Question | Open |
|---|---|
| What may be built, and how much | `hk-spatial-planning`, `hk-lease-compliance`, `hk-building-codes` |
| How the building is designed | the performance skill for that constraint (fire, access, daylight, sustainability) |
| How the proposal is approved, and how work starts | `hk-construction-documentation`, `hk-consent-scheduling` |
| How the completed work is accepted and occupied | `hk-site-supervision`, `hk-op-submission-strategy` |
| How the building may be sold | `hk-certificate-of-compliance` |
| What may be altered, and how | `hk-alterations-additions`, `hk-minor-works` |
| Orders, and the preventive inspection schemes | `hk-unauthorised-building-works`, `hk-mandatory-inspection` |

Composite domestic plot ratio is not an outline-zoning-plan product. Building (Planning) Regulation 21(2), in `hk-building-codes` section 2.2, caps it. The outline zoning plan and the lease can be stricter than the First Schedule. Do not copy the schedule into an exam answer from memory; use the Cap. 123F summary linked from that section.

## 6. Where a Paper 2 question is answered

Lecture 2 of Paper 2 is in the library: conduct, the comparison of the two codes, and the ICAC seminar. Contract, appointment, and scale-of-charges lectures from that course are not.

| Question | Open |
|---|---|
| HKIA Code, ARB Code, Rules, title, registration | `hk-professional-conduct` |
| Prevention of Bribery Ordinance, as printed in the 18 July 2025 ICAC handout | `hk-professional-conduct` section 7 |
| Building contract, instructions, certificates | `hk-tender-contract-administration` |
| Procurement route | `hk-procurement-strategy` |
| Fee proposal and conditions of engagement | `hk-fee-proposal-strategy` |
| Standard Form of Agreement clauses | Stop. The form is not in this library |

---

*Sources: HKIA/ARB Professional Assessment Handbook, revised July 2025, sections 1.3, 2.1, 2.2, 2.3, 2.5, 2.8.1 and Appendix D; Paper 1 Lecture 1, 4 August 2025; Paper 2 Lecture 2 handouts, 18 July 2025. Library paths: `hk_s_reference/HKIA-ARB PA/PA Handbook_revised_2025 July.pdf` and `hk_s_reference/HKIA Exam/`.*
