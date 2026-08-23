# Practice Notes for Registered Contractors (PNRC)
**Architect critical summary for schematic design**  
Buildings Department — PNRC series (gateway PNRC 1, July 2012; individual notes revised on rolling basis)

> Scope note: PNRCs are BD’s contractor-facing channel for how the Building Authority applies the Buildings Ordinance (BO), subsidiary regulations, and related site procedures. They do **not** replace PNAP, CoPs, or Cap 123N Schedules — but they flag **hold points, test regimes, and construction constraints** that must be designed in from SD. Cross-read matching PNAPs (especially APP-19, APP-23, APP-24, APP-37, APP-53, APP-55, APP-126, APP-147, APP-155, APP-158) for the AP/RSE side.

---

## Regulatory Overview

PNRCs apply to **Registered Contractors** (RGBC, RSC, RMWC) on all BO-controlled building and street works — new build, A&A, demolition, minor works, and validation schemes. For schematic design, treat PNRCs as the **construction-compliance layer**: they tell you what must appear on approved plans, what tests and supervision BD will impose at consent, and which future repair/alteration paths (MWCS, validation) your envelope, projections, and site interface must support.

---

## Critical main topics and subtopics

### 1. SD routing — which PNRC cluster governs your design decision

| If you are fixing at SD… | Lock these PNRCs first | Paired PNAP / CoP |
|---|---|---|
| Façade, CW, windows, window walls | **47**, **84**, **60** | APP-37, APP-53, Glass Code 2018 |
| External tiles / render | **67** | ADV-31 |
| Balconies, canopies, projecting slabs | **27** | APP-19, APP-105 |
| Metal gates at boundary | **68** | APP-146 |
| Signboards / shopfront projections | **75**, **71** | APP-126, APP-155 |
| Railway-adjacent / Area 3 sites | **14** | APP-24, APP-39 |
| Demolition or phased redevelopment | **6**, **83** | Demolition CoP 2004, TMSP 2009 |
| Precast structure | **63** | Precast CoP 2016 |
| Site hoardings / covered walkways | **4** | APP-23 |
| Vehicular run-in/out | **65** | HyD standard drawings |
| Scaffolding screens / plastic sheeting | **85** | — |
| Future A&A without full s.14 | **71**, **52** | Cap 123N Sch 1, Technical Guidelines MWCS |
| Approval/consent conditions stack | **80**, **76**, **77** | Site Supervision CoP 2009, APP-158 |
| Asbestos risk (existing fabric) | **15** | ADV-1, Demolition CoP |
| Environmental nuisance | **17** | EPD / FEHD circulars |

---

### 2. Envelope — curtain wall, windows, window walls (PNRC 47, 84, 60)

**Performance stack (B(C)R):** wind loads, horizontal imposed loads (Table 3 where no barrier), opening protection, corrosion, fire/smoke spread between floors, lighting/ventilation (B(P)R).

| Element | SD / detail design lock-in |
|---|---|
| **Aluminium windows (47)** | Min 2 mm aluminium; mullion depth ≥ 38 mm; fixing lugs SS or HDG ≥ 1.5 mm @ **300 mm centres max** (wider spacing needs AP/RSE justification); side-hung width ≤ **700 mm**; top-hung area ≤ **2.5 m²**; built-in projecting fin with drip at head; 4-bar hinges: SS ≥ 2.5 mm, ≥ 3 rivets/screws per bar, length ≥ **60% sash width**, dissimilar-metal isolation; field water penetration test advised (Glass Code Annex A) |
| **Tempered glass (84)** | ISO 9001 factory; QAS + RSE statement **14 days before production**; **heat soak** BS EN 14179-1 per Glass Code 9.3; QCS (T3) supervises ≥ **30% of panes**; QCC (T1) full-time at factory with independent data logger; compliance reports before OP/BA14; structural sealant compatibility/adhesion/deglazing certificates before OP |
| **Spider fixings (84)** | Proof load test per Steel CoP — sampling ≥ **1% or 3 nr**; exempt if on BD Central Data Bank (PNAP ADM-20) |
| **Locking devices (84)** | Non-combustible durable materials; FOS **1.8** on characteristic strength; proof load ≥ **0.1% or 5 nr**; one handle bar ≤ **8 locking points** |
| **CW safety test (84)** | HOKLAS (or MRA) lab before OP — representative panes justified; exempt for MW fast-track repair (ADM-19) or MW item **1.61** |
| **Spare glass (84 App E)** | Schedule A at completion → maintenance manual; reuse in A&A with RSE inspection + Schedule B |
| **Water seepage (60)** | Design roofs, external walls, windows, wet areas, basements to B(C)R 3, 34, 38, 41, 48; follow BD *Guidelines on Prevention of Water Seepage in New Buildings* |

