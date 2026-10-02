# Cap 123J — Building (Ventilating Systems) Regulations
**Architect critical summary for schematic design**  
Consolidated version: 13 May 2021 | Cap. 123 sub. leg. J  
Enabling power: Cap. 123 s.38 | Commencement: **23 October 1964** | Format revision: E.R. 2 of 2021

> Scope note: Cap 123J is the **Fire Services–facing statutory rulebook for ducted inter-compartment ventilating systems**. It fixes: when the Cap applies; intake siting and mesh; fencing and inspection access; duct material / cleaning access / fire dampers at penetrations; one-building-only ducts; filter combustibility; FSD-approved electrostatic kit; owner annual RSC inspection; certificates to FSD; FSD test powers; and grandfathering of pre-1964 systems.  
> It is **not** the FS Code / FRC package, not Cap 123F (planning), not Cap 123Q (construction performance), not Cap 132 scheduled-premises HVAC rules, and not a substitute for smoke-control or MOE design. Use at SD whenever any scheme uses **ducting or trunking that crosses fire compartments**.

---

## Regulatory Overview

Cap 123J applies to every **ventilating system that embodies ducting or trunking which passes through any wall, floor or ceiling of the building from one compartment to another** (reg. 3(1)), subject to the Cap 132 scheduled-premises carve-out and the pre-1964 grandfathering in reg. 7. The enforcing “Director” is the **Director of Fire Services** (reg. 2) — so damper approvals, intake fire-hazard opinions, exemptions, certificates, and on-site tests sit with **FSD**, not BD alone.

---

## Critical main topics and subtopics

### 1. Authority & definitions that matter at SD (regs. 1–2)

| Term | Meaning in Cap 123J | SD consequence |
|---|---|---|
| **Director** | Director of **Fire Services** (reg. 2) | Intake fire-hazard opinion, fusible-link / electrostatic **type approval**, written **exemptions**, receipt of annual certificates, and authorized **tests** are all FSD decisions |
| These regulations | Building (Ventilating Systems) Regulations (reg. 1) | Cite Cap **123J** on FS narratives / consultant briefs — not Cap 123A admin alone |

**SD takeaway:** Treat Cap 123J as an **FSD compliance track** that must be coordinated with FS Code compartmentation drawings from day one. BD plan approval does not replace FSD type approvals or annual inspection duties.

---

### 2. Application trigger — when Cap 123J is “on” (reg. 3)

#### 2.1 Positive trigger (reg. 3(1))

All three elements must be present:

1. A **ventilating system**; **and**
2. That system **embodies the use of ducting or trunking**; **and**
3. That ducting / trunking **passes through any wall, floor or ceiling** of the building **from one compartment to another**

| Situation | Cap 123J applies? | SD implication |
|---|---|---|
| Supply / return / exhaust duct crosses a **fire compartment** wall, floor or ceiling | **Yes** | Full reg. 4 hardware + access + annual RSC path |
| Vertical shaft riser serving multiple storeys (each floor a compartment / each storey crossed) | **Yes** (each floor / wall / ceiling penetration) | Damper + FR continuity at **every** storey penetration — count dampers early |
| Horizontal duct in corridor / ceiling void crossing compartment walls between tenancies / suites / hotel rooms / offices | **Yes** | Ceiling coordination: damper locations = access panels |
| Duct wholly within **one** compartment (no inter-compartment penetration) | **No** under reg. 3(1) | Cap 123J threshold not triggered; still satisfy FS Code / Cap 123Q / other CoPs |
| Flexible connectors / short trunks that still pierce a compartment boundary | **Yes** if they are “ducting or trunking” crossing compartments | Do not assume “short run = exempt” |
| Natural ventilation only (no mechanical ducted VS) | Outside Cap 123J’s ducted-system framing | Design under other instruments (FS Code openings, Cap 123F light/vent, etc.) |

**SD takeaway:** Your **fire compartment plan is also your Cap 123J duct plan**. Every red line a duct crosses is a statutory damper + FR + future RSC inspection point.

#### 2.2 Absolute carve-out — Cap 132 scheduled premises (reg. 3(2))

Cap 123J **shall not apply** to any ventilating system in buildings which are **scheduled premises** for the purposes of the Public Health and Municipal Services Ordinance (**Cap. 132**).

| Check | Action |
|---|---|
| Is the building / premises Cap 132 scheduled? | Confirm early with AP / licensing counsel (food business, certain entertainment, etc. as scheduled under Cap 132) |
| If **yes** | Cap 123J **off** — use the Cap 132 / FEHD (or relevant) ventilating regime instead; do not dual-cite Cap 123J as if it governs |
| If **no** | Cap 123J applies whenever reg. 3(1) trigger is met |

