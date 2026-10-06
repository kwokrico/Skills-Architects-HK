# Foundation Quick Reference

Routine Hong Kong lookup tables. Read this file when the master router sends a single-table question here. Open a topic file only when the question needs a workflow or an edge case.

### 1.1 Floor-to-Floor Heights
 
| Building Type | Typical F-F | BO / PNAP Basis |
|---|---|---|
| Domestic (residential) | 2.9 – 3.1 m | BO Reg. 30: min 2.5 m headroom |
| Non-domestic (office) | 3.8 – 4.2 m | BO Reg. 30: min 3.0 m headroom |
| Retail (ground / podium) | 4.5 – 5.5 m | PNAP APP-2; double-height common |
| Car park (within building) | 2.3 – 2.5 m clear | BO Reg. 46: min 2.0 m clear |
| Plant room | 3.5 – 5.0 m | Project-specific; coordinate BD submission |
 
### 1.2 Plot Ratio & Site Coverage by OZP Zone
 
| Zone | Domestic PR | Non-Domestic PR | Site Coverage | Notes |
|---|---|---|---|---|
| **R(A)** High-density residential | 5.0 | — | 33% tower / 66% podium (≤15 m) | Most common urban residential zone |
| **R(B)** Medium-density residential | 3.0 | — | 33% | Typically suburban |
| **R(C)** Low-density residential | 1.0 | — | 25% | Peak, outlying areas |
| **C(1)** High-density commercial | — | 9.5 | 100% podium | CBD/Kowloon core |
| **C(2)** Medium-density commercial | — | 6.5 | 100% podium | District centres |
| **OU** (annotated) | Per OZP | Per OZP | Per OZP | Always check OZP Notes |
| **G/IC** Govt / Institution / Community | Per schedule | Per schedule | Per schedule | PlanD/BD to confirm |
| **V** Village type | NTEH policy | — | 66.7% max | Indigenous villager entitlement |
 
> **Critical rule**: Always read the OZP Notes and Explanatory Statement for the specific site — site-specific restrictions override HKPSG defaults. Check lease conditions (Lands Dept) separately; lease may impose a lower GFA cap than the OZP.
 
### 1.3 GFA Exemptions — PNAP APP-2 Key Items
 
| Feature | Exemption Limit | Conditions |
|---|---|---|
| Balcony | ≤ 2 m depth; aggregate ≤ ½ unit facade width | Open on ≥ 1 long side; aggregate cap per building |
| Bay window | ≤ 0.5 m projection; ≤ 50% of facade width per floor | Non-habitable; open on ≥ 1 side |
| Utility platform | ≤ 1.5 m × 2.0 m per unit | Kitchen/laundry use only |
| Covered public walkway | Full exemption if publicly accessible 24/7 | Per PNAP APP-2 conditions |
| Plant room / lift overrun | Full exemption | Must not breach BHR |
| Caretaker unit | ≤ 35 m² per building | One per building only |
| Refuse chamber | Full exemption | Per EPD/BD standards |
 
### 1.4 Key PNAP Reference Index
 
| PNAP | Subject | Sub-skill for deep detail |
|---|---|---|
| **APP-2** | GFA and non-accountable GFA (exemptions) | `hk-building-codes` |
| **APP-40** | Sustainable building design (setback, greenery ratio ≥ 20–30%) | `hk-building-sustainability` |
| **APP-41** | Barrier-free access (Design Manual: Barrier Free Access 2008) | `hk-accessibility-design` |
| **APP-130** | Means of escape — general principles | `hk-fire-life-safety` |
| **APP-152** | Sustainable Building Design Guidelines | `hk-building-sustainability` |
| **ADV-36** | Amenity features (balconies, utility platforms) | `hk-building-codes` |
| **ADV-49** | Green and innovative buildings | `hk-building-sustainability` |
 
### 1.5 Means of Escape — Quick Numbers (BO Reg. 41 + FS Code 2011)
 