**SD takeaway:** Window module sizes, hinge types, and CW system selection are **approval conditions**, not site tweaks. Reserve OP pathway time for heat soak, CW test, sealant Certs, and locking-device tests.

---

### 3. External finishes — wet-fixed tiles (PNRC 67)

| Topic | Requirement |
|---|---|
| **Movement joints** | Full-depth in render; between panels at regular intervals; at substrate CJs/control joints; joints **≥ 3 mm** (typically **8–10 mm**) |
| **Render build-up** | Each coat **8–16 mm**; total ≤ **20 mm**; **6 weeks** drying after concrete before render (unless bonding agent remedial); work **top-down** by storey |
| **Mechanical keys** | Spatter dash within **24 h** of strike; horizontal fins to subdivide panels encouraged |
| **Tiles** | Ext. GF: water absorption ≤ **0.5%**; above GF ≤ **3%**; tiles **> 0.1 m²** need mechanical fixings; poor-absorption tiles need polymer-modified adhesive |
| **Reinforcement** | Austenitic SS mesh ~**2.5 mm @ 50 mm**; no galv on exposed faces |
| **Pull-off test** | HOKLAS lab; ≥ **3 samples per tile type per 10 typical floors**; AP/RSE pick locations; not over waterproofing |
| **MW path** | External render/tiles/roof finishes on existing buildings → MWCS (Sch 1 + PNRC 71) |

**SD takeaway:** Fix tile format, panelisation, movement joint grid, and fin projections on elevation studies — debonding risk scales with panel size and build sequence.

---

### 4. Cantilevered RC projections (PNRC 27)

| Rule | Limit / detail |
|---|---|
| **Span > 1 m** | Prefer beam-and-slab over pure slab cantilever |
| **Slab thickness** | 110 mm (≤ 500 mm span); 125 mm (≤ 750 mm); 150 mm (> 750 mm) |
| **Reinforcement** | HYS in both faces both directions; main bars ≥ **10 mm @ ≤ 150 mm**; As ≥ **0.25%** |
| **Exposure span > 750 mm** | **35 MPa** waterproof concrete; **HDG main bars**; construction report + BA14; crack width ≤ **0.1 mm** SLS or bar stress ≤ **100 N/mm²** |
| **Construction** | Cast monolithically with support — **no CJ at external edge**; drainage fall ≥ **1:75** mortar; canopy drainage to SW system; drain outlets max **5 m** apart if inaccessible |
| **Planning** | Projections must comply **B(P)R 7 & 10** and **PNAP APP-19**; detail for future removal without main-structure damage |
| **Maintenance manual** | AP coordinates IO inspection/maintenance doc at completion |

**SD takeaway:** Pure slab balconies/canopies > 750 mm clear span trigger **enhanced durability spec + as-built report** — flag on massing and typology early.

---

### 5. Railway protection & Area Number 3 (PNRC 14)

**Protection zone:** ~**30 m** from railway structures/fence/track centreline (stations may be larger). Area 3 (Sch 5 BO) = full BA approval + consent for GI and underground drainage.