**SD takeaway:** Mixed-use schemes (e.g. residential tower + F&B podium) may split regimes by premises type — map which floors / tenancies are Cap 132 scheduled before freezing a single MVAC compliance narrative.

#### 2.3 Interaction with reg. 7 (existing systems)

Reg. 3(1) says application is also “save as provided … in regulation 7.” Pre-23 Oct 1964 systems can be inside Cap 123J’s *scope* but temporarily free of **reg. 4 construction requirements** until altered / removed / FSD fire-hazard finding. See §9.

---

### 3. Hard design rules — full reg. 4(1) unpack (a)–(h)

Reg. 4(1) applies to every Cap 123J system **unless** FSD grants a written exemption under reg. 4(2) **or** the system is still under reg. 7 grandfathering.

#### 3.1 Moving parts — secure fencing (reg. 4(1)(a))

| Rule | Detail |
|---|---|
| Requirement | **All moving parts** of the ventilating system shall be **securely fenced** |
| Typical kit | Fan blades / belts / couplings / drive assemblies |
| SD / detail implication | Plant-room layout must allow **guarded** equipment with clearance for fence removal (see also spindle access under (b)(i)); public / tenant-accessible plant decks need physical barriers that still permit RSC inspection |

#### 3.2 Whole-system inspection access + two mandatory access cases (reg. 4(1)(b))

**General rule:** every part of the system shall be **accessible for the purposes of inspection**.

**In particular** (non-exhaustive but mandatory):

| Sub-clause | Exact requirement | Architectural / spatial claim |
|---|---|---|
| **(b)(i)** Fan spindle | Spindle of **every fan** so sited that its **guard may be removed** and a **tachometer** applied | Do not sandwich fans tight against walls / beams / acoustic enclosures with no spindle approach; allow guard-off + instrument space |
| **(b)(ii)** Intake **and** exhaust | **Every** air intake and exhaust accessible for **measurement** | Louvres / cowls / roof terminations / façade intakes must be reachable (catwalk, plant platform, reachable roof, openable grille) — not sealed behind unopenable cladding |

**SD takeaway:** Access is a **Cap 123J statutory duty**, not only an O&M preference. At massing: roof plant, AHU rooms, riser doors, façade intake ledges, and false-ceiling access panels must be sized for inspection **and** annual damper / filter / precipitator checks (reg. 5).

#### 3.3 Air-intake siting bans (reg. 4(1)(c))

No air intake shall be sited in any place:

| Ban | Wording | Practical SD keep-away list |
|---|---|---|
| **(c)(i)** | Which **in the opinion of the Director** constitutes a **fire hazard** | Refuse rooms / chutes; kitchen / restaurant exhaust confluence; LPG / dangerous-goods stores; transformer / switch rooms; carpark exhaust outlets; hot-work / ignition yards; fire-service access conflict zones; smoke-discharge proximity |
| **(c)(ii)** | Where **waste or rubbish is likely to accumulate** | Service lanes with dumpsters; loading-bay trash corners; grade-level dead recesses; behind low landscape walls that trap litter |

**SD takeaway:** Intake location is an **FSD-opinion** risk. Lock intakes on roof / high façades / clean courtyards early; document separation from refuse, kitchen exhaust, and DG. Do not rely on “we’ll screen it later.”

#### 3.4 Intake opening screen — hard number (reg. 4(1)(d))

| Item | Statutory rule |
|---|---|
| Where | Opening of **every** air intake |
| Material | Constructed of **corrosion-resistant** material |
| Mesh | **Not greater than 12 mm** |

**SD takeaway:** Specify mesh ≤ 12 mm in the architectural / façade / MVAC schedule at SD. Coordinate with insect screens, weather louvres, and acoustic attenuators so the **statutory mesh** is not defeated by a coarser outer grille alone (the intake opening itself must have the compliant screen).

#### 3.5 Every duct — material, cleaning access, fire damper (reg. 4(1)(e))

##### (e)(i) Material
- Wholly constructed of **non-combustible** material
- Strength and durability **not less than** that of **galvanized sheet-iron or steel**

**SD takeaway:** Combustible duct liners / plastic ducts / timber trunks that form the duct itself fail this Cap. Coordinate acoustic lining so the **structural duct** remains non-combustible to the GI/steel durability bar.

##### (e)(ii) Cleaning access
- Accessible for cleaning **throughout its entire length**

**SD takeaway:** Long buried runs in transfer structures, deep beams, or sealed decorative soffits without cleaning doors / removable panels fail. At SD: riser strategy, horizontal mains routes, and ceiling depths must include **cleaning access intervals** along the full length — not only at AHUs.

