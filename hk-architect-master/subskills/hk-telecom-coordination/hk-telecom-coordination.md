---
name: hk-telecom-coordination
description: Activate for Office of the Communications Authority (OFCA) and licensed telecommunications works in Hong Kong — cable and fibre protection and diversion, utility undertaker coordination, excavation near telecom plant, record drawings, and BD referral interfaces during site establishment and construction.
disable-model-invocation: true
---

# HK Telecom Coordination (OFCA)

Covers **licensed telecommunications works** and undertaker coordination during site establishment and construction. Distinct from **EMSD** (lifts/electrical), **CLP/HKE** (power), and **BD** building approval.

**Deep reference:** `hk-ofca-licensed-works.md` (via dispatcher `references_available`).

**Halt:** Do not certify undertaker approval or excavation clearance without written undertaker confirmation. Verify current OFCA codes and undertaker requirements at project inception.

For **OFCA / telecom / fibre diversion**, use `hk-telecom-coordination`. For other topics, see the routing table below.

## When to Use This Skill

OFCA, telecom undertakers, fibre/cable protection and diversion.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| OFCA, telecom diversion, licensed works | `hk-telecom-coordination` | `—` |
| Electrical supply (CLP/HKE) | `—` | `hk-building-services` |
| Lane 1 mobilisation (general) | `—` | `hk-site-establishment` |
| Lifts / Form 5 | `—` | `hk-building-services`, `hk-fsd-licensing-compliance` |

---

## 1. Scope — Do Not Conflate

| Body | Regulates / owns |
|------|----------------|
| **OFCA** | Telecom licensing framework; undertaker standards |
| **Licensed undertakers** | Fixed telecom plant in streets and buildings |
| **EMSD** | Electrical and mechanical installations (lifts, BEC) |
| **CLP / HKE** | Electricity supply cables and substations |
| **BD** | Coordinated utility drawings in GBP referral |

Telecom clearance is a **separate approval chain** from BD plan approval.

---

## 2. When Triggered

- New development with basement excavation or street opening.
- Hoarding footings or piling near recorded telecom plant.
- Utility diversion in lane 1 (`hk-site-establishment` §5).
- A&A works affecting common telecom risers — `hk-alterations-additions`.
- Road opening for external works / CC handover.

---

## 3. Licensed Works Framework

High-level workflow (verify live undertaker procedures):

1. **Record search** — undertaker plans; supplement with trial holes / GPR if records uncertain.
2. **Protection proposal** — if plant remains in place during works.
3. **Diversion application** — if reroute required; negotiate programme and cost.
4. **Witness and inspection** — undertaker attendance for critical exposures.
5. **Completion** — as-built records updated for handover.

Load `hk-ofca-licensed-works.md` for protection vs diversion decision tree.

---

## 4. Site Establishment Interface

Before hoarding or bulk excavation:

| Step | Action |
|------|--------|
| Search | Commission utility search including telecom |
| Mark-up | Show plant on hoarding/piling drawings |
| Protect | Install protection per undertaker spec before dig |
| Sequence | Align diversion with `hk-construction-programme` lane 1–4 |
| Sign-off | Written clearance before excavation in protection zone |

Coordinate with PM and MEP; architect ensures design drawings and PCI reflect search results.

---

## 5. Construction Coordination

- Sequence diversion before critical path excavation where possible.
- Service strike risk: stop-work, undertaker notification, incident log.
- Maintain document register: search report, approval letters, as-builts.
- Interface with external works and CC packages — `hk-certificate-of-compliance`.

---

## 6. BD and Referral Context

- Utility coordination drawings form part of GBP / E&S submissions.
- BD referral comments on utilities do **not** replace undertaker field approval.
- Keep one controlled drawing set for BD and undertaker mark-ups.

---

## 7. Risk Hotspots

| Risk | Mitigation |
|------|------------|
| Unrecorded plant | Trial holes; contingency in programme and cost |
| Late diversion application | Start search at design stage; float in lane 1 |
| Strike during piling | ITP hold point; undertaker witness |
| Incomplete as-builts | Require undertaker completion cert before backfill |

---

## 8. Cross-references

| Topic | Skill |
|-------|-------|
| Lane 1 checklist | `hk-site-establishment` |
| Stakeholder map | `hk-construction-stakeholder-register.md` |
| MEP utilities | `hk-building-services` |
| Programme | `hk-construction-programme` |
| External works CC | `hk-certificate-of-compliance` |

---

## 9. Output Checklist

- [ ] Telecom record search completed and filed
- [ ] Protection or diversion proposal submitted to undertaker
- [ ] Written undertaker approval before excavation in zone
- [ ] PCI updated with telecom constraints
- [ ] Diversion sequenced on master programme
- [ ] As-built / completion records for handover

---

*Advisory only — not undertaker or OFCA sign-off. Verify live codes and circulars.*