| Constraint | Empirical limit (unless engineering approach agreed) |
|---|---|
| Piles / GI near underground railway | **No** pile/borehole/well/soil nail within **3 m** of underground railway structure |
| Piling near at-grade track | **No** piling within **3 m** of fence or **7 m** from track centreline (no fence) |
| Pressure change on underground railway | ≤ **20 kPa** vertical/horizontal |
| Openings near railway ventilation | ≥ **5 m** (may reduce to **2.5 m** if exhaust directed away) |
| Scaffolding / storage above track | Not within **6 m** plan of tracks without MTRCL agreement |
| Movement — angular distortion | Alert **1:2000** / Alarm **1:1350** / Action **1:1000** |
| Total movement any plane | Alert **10 mm** / Alarm **15 mm** / Action **20 mm** |
| PPV — blasting / prolonged vibration | **25 / 15 mm/s** |
| PPV — OHL/signalling furniture | **10 mm/s**; amplitude **80 µm** |

**SD takeaway:** Foundation type, basement depth, and façade line within ~30 m of MTR must be **MTRCL-coordinated** from concept; GI/drainage in Area 3 cannot be deferred to MWCS without MTRCL agreement.

---

### 6. Minor Works Control System — design for future lawful change (PNRC 71, 69, 75, 52)

| Class | Appointment | Typical SD-relevant items |
|---|---|---|
| **I** | PBP + PRC | Internal stair between floors; structural signboards; spread footing in sensitive areas |
| **II** | PRC prepares plans + supervises | External wall repair; window replacement; many A&A repairs |
| **III** | PRC notice + completion | AC frames; small canopies; Class III signboards |

**187 MW items** in Cap 123N Sch 1 — no referral to other departments on MW submission (consult them yourself: **PNRC 71 ¶18**).

| Validation scheme | Pre-cutoff | Cycle |
|---|---|---|
| **Signboard (75)** | Erected before **2 Sep 2013** | **5-year** re-inspection |
| **HMWVS / MAFVS (71)** | Pre-2011 / pre-2020 amenity features | Certification by AP/RSE/RC |

**Minor amendments during construction (52):** Reg 33(1) exemption allows site changes without new consent **except** items in PNRC 52 App A — includes major revisions (APP-55), OZP conflicts, works outside lot, foundation pile relocations **> 5 m**, pile count increases **> 5%** ( **> 15%** for LDBP), railway/DSD tunnel limit breaches, Type 1↔2 coupler changes, etc. Secondary elements (CW, cladding, canopy, balustrade…) ride the superstructure exemption once granted.

**SD takeaway:** Design documents and specs so post-occupation repairs (windows, tiles, signboards) can trace to **MW class/item**; avoid geometry that forces full s.14 for routine MBIS/MWIS repairs.

---

### 7. Site interface & public realm (PNRC 4, 65, 61)

**Hoardings / covered walkways (4):**
- Min clear pedestrian width **1.1 m** always
- Demolition in urban areas: **steel frame + steel plate** hoardings; covered walkway lighting (~**18–20 W fluorescent @ 3 m** spacing for 2 m × 2.5 m walkway)
- Self-cert under **PNAP APP-23** (30-day hoarding permit; renewal ≥ 30 days before expiry)
- On-street parking suspension: TD **7 working days** (< 3 months) or **30 days** (> 3 months)

**Run-in / run-out (65):**
- Match adjoining footpath material (concrete or pavers with visual contrast)
- **Saw-cut** method — no damage outside RIO footprint
- Show on **GBP** for HyD comment; utilities check + Excavation Permit early
- **Certificate of Completion** before OP — HyD defects can block **s.21 OP**

**Streams/rivers (61):** EPD consultation for works affecting natural watercourses — sediment, discharge, timing.

**SD takeaway:** Site logistics plan at SD must show hoarding/covered walkway width, crane swing vs railway (PNRC 14), and permanent RIO geometry on HyD standards.

---

### 8. Demolition & existing fabric (PNRC 6, 15, 83)