##### (e)(iii) — **Repealed** (L.N. 7 of 2020)
Former sub-paragraph repealed. Do **not** design to any historic Cap 123J (e)(iii) wording from old editions. Current compliance is (e)(i), (ii), and (iv) only under (e).

##### (e)(iv) Fire damper at every floor / wall / ceiling penetration — critical geometry

At the point where the duct **passes through any floor, wall or ceiling**, fit a damper that:

| Requirement | Spec |
|---|---|
| Damper location | **At the penetration point** (floor / wall / ceiling crossed) |
| Operation | Operated by **fusible links** of a type **approved by the Director** (FSD) |
| Temperature | Designed to operate up to **69°C** |
| Fire resistance | Constructed **or protected** to resist fire for a period **not less than** the period for which the floor / wall / ceiling penetrated is designed to resist fire |

**SD implications (expand):**
- Compartment FR rating (e.g. 1-hour / 2-hour walls and floors under FS Code / FRC) **drives damper FR** — match or exceed the penetrated element
- Every storey penetration of a vertical riser = a Cap 123J damper point
- Every compartment wall crossed by a corridor / ceiling duct = a damper + **access panel** for annual RSC inspection (reg. 5)
- Fusible-link **type** must be on FSD’s approved list — do not substitute unapproved hardware at tender
- “Constructed **or protected**” allows damper assemblies with fire-protective cladding / installation methods that achieve the required FR period — still prove equivalence to FSD / FS submission

#### 3.6 One duct, one building (reg. 4(1)(f))

| Rule | **No duct shall serve more than one building** |
|---|---|

| Scheme type | Cap 123J risk | SD fix |
|---|---|---|
| Linked towers sharing one MVAC duct spine | **Forbidden** if a single duct serves both buildings | Separate systems per building; or break / terminate and restart at the legal building boundary |
| Podium + multiple towers as separate buildings | Shared podium duct into two towers | Split at tower interfaces; no continuous duct serving Building A and Building B |
| Single building with multiple wings / blocks under one building as defined | Usually OK if legally **one** building | Confirm “building” definition with AP / lease / BD — Cap 123J uses “building,” not “lot” |
| Footbridge / connection with ducts between buildings | High risk | Independent VS each side; no continuous duct across the connection |

**SD takeaway:** This is a **massing / legal-entity** constraint as much as an M&E one. Freeze building subdivision early before shared plant is assumed.

#### 3.7 Filters — non-combustible; steel wool banned (reg. 4(1)(g))

| Rule | Detail |
|---|---|
| Construction | Every filter wholly of **non-combustible** material |
| Explicit ban | **Other than steel wool** — steel wool is **not** acceptable even if “metal” |

**SD takeaway:** Spec filters as non-combustible media only. Ban steel-wool type products in schedules and shop drawings.

#### 3.8 Electrostatic filters / precipitators — FSD type approval (reg. 4(1)(h))

| Rule | Every electrostatic filter or precipitator shall be of a type **approved by the Director** |
|---|---|

**SD takeaway:** Kitchen / industrial ESP units and similar must be on FSD-approved types before procurement. Allowance for “or equal” without FSD approval is non-compliant.

---

### 4. FSD exemption path (reg. 4(2)) — do not design on hope

| Element | Requirement |
|---|---|
| Who may exempt | **Director** (FSD) |
| When | Where he **thinks fit** |
| How applied for | **Application in writing** in that behalf |
| How granted | **Notice in writing** |
| Scope | Exempt from **all or any** of the provisions of reg. 4(1) |
| Conditions | Subject to **such conditions as he may specify** |

**SD takeaway:**
- Base the scheme on **full reg. 4(1)** compliance
- Treat exemption as last-resort variance with conditions (may require compensatory fire measures)
- Programme: written application → written notice — do not freeze SD on an assumed exemption

---

### 5. Owner duties — continuous maintenance + annual RSC inspection (reg. 5)

Applies to the **owner of any building** in which a Cap 123J ventilating system is installed.

#### 5.1 Two concurrent duties (reg. 5(1))

| Duty | Interval | Substance |
|---|---|---|
| **(a)** Safe & efficient working order | **At all times** | Whole Cap 123J system kept safe and efficient |
| **(b)** Inspection of listed components | Intervals **not exceeding 12 months** | Every **damper**, **filter** and **precipitator** inspected by a **registered specialist contractor in the appropriate category** |