| Parameter | Value |
|---|---|
| Max travel distance — domestic, sprinklered | 45 m |
| Max travel distance — domestic, unsprinklered | 30 m |
| Max travel distance — non-domestic, sprinklered | 60 m |
| Max travel distance — non-domestic, unsprinklered | 45 m |
| Min exit width — ≤ 50 persons | 750 mm |
| Min exit width — 51–200 persons | 1,050 mm |
| Min exit width — > 200 persons | 1,050 mm + 150 mm per 50 persons above 200 |
| Min corridor width — residential common | 1,050 mm |
| Min corridor width — non-domestic | 1,200 mm |
| Max dead-end corridor (sprinklered) | 15 m |
| Max dead-end corridor (unsprinklered) | 6 m |
| Staircase pressurisation threshold | > 30 m building height |
 
### 1.6 Building Height Restriction (BHR)
 
- BHR is defined in the OZP in metres above **Principal Datum (mPD)** or by storey count.
- Check the OZP annotation and Explanatory Statement for the specific site before any massing study.
- **Aviation restrictions** (CAAS): mandatory consultation for Kowloon, Lantau, and airport environs.
- **Ridgeline protection**: refer to HKPSG Chapter 11 and relevant OZP; no development to intrude visually on natural ridgelines from designated vantage points.
- **Harbour view corridors**: maintain per HKPSG Fig. 11.1.

### 1.7 Sprinkler Thresholds (FS Code 2011)
 
| Building Type | Sprinkler Required When |
|---|---|
| Domestic (residential) | > 13 storeys or > 40 m height |
| Non-domestic | > 230 m² per floor or > 3 storeys |
| Basement (occupied) | All cases |
| Composite building | Per most stringent applicable use |
 
### 1.8 Village Houses (NT Exempted Houses — NTEH)
 
| Parameter | Limit |
|---|---|
| Max storeys | 3 |
| Max floor area per storey | 65.03 m² (700 sq ft) |
| Max height | 8.23 m (27 ft) |
| Max site coverage | 66.7% |
 
> All four limits must be met simultaneously — BD rejects if any single limit is exceeded.
 
### 1.9 Environmental Performance — HK Subtropical Climate (CZ 1A)
 
| Metric | Target | Source |
|---|---|---|
| OTTV (non-domestic) | ≤ 20 W/m² | BEAM Plus NB |
| RTTV (roof) | ≤ 25 W/m² | BEAM Plus NB |
| Window-to-wall ratio, N/S facade (residential) | 25–35% | BEAM Plus / OTTV compliance |
| Window-to-wall ratio, E/W facade (residential) | 15–25% | Limit solar gain |
| Natural ventilation depth (cross-ventilated unit) | ≤ 12 m per side | BEAM Plus IEQ |
| Podium greenery ratio | ≥ 20–30% site area | PNAP APP-40 |
 
### 1.10 Key HK Architects (Quick Reference)
 
| Architect / Practice | Signature Approach | Key Works |
|---|---|---|
| **Tao Ho** (何弢) | Chinese spatial grammar in modern form | HK Arts Centre (1977), Bauhinia emblem |
| **Rocco Yim** (嚴迅奇) | Layered urbanism, section as generator | Guangdong Museum, HK Planning Dept HQ |
| **P&T Group** | Pragmatic high-rise and composite buildings | Jardine House, Exchange Square |
| **Aedas HK** | Supertall and MTR transit hubs | ICC, various MTR stations |
| **Ronald Lu & Partners** | Sustainable urbanism, BEAM Plus | Community and green building projects |
| **Wong & Ouyang** | Complex mixed-use, hospitals, infrastructure | Hospital Authority projects |
 
> For full design theory, critical regionalism, and HK urban discourse, read [hk-design-theory](../subskills/hk-design-theory/hk-design-theory.md).

### 1.11 Completion Checklist

| Milestone | Authority / Form | Critical Requirement |
|---|---|---|
| FSD Inspection | Form FSI/501 | All Fire Services Installations (FSI) must be 100% functional and tested. |
| BD OP Inspection | Form BA14 | Building must be "rendered fit for occupation." No "Unauthorized Building Works" (UBW) vs. approved plans. |
| Water Supply | WSD Form WWO 46 | Final inspection of plumbing and fire mains by Water Supplies Dept. |
| Lifts/Escalators | EMSD Form 5 | "Permit to Use and Operate" from Electrical and Mechanical Services Dept. |
| Practical Completion | HKIA PC Cert | Building is functionally complete; minor snags only. Transfer of insurance/risk to Client. |
 
---