| Topic | Lock-in |
|---|---|
| **Demolition supervision (6)** | Supervision plan (TMSP 2009); video record entire demolition ≥ **14 days** retention; TCP Form BA20 on site; pre-demolition MW streamlining (App A) — MW01 with demolition plan if same project team |
| **Asbestos (15)** | **Banned** import/use/supply (APCO); in-situ ACM → registered asbestos consultant + contractor; **28-day EPD notice**; complete abatement **before** other building works |
| **Demolition CoP (83)** | PNRC 83 promulgates Demolition CoP 2004 — full-time site engineer for complex structures, debris management |

**SD takeaway:** Refurb/demolition briefs need **asbestos survey gate** before design freeze; partial retention sequences must allow PNRC 6 MW pre-works.

---

### 9. Materials, testing & production QA (PNRC 13, 33, 48, 63, 80, 81, 82)

| PNRC | SD-relevant hook |
|---|---|
| **13** | PFA in concrete — environmental/technical benefits; specify with structural acceptance |
| **33** | BO s.17(1)(6) — BD may require **rebar testing**; coordinate with APP-45 |
| **48** | Building materials testing — AP/RSE may specify; RC executes |
| **63 Precast** | ISO **9001** factory; QCS/QCC regime; QA audit; applies to structural precast — **not** small architectural planters |
| **80** | Consent conditions: QSP, material Certs, monitoring instrumentation, **$30M+ projects** → Smart Site Safety (mobile plant + tower crane alert) from **1 Jul 2025**; AP cost declaration at first consent |
| **81** | Product Certification System — third-party CB for declared building products |
| **82** | Early-age insitu RC quality — curing, formwork strike, temperature control |

**SD takeaway:** Spec proprietary systems (precast, PC products, tempered glass, mechanical couplers) only from manufacturers who can satisfy **ISO 9001 + BD-imposed QAS** — lead times affect programme.

---

### 10. Banned / restricted construction methods

| PNRC | Prohibition / restriction |
|---|---|
| **22** | **Ban on hand-dug caissons** |
| **24** | Metal barrel refuse chutes prohibited at sites |
| **26** | Plastic sheet on external scaffolding — must use proper screens/fans/catch platforms (see also **85** fire-retardant standards) |
| **05** | Pouring concrete against adjoining owners' walls as permanent shuttering — not permitted practice |

---

### 11. Metal gates (PNRC 68)

| Trigger | Submission |
|---|---|
| New building | Show gates on approved plans |
| Height **> 3.2 m** | Structural plans + calculations required |
| Existing building, new gate **> 3.2 m** | Full BA approval before install |
| Drilled anchors | Pull-out test **≥ 5 nr per type/size** @ **1.5×** manufacturer recommended load |
| Electric sliding gates | EMSD CoP for electrically operated sliding gates |
| Maintenance | AP/RGBC doc for IO — inspect **every 3 months** |

**MW path:** Existing building gate install may be MWCS (Sch 1 + PNRC 71).

---

### 12. Scaffolding protective materials — fire retardant (PNRC 85, Dec 2025)

Applies to nets, screens, tarpaulins, plastic sheeting on external scaffolding (construction, demolition, A&A, MW repair).

| Standard | Application |
|---|---|
| **GB 5725-2009** (→ GB 5725-2025 from **1 Sep 2026**) | Safety nets |
| **BS 5867-2:2008 Type B** | Nets, screens, tarpaulins, sheeting |
| **NFPA 701:2023 Method 2** | Same |

**Process:** Third-party random sampling per **ISO 2859-1** lot sizes; sample ≥ **1.8 m × 2 m**; HOKLAS designated lab; **failed lot = entire lot rejected**; notify BD within **7 days** of full scaffold completion (Form App IV); BD site audit — **failed elevation = remove all materials on that elevation**; re-test every **≤ 12 months**.

**Existing buildings:** Applies to scaffold ≥ **3 consecutive storeys** or full elevation / full re-entrant height (truss-out single-unit repair excluded). Low-rise domestic ≤ **3 storeys** exempt.

