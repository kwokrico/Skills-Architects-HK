---
name: hk-traffic-coordination
description: Activate for Hong Kong traffic consultant appointment, Traffic Impact Assessment (TIA), Temporary Traffic Management Plan (TMP), Transport Department (TD) and Highways Department (HyD) submissions, construction-phase traffic accommodation, bus stop and loading bay impacts, and lane-closure coordination.
disable-model-invocation: true
---

# HK Traffic Coordination

Covers **planning-stage TIA** and **construction-stage TMP** coordination with Transport Department (TD) and Highways Department (HyD). Distinct from acoustic/EPD noise (`hk-acoustic-design`) and highway **handover** at CC (`hk-certificate-of-compliance`).

**Deep reference:** `hk-td-submission-types.md` (via dispatcher `references_available`).

For **traffic consultant / TD / TMP / TIA**, use `hk-traffic-coordination`. For other topics, see the routing table below.

## When to Use This Skill

TIA, TMP, TD, HyD, lane closure, construction traffic.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Traffic consultant, TIA, TMP, TD submissions | `hk-traffic-coordination` | `—` |
| Planning s.16 / OZP conditions only | `—` | `hk-spatial-planning` |
| Hoarding layout (non-traffic) | `—` | `hk-site-establishment` |
| Green Area road handover at CC | `—` | `hk-certificate-of-compliance` |

---

## 1. Scope

| Stream | When | Authority | Output |
|--------|------|-----------|--------|
| **TIA** | Planning / feasibility | PlanD condition → TD | Traffic study, mitigation measures |
| **TMP** | Construction lane 1+ | TD | Hoarding egress, haul routes, temporary arrangements |
| **HyD** | Public highway works / handover | HyD | New roads, footpaths — link CC pathway |

Do not conflate **TD traffic operations** with **HyD highway engineering handover**.

---

## 2. When to Engage

- **s.16 planning condition** requiring TIA — `hk-spatial-planning` §3.3, §6.
- **Site frontage** on busy carriageway, bus route, or narrow footpath.
- **Hoarding / haul route** affects public road — `hk-site-establishment` §3.
- **MiC module delivery** — oversize transport — `hk-mic-dfma` §4.
- **Crane lifts** over carriageway — lane occupation submission.

Engage traffic consultant at **feasibility** if TIA is likely; at **tender/award** for TMP at latest.

---

## 3. Traffic Consultant Scope

| Deliverable | Typical content |
|-------------|-----------------|
| TIA report | Trip generation, parking, access, pedestrian safety |
| TMP drawings | Hoarding, signage, barriers, phasing |
| Submission liaison | TD comments, condition compliance |
| Event TMPs | Crane lifts, concrete pours, night works |

Fee basis: specialist package — `hk-fee-proposal-strategy` §8. RACI: architect coordinates layout; traffic consultant owns TD submission technical content.

---

## 4. TIA (Planning Stage)

| Aspect | Guidance |
|--------|----------|
| Trigger | s.16 condition; large trip generator; constrained access |
| Methodology | Verify PlanD/TPB and TD requirements for study type |
| Mitigation | Access geometry, loading bays, parking provision, pedestrian links |
| Interface | PlanD condition discharge before practical reliance |

TIA conditions flow into **built form** (podium access, carpark counts) — track through detailed design.

---

## 5. TMP (Construction Stage)

| Topic | TMP must address |
|-------|------------------|
| Hoarding | Pedestrian diversion, sight lines, bus stop clearance |
| Haul route | Turning radii, weight limits, time windows |
| Crane works | Lane closure, escort, emergency access maintained |
| Night works | Lighting, noise interface with EPD CNP |
| Emergency access | Fire appliance route never permanently blocked |

Freeze hoarding design only after TMP concept agreed with TD.

---

## 6. TD Submission Workflow

Load `hk-td-submission-types.md` for submission type table.

1. Pre-submission meeting (recommended for complex frontages).
2. Submit TMP / lane occupation drawings and method statement.
3. Address TD comments; obtain written approval before works on carriageway.
4. Maintain compliance during construction; update TMP for phase changes.
5. Reinstate and obtain closure confirmation where required.

**Halt:** Do not state TD approval is in place without written confirmation.

---

## 7. HyD Interface

- **TD:** temporary traffic arrangements on existing public roads.
- **HyD:** design and **handover** of public highway assets (roads, footpaths) under grant — `hk-certificate-of-compliance` §4.
- Private internal roads vs public highway: confirm boundary on lease plan and survey.

---

## 8. Programme and Risk

| Risk | Mitigation |
|------|------------|
| TMP delay blocks hoarding | Start TMP 6–8 weeks before lane 1 target |
| T8 stand-down | No lane occupation during typhoon signal; `hk-procurement-strategy` EOT |
| Bus stop relocation | Long lead — plan with TIA if possible |
| Phase change | TMP amendment before new carriageway occupation |

Interface: lane 1 (`hk-site-establishment`), lane 4 concrete pours (`hk-construction-programme`).

---

## 9. Output Checklist

- [ ] Traffic consultant appointed with clear deliverables
- [ ] TIA condition discharged (if applicable)
- [ ] TMP approved by TD before hoarding on public interface
- [ ] Lane occupation approvals for crane/lift events
- [ ] HyD scope separated from TD TMP where both apply
- [ ] Emergency access and bus routes maintained per approval

---

*Verify current TD/HyD forms and processing times. Advisory only — not TD sign-off.*