**SD takeaways:**
- Design for **repeatable annual access** to every damper / filter / precipitator — not only construction commissioning access
- False ceilings, hotel corridors, office fit-outs, and retail shopfronts must keep damper locations **inspectable** after fit-out
- RSC category must be the **appropriate** ventilating / related specialist category under Cap 123 — brief the client’s FM / IO early

#### 5.2 Offence (reg. 5(2))

| Who | Offence | Penalty |
|---|---|---|
| Any person who contravenes reg. 5(1) | Guilty of an offence | Fine at **level 1** (E.R. 2 of 2021) |

---

### 6. RSC certificates — content, timing, offences (reg. 5A)

#### 6.1 Issue & copy duties (reg. 5A(1))

After inspecting any ventilating system, the RSC in the appropriate category shall:

1. Within **14 days** of the inspection, **issue a certificate** to the person on whose instructions the inspection was carried out; **and**
2. **Send a copy** of that certificate to the **Director** (FSD)

#### 6.2 Mandatory certificate contents (reg. 5A(2))

| Field | Must state |
|---|---|
| **(a)** | The **address** at which the inspection was carried out |
| **(b)** | Whether or not the **dampers, filters and precipitators** are in **safe and efficient working order** |
| **(c)** | The **name and address** of the RSC (appropriate category) who carried out the inspection |

#### 6.3 Offences (reg. 5A(3))

| Conduct | Penalty |
|---|---|
| Contravene reg. 5A(1) (late / no certificate / no FSD copy) | Fine at **level 1** **and** imprisonment for **6 months** |
| Make or cause a certificate statement known (or that ought reasonably to be known) to be **false in a material particular** | Same: level 1 fine **+** 6 months |

**SD takeaway:** Architecture that hides dampers behind sealed décor creates **compliance liability** for owners and RSC access failure — design access so truthful annual certificates are physically possible.

---

### 7. FSD testing power (reg. 6)

Any officer of the Fire Services Department **authorized in writing by the Director** may carry out such **tests** of any Cap 123J ventilating system as may be necessary to ascertain whether it is in **safe and efficient working order**.

**SD / handover implications:**
- Systems must remain **testable** after occupation (access, isolation, measurement points at intakes / exhausts — see reg. 4(1)(b))
- Coordinate with FS inspections / FSI commissioning so Cap 123J testability is not blocked by locked plant rooms or sealed louvres
- This is an ongoing FSD power, not only a construction-stage check

---

### 8. Existing / pre-1964 systems — grandfathering (reg. 7)

Where a Cap 123J-applicable ventilating system was installed in any building **before commencement** (**23 October 1964**):

There is **no requirement to comply with regulation 4** unless and until either:

| Trigger | Effect |
|---|---|
| **(a)** The ventilating system has been **removed** or is **altered in any way** | Full reg. 4 compliance required |
| **(b)** The Director is of the opinion that the system constitutes a **fire hazard** | Full reg. 4 compliance required |

**SD implications for A&A / adaptive reuse / heritage:**
- “Altered **in any way**” is a wide trigger — duct reroutes, AHU replacement tied into existing trunks, new branch penetrations, damper works, and material changes can end grandfathering
- Early survey: installation date, as-built ducts, compartment crossings, existing damper / filter condition
- Decide at SD: **(i)** leave pre-1964 system wholly untouched, or **(ii)** redesign to current reg. 4 (materials, 69°C FSD-approved fusible links, intake mesh ≤ 12 mm, cleaning access, etc.)
- Even if reg. 4 is deferred, **regs. 5 / 5A / 6** (owner maintenance, annual RSC inspection of dampers/filters/precipitators, FSD tests) still sit in the Cap’s structure once the system is one “to which these regulations apply” — do not assume grandfathering = zero Cap 123J duties; confirm with AP/FSD on live cases

---

### 9. Schematic-design checklist (print this)

**Trigger & regime**
- [ ] Confirm ducting / trunking crosses compartment wall / floor / ceiling → Cap 123J **on** (reg. 3(1))
- [ ] Confirm building / premises is **not** Cap 132 scheduled (else Cap 123J **off**) (reg. 3(2))
- [ ] Confirm “Director” track = **FSD** for approvals / certificates / tests (reg. 2)