**SD takeaway:** Façade access strategy and A&A phasing must budget sampling lead time and fire-retardant material traceability (QR/NFC/RFID if off-site sampling).

---

### 13. Supervision, site audit & electronic submission

| PNRC | Architect programme note |
|---|---|
| **76 / 77** | Site Supervision CoP 2009 + quality supervision of building works — TCP grades, hold points |
| **49** | BD site auditing strategy — RC must maintain compliance on site |
| **31** | Site Monitoring Section audits |
| **42** | Electronic plan submission (ETO Cap 553) |
| **74** | Statutory processing time limits — incomplete submissions delay consent |

---

### 14. Specialist temporary works & plant (PNRC 23, 29, 30, 54)

| PNRC | Key constraint |
|---|---|
| **23** | Certified plant operators for lifting appliances (B(A)R) |
| **29** | Lift shaft platforms — temporary works design/supervision |
| **30** | Gondolas/suspended platforms: min width **440 mm**; guard-rails **900–1150 mm**; toe boards **≥ 200 mm**; counterweight **≥ 3×** balance load; LD FIU(SWP)R applies |
| **54** | Contractor's sheds — UBW risk if not approved; show on plans or MW |

**SD takeaway:** Maintenance access (gondola anchors, davits, BMU) must be on **approved structural plans** — not added ad hoc.

---

### 15. Lift & barrier-free interfaces (PNRC 36)

Maintenance/replacement of lift installations — fire-resisting construction linkage (**FRC CoP ¶11.2**). Coordinate shaft, lobby, and refuges with lift contractor early.

---

### 16. Environmental & sustainability hooks (PNRC 17, 21)

| PNRC | SD action |
|---|---|
| **17** | Construction environmental checklist (noise, dust, wastewater, waste) — design for enclosed works, haul routes, stockpile locations |
| **21** | Tropical hardwood — avoid unless certified sustainable source |

---

### 17. PNRC index — documents in this summary

