---
name: hk-building-sustainability
description: BEAM Plus (NB, EB, Interiors, Neighbourhood), OTTV/RTTV, HK energy codes, green building credits, and subtropical climate performance strategies for Hong Kong.
disable-model-invocation: true
---

# HK Building Sustainability

For **Cap. 403 refrigerant selection, replacement, recovery and scheduled-HFC supply controls**, use [environmental site controls](../../references/hk-environmental-site-controls.md#cap-403--ozone-layer-protection-ordinance). Cap. 311 air/process/asbestos, Cap. 358 discharge and Cap. 354 waste gates are in the same reference; read only the applicable section. BEAM Plus or an EIA environmental permit does not establish those separate approvals.

Covers BEAM Plus rating system, OTTV/RTTV compliance, energy codes, and climate-responsive design for Hong Kong (ASHRAE CZ 1A — hot-humid subtropical).

For **BEAM Plus / energy performance strategy**, use `hk-building-sustainability`. For other topics, see the routing table below.

## When to Use This Skill

Use section 8 for evidence-led performance feedback in use and its architectural implications; refer systems analysis/tuning to **Skills-MEP-Engineer-HK**.

For embodied-carbon option appraisal, retention versus replacement, or a whole-life carbon study brief, use section 7. Product evidence is coordinated through material selection; this workflow does not add a calculator or certification service.

BEAM Plus, OTTV/RTTV, greenery, EIA interfaces, green building credits, integrated indoor-environment and occupant-comfort briefs. Use section 6 to coordinate air quality, thermal comfort, daylight/glare, acoustics and material choices. Sustainable Building Design quantitative rules (building separation, setback, site coverage of greenery) are PNAP APP-152.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| BEAM Plus / energy performance strategy | `hk-building-sustainability` | `—` |
| Daylight factor / Reg. 30 | `—` | `hk-daylighting-design` |
| Facade U-value detail only | `—` | `hk-building-envelope` |
---

## 1. BEAM Plus Overview

| Scheme | Scope | Certifier |
|---|---|---|
| NB (New Buildings) v2.0 | New construction; PA → CA → RFA (Assessment Manual Feb 2025) | HKGBC |
| EB (Existing Buildings) v3.0 | In-use buildings; Comprehensive Scheme A or B (Assessment Manual 2025). Brochure V2.0 remains a separate summary | HKGBC |
| Interiors (older v1.0 label) | Use the non-residential v2.0 or residential tool in the rows below for a current fit-out | HKGBC |
| Neighbourhood | Master plan / district scale. A Neighbourhood certificate is not a New Buildings certificate; reassess under NB when the project moves from planning to building design | HKGBC |
| Data Centres (NDC / EDC) | Data-centre area at least 500 m², and data halls plus related plant a significant majority of floor area. New construction or major alteration uses NDC; operations use EDC | HKGBC |
| Existing Schools | Existing primary and secondary schools only, after at least one school calendar year of operational data. Not a generic existing-buildings scorecard | HKGBC |
| Interiors, non-residential v2.0 | Completed fit-out of offices, retail, restaurants, clubhouses, and other non-residential premises. Not whole-building NB or EB | HKGBC |
| Interiors, residential | Completed home fit-out. Item-count tool (Green at 30 items, Green+ at 45). Do not import the non-residential Platinum point table | HKGBC |
| Existing Buildings, global v1.0 | Existing buildings **outside Hong Kong**. Do not apply local EB v2.0 energy, water, or indoor-air baselines. The brochure has no rating table | HKGBC |

### 1.1 BEAM Plus NB Credit Categories

| Category | Max Points | Key Credits |
|---|---|---|
| Site Aspects (SA) | 30 | AVA, greenery, permeable paving, heritage |
| Materials Aspects (MA) | 20 | Recycled content, FSC timber, low-VOC |
| Energy Use (EU) | 35 | OTTV, RTTV, lighting power density, renewables |
| Water Use (WU) | 20 | Low-flow fixtures, rainwater harvesting, greywater |
| Indoor Environmental Quality (IEQ) | 30 | Natural ventilation, daylighting, acoustic, IAQ |
| Innovations & Additions (IA) | 10 | Pilot credits, exemplary performance |

### 1.2 Rating Levels

| Level | Points Required |
|---|---|
| Bronze | 40 |
| Silver | 55 |
| Gold | 65 |
| Platinum | 75 |

---

## 2. OTTV & RTTV

### 2.1 Overall Thermal Transfer Value (OTTV)

```
OTTV = Σ [Uw × (1 - WWR) × TDeq] + Σ [Uf × WWR × ΔT] + Σ [SC × WWR × SF]
```

| Parameter | Typical HK Value |
|---|---|
| Target OTTV (non-domestic) | ≤ 20 W/m² (BEAM Plus EU credit) |
| Baseline OTTV (code minimum) | ≤ 35 W/m² (EMSD BEC) |
| Solar factor (SF), E/W facade | ~150–180 W/m² |
| Shading coefficient (SC) target | ≤ 0.25 (high-performance glass) |

### 2.2 Roof Thermal Transfer Value (RTTV)

- Target: ≤ 25 W/m² (BEAM Plus); ≤ 35 W/m² (BEC baseline)
- Strategies: reflective coating (SRI ≥ 78), green roof, insulation (R ≥ 2.0 m²K/W)

---

## 3. Climate-Responsive Strategies (CZ 1A)

| Strategy | Application | Priority |
|---|---|---|
| External shading (E/W) | Horizontal fins, deep reveals, brise-soleil | High |
| High-performance glazing | Low-e, SHGC ≤ 0.25 for E/W; ≤ 0.35 for N/S | High |
| Natural cross-ventilation | Dual-aspect units; operable windows; stack effect | High |
| Green/reflective roof | Reduce RTTV; mitigate urban heat island | Medium |
| Rainwater harvesting | Irrigation, toilet flushing; HK annual rainfall ~2400 mm | Medium |
| PV panels | Roof + south facade; limited by typhoon wind loads | Medium |
| Thermal mass | Less critical in CZ 1A; focus on shading over mass | Low |

---

## 4. Energy Code (EMSD BEC) and Cap. 610

- **Building Energy Code (BEC)** administered by EMSD. Numerical standards sit in the code issued under the Buildings Energy Efficiency Ordinance, not in the Ordinance text.
- **Cap. 610** applies to prescribed buildings. Residential flats themselves are not a prescribed building; their common areas are. Classify every portion (commercial, residential common area, industrial, hotel, data centre) and confirm the main-switch approved loading and the Schedule 2 carve-outs before treating the project as fully inside the Ordinance.
- Stage-one declaration is due **two months after superstructure consent**. Freeze building-services design to the Gazette code in force for that consent, and name that edition in the declaration.
- The stage-one declaration, stage-two declaration, Form of Compliance, and energy audit must be certified by a **registered energy assessor** who is registered on the day of the act (Cap. 610B). Stage two carries the fee in Cap. 610A; stage one is not a fee item in that Schedule.
- The first Certificate of Compliance Registration is the maintenance baseline for central plant and for unit installations the developer provides.
- A later Form of Compliance clock (two months) starts for a fit-out of **500 m²** or more, a new **400 A** circuit, a chiller or unitary air-conditioner at or above **350 kW**, or a lift or escalator drive replacement.
- An Energy Audit Form is displayed at a conspicuous main-entrance position. Central plant of a Schedule 4 building above **7,000 m²**, and every data centre regardless of that floor-area relief, is on a **5-year** audit cycle once the relevant date has passed.
- BEAM Plus energy credits require performance above the BEC baseline. They do not replace Cap. 610.

### 4.1 Statutory OTTV under Cap. 123M

Cap. 123M requires a suitable overall thermal transfer value for the external walls and roofs of commercial buildings and hotels. The regulation does not print the W/m² caps. APP-67 (as amended September 2025) sets them, for new building plans or major revisions submitted **on or after 31 December 2025**:

| Envelope zone | Cap |
|---|---|
| Building tower | ≤ 20 W/m² (previous 21 W/m²) |
| Podium | ≤ 40 W/m² (previous 50 W/m²) |

Basement perimeter walls are not external walls for Cap. 123M. Where site coverage steps under PNAP APP-132, the notional podium for the calculation may be taken as 20 m above mean street level, or at a lower demarcation. Consent needs an OTTV summary sheet; occupation permit needs the full OTTV report and glass shading coefficients on the record plans. A residential recreational facility is controlled like commercial or hotel under APP-156 (same 20 / 40 caps); that path is not Cap. 123M.

### 4.2 Environmental Impact Assessment Ordinance (Cap. 499)

Screen the brief against Schedules 2 and 3 before massing. Splitting one scheme into contiguous pieces that each sit under a threshold can still be specified as one designated project. Do not start construction, operation, or decommissioning of a Schedule 2 designated project without an environmental permit, and do not depart from permit conditions on layout, method, or mitigation. A material change of layout, alignment, throughput, or mitigation after the permit is a fresh assessment problem. The Technical Memorandum on the Environmental Impact Assessment Process is the content specification the Director must follow.

Design locks that most often catch a building or site brief include the road class in Schedule 2 item A.1, the 100 m depot and cavern setbacks, the 5 ha and 1 ha reclamation tests and the dredging distances, sewage capacity and the 200 m sewage setback, a 400 kV substation, industrial-estate and batching-plant thresholds, a 20 ha theme park, a 10,000-person outdoor venue, and Deep Bay Buffer Zone residential or recreational development.

---

## 5. BEAM Plus Design Integration by Stage

| Stage | Action |
|---|---|
| Feasibility | Appoint BEAM Pro; select target level; map SA credits (site, AVA) |
| Concept | Fix orientation, shading strategy, OTTV target; confirm NV feasibility |
| Scheme | Specify glazing SC/U-values; size PV/rainwater systems; confirm IEQ strategy |
| Detail | Low-VOC specs, FSC timber, recycled content schedules |
| Construction | Commissioning plan; IAQ testing protocol |
| Occupation | Final BEAM Plus submission; post-occupancy monitoring |

## 6. Integrated indoor-environment and occupant-comfort brief

Use when daylight, glare, acoustics, air quality, thermal comfort and materials must work together in a Hong Kong project. This is integrated design coordination, not a health diagnosis or certification. Identify statutory requirements, client objectives and optional assessment credits separately.

### 6.1 Inputs and responsibilities

Obtain room uses, occupancy/activity schedules, user needs, hours, orientation/obstructions, external noise/air sources, facade options, ventilation/cooling concept, finishes and FM constraints. For existing premises obtain complaints and measurements with dates and operating conditions. Do not infer targets from a neighbouring use or generic table.

The architect coordinates spatial design and conflicting objectives. MEP establishes ventilation, cooling/dehumidification and controls; acoustic/daylight reviewers establish metrics/methods; materials reviewers check product evidence; client/FM confirms operation. Record appointed specialists and outstanding inputs.

### 6.2 Room-level brief

| Room/use/hours | Objective and criterion source | Design response | Owner | Verification and conditions | Missing input |
|---|---|---|---|---|---|
| Open-plan office / working hours | Useful daylight with glare control; criteria to agree against brief/applicable assessment | Compare glazing, shading and workstation layout | Architect + daylight reviewer | Simulation with actual obstructions/glazing/blinds, representative positions/times | External geometry and glazing data |
| Meeting room / intermittent high occupancy | Ventilation, comfort and privacy; MEP/acoustic criteria to confirm | Coordinate occupancy, distribution, enclosure and door | MEP + acoustic reviewer; architect coordinates | Calculations and agreed commissioning/testing under stated occupancy and opening modes | Peak occupancy and schedule |

For every numerical criterion record metric/unit, source/edition, applicability, assessment location/time and accepting reviewer. Missing criteria stay `To agree`; this workflow introduces no default temperature, pollutant, ventilation or noise limits. Generic tables must be verified against applicable sources before use. Product certificates or simulations alone do not prove as-built performance.

### 6.3 Option review sequence

1. Agree room objectives and their statutory/project/certification basis before selecting systems.
2. Identify competing requirements below. Compare complete operating modes, not isolated products.
3. Send focused questions to [daylighting](../hk-daylighting-design/hk-daylighting-design.md#6-inputs-to-an-integrated-indoor-environment-review), [acoustics](../hk-acoustic-design/hk-acoustic-design.md#7-inputs-to-an-integrated-indoor-environment-review) and [building services](../hk-building-services/hk-building-services.md#11-inputs-to-an-integrated-indoor-environment-review). Use [materials](../hk-material-selection/hk-material-selection.md) for finish/product evidence and moisture compatibility.
4. Compare objectives, energy/operation, cost, maintainability and risks. State needed modelling/measurement/mock-ups; do not invent scores for unmeasured performance.
5. Record the selected option and conditions; coordinate drawings, specifications and commissioning requirements. Return substitutions or value-engineering changes to this brief.
6. At handover review test results, operation instructions and unresolved defects with specialists/FM. Design expectations remain conditional until supporting evidence is available.

| Change | Potential benefit | Competing issue | Coordinated response |
|---|---|---|---|
| Larger operable windows | Ventilation opportunity | Traffic noise/pollutants, humidity and weather | Assess open/closed modes with acoustic/MEP reviewers; check natural-ventilation requirements separately |
| Darker glass or deeper shading | Reduced solar gain/glare | Less useful daylight and more lighting demand | Reassess daylight and thermal performance using actual geometry/product data |
| Tighter enclosure | Better noise/air-leakage control | Planned ventilation and moisture control | MEP verifies ventilation/dehumidification; closing openings is not a complete solution |
| Acoustic lining/ceiling | Improved room acoustics | Emissions, moisture durability, fire and services access | Review assembly/product evidence and specialist interfaces |

### 6.4 Hypothetical trade-off: road-facing office refurbishment

**Brief:** a Hong Kong office client proposes opening road-facing windows to reduce stuffiness/cooling demand. Occupants also report traffic noise. Outdoor-air/noise measurements, confirmed occupancy and ventilation records are missing.

**Assessment:** opening windows may improve air movement but worsen noise and admit pollutants/moisture. Sealing them may improve acoustics but does not provide ventilation. Neither option can be declared compliant or comfortable from these facts.

**Actions:** architect confirms use and facade constraints; acoustic reviewer scopes relevant operating modes; MEP investigates outside-air provision, filtration, moisture control and maintenance; FM supplies operation/complaint records. Compare source/maintenance remedies, a reviewed mechanical-ventilation option and a mixed-mode option only where applicable requirements and site conditions support it. Review any shading/glazing changes for daylight as well.

**Output:** provisional option matrix with benefits, unresolved disadvantages, evidence needed, owners and next review date. Keep the opening/ventilation decision unresolved until a workable mode is evidenced. Do not invent temperature, air-change, pollutant or noise limits. Reassess if occupancy, hours or facade specification changes.

**HK source context:** the [Hong Kong IAQ FAQ](https://www.iaq.gov.hk/en/faq.html) identifies indoor sources, outdoor pollution, ventilation and humidity as relevant factors. [EPD ventilation guidance](https://www.epd.gov.hk/epd/english/greenproperty/poll_pro/poll_pro_ven.html) supports considering sources, intake/exhaust interfaces and maintenance. Pages checked 24 November 2026. The brief, matrix and example are practice workflows, not statutory thresholds or copied certification criteria.

---

*Sources: BEAM Plus NB v2.0 Assessment Manual (2025.02) and EB v3.0 Assessment Manual (BSL/HKGBC); NB/EB/Neighbourhood/Interiors/Data Centres/Existing Schools brochures (HKGBC); Cap. 123M; PNAP APP-67 (September 2025 amendment); Buildings Energy Efficiency Ordinance Cap. 610 (20 September 2026) and Cap. 610A / 610B; Environmental Impact Assessment Ordinance Cap. 499 (11 April 2025) and its Technical Memorandum; EMSD Building Energy Code; ASHRAE 90.1-2022 (CZ 1A).*

Assessment Manual Critical Summaries: `references/catalogues/beam-plus.md` and `references/statutory/beam-plus/`. PNAP energy gates: `references/catalogues/pnap-hk-building-sustainability.md`. Library copies and PDFs: `hk_s_reference/BEAM Plus Assessment Tools/`.

## 7. Carbon option appraisal

Use to compare functionally equivalent design, material, retention or refurbishment options for a Hong Kong project. The architect sets the design question; the appointed carbon assessor establishes the assessment method, factors and reporting basis. QS confirms quantities; structural/MEP consultants establish performance and system assumptions. A low-carbon preference does not override safety, durability or statutory requirements.

### 7.1 Scope and inputs

Agree the decision, baseline, options, functional unit, area convention, reference study period and included lifecycle stages. Record demolition, retention/repair, new products, transport, site works, maintenance/replacement, operation and end-of-life inclusions separately. A construction-stage assessment is not a whole-life assessment. Report benefits outside the adopted system boundary separately; do not silently deduct assumed recycling credits or offsets.

Request dated quantity take-offs with revisions, existing-building condition/retention evidence, product/environmental declarations, factor sources/versions, transport origins/routes/modes, site energy/waste assumptions, replacement cycles and energy-use scenarios if included. Obtain density/unit conversions where needed. Separate measured quantities, design estimates and proxies. Do not insert generic carbon factors or claim tool access that was not available.

### 7.2 Review sequence

1. **Normalise options:** compare the same service, area basis, performance, study period and boundaries. Where capacity/use differs, report it and avoid a simple percentage ranking.
2. **Validate data:** QS checks quantities and exclusions; the assessor checks declared units, lifecycle modules, methodology and geographic/temporal relevance. Use the [material evidence handoff](../hk-material-selection/hk-material-selection.md#7-product-evidence-and-substitution-review).
3. **Calculate transparently:** retain input-to-result lineage and units. A quantity multiplied by a factor is valid only for matching units and scope. Count transport, waste, replacement and site impacts once; do not add stages already included in a factor. This topic provides a workflow, not executable calculations.
4. **Expose uncertainty:** assess plausible quantity, service-life, logistics and operational scenarios with the relevant specialists. Mark absent stages as `Not assessed`, never zero. If missing data could reverse the ranking, keep the recommendation conditional.
5. **Compare broader consequences:** state carbon result/boundary alongside cost, programme, durability, structural feasibility, occupation disruption and maintenance. Record conflicts and who resolves them.
6. **Close the decision:** obtain reviewed evidence, record the selected option/conditions and update specifications, drawings and quantity baseline. Reassess substitutions or scope changes that affect the comparison.

| Option / baseline revision | Function and area basis | Stages / period | Quantity and factor evidence | Result and units / unassessed stages | Sensitivities | Other consequences | Decision / owner / next evidence |
|---|---|---|---|---|---|---|---|
| Retain/repair versus replacement | Same agreed use and service capacity; confirm area convention | Explicitly list included stages and study period | QS take-off; assessor-reviewed factors; condition survey | Pending assessment; missing information is not zero | Repair extent, replacements, energy and logistics | Structural feasibility, occupied works and cost | Conditional; architect coordinates assessor/engineers/QS |

### 7.3 Hypothetical case: retaining a Hong Kong office structure

Compare retaining the frame with repairs and facade/services upgrades against replacement to deliver the agreed brief. The existing slab capacity and repair quantities are unconfirmed; only replacement-product data are available. Do not conclude that either option has lower whole-life carbon yet.

Ask the structural engineer to assess retention feasibility, QS to prepare comparable take-offs, MEP to define operating-energy scenarios and the assessor to align boundaries/factors. Show the available construction-stage subtotal only with its exclusions, and keep unknown repairs and operational impacts visible. For a forward-looking comparison, state how existing materials are treated and do not charge historical production to one option but not the other. Test whether repair extent or shorter remaining service life changes the ranking. The outcome is an option note with evidence gaps and decision owners, not a claimed saving invented from generic factors.

**HK reference:** [CIC Carbon Assessment Tool methodology](https://cat.cic.hk/Landing/Methodology) describes a boundary covering material embodied carbon, transport and site impacts. Check the actual tool/method version and exported scope before describing its result; it does not by itself establish a full whole-life comparison. Source checked 24 November 2026. The option procedure above is independently authored practice guidance.

## 8. Performance feedback in use

Support the [Stage 7 POE workflow](../hk-plan-of-work/hk-plan-of-work.md#9-post-occupancy-evaluation-and-aftercare-service) by comparing design objectives with actual operation. Use the existing integrated indoor-environment brief as the baseline. Keep rating/certification, occupant satisfaction and measured performance distinct.

**Inputs:** original objectives and assessment scope; actual occupancy/use/hours; weather/season and operating mode; available measured data with timestamps, units and measurement boundaries; commissioning/maintenance records; user feedback and changes since design. Record gaps in coverage, calibration or comparability. A simulation forecast is not measured performance.

Compare like-for-like periods and areas where evidence permits; disclose changes in use, operating hours and measurement boundaries. Refer meter validation, energy analysis, ventilation/thermal diagnosis and systems tuning to **Skills-MEP-Engineer-HK** rather than calculating specialist results from incomplete data. Refer interior-led changes to **Skills-Interior-Designer-HK** and landscape performance/design questions to **Skills-Landscape-Architects-HK**. Do not make medical or health-effect diagnoses from occupant reports.

**Output:** objective/source; observed or reported result; conditions and evidence limits; possible explanations; specialist referral/status; architectural implication; authorised follow-up; verification plan. Keep alternatives open until investigated. Do not claim energy savings or certification improvement from a simple before/after bill or questionnaire score.

**Hypothetical case:** electricity use increases after a building's opening hours and occupancy increase. Record those changes before alleging design failure. Ask MEP/FM to review comparable measurement and operating evidence; the architect reviews whether revised use conflicts with the agreed spatial/comfort brief. Feed evidenced lessons into a proposed brief revision, not an automatic new performance benchmark.