**Reg. 4 hardware & geometry**
- [ ] All moving parts securely fenced; fan spindles reachable for tachometer with guard off (reg. 4(1)(a)–(b)(i))
- [ ] Every intake **and** exhaust accessible for measurement (reg. 4(1)(b)(ii))
- [ ] Intakes clear of FSD fire-hazard opinion zones and rubbish accumulation (reg. 4(1)(c))
- [ ] Every intake opening: corrosion-resistant screen, mesh **≤ 12 mm** (reg. 4(1)(d))
- [ ] Ducts wholly non-combustible, durability ≥ GI / steel (reg. 4(1)(e)(i))
- [ ] Cleaning access **throughout entire duct length** (reg. 4(1)(e)(ii))
- [ ] Do **not** cite repealed (e)(iii)
- [ ] Fire damper at **every** floor / wall / ceiling penetration: FSD-approved fusible links, operate to **69°C**, FR ≥ penetrated element (reg. 4(1)(e)(iv))
- [ ] **No duct serves more than one building** (reg. 4(1)(f))
- [ ] Filters non-combustible; **no steel wool** (reg. 4(1)(g))
- [ ] Electrostatic filters / precipitators = FSD-approved types only (reg. 4(1)(h))
- [ ] No SD reliance on reg. 4(2) exemption unless written FSD notice secured

**O&M / certificates / existing**
- [ ] Annual (≤ 12 months) RSC access designed for every damper / filter / precipitator (reg. 5)
- [ ] Certificate path understood: 14 days + copy to FSD; address / pass-fail / RSC particulars (reg. 5A)
- [ ] System remains FSD-testable after occupation (reg. 6)
- [ ] If pre-23 Oct 1964: alteration vs untouched strategy locked before SD freezes MVAC (reg. 7)

---

### 10. Typical SD failure modes (architect watch-list)

| Failure mode | Which clause bites |
|---|---|
| Shared duct spine across two towers / “linked buildings” | reg. 4(1)(f) |
| Intake next to refuse room / kitchen exhaust / DG store | reg. 4(1)(c) |
| Coarse façade grille without ≤ 12 mm corrosion-resistant intake screen | reg. 4(1)(d) |
| Damper missing or under-rated vs compartment FR at shaft floor slabs | reg. 4(1)(e)(iv) |
| Long duct buried in transfer / sealed soffit with no cleaning doors | reg. 4(1)(e)(ii) |
| Fan buried so spindle / tachometer access impossible | reg. 4(1)(b)(i) |
| Fit-out seals off dampers → annual RSC inspection impossible | regs. 5 & 5A |
| A&A “minor” duct tweak on pre-1964 system without full reg. 4 upgrade | reg. 7(a) |
| Assuming Cap 123J applies to Cap 132 scheduled premises | reg. 3(2) |
| Specifying unapproved ESP / fusible-link type | regs. 4(1)(h) & 4(1)(e)(iv) |

---

### 11. Cross-reference map (do not confuse)

| Need | Instrument |
|---|---|
| Inter-compartment ducted VS: intakes, ducts, dampers, filters, annual RSC | **Cap 123J** (this Cap) |
| Fire compartmentation, FR periods, smoke control, MOE | FS Code / FRC (+ related Cap 123 fire provisions in plans) |
| Cap 132 scheduled premises HVAC / licensing | Cap **132** regime — Cap 123J **excluded** |
| Construction performance / large person-entry ducts (broader) | Cap **123Q** (+ APP-53 CoPs) — not a substitute for Cap 123J |
| Plan submission / AP duties on building works | Cap **123A** |
| RSC registration categories (who may inspect) | Buildings Ordinance RSC framework pairing with Cap 123J regs. 5 / 5A |
| FSD type approvals (fusible links, electrostatic kit) | Director of Fire Services under Cap 123J regs. 4(1)(e)(iv) & 4(1)(h) |

---

### 12. Regulation index (quick jump)

| Reg. | Title | Architect focus |
|---|---|---|
| 1 | Citation | Name: Building (Ventilating Systems) Regulations |
| 2 | Interpretation | **Director = Director of Fire Services** |
| 3 | Systems to which regulations apply | Inter-compartment duct/trunk trigger; Cap 132 carve-out |
| 4 | Requirements | Fencing, access, intakes, mesh ≤ 12 mm, duct material/cleaning/dampers 69°C, one building, filters, ESP; FSD exemption |
| 5 | Duty of owners | Continuous safe order + ≤ 12-month RSC inspect of dampers/filters/precipitators; level 1 fine |
| 5A | RSC certificates | 14 days; copy to FSD; required contents; level 1 + 6 months for breach / false cert |
| 6 | Power of authorized officer | FSD written-authorized tests for safe & efficient order |
| 7 | Existing systems | Pre-**23 Oct 1964**: reg. 4 deferred until remove/alter **or** FSD fire-hazard opinion |

---

*Source: Cap. 123J Building (Ventilating Systems) Regulations — consolidated version 13 May 2021 (English). This summary is for design workflow only; verify against the current verified copy and FSD practices on live projects.*