| PNRC | Title (short) | SD relevance |
|---|---|---|
| 1 | Practice Notes in Force | Web-only index; check bd.gov.hk for current list |
| 2 | Specified Forms | Form mechanics for RC submissions |
| 3 | Cease Works Orders | Enforcement — design non-compliance stops site |
| 4 | Hoardings, Covered Walkways and Gantries | **High** — site layout, demolition |
| 5 | Pouring Concrete against Adjoining Walls | **High** — party wall/interface |
| 6 | Demolition Works | **High** — phasing, video, MW pre-works |
| 7 | HK Airport Obstructions (Cap 301) | Height/obstacle near airport |
| 11 | Testing of Drainage Works | B(SSFPDW)R 73 — water test hold point |
| 12 | Overheight Vehicles | Logistics — RT Cap 374 |
| 13 | PFA in Concrete | Material spec |
| 14 | Railway Protection | **Critical** — foundation/massing near MTR |
| 15 | Asbestos | **Critical** — refurbishment/demolition |
| 17 | Environmental Nuisance | Site logistics |
| 19 | Change of Address | Admin |
| 21 | Tropical Hardwood Timber | Material ethics/spec |
| 22 | Ban on Hand-dug Caissons | **Critical** — foundation type |
| 23 | Plant Operator Certification | Programme |
| 24 | Metal Refuse Chutes | Site logistics |
| 25 | BA13 / BA14 / materials schedule | Completion docs |
| 26 | Plastic Sheet on Scaffolding | Superseded in part by **85** |
| 27 | Cantilevered RC Structures | **Critical** — balconies/canopies |
| 29 | Lift Shaft Platforms | Temp works |
| 30 | Suspended Working Platforms | **High** — maintenance access design |
| 31 | Site Monitoring | Audit exposure |
| 32 | Display of Site Information | Site board |
| 33 | Reinforcement Testing | Structural QA |
| 34 | Water Carrying Services Affecting Slopes | Slope/drainage CoP |
| 36 | Lift Maintenance/Replacement | Lift fire interface |
| 37 | Sale Offices on Site | Temporary occupancy |
| 38 | RC Registration | Procurement — contractor class |
| 41 | Fixing of Reinforcement | Site QA |
| 42 | Electronic Submission | Digital workflow |
| 43 | Corruption Prevention | Admin |
| 46 | Site/Ground Investigation | GI method near sensitive infra |
| 47 | Aluminium Windows | **Critical** — fenestration spec |
| 48 | Testing of Building Materials | Material Certs |
| 49 | Site Auditing | Compliance |
| 52 | Minor Amendment Works | **High** — design change strategy |
| 54 | Contractor's Sheds | Temporary buildings |
| 59 | Authorised Signatory (RC) | Contract admin |
| 60 | Water Seepage | **Critical** — envelope performance |
| 61 | Protection of Streams/Rivers | EPD interface |
| 62 | Employment Statistics | Admin |
| 63 | Precast Concrete QC | **High** — modular/precast |
| 64 | Site Safety Enhancement | Safety |
| 65 | Run-in and Run-out | **High** — OP critical path |
| 67 | Wet-fixed External Tiles | **Critical** — façade system |
| 68 | Large Metal Gates | **High** — boundary design |
| 69 | MW Contractors Registration | A&A contractor selection |
| 70 | Identification of RCs | Admin |
| 71 | Minor Works Control System | **Critical** — lifecycle repairs |
| 72 | Authorised Signatory (PRC) | MW contract admin |
| 73 | Inspection of Plans | Admin |
| 74 | Submissions to BD | Programme |
| 75 | Signboard Validation Scheme | **High** — existing signage |
| 76 | Site Supervision CoP 2009 | Supervision stack |
| 77 | Quality Supervision | TCP/hold points |
| 78 | Pay for Safety Scheme | Contract |
| 79 | Conduct of RCs | Compliance culture |
| 80 | BO Approval/Consent Conditions | **Critical** — consent stack |
| 81 | Product Certification | Spec |
| 82 | Early-age RC Quality | Structural programme |
| 83 | Demolition CoP 2004 | Demolition |
| 84 | Curtain Wall / Window / Window Wall | **Critical** — façade |
| 85 | Fire Retardant Scaffolding Materials | **Critical** — A&A/construction |

---

### 18. Schematic design checklist (minimum)

- [ ] Façade system chosen with PNRC **47/84** limits (sash sizes, tests, heat soak if tempered)
- [ ] External finish system with **67** movement joints, render build-up, pull-off test regime
- [ ] Projections typed per **27** (beam-slab vs slab; span thresholds; drainage)
- [ ] Foundation scheme checked against **14** railway limits and **22** banned methods
- [ ] Boundary gates **68** sized; structural submission if **> 3.2 m**
- [ ] Run-in/out **65** on GBP; HyD coordination in programme
- [ ] Hoarding/covered walkway **4** width and demolition steel specification
- [ ] MWCS item numbers identified for predictable future repairs (**71**)
- [ ] Signboard strategy — new (APP-126) vs validation (**75**) vs enforcement
- [ ] Scaffolding/fire-retardant material compliance path (**85**) for A&A phasing
- [ ] Consent conditions anticipated per **80** ($30M 4S, QSP, monitoring)
- [ ] Demolition/refurb: asbestos **15** + demolition sequence **6/83**
- [ ] Maintenance access: gondola/BMU anchors **30** on structural plans

---

## Cross-references

- **PNAP series** — AP/RSE mirror notes for same topics
- **Minor Works Control System_CS.md** — Cap 123N Schedules + Technical Guidelines
- **Code of Practice on Access for External Maintenance 2021_CS.md** — aligns with PNRC 30, ADV-14
- **PNBI-1_CS.md** — MBIS/MWIS PNRC cross-index (App I)

*Verify live PNRC list and revision dates at [bd.gov.hk — PNRC](https://www.bd.gov.hk). PNRC 1 (July 2012) confirms hardcopy issue ceased; website is authoritative.*
