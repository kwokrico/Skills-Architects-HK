# PNAP APP Series (A–B) — Technical Design Summaries

**Scope:** PNAP APP-1 to APP-174 from `PNAP_APPa_e` and `PNAP_APPb_e`  
**Focus:** Design impact, GFA/site parameters, BD submission requirements, AP liability red flags  
**Coverage:** 165 practice notes summarised (one section each). Missing numbers with no source file in this library: APP-6, 36, 77, 102, 103, 113, 131, 160, 161.  
**Caveat:** Advisory desk reference only — verify the current BD PNAP revision, OZP Notes, and lease before submission reliance.

---


<!-- Source: batch_01_APP001-025.md -->

# PNAP Technical Summaries — Batch 01 (APP-1 to APP-25)

Source: `PNAP_APPa_e` main APP###.md files. APP-6 not present (skipped). Summaries extract only design, GFA/SC, submission and liability content from the source files.

---

## PNAP APP-1: Landlord and Tenant (Consolidation) Ordinance, Cap. 7 / Demolished Buildings (Re-development of Sites) Ordinance, Cap. 337 — Validity of Approved Plans
**Status/Context:** Administrative workflow (Exclusion Orders / Re-development Orders interface with BO approvals)

### 1. Core Technical Requirements & Metrics
* **BO s16(3A) treatment of Exclusion Order plans:** Approved plans forming the basis of an Exclusion Order under Cap. 7 are normally excluded by BO s16(3A) from application of BO s16(3)(d). Consent applied for more than two years after approval will be given if it is still practical for the work to be completed within the Re-development Order period.
* **Material variation thresholds (Exclusion Order projects):** Amendments deemed a "material variation" if: (a) reduction in floor space of more than **10%**; or (b) change in use of any part of the proposed building; or (c) involvement of other premises also subject to Cap. 7 (e.g. project extension).
* **Penalty-free commencement extension:** One month may be granted by BA upon request before expiry of the commencement period laid down in an Exclusion Order. Justifying examples include: inability to obtain vacant possession (proceedings commenced and pursued with due diligence); inability to enter adjacent property for shoring/precautionary works; inability to obtain demolition consent for reasons beyond applicant’s control.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact. The note regulates Exclusion Order administrative interface and material variation of approved schemes, not SC/PR/GFA measurement.

### 3. BD Submission & Certification Procedures
* AP (or client’s solicitors) must apply to the Lands Tribunal (Registrar, Lands Tribunal, Wanchai Law Courts) for an amending Exclusion Order if material variation occurs.
* Penalty-free extension of commencement must be requested of BA before expiry of the commencement period.

### 4. Critical Red Flags & AP Liability
* BA approval under BO does **not** imply acceptance under Cap. 7 — dual track compliance risk.
* Consent after >2 years still depends on practicality of completing within Re-development Order period.
* Material variation without amending Exclusion Order risks Cap. 7 non-compliance even if BD plans are otherwise acceptable.

---

## PNAP APP-2: Calculation of Gross Floor Area and Non-accountable Gross Floor Area — Building (Planning) Regulation 23(3)(a) and (b)
**Status/Context:** GFA concession requirement (core GFA/SC measurement and disregard rules; APP-151 / BEAM Plus cross-referenced)

### 1. Core Technical Requirements & Metrics
* **GFA basic rule (B(P)R 23(3)(a)):** Area within outer surface of external walls at each floor level; unfloored portions also included.
* **Voids — modification cases (paras 2–3):** Modification may be granted for voids in: (a) cinema/theatre balconies; (b) banking halls; (c) shopping arcades where total void area ≤ **10%** of shopping arcade GFA; (d) single-staircase buildings with ground-storey cockloft storage; (e) auditoria, sporting halls (incl. squash courts), school halls, religious institutions; (f) main common entrance lobbies of non-domestic buildings; (g) duplex flats/houses meeting Appendix A. Items (a)–(g) subject to APP-151 prerequisites (a–g); overall cap on GFA concessions for (f) and (g) only (APP-151). Split level < **1 m** may be treated as level; >1 m requires prior BD clarification.
* **Duplex/house void criteria (Appendix A):** Duplex: UFS min **150 m²**, void ≤ **10%** of UFS, headroom max **6.5 m**, location living/dining or entrance foyer; only two void levels per tower subject to max **0.5%** of total domestic GFA (flexibility for low-rise low-density). Houses: UFS min **250 m²**, void ≤ **5%** of UFS, headroom max **7.0 m** (sloping pitch roof: measure to mean underside above void). Conditions: abuse prevention (upstand beams, large exterior glazing, no adjoining structural wall/beam); no town-plan/lease contravention after void exemption; DMC (or SPA/tenancy) undertaking designating voids.
* **Facilities/features (para 4):** Favourable modification consideration (APP-151 prerequisites for all except (e); APP-151 overall GFA concession cap for (a)–(d) only): chimney shafts; filtration plant rooms for hotel swimming pools / communal water features; SMATV room ≤ **1.2 m (W) × 1.2 m (D)** (APP-42 para 33); pipe/air ducts for non-mandatory/non-essential plant; pipe/air ducts for mandatory/essential plant (no APP-151 prerequisite/cap for (e)); E&F plant rooms (rainwater/greywater recycling, solar battery rooms).
* **Refuge floors:** Modification may be granted if FS Code compliant.
* **Curtain walls (paras 6–8):** Non-loadbearing enclosure on load-bearing structure (B(C)R s26). Outer face of structural elements accepted for GFA/SC if: (a) CW not part of parent structural system; (b) RC dwarf perimeter wall ≥ **300 mm** high from floor (no extra floor area); (c) projection ≤ **200 mm** domestic / **250 mm** non-domestic (hotels treated as non-domestic); (d) glass external reflectance ≤ **20%**. Not applicable to industrial buildings with small workshop units. Wholesale conversion CW projecting over streets: favourable BO s31(1) exemption if low-energy glazing/energy-efficient design achieving **40%** in BEAM Plus EU and IEQ (HKGBC); require HKGBC registration acknowledgement + undertaking for Provisional Assessment before consent and Final Assessment within **6 months** of BA’s BA14 acknowledgement. Localised facade / existing balcony CW over street not accepted. If street projection permitted, not GFA/SC accountable.
* **Cladding (para 9):** Nominal thickness or cladding overall ≤ **90 mm** (≤ **75 mm** for cladding to non-structural prefabricated external walls) disregardable for B(P)R 23(3) measurement; no projection beyond site boundaries; street projection needs BO s31(1) exemption.
* **Non-accountable GFA (B(P)R 23(3)(b)):** Machinery/equipment for lift, A/C, heating or similar services — interpreted to include fire control centre, water tanks, electrical switch/meter rooms, transformer/generator/pump rooms, telephone equipment, cable riser duct, CO rooms, hose reel closets, sewage treatment plant rooms, smoke extraction. Single-family/house: no service duplication where GFAs also separately excluded; only minimum GFA; may require multipurpose/centralised rooms. Enclosing walls/protected lobby solely serving disregarded rooms (max wall thickness normally ≤ **100 mm**) may also be disregarded. A/C/heating plant room GFA concession subject to APP-151 prerequisites and overall cap. Staircases/lift shafts/vertical ducts measured with floors they pass (except refuge floors); may be discounted if solely serving non-accountable floors.
* **Car park GFA disregard (paras 15–19, Appendix C):** Reference to C for T, statutory town plans, HKPSG; open/podium roof generally not GFA accountable. Principles (EV charging-enabling required except automated parking): underground — private/public **100%**, L/UL **100%**; aboveground ≤2 floors — **100%** / other floors **50%** (L/UL: GL **100%**, above GL **50%**); aboveground with technical infeasibility underground or no adverse env/visual impact — **100%**; GA under lease — **100%**; HKHS/URA subsidised flats under lease — **100%**. Effective dates: underground public car parks from **1 Mar 2017**; para 18(b) and aboveground public under 18(c) from **1 Nov 2025**; 18(d)/(e) from **1 Aug 2023**. EV requirements (Appendix C para 4) for new GBP/major revision on/after **1 Nov 2025**; pre-revision approvals reference Dec 2023 PNAP version. Underground definition: soffit ≤ mean street level (1 street) or ≤ average of abutting streets, with ≤ **5 m** above lowest street mean; or ≤ half storey / ≤ **2.5 m** protrusion for natural LV; special site-constraint semi-sunken. 18(c)(i) examples: major underground utilities; BO Schedule 5 Areas 1–4; complex geotech. 18(c)(ii) example: PR ≤ **1**, ≤ **6** storeys (5 above 1-storey car park). Aboveground >2 floors may still get 100% if total aboveground carpark floor area ≤ **2× site area** due to site constraints (slope, OVT, GA, POS, NBA, wind corridor, railway reserve, etc.). Ancillary areas: 100%/50%/0% depending on whether they solely serve 100% or 50% disregarded parks. Loading/unloading ramps direct to warehouse floors fully GFA. Mixed run-in serving 100% and 50% floors: pro-rata. Refuse-vehicle parking next to RSMRC may be disregarded if vehicular access required under Refuse Storage regs.
* **PTT:** Generally GFA accountable unless town plan/planning approval provides otherwise.
* **Bicycle parking:** Covered spaces required under lease and designated as common areas — GFA exemption of B(P)R 23(3)(a) on application.

### 2. GFA, Site Coverage, or Design Concession Impact
Central GFA/SC measurement instrument. Multiple categories of void, plant, curtain wall, cladding, car park and bicycle parking concessions; several categories expressly tied to **PNAP APP-151 overall GFA concession cap and pre-requisites**. Wholesale conversion curtain walls over streets require **BEAM Plus** EU/IEQ 40% pathway. EV-enabling is a precondition for car park GFA disregard (subject to listed exceptions and effective dates).

### 3. BD Submission & Certification Procedures
* Modification applications for voids/features; duplex void owner’s DMC/SPA undertaking.
* Wholesale CW street projection: HKGBC registration letter + undertaking for Provisional Assessment (pre-consent) and Final Assessment (within 6 months of BA14 ack).
* Car park: GBP carparking schedule + EV charging facility report by RPE (Electrical or Building Services); may defer EV report to consent with BA condition before superstructure consent; EPD comments within **22** calendar days; RPE completion certificate then EPD no-objection within **10** days for OP; EV meter rooms essential plant under 23(3)(b). HKHS/URA letter + TD-agreed provisions before plans for subsidised flats.

### 4. Critical Red Flags & AP Liability
* APP-151 10% overall cap / prerequisites missed for capped items → concession refused.
* Curtain wall projection, reflectance >20%, or no 300 mm dwarf wall → full GFA/SC to outer CW face.
* Abuse of house/single-family plant rooms; oversized disregarded areas.
* Car parks without EV charging-enabling (from applicable date) lose disregard.
* PTT assumed accountable unless town plan provides otherwise.
* Site constraint / “no adverse impact” claims for 100% aboveground parking need evidence.

---

## PNAP APP-3: Nomination of an Authorized Person, Registered Structural Engineer or Registered Geotechnical Engineer to act in stead
**Status/Context:** Administrative workflow (temporary nomination during illness / absence from Hong Kong)

### 1. Core Technical Requirements & Metrics
* Nominate temporary replacement via Form **BA 21** (building/street works) or **MW09** (Class I minor works) within **7 days** of incapacity/absence (BO ss4(2), 4A(5); B(A)R 23(2); B(MW)R s49).
* One BA21 for all active building/street works projects (list in duplicate); for RSE/RGE under different APs — one BA21 per AP, signed by that AP; Class I MW — one MW09 for all active MW projects.
* Nominee must reference BA21/MW09 authority when communicating with BD; **cannot** further nominate another AP/RSE/RGE.
* Recovery/return before nominated expiry: advise BD by letter within **7 days**. Class I MW cessation: nominee notifies BD via **MW31** within **7 days** (B(MW)R s50).
* Temporary only AND due to illness or absence from HK. Acting period > **3 months** or frequent intervals generally **not** temporary — BA may refuse; owner advised to appoint another.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
Submit BA21/MW09; BD formally acknowledges with copy to owner / person arranging MW, stating period and reason.

### 4. Critical Red Flags & AP Liability
* Using temporary nomination for long-term or frequent absences — likely refusal and pressure for substantive reappointment.
* Multiple APs / projects without proper per-AP BA21 splits.
* Nominee sub-nominating (prohibited).

---

## PNAP APP-4: Water Supply and Wells
**Status/Context:** Administrative / services design workflow (water supply certification; well sinking permission)

### 1. Core Technical Requirements & Metrics
* Early Water Authority Certificate Regarding Water Supply Availability (Form WWO 1004 or equivalent) with first GBP submission.
* Where Water Authority certifies mains supply not available (B(SSFPDWL)R 10A(5)), well/other source permission may be considered.
* **Flushing demand standards:** Domestic / offices etc.: **450 litres** per required soil fitment per day; restaurants **13.5 L**/seat/day; cinemas **4.5 L**/seat/day; schools **18 L**/head/day; hotels/boarding **90 L**/room/day. Potable: assess on merits.
* **A/C:** No fresh/salt mains for evaporative A/C except specific industrial process immediate needs.
* Wells normally not on government land. Private land well permission (B(C)R 85) only if yield adequate and abstraction will not adversely affect nearby services/buildings/structures/land. Yuen Long Town (Area 2) and Ma On Shan (Area 4) — wells may cause excessive settlement; flushing usually supplied when possible.
* **Yield test (Appendix A):** Only **1 Dec–30 Apr**; **7 consecutive days**; pumping ≤ **12 h**/day (≥12 h recovery); day 1–6 at proposed daily yield averaged over pumping period; metered quantity (not pump rating); water levels timed; day 7 suspended particles check at full pump discharge / max drawdown; discharge to drain not back to aquifer. Accept if daily quantity ≥ required and adequate recovery, water clean. >12 h/day or long-term yield concern → more sophisticated test (e.g. BS 6316:1983) may be required. Notify BD and GEO ≥ **1 week** before yield test.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact (services adequacy / groundwater risk).

### 3. BD Submission & Certification Procedures
* Well application: plans/cross-sections of drawdown influence; well design/screen/switching/development method; rate/duration per day; yield test proposal; if needed RGE SI report, geotech assessment with calculations, field verification tests.
* AP Certificates under B(A)R 25A — model Appendix B (permanent connection) / Appendix C (yield test 10A(7)); extra yield test report copy to GEO Information Unit. Water quality to BA satisfaction — Water Authority sample report may be required.

### 4. Critical Red Flags & AP Liability
* Designing without Water Authority availability certificate.
* Wells in geologically sensitive scheduled areas without adequate RGE assessment → settlement risk and refusal.
* Yield tests outside Dec–Apr window or without BD/GEO notice.

---

## PNAP APP-5: Height of Storeys — Regulations 3(3) & 24 of Building (Planning) Regulations
**Status/Context:** Mandatory dimensional / GFA measurement rule (storey height; transfer plate GFA)

### 1. Core Technical Requirements & Metrics
* Storey height (B(P)R 24) measured between structural members, **disregarding** finishes (false ceilings, screeding, plaster, flooring). Same for balcony clear height (B(P)R 3(3)).
* Peripheral beams projecting internally from external walls: **2 m** to underside permissible where **2.3 m** minimum hard; beams over doorways at door height OK. Staircase clear height min **2 m**; beams across narrow corridors may be at “notional doorway” height.
* Habitation/office rooms min clear height **2.5 m** (health).
* **Domestic storey height maxima for B(P)R 23(3)(a):** Flat typical **3.5 m**; topmost floor **4 m** (duplex/triplex: max only to one storey of the duplex/triplex); House **4.5 m**.
* **Transfer plate not GFA accountable if:** (a) domestic ≤40 storeys: plate thickness ≤ typical floor storey height; (b) domestic >40 storeys and non-domestic: thickness ≤ **4.5 m**; (c) total transfer plate area ≤ **2×** total GFA of lowest floor of blocks atop. Multiple domestic blocks on one plate: refer to lowest domestic block. Building services zone within plate excluded from thickness measurement but needs safe maintenance access.

### 2. GFA, Site Coverage, or Design Concession Impact
Transfer plate GFA exemption under the metric caps above. Excess storey height can affect GFA accountability under B(P)R 23(3)(a) practice.

### 3. BD Submission & Certification Procedures
Design storey heights and transfer plate dimensions to satisfy the measurable parameters above on plans; no special form beyond normal plan approval.

### 4. Critical Red Flags & AP Liability
* Measuring clear height to finishes rather than structure.
* Oversized transfer plates (thickness or area) become GFA accountable.
* Applying 4 m topmost duplex height to more than one storey of the stack.

---

## PNAP APP-7: Application for Registration as Authorized Persons, Registered Structural Engineers, Registered Geotechnical Engineers and Registered Inspectors
**Status/Context:** Administrative workflow (professional registration — not project design)

### 1. Core Technical Requirements & Metrics
* Inclusion requires prescribed qualifications + RC recommendation (exception: AP/RSE with prescribed experience may join Inspectors’ register without IRC recommendation — BO s3(7AA)(a)).
* **AP:** RA, RPE (structural or civil), or RPS; plus continuous **1 year** HK practical experience within preceding **3 years**.
* **RSE:** RPE structural, or RPE civil with RC-approved structural experience; + 1/3 year HK experience as above.
* **RGE:** RPE geotechnical; + 1/3 year HK experience.
* **RI:** AP, RSE, RA, RPE (building/structural/civil/BS(building)/materials(building)), or RPS (BS or QS); experience pathways within 7 years (AP/RSE) or aggregate 1 year in 3 years / 3 years with ≥1 in last 3 years depending on discipline.
* Registration validity **5 years**. Retention: Form BA1A not earlier than **4 months** and not later than **28 days** before expiry. Restoration within **2 years** of expiry (BA1B).

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
Form **BA 1** + fee; retention BA1A; restoration BA1B. Professional interview scopes in Appendix A (BO/regs, codes, roles, local knowledge).

### 4. Critical Red Flags & AP Liability
* Late retention applications outside statutory window — not accepted.
* Inadequate HK experience window documentation → RC rejection at interview.

---

## PNAP APP-8: Chimneys and Flues
**Status/Context:** Mandatory structural-fire / environmental design rule (B(C)R s44)

### 1. Core Technical Requirements & Metrics
* Comply with B(C)R s44: non-combustible materials; fire safety for design, construction and termination (s44(2)–(4)); insulation justified by calculation (fuel type/rate, nearby materials, use) — BS 5854:1980 guidance.
* Steel chimney structural design per Steel Code 2011, esp. Clause 13.2; wind-excited oscillations by aerodynamic methods; circular chimneys may use Clause 13.2.8 simplified method.
* Corrosion protection / avoid bimetallic action (Clause 13.2.7; Annex A Steel Code; manufacturer instructions). Penetrations: flashing/weather hood for differential expansion and bimetallic action. Also BS EN 1856-1:2009, BS 5854:1980.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact under this note (chimney shaft GFA modification is in APP-2).

### 3. BD Submission & Certification Procedures
GBP with chimneys/flues referred to EPD under ADM-2 centralised processing. Air Pollution Control Ordinance prior EPD approval may be required. Food business / offensive trade licensing requirements may also apply.

### 4. Critical Red Flags & AP Liability
* Missing insulation/fire justification or oscillation analysis.
* EPD comments/approvals not obtained — APCO and licensing delays.

---

## PNAP APP-9: Country Parks Ordinance, Cap 208 — Buildings Ordinance section 16(1)(d)
**Status/Context:** Administrative workflow / refusal ground (country park / special area development control)

### 1. Core Technical Requirements & Metrics
* After notice under Country Parks Ordinance s9(1), no new development in proposed country park on draft map without prior Country Parks Authority approval (s10(1)).
* BO s16(1)(d) may be invoked to reject BD proposals unless/until Country Parks Authority prior approval obtained; failure of attached conditions may likewise lead to rejection.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
Consult Country Parks Authority as early as possible for affected sites; purchase boundary plans from Agriculture and Fisheries Department (as named in note).

### 4. Critical Red Flags & AP Liability
* Submitting GBP for sites in designated/proposed country parks or special areas without Authority approval → s16(1)(d) refusal.

---

## PNAP APP-10: Oil Storage Installations — Building (Oil Storage Installations) Regulations
**Status/Context:** Mandatory structural-fire / hazardous installation licensing regime

### 1. Core Technical Requirements & Metrics
* **Definition (BO s2(1)):** Tank ≥ **110,000 litres**, or group within same cluster/bunded area any one ≥ **110,000 litres**, above ground for petroleum products.
* Construction needs BO s14(1) approval and consent. Deemed to satisfy B(OSI)R if meets Code of Practice for Oil Storage Installations **1992**. Must not operate before licence. A&A (incl. new tank) need licence endorsement.
* **General inspection (Reg 8(1)(a)):** Internal inspection of all tanks not later than **10th year** of tank life; thereafter in the **5th year** after first inspection year. Annual licence renewal with external inspection certificates (Reg 8(1)(b)) and associated works certificates (8(1)(c)).
* Repair/A&A: two copies of proposals signed by RSE for Reg 10 written authorization; extensive repair or non-exempted building works also need BO s14(1).
* Demolition: method statement for BA agreement before/with consent or authorization; follow Appendix D + PNAP 71 (APP-21) public safety measures. Typhoon damage risk to partially constructed tanks — need weather precautions.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
* New licence: six English + one Chinese copies of operation instructions; one set GA plans; OP + general inspection certificate required before licence.
* Certificates Appendices A (general), B (external), C (associated works). Demolition: contamination assessment report (EPD guidance), gas-free certification by competent person, sludge/chemical waste disposal under Waste Disposal (Chemical Waste) regs, oil interceptor control under WPCO, soil hydrocarbon/lead tests after demolition.

### 4. Critical Red Flags & AP Liability
* Operating/altering without licence/endorsement.
* Incomplete bilingual operation instructions.
* Demolition without gas-freeing, interceptor control, or contamination assessment → pollution/explosion risk and BA refusal.

---

## PNAP APP-11: Street Improvement Schemes — Submission of Building Plans in respect of Lots affected thereby
**Status/Context:** Administrative workflow (street improvement plan vs BO approval — no compensation implication)

### 1. Core Technical Requirements & Metrics
* Pre-1982 approved street improvement schemes remain valid despite Cap 370. Improvement plans indicate desirable works only — no representation of implementation or resumption.
* Improvement plan existence is not a basis for owner compensation/damages.
* BO approval of plans conforming to improvement plan does not imply implementation or compensation. Approval of non-conforming plans is without prejudice to Government action under other enactments including resumption.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact (compensation/schematic interface only).

### 3. BD Submission & Certification Procedures
For lots apparently affected: enquire Highways Department on Government intention before formal GBP submission to reduce abortive work.

### 4. Critical Red Flags & AP Liability
* Assuming BO approval locks in street improvement implementation or compensation rights.
* Designing to unimplemented improvement lines without HyD confirmation — abortive redesign risk.

---

## PNAP APP-12: Prestressed Ground Anchors in Building Works
**Status/Context:** Mandatory structural / geotechnical rule (generally refuse permanent anchors needing long-term monitoring)

### 1. Core Technical Requirements & Metrics
* BD view: permanent prestressed ground anchors requiring long-term monitoring are short-lived temporary works — BA may refuse incorporation into permanent buildings under BO.
* Exceptional acceptance: GEOSPEC 1 + GEO Prior Approval System for Permanent Prestressed Ground Anchors (PASA) for Approved Anchor Systems/Types.
* Outside site boundary into public/private streets, government or adjacent private land — only exceptional approval; government land needs early Lands Dept permission; adjacent private land: Form BA5 for site formation should include adjoining lot number (acquiescence).
* Grease monitoring: GEOSPEC 1 Corrigenda 1/98 and 2/98 (hexane extraction; blank determination; ion contents as ppm by mass of final aqueous extract / deionized water mass).

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
* Approval stage (PASA anchors): location/inclination/length plans; Anchor Class, design working load, free length + geotech/design calcs; Suitability/Extended Acceptance test schedule; compression movement allowance; anchor pad details; long-term monitoring schedule, access, and **maintenance party agreement**.
* Plans/sections with boundaries and geotech info + own design calcs; utility/structure plans demonstrating no damage.
* Pre-consent: Approved System/Type names; replaceable materials specs; monitoring schedule/interpretation guidelines; Nominated Anchor Contractor name/experience. BO s17(1) conditions on workmanship/supervision may be imposed.
* Keep certified Prior Approval Documents on site. Post-installation: as-built full length drawings + system/type, loads, as-built lengths/strata/grout/pressure, dates, stressing/test records, monitoring results, future monitoring schedule/guidelines.

### 4. Critical Red Flags & AP Liability
* Proposing permanent monitored anchors as routine — likely refusal.
* Missing maintenance party undertaking; anchors outside lot without Lands/neighbour consent.
* PASA does not discharge AP/RSE BO duties.

---

## PNAP APP-13: Submission of Certificate of Completion of Building Works, Application for Occupation Permit and Submission of Record Plans and Information
**Status/Context:** Administrative workflow (completion / OP documentation)

### 1. Core Technical Requirements & Metrics
* Completion: BA14/14A/14B/14C and/or MW02/04 (not resulting in new building) or BA12/13 (new building) under B(A)R 25. Typical BD reply: BA14/14A **28 days**; BA14B/14C **14 days** non-audit / **28 days** audit; BA12/13 with OP within **14 days** (BO s21).
* Same contractor for spread footing (excavation ≤ **4.5 m**) + superstructure: single BA12/13 or BA14 may cover both — separate footing BA14 not required.
* Amend plans and secure approval **before** OP (minor positional deviations that do not contravene BO may be OK).
* Record plans (reg 46 “new plans” if major alterations): amalgamated GBP as completed with BA approval chop or AP certification identical to approved; soft copy DVD-ROM or photo-reduced ≥ **1:200**; no unapproved amendments. Encourage AutoCAD/Microstation DVD for RVD.
* Materials schedule under B(A)R 44 with OP: AP certifies compliance; RC confirms use; cover structural integrity and fire safety products not on approved plans + cast iron pipes (APP-133); fire-rated doorsets/partitions may use APP-165 PCC certificates. Fire dampers: RSC(V) inspect/certify safe working order (FS Code E8.3).
* RSE structural document summary tables half-yearly + at foundation completion/OP (Appendices C–E).
* OP soft docs: DVD for ADM-2, **APP-126, APP-151, APP-152, APP-156** uploadables.
* Fast-track BA14C for: simple A&A under ADM-19 para 29; curtain/window wall/cladding repair replacement under ADM-19 para 32; signboards under APP-126 paras 8–10 — need record plans/docs + colour photos/mark-ups.

### 2. GFA, Site Coverage, or Design Concession Impact
No direct spatial measurement rule. OP dossier must include APP-151-related soft documents when concessions were granted — incomplete APP-151 package can block OP.

### 3. BD Submission & Certification Procedures
BA12/13/14 series; materials Schedule Appendices A/B; RSC(V) for dampers; checklists Appendices F/G; paperless DVD except specified hard certificates. Appendix H indexing for discs; AP declaration on disc cover.

### 4. Critical Red Flags & AP Liability
* Simultaneous OP and unapproved amendment plans.
* Record plans showing unapproved deviations; false materials certification (criminal risk noted on forms).
* Missing APP-151 / BEAM-related soft copies at OP.
* RSE late structural documents delaying BA14/OP.

---

## PNAP APP-14: Cinemas and Other Places of Public Entertainment in Non-domestic Buildings or Composite Buildings
**Status/Context:** Mandatory structural-fire / MOE design rule (B(P)R 49B; MOE/FRC/MOA Codes)

### 1. Core Technical Requirements & Metrics
* B(P)R 49B: cinema(s) ≤ **2,000** persons aggregate may be in any storey of non-domestic building or non-domestic part of composite; may share exits, foyers, waiting, vestibules, projection rooms.
* **Shared exits conditions:** dedicated smoke extraction + FSI to DFS satisfaction; FRP walls/floors per FRC Code (doors ≥ wall FRP); foyer separation same FRP unless foyer also smoke-extracted then separate foyer from other accommodations; openings to adjoining non-domestic protected by door/shutter of equal FRP; shared exits accessible from common circulation without passing private premises; staircases directly connected to cinema(s) only → MOE Code 17.2(b) & 26.2; widths based on combined occupancy (paras 4–7); composite: cinema exits separated from domestic exits; discharges to streets ≥ **4.5 m** wide with two routes to different thoroughfares; **not in basement** (for shared-exit regime of para 2).
* Height ≥ **12 m** above pavement: MOE Code paras 25.1, 25.3, 25.4 widths apply. Shared exit wider than floors below → that width must continue down to ground.
* **Horizontal exits** via adjoining accommodations: ≤ **half** of total required exit width for that cinema; common circulation floor area ≥ **0.5 m²**/person based on pro-rata cinema load through those exits + foyer at 1 person/0.5 m² + adjoining circulation per MOE Table 1.
* **Seatways:** max row length **12 m** (one gangway) / **24 m** (two); seat counts per seatway width Table A (300–324 mm → 7/14 seats … 500 mm+ limited by 12 m/24 m length). Seatway width = clear distance back of seat to nearest projection behind (tip-up measured tipped).
* **Gangways Table B:** <500 pax **1,100 mm**; 501–1000 **1,200**; 1001–1500 **1,350**; >1500 **1,500**.
* **Projection rooms:** FRP ≥ **1 hour** walls/floors; door leakage ≤ **3 m³/hour/m** (head/jambs) at 25 Pa BS 476 Sec 31.1 + FRP ≥1 h (except if no film/arc/xenon/hazard light sources). Elevated projection room for one box may have one exit if MOE 14(3)(b) distances OK; may discharge via seating to staircase. Mechanical ventilation to open air by independent system if no natural vent.
* **Foyers (Reg 49E):** **0.5 m²**/person at ratio **1 in 6** of seating capacity. Basement cinemas: foyer on **ground floor** at **0.5 m²**/person at **1 in 3**; 4-hour FRP separation; lifts via protected lobby; fireman’s lift via ventilated lobby in firefighting stairway.
* Capacity ≤ **50** PPE/cinema per premises may share exits without Part III MOE PPE rules / this PNAP shared-exit full suite if: aggregate such premises ≤ **150**; not basement; projection rooms comply; foyer per para 13.
* Other PPE ≤ **500** aggregate in non-domestic (non-polluting industrial) / composite non-domestic: may abut one thoroughfare if EVA + DFS no objection; B(P)R 49A modification may be considered.

### 2. GFA, Site Coverage, or Design Concession Impact
No GFA concession rule. Design impacts MOE, FRP and foyer areas (waiting space sizing). Cinema foyer voids may interact with APP-2 void modification separately.

### 3. BD Submission & Certification Procedures
Plans demonstrating MOE/FRC compliance; DFS satisfaction for smoke extraction/FSI. Seats need not be installed before OP/BA14 if gangways/seatways demarcated and developer/AP undertaking submitted that seats will be installed before cinema licence application.

### 4. Critical Red Flags & AP Liability
* Sharing exits without dedicated smoke extraction / inadequate FRP / basement shared-exit regime.
* Discharge streets <4.5 m or both exits to same thoroughfare.
* Seatway/gangway dimensions outside Tables A/B.
* Missing foyer ratio (esp. basement 1-in-3 vs normal 1-in-6).
* Composite buildings lacking domestic/non-domestic exit separation.

---

## PNAP APP-15: Site Formation — Temporary or Permanent Filling Work
**Status/Context:** Mandatory geotechnical / site formation rule (compaction standards)

### 1. Core Technical Requirements & Metrics
* Flowslide risk of loosely placed unretained earth fill. Where failure could endanger public, BA requires drawings specifying Appendix A standards; RGE periodic supervision and inspections; supervision plan under BO s39A TMM and s17(1)(6)(e) as in PNAP 83.
* **Compaction (Appendix A):** Peripheral portion of earth fill slope in-situ field dry density ≥ **95%** of max dry density (Geospec 3). Max dry density/OMC per Geospec 3 for each soil type at first use and with each field density set. In-situ density frequency Table 1 (e.g. excavations/formations 0–100 m²: **3** determinations; other areas 0–1 ha: **4** per 1000 m², etc.). Small fill (depth < **1 m** and volume < **300 m³**) may reduce frequency if supplemented by penetration tests. Tests only by HOKLAS-accredited labs for relevant tests. Same batch type/source for MDD vs in-situ pairing.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
* Notice of fill commencement date to BA. Monthly RGE-signed compaction reports (in-situ density summary, lab compaction, relative compaction, non-compliance + corrective measures). Keep records on site for BD/GEO.
* BA may require GCO probes / trial pits; AP/RGE arrange labourers. Loose fill: in-situ density tests in presence of BD/GEO; extensive risk → Cease Works Order BO s23 or 24A.
* Completion before BA14 site formation / OP: as-built plans/sections + complete compaction records. Structural works: RSE signs structural calcs/assessment and certifies structural completion.

### 4. Critical Red Flags & AP Liability
* Temporary fills left on site or permanent fills failing Appendix A → OP refusal under BO s21(6)(a).
* Non-HOKLAS testing; wrong soil pairing for MDD vs field density.
* Missing monthly reports / RGE involvement.

---

## PNAP APP-16: Cladding
**Status/Context:** Mandatory structural / fire / durability design rule (B(C)R ss3 & 28)

### 1. Core Technical Requirements & Metrics
* Cladding = facing/architectural decoration additional to structure (metal, stone, GRC, etc.). Performance: materials, fixings, strength, durability, non-combustibility, maintenance access. Flexible horizontal/vertical joints for differential movement; anchors/dowels/fixings stainless/corrosion-resistant. Sand/cement bedding and/or epoxy alone **not** suitable permanent stone fixings.
* Non-combustibility: FS Code Part E s5; external cladding E10.1 & E12.1; internal cladding E13.1 deem-to-satisfy.
* Structural plans required when cladding > **6 m** above adjoining ground/floor: thickness, strength, durability, type, fixings, support layout; framing, elevations with expansion joints, anchors/supports, loads/codes, material & workmanship specs (welding, galvanising, bi-metallic), calcs (parent structure check, stability, element design, deflection).
* Metal cladding may be streamlined into superstructure plans (location still on GBP) — reference ADV-33 Appendices B6/B9.
* Separate RSE for cladding: BA4/BA5; completion cert B(A)R 25(3); assessment report + project RSE awareness statement on parent structure; separate RSE supervises construction including cast-in anchors unless pre-installed by project RSE under superstructure plans.
* **Anchor tests (>6 m):** representative pull-out to ≥ **1.5×** manufacturer recommended tensile load; no separation/plastic deformation/deleterious effect.
* **Stone tests:** ASTM C880 or BS EN 12372 flexural; ASTM C1354 anchorage; ≥ **5** random specimens each; independent testing agency; AP/RSE endorse results; submit before OP. Limestone: aged residual flexural & anchorage ≥ **80%** of standard after 50 thermal + 50 wet/dry cycles (Appendix B). Acceptance: char. flexural > **3×** design allowable; avg flexural > allowable × FSF; char. anchorage > **4.2×** allowable; avg anchorage > allowable × ASF. Characteristic = avg − Kσ (K=**3.41** for ≥5). ASF = FSF × **1.4**; default FSF/ASF examples granite **4.5/6.3**, limestone **7.2/10.08**, marble **6.3/8.82**.
* Minor works for certain cladding erection/repair/replacement/removal — APP-147 / B(MW)R Schedule 1.

### 2. GFA, Site Coverage, or Design Concession Impact
Cladding thickness limits for SC/GFA measurement are in **APP-2** (≤90 mm / ≤75 mm prefab). This note governs structural/fire/testing acceptance.

### 3. BD Submission & Certification Procedures
GBP cladding location/material; structural plans as above; BA4/BA5 if separate RSE; test reports before OP; MW path where applicable.

### 4. Critical Red Flags & AP Liability
* Stone fixed only by bedding/epoxy; missing >6 m structural details → approval/consent delay or refusal.
* Limestone without aged testing; failing FSF/ASF criteria.
* Cast-in anchorage responsibility split unclear between project and cladding RSE.

---

## PNAP APP-17: Rock Faces — Building (Planning) Regulations 27 and 47
**Status/Context:** Mandatory geotechnical / site formation rule

### 1. Core Technical Requirements & Metrics
* For B(P)R 47, “massive rock face” only if **widely jointed (spacing > 600 mm)** with no unfavourable joints/discontinuities/defects. Other rock faces → B(P)R 27 provisions apply.
* Design start: SI, API, mapping, drillholes; packer/impression/CCTV etc.; Geoguides 1–4 and Geotechnical Manual for Slopes (Tables 5.6–5.7 for analysis/stabilisation).
* Plans must state assumptions on jointing for overall/local support. Good practice notes: controlled blasting / pre-split or smooth-face where suitable; expanding agents — prevent uncontrolled flow and assess stability effects; immediately after excavation scale final face and survey by qualified geotechnical engineer/engineering geologist (e.g. RPE Geotech with rock face experience) including seepages and weak impermeable zones (e.g. kaolinitic clay layers — Fei Tsui Road lesson); large-scale engineering geological drawings + support/drainage details + calcs + photos for BA approval.
* Prevent uncontrolled rockfalls during construction, especially on existing faces affecting public safety.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
Site formation plans with assumptions, good-practice notes, post-excavation geological drawings/photos/calcs for approval; engage qualified geotechnical professionals for surveys.

### 4. Critical Red Flags & AP Liability
* Claiming “massive rock face” without >600 mm joint spacing and favourable discontinuities.
* Missing post-excavation scaling survey — Fei Tsui-type undetected weak layers.
* Inadequate blast/expanding-agent controls near public.

---

## PNAP APP-18: Code of Practice for Foundations 2017
**Status/Context:** Mandatory structural / geotechnical foundation code application & administrative streamlining

### 1. Core Technical Requirements & Metrics
* Compliance with CoP Foundations 2017 (2024 Edition + Appendix A Sep 2025 amendments) is deemed-to-satisfy relevant B(C)R. Key 2025 amendments include: granular soil ultimate bearing capacity limit **3,000 kPa**, raised to **4,500 kPa** for foundations supporting buildings with basements on granular soil; overburden depth for qo generally ≤ **3 m or B**, whichever smaller — for basement on granular soil effective perimeter overburden ≤ **10 m or B**; shallow foundation Es ≈ **1×** SPT N; raft on granitic saprolite/residual with N>30 may use Es ≈ **1.5×** N; related plate load / tension test wording updates.
* Novel piling systems: pre-submission ADM-19 enquiry; full system technical details + demonstration.
* Steel H-pile sections: manufacturing, mill certs, CEV, HOKLAS mechanical/chemical, welding, QA — BD “Deemed-to-Satisfy” web list; otherwise include in plans.
* GEO TGN 26/53 presumed capacities (marble / igneous): BA conditions under BO s17(1) item 6 for as-built settlement analysis, structure tolerance assessment, post-foundation report, settlement monitoring scheme before pile cap/superstructure, and final performance review before OP/BA14.
* Mass concrete fill under shallow foundations with max depth > **1 m** = structural element (Concrete Code 2013).
* Pre-/post-/proof core drilling by RSC Ground Investigation Field Works; independence declaration vs foundation contractor for Reg 20 B(C)R proof coring.
* Large diameter bored pile interface: optional ≥ **150 mm** pipe stopped ~1 m above interface; thin sediment/segregation/weathered seam may be acceptable with RSE/RGE justification or pre-approved remedial method statement + supervision.
* **Two-stage pile plan submission:** Stage 1 — max capacities, layout/specs without rigorous pile-cap analysis or load schedules; Stage 2 — full load path, schedules, rigorous analysis. Consent after Stage 1 possible; BA14 only after Stage 1 amendments (if any) and Stage 2 approved.
* **Deferred site-specific GI:** Non-scheduled areas and Schedule Areas **3 & 5** may approve on existing GI within **20 m** of boundary (GIU/previous development); site-specific GI + assessment verifying assumptions concurrent with consent; incompatible → revise plans before consent or consent refused under BO s16(3)(ba).
* Piles within **10 m** of boundary: consent may wait for pile wall/grout curtain records and assessment.
* Concurrent approval+consent: Form BA8 not before **32nd day** after plan submission.
* Driven H-piles: working pile consent without completed trial proof load test if PDA+CAPWAP satisfactory; proof load reports within **14 days** of test completion.
* Initial ELS concurrent: excavation to bottom of first strut layer but ≤ **1.5 m** below EGL + first waling/struts.
* Pile cap/superstructure consent only after satisfactory records, BA14, proof tests, imposed conditions.
* As-built pile length vs approved ± **5%** or significant uneven lengths → back-analysis and load schedule amendment; Areas 2 & 4 also APP-61 / Code cl.7.8. Large diameter BA14 after ≥ **85%** interface proof drilling may allow early pile selection for proof coring.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
Foundation plans/calcs/reports (RGE for geotech docs — APP-141); BA14 + phased records; Stage 1/2 packs per Annex C1; monitoring and final settlement performance reviews where TGN presumed values used.

### 4. Critical Red Flags & AP Liability
* Consent/BA14 without Stage 2 (two-stage path), proof tests, or TGN settlement reviews.
* Boundary piles without wall/curtain records.
* Mass concrete fill >1 m untreated as structure.
* Deferred GI assessment incompatible with approved plans → consent refused.

---

## PNAP APP-19: Projections in relation to Site Coverage and Plot Ratio — Building (Planning) Regulations 20 & 21
**Status/Context:** GFA / SC / PR concession and exclusion rules for projecting features

### 1. Core Technical Requirements & Metrics
* SC includes all building components including projections (bulk control). Non-floor-level projections that do not dominate facade need not be GFA.
* **SC and PR disregard list (para 3) if not exaggerated:** pitched eaves / flat roof overhangs per B(P)R 7(1) (not within parapet as accessible roof); individual A/C boxes/platforms ≤ **750 mm** with built-in condensate disposal; A/C platforms per CoP Access for External Maintenance Apps B/C; window hoods/porches projection ≤ **2 m** complying B(P)R; window cills/surrounds ≤ **100 mm**; string courses/fins/mouldings per B(P)R 7(1) (not structural beams/columns); window flower boxes ≤ **500 mm** (Diagram 1); drainage pipes/gutters B(P)R 7(2); sunshades for energy conservation ≤ **1.5 m** (**APP-67 & APP-156**); reflectors ≤ **1.5 m** (quantitative environmental assessment if > **0.5 m**); entrance canopies ≤ **3.5 m**; drying racks/light fittings/telecom frames B(P)R 7(3); retractable awnings B(P)R 7(4) + MW item 2.43; plant support frames ≤ **300 mm** within lot (Diagram 2).
* **Projecting windows (not GFA/SC/PR) if all met:** from living/dining/bedroom only; one per room, one wall; elevational area ≤ **50%** of that external wall area; projection ≤ **100 mm**; base ≥ **500 mm** AFFL; B(P)R 3A protective barrier (1,100 mm from floor — fixed/protected within that height); not piecemeal addition to existing buildings.
* **Covered areas under overhangs:** if clear height > **7.5 m**, no weather-protected functional shelter, access impossible/abuse unlikely, and covered-width : clear-height ≥ **1:8**, and no departmental objection — not GFA (exclude shopfront overheads/signboards). Non-compliant special forms: justify with design merits (see APP-2).
* **Street projections:** normally none except Part II B(P)R or public interest; individual A/C ≤750 mm / window hoods ≤500 mm may be permitted if ≥ **2.5 m** above ground (APP-42). Wholesale IB conversion A/C >750 mm / street projection favourably considered with layout constraints + Grade 1 room A/C (EMSD energy labelling CoP) as condition.
* **Common-part greenery projections within lot:** planters ≤ **600 mm** (Diagram 3) with CoP External Maintenance safety + auto irrigation + drainage — GFA/SC exemption **NOT** subject to **APP-151** prerequisites/cap. Maintenance walkway 400–600 mm wide, ≥150 mm drop, CoP safety — GFA concession **IS** subject to **APP-151** prerequisites and overall cap. Combined walkway+planter projection > **750 mm** obstructs prescribed windows. DMC/SPA undertaking + Land Registry registration before OP.

### 2. GFA, Site Coverage, or Design Concession Impact
Defines extensive SC/PR exclusions for minor projections; projecting windows criteria; high-level overhang covered-area exemptions; greenery concessions with explicit **APP-151** distinction (planters exempt from cap; walkways under cap).

### 3. BD Submission & Certification Procedures
Show drainage for cantilevered RC structures per APP-68 on GBP and drainage plans. Greenery: developer undertaking for common parts with Land Registry registration pre-OP. Street A/C exceptions need justification and EMSD Grade 1 condition compliance.

### 4. Critical Red Flags & AP Liability
* Exaggerated “flower box” that is structural beam → counted for SC/PR.
* Projecting windows failing 50%/100 mm/500 mm AFFL criteria.
* Claiming APP-151-free concession for maintenance walkways.
* Combined greenery projection >750 mm affecting prescribed windows.

---

## PNAP APP-20: Building Proposals affected by Street Widening — Building (Planning) Regulation 22(2)
**Status/Context:** GFA concession / bonus PR-SC administrative workflow

### 1. Core Technical Requirements & Metrics
* Compensation for land for street widening may be: bonus PR and/or SC under B(P)R 22(2); cash (Lands); or land exchange (Lands).
* If bonus adopted: subject to para 4 and B(P)R 23(2)(a), BA prepared to accept surrendered street-widening land as counting also as ‘site area’ **only for the first building** subsequently erected on the reduced site, for permitted PR and SC. Additional PR under 22(2)(b) only if density not excessive. Cases individual.
* B(P)R 25: similar principle — setback may count as open space at side/rear.
* TOP/OP will **not** issue before execution of Agreement to Surrender incorporating relevant terms.

### 2. GFA, Site Coverage, or Design Concession Impact
Bonus site area / PR / SC for street widening surrender — first building only; density check for additional PR.

### 3. BD Submission & Certification Procedures
Separate block plan (quadruplicate) showing surrender area; building plans endorsed with surrender areas; formal Agreement to Surrender to Lands Dept satisfaction, registered in Land Registry. Simultaneously copy plans to Chief Estate Surveyor/Acquisition (Lands) when street widening affects lot.

### 4. Critical Red Flags & AP Liability
* Claiming bonus without Agreement to Surrender — OP/TOP blocked.
* Assuming bonus site area applies beyond first subsequent building.
* Missing block plan / endorsement / density justification.

---

## PNAP APP-21: Demolition Works — Measures for Public Safety
**Status/Context:** Mandatory structural-fire / public safety administrative and site safety regime

### 1. Core Technical Requirements & Metrics
* Demolition proposals for formal approval under B(A)R 8(3)/(4); follow Demolition Code 2004. No consent without approved plans (BO s16(3)(a)(b)).
* Certain protective items may be erected without consent if not affecting structure: screens/nets, dust sheets, scaffolds/catchfans, hoarding/walkway/gantry/catch platforms, shoring/propping.
* Supervision plan required before/with consent (except TM para 11 criteria); prepare to Site Supervision CoP 2009 (2024 Ed). Consent may be refused under s16(3)(bc) without plan.
* Full-time site engineer for complex structures per Demolition Code — responsible to RSC; changes reported to AP/RSE/RGE and BA.
* ≥ **1** video camera per site at strategic locations (shown on plan); records kept ≥ **14 days**.
* Powered plant operators: B(DW)R 9(3); training “Demolition of Building Course for Plant Operators” (HKIC) or equivalent; particulars with consent (B(A)R 31); notify BA of change within **7 days**.
* Dangerous buildings under order: secure after closure; steel shores Grade 250+ per Steel Code; party wall shoring detail agreement with EBD; joint demolition coordination; notify BA of unexpected weaknesses.
* Fast-track BA14B if: structurally independent; no basement/below-ground structures (fill debris for buoyancy OK; fill for earth retention fails criterion); nothing above GF slab/beam remains except those; no party-wall/adjoining support needed; no slope/RW stability/drainage/stabilisation works needed. Reply 14/28 days non-audit/audit.
* Hoarding/walkway design: Demolition Code Ch.3 + **APP-23**. Fire-retardant protective nets/screens evidenced on site.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
Approval plans; Form BA8 + TCP Form BA20 + supervision plan + operator particulars + debris management + Chinese demolition plans as checklist Appendix B. Completion BA14A or BA14B. Notify HyD (street name plates), DSD (drain sealing). MW streamlined before demolition Appendix C (MW01 with demolition approval; MW02 with BA14A/B).

### 4. Critical Red Flags & AP Liability
* Consent without approved plans / supervision plan / operator particulars / protective measures (s16(3)(bb)).
* Crane-and-hammer in dense urban areas called out as potentially unsafe.
* Fast-track BA14B claimed when basement/party walls/slopes involved.
* Flammable materials left on site (B(DW)R 6).

---

## PNAP APP-22: Dewatering in Foundation and Basement Excavation Works
**Status/Context:** Mandatory geotechnical / settlement control rule

### 1. Core Technical Requirements & Metrics
* Dewatering procedures and precautions against impairing stability / undue settlement of adjoining buildings, streets and land must satisfy BA.
* Plans must show: adjoining foundation and utility details; dewatering proposals incl. ground treatment (grout/recharge); method/sequence; instrumentation for monitoring effects (groundwater change) with (i) limiting movement/groundwater pressure criteria and actions if exceeded; (ii) reading intervals; (iii) monitoring record availability.
* Supporting: SI report (groundwater, geology, permeability, compressibility, consolidation, particle size); adjoining building condition report; shoring/underpinning if needed; excavation/dewatering effects assessment.
* AP/RSE supervise to Code/approved plans and verify design assumptions; full-time experienced supervisor where necessary. Piezometric and settlement records available at all times; copies to BA periodically. Also Civil Engineering GS groundwater/drawdown sections and BS 8004:1986.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
Include monitoring scheme and supporting reports with foundation/basement plans; submit monitoring copies to BA periodically during works.

### 4. Critical Red Flags & AP Liability
* Dewatering without utility/building assessment or trigger-action monitoring.
* Exceeding limit criteria without prescribed action — adjoining settlement liability.

---

## PNAP APP-23: Hoardings, Covered Walkways and Gantries (including Temporary Access for Construction Vehicles) — Part IX of Building (Planning) Regulations
**Status/Context:** Mandatory public-safety / highway-interface administrative and design rule

### 1. Core Technical Requirements & Metrics
* Erect/maintain hoardings/walkways/gantries per permit under B(P)R 65/66 before works start. Application (reg 64): six plan sets (one if Electronic Submission Hub) showing temporary vehicular access, post holes, traffic signs/provisions, planters/trees; declare obscured/resited signs/lights and affected public transport/crossings/carriageway width.
* Trees on government land: prior approval of tree-maintenance dept; preservation/protection/monitoring proposal before hoarding permit; report damage same day.
* Carriageway encroachment: maintain lane ≥ **3 m** one-way; single carriageway two-way ≥ **5.5 m**; temporary traffic arrangement per HyD Lighting Signing Guarding CoP. Below minima on traffic-sensitive roads (red/pink/bus corridor or within **70 m** of signalised junction with such) → TIA ≥ **2 months** before hoarding permit.
* Clear pedestrian walkway: on carriageway ≥ **1.1 m**; on pavement — existing ≤2.5 m: normally ≥ **1.5 m** (exemption if LOS “C” maintained, never < **1.1 m**); >2.5–3 m: pavement width − **1 m**; >3 m: ≥ **2 m**. Vertical clearance inside covered walkway ≥ **2.3 m**. No obstruction by trees, signs, scaffold poles, gate leaves, etc.
* Lighting: average floor illuminance **35–50 lux**; typical 18/20 W 600 mm fluorescent at **3 m** spacing for 2 m × 2.5 m walkway.
* Gantry width normally ≤ **7.3 m**; wider needs swept path + frequency + pedestrian safety measures. Excavation Permit Cap 28 for works on HyD roads. Temporary access per HyD Standard Drawings / Annex 1 + APP-144.
* **Self-certification first permit: 30 days** if Appendix A HyD/TD met, no TIA, no contractor shed on top, BO-compliant structurally safe design, no tree felling/pruning interference, demolition uses standard designs, slope/RW not adversely affected (App E cert). Else **60 days**. Consent for building works refused if required hoarding proposals not received.
* Validity: demolition permits normally **6 months**; general building works **3 years** with annual safety certificate (App F) ≥ **7 days** before each anniversary. Idle site / missing annual certificate → cancellation. Renewal ≥ **30 days** before expiry with BD109, App G cert, colour photos. Minor amendments self-certifiable within App H criteria — deposit amended plans/cert within **7 days**. No advertising/storage use of walkways.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact (temporary public protection works).

### 3. BD Submission & Certification Procedures
Form BA19 + plans + App E for streamlining; annual App F; renewal App G + photos; minor amendment App H deposit. TD/HyD interface for TIA, parking suspension (Annex 2), Excavation Permit.

### 4. Critical Red Flags & AP Liability
* Undeclared affected traffic facilities delaying permit.
* Substandard walkway width / obstruction / inadequate lighting — public safety and BA repair under reg 67 at owner cost.
* Consent blocked for missing hoarding proposals.
* Using walkways for advertising/storage.

---

## PNAP APP-24: Railway Protection under Railways Ordinance, Mass Transit Railway (Land Resumption and Related Provisions) Ordinance and Area Number 3 of the Scheduled Areas in Schedule 5 to the Buildings Ordinance
**Status/Context:** Mandatory structural / railway safeguarding rule (Scheduled Area 3 + railway protection areas)

### 1. Core Technical Requirements & Metrics
* Protection area guide: ~ **30 m** outside outer railway structure/fence/wall or nearest rail; may encompass whole lot if any part within 30 m; stations may be more extensive. Some lines = BO Schedule 5 Area Number **3**.
* Works in protection areas: special scrutiny; RO s27 / MTR(LR&RP)O s15 measures. Monitoring plan for SI/foundation/ELS and works causing movement/vibration; inform MTRCL of commencement; send monitoring records to MTRCL bi-weekly or agreed frequency. Suspension if Alert/Action limits reached — BD/EMSD joint press within **48 hours**; resumption press within **48 hours** after agreed restart.
* **Area 3 GI:** prior approval and consent (B(A)R 8(1)(l)); plans follow Appendix B; concurrent approval/consent per ADM-16. Area 3 underground drainage (except certain MWCS) **not** exempt — full BO. Outside Area 3 but in protection areas: forward GI/underground drainage proposals to MTRCL before start. Class I/II MW (spread footing/excavation/underground drainage) in Area 3 forwarded to MTRCL; obtain MTRCL agreement before start.
* **Appendix B technical clearances / limits:** No pile/foundation/borehole/well/soil nail etc. within **3 m** of underground railway structures without MTRCL prior special agreement. No piling within **3 m** of railway fence/wall or **7 m** of nearest track centreline (no fence) without agreement. Anchors: any part > **3 m** from railway structure; fixed-length centroid > **2×** fixed length away. Vertical/horizontal pressure change on underground structures ≤ **20 kPa** (reviewable by engineering approach). Boreholes within **10 m** plan of underground structures with tip within **3 m** depth of highest point: verticality method; within **3 m** plan: depth control method. Building openings vs railway ventilation: ≥ **5 m** (or **2.5 m** if exhaust directed away). Scaffolding/signs/projections above tracks: not within **6 m** plan without MTRCL agreement. Vertical greening ≥ **5 m** from railway ventilation openings. Trees unfenced sections ≥ **2 m** from nearest rail. Crane jib arc / storage / mobile plant within **6 m** control.
* **Empirical movement limits (Appendix B C(a)):** angular distortion ≤ **1:1000**; total movement ≤ **20 mm**; rail level difference ≤ **5 mm**; ppv blasting ≤ **25 mm/s**, prolonged vibration ≤ **15 mm/s**; OHL/signalling furniture ppv ≤ **10 mm/s**, amplitude ≤ **80 µm**. AAA levels for movement ~50/75/100%; vibration ~60/80/100% of those limits (table: Alert distortion 1:2000, Alarm 1:1350, Action 1:1000; movements 10/15/20 mm; etc.). Engineering approach (Appendix C): stage AAA based on estimated movements with each stage 10–50% of total; Alert = 50% current stage + prior; Alarm = 100% current + prior (last stage mean of Alert/Action); Action = 100% total estimated.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
Plans circulated to MTRCL; monitoring plan in approval documents; commencement notice + bi-weekly records to MTRCL; Area 3 GI/drainage full approval/consent; MWCS submissions copied to MTRCL; engineering approach via pre-submission enquiry; independent survey team initial readings report to BD and MTRCL before works; stage-by-stage consent may follow monitoring reviews.

### 4. Critical Red Flags & AP Liability
* Boreholes punching tunnels; works within 3 m / piling within fence/track buffers without MTRCL agreement.
* Exceeding AAA without suspending works — press announcement and regulatory stoppage.
* Pressure change >20 kPa without accepted engineering approach.
* Openings/greenery too close to railway vents; crane/storage within 6 m without agreement.

---

## PNAP APP-25: Requirements for a Geotechnical Assessment at General Building Plan Submission Stage — Regulation 8(1)(ba) of Building (Administration) Regulations
**Status/Context:** Administrative / geotechnical feasibility gate at GBP stage

### 1. Core Technical Requirements & Metrics
* BA may require geotechnical assessment of site adequacy at GBP stage (B(A)R 8(1)(ba)).
* **Required with GBP if (new building / A&A resulting in new building):**
  * (i) max gradient boundary-to-boundary (or any **50 m** strip on large site) > **15°**;
  * (ii) slope > **30°** and > **7.5 m** high (incl. RW at toe/crest) on site or within **7.5 m**;
  * (iii) excavation face > **10 m** long and either deeper than **7.5 m** at any stage, or below 45° plane from toe of any RW, or below **HKPD −1 m** on reclaimed coastal land;
  * (iv) retaining wall > **6 m** retained height on site, or ≥ **6 m** length of such wall within **6 m** of site;
  * (v) special geology (previous landslides, debris flows, threatening boulders, potential rockfalls).
* **A&A not resulting in new building:** if significant impact on existing geotech features/adjacent foundations, or excavation under 2(a)(iii).
* **Contents:** topography/geology/presumed GW; description how features/foundations affect/are affected; feasibility including methods/sequence; schematic site formation/foundation plans/sections; GI scope plan with Geoguide 2 s15.3 supervision level; intended stability investigations and preventive/remedial works.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact (feasibility assessment).

### 3. BD Submission & Certification Procedures
Submit geotechnical assessment with GBP when criteria met; absence may lead to rejection under BO **s16(1)(a)**.

### 4. Critical Red Flags & AP Liability
* Submitting GBP on sloping/excavation/RW criteria without assessment → plan refusal.
* Thin assessment missing sequence feasibility or GI supervision level → deficient for early constraint identification.

---

*End of Batch 01. APP-6: not present in source directory (skipped).*


<!-- Source: batch_02_APP026-050.md -->

# PNAP Batch Summaries: APP-26 to APP-50

Source directory: `PNAP_APPa_e`. Skip: **APP-36** (file not present). Revision status taken from each source markdown.

---

## PNAP APP-26: Pouring of Concrete against Walls of Adjoining Buildings
**Status/Context:** Mandatory structural / site safety rule; potential BO s.40 offence for negligence.

### 1. Core Technical Requirements & Metrics
* **Prohibited practice:** Using walls of adjoining buildings as permanent shuttering during concrete pouring is not acceptable unless a physical check confirms wall safety.
* **Physical check must confirm:** thickness; condition; structural capability to withstand loads from wet concrete and tamping.
* **If stability in doubt / unverifiable:** provide independent shuttering so no load is imposed on the adjoining wall; or take precautionary measures for adequate support and load minimisation.
* **Legal presumption:** Unless evidence clearly indicates otherwise, total or partial failure of such a wall is taken to indicate negligence in checks or precautions, and is considered an offence under Buildings Ordinance section 40.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
No specific plan-form submission prescribed. AP/RSE site control and design decisions must ensure adjoining-wall checks (or independent shuttering) before pouring.

### 4. Critical Red Flags & AP Liability
Assuming party/adjoining walls are adequate formwork without verified thickness/condition/capacity; any wall failure triggers BO s.40 negligence presumption. Prefer independent formwork wherever verification is incomplete.

---

## PNAP APP-27: Gas Water Heaters — Regulation 35A of Building (Planning) Regulations
**Status/Context:** Mandatory B(P)R 35A design provision (room-sealed gas water heater aperture); exemption path with DMC / sales undertakings.

### 1. Core Technical Requirements & Metrics
* **Statutory basis:** B(P)R 35A requires suitable provision for a room-sealed gas water heater in every bathroom.
* **Standard aperture size:**
  * Normally **320 mm wide × 420 mm high**; or
  * **240 mm × 240 mm** where bathroom size allows only a shower.
* **Non-standard apertures:** allowed only to suit a specific water heater flue installed before completion; and must be enlargeable later to standard size (clearly discernible provision) without cutting reinforcing bars or re-positioning services.
* **Location (key metrics):**
  * External-wall clear face (or vent into permanently open, well-ventilated balcony approaches);
  * Unobstructed internal clearance around aperture: **50 mm above**, **100 mm each side**, **150 mm below**;
  * Base ≥ **200 mm** above floor;
  * ≥ **300 mm** from any corner or other opening (window, vent, A/C opening, other aperture);
  * Facing clear space ≥ **1 500 mm** to facing wall / building part / site boundary (boundary abutting a street: aperture may abut that street);
  * Not directly below fixed clothes-drying racks; flue terminal guards if no overheating protector;
  * Hot-water pipe lengths per Waterworks Regulations Cap. 102A reg. 19.
* **Enclosed space / light well:** no obstruction to vertical airflow; vents below lowest aperture ≥ **0.05 m² per aperture**, each vent internal dim. ≥ **200 mm**; plan dimension vs height: **≥3 m** (≤10 storeys), **≥4 m** (11–19 storeys), **≥5 m** (≥20 storeys).
* **Re-entrant:** min plan width **≥1.5 m**; open-end obstruction (e.g. tie beam) ≤ **20%** of vertical open area; no obstruction to vertical airflow.
* **False-ceiling / confined cavity install:** quick-release access panel (no tools); non-adjustable louver ventilation not easily blocked; follow manufacturer requirements.
* **Sealing unused apertures:** easily removable materials (plain concrete, brick, block); must remain clearly discernible (e.g. recessing) from inside.
* **Reference:** EMSD CoP GU03 (domestic gas water heaters ≤70 kW).

### 2. GFA, Site Coverage, or Design Concession Impact
No GFA concession. Design impact on facade aperture, light-well / re-entrant geometry, and bathroom layout. Exemption may allow all-electric domestic buildings (no gas apertures) subject to para. 12 undertakings.

### 3. BD Submission & Certification Procedures
Show compliant apertures on GBPs; Appendix A location diagram. **Exemption application:** AP justifications (e.g. design constraint) plus developer/owner letter undertaking: (a) no Cap. 51 gas supply to domestic parts; (b) effective DMC measures (or S&P / Assignment / tenancy where no DMC) restricting gas supply and LPG cylinder delivery (excl. disposable cassette cooker cartridges with EMSD GU mark); (c) electric water heaters and electric/induction cookers installed in all domestic units before OP.

### 4. Critical Red Flags & AP Liability
Apertures too close to openings/corners; inadequate light-well vents or plan width; sealed apertures not discernible/removable; exemption without enforceable no-gas DMC / S&P controls or without electric appliances before OP.

---

## PNAP APP-28: Requirements for Qualified Supervision of Site Formation Works, Excavation Works, Foundation Works on Sloping Ground, and Ground Investigation Works in the Scheduled Areas — BO Section 17
**Status/Context:** Administrative / BO s.17 qualified supervision (geotechnical) categories imposed at approval or consent.

### 1. Core Technical Requirements & Metrics
* **Category (I):** periodic inspections by a qualified geotechnical engineer involved in preparing the geotechnical submission — for sites where stability/ground-movement results are sensitive to design assumptions; check assumptions on site (B(A)R 8(1)(bb), (bc) etc.) and judge design modifications. Critical assumptions often wrong: geological model (e.g. weathering vs sheet-pile penetration); groundwater regime (e.g. perched water table).
* **Category (II):** periodic inspections by a **senior** qualified geotechnical engineer responsible for the geotechnical submission — high-sensitivity sites (e.g. excavation adjoining old buildings with shallow foundations); personal senior-level attention required.
* **Category (III):** full-time supervision by suitably experienced person — day-to-day compliance with specifications/procedures (e.g. ground anchors, fill-slope compaction, complex ELS).
* **Combinations** of Categories (I)–(III) may form a package; nominee details must be submitted to BA for agreement.
* **Typical nominees:** Cat I — RPE(Geotechnical) or equivalent from the firm that prepared the submission; Cat II — RPE(Geotechnical) who is partner/director or equivalent of that firm; Cat III — suitably experienced/qualified graduate engineer/geologist or technical inspector/works supervisor.
* **RPE(Geotech) not always mandatory** for Cat I/II; case-by-case. Minor geotechnical risk / insignificant failure consequence: BA normally will **not** impose qualified geotechnical supervision.
* Lease/title may already impose geotechnical supervisory requirements — check via sectional CBS.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
BA imposes s.17 conditions at plan approval or consent. Submit individuals for BA agreement. Cross-ref: lease/title geotech supervision; geotechnical content under B(A)R 8.

### 4. Critical Red Flags & AP Liability
Nominating supervisors without design-firm involvement (Cat I/II); inadequately graded Cat III for anchors/ELS/compaction; failing to verify lease-imposed supervision; not checking sensitive assumptions (geology/groundwater) as works proceed.

---

## PNAP APP-29: Lift and Escalator Installations — Building Works Requirements
**Status/Context:** Mandatory building-works / structural-fire performance for lifts & escalators (B(C)R 9A; 2011 Lift Code + amendments); EMSD Cap. 618 interface.

### 1. Core Technical Requirements & Metrics
* **Primary standard:** Code of Practice for the Design and Construction of Buildings and Building Works for the Installation and Safe Use of Lifts and Escalators **2011** (Lift Code); other standards only if proven equivalent to BA.
* **Fixings:** AP/RSE must ensure adequate strength for guide-rail brackets, lift machine, deflector sheave brackets; machine/pulley rooms and liftwells to withstand normal loads/forces.
* **Key Lift Code amendments (App A – Aug 2015):** inspection traps dual/single lock rules; emergency doors dual key-operated locks from outside + openable from inside without key; prominent warning figure ≥ **100 mm** high beside keyholes (exceptions: landing doors; sills ≥ **1 m** above adjoining floor allow single designated key).
* **Key Lift Code amendments (App B – Sep 2019; plans on/after 1 Dec 2019):** well top ventilation min **1%** of horizontal cross-section, min net free **0.3 m²** per well (common wells 4/5/6 lifts: **0.4 / 0.5 / 0.6 m²**); ferrules ≥ **50 mm** above slab; full-height partitions between lifts through entire well; pit access door mandatory if pit depth > **2 m** (imperforate, not opening into well, lockable, bilingual notice durable ≥ **25 mm**); if pit > **1.6 m** but ≤ **2 m**, door if layout permits; permanent fall-arrest anchorages at lowest landing **1.5–1.8 m** AFFL (not required if compliant pit access door); stairs required where level difference > **0.6 m** (width ≥ **900 mm**; tread ≥ **225 mm**; riser ≤ **175 mm**; ≤ **16** steps/flight; both-side handrails; edge barriers ≥ **1.1 m**); metal supports/hooks in machine rooms **and** liftwell ceilings for hoisting; durable embossed notices.
* **Incomplete works lists (App C/D):** commonly incomplete permanent doors/notices, lighting, partitions, pit waterproofing, ventilation, isolation switches, escalator headroom ≥ **2.3 m**, unrestricted landing areas, obstruction guards, etc.

### 2. GFA, Site Coverage, or Design Concession Impact
No GFA concession in this PNAP. Design impacts liftwell ventilation, pit depth, machine-room stairs, partition walls, and lobby clearances.

### 3. BD Submission & Certification Procedures
Design per B(C)R 9A / Lift Code on structural/building plans. Complete **all** associated building works before DEMS application under Cap. 618 to put lifts/escalators into service. Electrical/mechanical/operational: EMSD CoPs under Cap. 618.

### 4. Critical Red Flags & AP Liability
Submitting DEMS put-into-service applications with incomplete building works (App C/D lists); undersized well vents; missing full-height partitions; pit >2 m without compliant stair access door; durable bilingual notices not provided; inadequate fixing details for rails/machines/sheaves.

---

## PNAP APP-30: Geotechnical Control on Developments in Mid-levels Scheduled Area
**Status/Context:** Mandatory geotechnical control for Scheduled Area No. 1 (Mid-levels) under BO Schedule 5 / B(C)R 25 / B(A)R.

### 1. Core Technical Requirements & Metrics
* **Scheduled Area No. 1:** Mid-levels; all geotechnical aspects need RGE input from early planning.
* **Ground investigation:** BO s.41(3) requires BA approval — submit GI plans incl. laboratory testing under B(A)R 8(1)(l) for approval **and** consent before start. Conform to Geoguide 2 & 3. BA typically requires s.17(1)(6)(e) adequate supervision by experienced engineer/engineering geologist; cores examined and logged. Cross-ref **PNAP APP-49**.
* **Demolition:** plans under B(A)R 8(3)–(4) must be submitted for approval.
* **Bulk excavation limit (BEL):** B(C)R s.25 — bulk excavation limited to minimise cumulative adverse hillside effects. Request GEO provisional BEL early (normally within **10 working days**). AP/RGE (RSE if needed) submit BEL assessment to BD for agreement **before** site formation / foundation / ELS / structural plans constrained by BEL. Follow GEO TGN 50; BEL so determined deemed to satisfy B(C)R s.25. BD agreement normally within **one month** = final BEL. Show excavation envelope and BEL on site formation plans (B(A)R 8(1)(bb)(vii)).
* **Foundation:** B(A)R 11A — foundation plan submitted **with** site formation plan; non-compliance may refuse under BO s.16(1)(a), (e) or (i).
* **Performance review:** may be imposed under BO s.2(1); if required and not satisfied, OP/TOP may be refused under s.21(6)(f).
* **Other controls:** landslip debris resistance, works sequence, groundwater drainage (BO s.16(1)(q), s.17(1)(6)(f), ss.28A–D).
* **Extra plan sets:** general building; site formation + reports/calcs; foundation incl. pile caps + reports/calcs; ELS plans.
* **Boundary plan:** BIC and BD website scheduled-areas page.

### 2. GFA, Site Coverage, or Design Concession Impact
No GFA/SC concession. BEL and Mid-levels geotech constraints strongly limit basement depth, bulk cut, foundation type and development envelope.

### 3. BD Submission & Certification Procedures
Appoint RGE; GI approval+consent before works; BEL agreement before constrained structural/geotech submissions; concurrent foundation + site formation; performance review when imposed; one extra set of key plans; use Mid-levels Study / GIU data (ADM-7).

### 4. Critical Red Flags & AP Liability
Commencing GI without approval/consent; submitting foundation/ELS before BEL agreement; foundation plans without concurrent site formation (B(A)R 11A refusal); OP without required performance review.

---

## PNAP APP-31: Permanent Water Supply to Fire Service Installations — BO section 21(6)(d)
**Status/Context:** Mandatory OP precondition — permanent FSI water connection when required by FSD CoP.

### 1. Core Technical Requirements & Metrics
* Where FSD CoP (Minimum Fire Service Installations and Equipment) requires permanent water supply to FSI, permanent connection must be made **before** occupation.
* **OP arrangements:**
  * (a) No FSI water required, **or** already permanently connected → F.S. certificate under BO s.21(6)(d) issued normally;
  * (b) FSI satisfactory to DFS but permanent water not yet connected → F.S. certificate issued with rider valid only when permanent supply connected;
  * (c) OP **will not** be issued until rider terms fulfilled.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
Coordinate Water Supplies / FSD connection timing with OP application; ensure F.S. certificate is unrestricted (or rider fulfilled) before OP.

### 4. Critical Red Flags & AP Liability
Applying for OP while F.S. certificate still carries an unmet permanent water-supply rider.

---

## PNAP APP-32: Hong Kong Airport (Control of Obstructions) Ordinance (Cap. 301) — Airport Height Restrictions
**Status/Context:** Mandatory aviation height control (Cap. 301 AHRs); temporary exemption workflow via DGCA.

### 1. Core Technical Requirements & Metrics
* Cap. 301 restricts building heights for aviation safety; AHRs vary by location per Airport Height Restriction Plans (Land Registry / LandsD Map Publication Centres; CAD website).
* **Temporary exemption:** from DGCA; normally ≤ **2 months**, extendable in further 2-month periods subject to conditions.
* **Construction plant:** where site subject to AHRs, AP/RSE must ensure RC obtains prior DGCA approval for any temporary plant/equipment that may project beyond prescribed heights (see PNRC 7).
* **Third runway / 3RS (Amendment Order 2021):** new AHRs operate from **31 May 2022** — more stringent near HKIA sea/mountainous surrounds; majority of HK less stringent. New AHRs **do not** apply to buildings erected per plans approved by BA **before 31 May 2022**, nor to minor works / designated exempted works completed before that date.

### 2. GFA, Site Coverage, or Design Concession Impact
No GFA concession. AHR caps absolute building and plant height (design envelope / construction method).

### 3. BD Submission & Certification Procedures
Check applicable AHR plan early; apply temporary DGCA exemptions for plant; ensure plans respect AHR unless grandfathered (pre-31 May 2022 approved plans).

### 4. Critical Red Flags & AP Liability
Cranes/plant exceeding AHR without DGCA temporary exemption; assuming old AHR envelope after 31 May 2022 for new approvals.

---

## PNAP APP-33: Pulverised Fuel Ash in Concrete
**Status/Context:** Permissive materials rule for PFA concrete under stated conditions; AP/RSE specification & QC duty.

### 1. Core Technical Requirements & Metrics
* PFA as partial cement replacement permitted if:
  * (a) Separate-constituent PFA only with OPC, complying with BS 3892: Part 1:1982 (max water requirement criterion may not apply);
  * (b) Blended cement with PFA complies with BS 6588:1985, nominal PFA ≤ **25%**; PFA not used **additionally** with blended cement;
  * (c) PFA content ≤ **35%** by mass of cementitious content (OPC+PFA). **25%** usual for normal works; >25% for special uses (marine, massive pours) needing expert advice and stringent site control;
  * (d) AP/RSE specify PFA content/extent in structural submissions; AP/RSE + RC ensure supplier QC; AP/RSE informed of deviations;
  * (e) If PFA > **25%**, AP/RSE must be satisfied no adverse effect from formwork striking, creep, long-term deflection, etc.
* Note: early strength may be lower than OPC mixes; effective curing essential, especially cold weather.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
State PFA content and extent on structural plans/specs; supplier QC and deviation reporting.

### 4. Critical Red Flags & AP Liability
PFA >35%; double-counting PFA with blended cement; >25% without addressing striking/creep/deflection; inadequate curing leading to underperformance.

---

## PNAP APP-34: Structural Design of Bridges and Associated Highway Structures
**Status/Context:** Split jurisdiction — BO-controlled if within/connected to private lot; HyD-controlled if wholly outside lot.

### 1. Core Technical Requirements & Metrics
* Design/construction per Highways Department **Structures Design Manual for Highways and Railways**; plans examined by **ACABAS** (BA arranges via centralised processing; see also APP-38 / formerly PNAP 107).
* **Wholly or partly within private lot / supported by private building:** processed under Buildings Ordinance — includes bridges between private buildings, or private building support at one end + government land at other. Must also satisfy B(C)R and BD CoPs/PNAPs.
* **Wholly outside private lot (free-standing on government land/public highways):** exempt from BO; Director of Highways is competent authority. HyD also requires: Transport Planning & Design Manual Vol. 2 geometry; GS for Civil Engineering Works 1992 materials/workmanship; GEOGUIDE 1 retaining walls; HyD Lighting Division / EMSD lighting; Geotechnical Manual for Slopes; landscape treatment (consult HyD Landscape Unit).
* **Submission route for outside-lot structures:** initially to BD — **3** sets plans, **2** sets calculations, **2** sets SI documents — for transmission to HyD; HyD certifies completion in writing.

### 2. GFA, Site Coverage, or Design Concession Impact
Bridge over streets may need BO s.31(1) exemption (APP-38); commercial uses on bridge generally GFA-accountable under OZP if allowed. Structure itself often outside lot GFA envelope depending on lease/control.

### 3. BD Submission & Certification Procedures
Within/partial lot: submit under BO (structural + ACABAS). Outside lot: submit via BD for HyD; HyD permits works, tests foundations, QC, corresponds with AP/RSE.

### 4. Critical Red Flags & AP Liability
Misclassifying support/connection so wrong authority; omitting ACABAS; private-lot bridges ignoring B(C)R despite HyD manual; incomplete plan/calc/SI sets for HyD transmission.

---

## PNAP APP-35: Refuse Storage and Collection — Building (Refuse Storage and Material Recovery Chambers and Refuse Chutes) Regulations
**Status/Context:** Mandatory refuse / material-recovery chambers & RCV access; GFA exclusion under B(P)R 23(3)(b); alternative RSR+RC modification path.

### 1. Core Technical Requirements & Metrics
* **RCV limiting specs (FEHD worst case):** length **11 m**; width mirror-to-mirror **3 m**; height **4 m**; bin-lift headroom **4.5 m**; ground clearance **0.24 m**; departure angle **10°**; turning circle wall-to-wall **20 m**; GVW **26 t**; max gradient **1:10**; access width preferably **4 m** (min **3.5 m**); parking space **5 m × 12 m**.
* If RCV cannot leave in continuous forward motion: hammer-head **27 m × 9.5 m**, approach **10.9 m** wide (or alternatives based on specs; App A).
* RS&MRC with RCV visits: G/F or podium with **direct** vehicular access from street (no intervening floors). Show access/exit routes on building plans.
* Submit calculations: usable floor space / aggregate, minimum chamber floor space, proposed chamber size (Schedule to reg. 3).
* **RS&MRR fire:** alarm + sprinkler; walls FRR ≥ **-/120/120**; door FRR ≥ **-/60/60**; self-closer must not hold door open (App B layouts/dims).
* **Ventilation:** central system may use single purifier before discharge; or fan + particulate filter per chamber if no particular odour. Main exhaust preferably upper roof away from neighbours (or at main RS&MRC if surrounded by taller buildings). Noise Control Ordinance Cap. 400 Technical Memorandum; fire dampers if ducts/grilles per floor. Air-purifying devices required in RS&MRC.
* **Alternative to per-floor RS&MRR (reg. 3A):** RSR each domestic floor + centralised recycling corner (RC), via modification, if App C met (TUFS ≥ **1 320 m²**). RSR min dimension **1 m**, floor area **1.5 m²**. RC size by TUFS/tower: Low **1 320–7 260 m²** → **10–14 m²**; Medium **7 260–13 200** → **14–16 m²**; High **>13 200** → **16–21 m²**. RC at main entrance/exit level; common parts / DMC undertaking; min dim **1.5 m**; manoeuvre **1.5×1.5 m**; mech vent ≥ **3 ACH** + purifying; lighting ≥ **120 lux**; same FRR as RS&MRR; water + sink; floor drain ≥ **100 mm** to back-inlet trapped gully outside. Shared RC: buildings <1 320 m² may share if combined TUFS ≥1 320, horizontal distance ≤ **75 m**, size per Table 1.

### 2. GFA, Site Coverage, or Design Concession Impact
Area of MRC, RS&MRC, RS&MRR, refuse chutes and hopper rooms (and, under alternative, RSR + RC) **may be excluded from GFA** under B(P)R **23(3)(b)** subject to satisfactory planning / App C compliance. RCV access geometry drives G/F and podium layout.

### 3. BD Submission & Certification Procedures
Show RCV routes; chamber sizing calcs; fire/vent details. Modification of reg. 3A for RSR+RC with App C compliance and DMC/common-parts undertaking where needed.

### 4. Critical Red Flags & AP Liability
Undersized RCV manoeuvring / indirect multi-floor access; missing FRR/self-closer; claiming GFA exclusion without compliant chamber design; RC too small for TUFS band or not in common parts; shared RC beyond 75 m.

---

## PNAP APP-37: Curtain Wall, Window and Window Wall
**Status/Context:** Mandatory structural submission / fire-compartment detailing / tempered-glass QC under BO s.17; concurrent approval-consent available (ADM-19).

### 1. Core Technical Requirements & Metrics
* **Curtain wall:** performance B(C)R ss.29–31; wind loads; horizontal imposed loads (s.9 / Schedule Table 3) if no protective barrier; corrosion; materials; fire/smoke spread compliance with B(C)R s.35 and FS Code 2011 (between floors, compartments, accommodation vs staircase/lobby).
* **Curtain-wall plan contents (para. 2):** framing/key details/install sequence; calcs (parent structure check, stability, Al, fixings, glazing, deflection); workmanship (weld/galvanise/bi-metallic/corrosion); elevations/pane layout; typical/non-typical sections & connections; support tolerance & remedial; support mode (cast-in / welded) or modification of B(C)R s.31 for drilled/bolted; codes; material specs; fire sections.
* **Window / window wall structural submission triggers:** forms external wall + least structural opening dim. > **1.8 m** or area > **6 m²**, and ≥ **100 m** above adjoining ground **or** Q₀,z ≥ **2.86 kPa** (or design wind pressure q_z if Wind 2004 CoP used); also if design span of structural elements (mullion, glass fins, etc.) > **6 m**.
* **Deflection:** Glass Code 2018 limits.
* **Minor works:** Schedule 1 B(MW)R / APP-147 for certain repair/replacement/alteration.
* **Separate RSE:** Forms BA4/BA5; Form completion cert under B(A)R 25(3); assessment report + project RSE statement on parent-structure effects; separate RSE supervises incl. cast-in anchors unless pre-installed by project RSE.
* **Tempered glass:** ISO 9001 factory; QAS ≥14 days before production (RSE declaration; Glass Code 9.1.3); heat soak to BS EN 14179-1:2016; compliance reports before OP/BA14; quality supervision plan ≥14 days before production; QCS (≈T3) ≥ **30%** panes (videotelephony option: ≥480p, non-rewritable DVD); QCC (≈T1) full-time with independent 1-minute data logger; quality supervision report before OP.
* **Structural sealant:** compatibility/adhesion/print-review + deglazing certificates before OP/BA14.
* **Spider fixings:** proof load test (App C: sample ≥ **1% or 3 nos.**; residual deformation ≤ **5%**); may waive if in Central Data Bank (ADM-20). Show proprietary model on plans.
* **Locking devices (plans on/after 1 Aug 2020):** durable non-combustible; ultimate design strength = characteristic / FOS **1.8**; proof test sample ≥ **0.1% or 5 nos.** (App D); ≤ **8** locking points per handle bar; top-hung sash ≤ **2.5 m²**; side-hung width ≤ **700 mm**.
* **Safety test:** HOKLAS-accredited lab; RSE statement; before OP/BA14 (waived for ADM-19 fast-track repair/replacement or MW item 1.61).

### 2. GFA, Site Coverage, or Design Concession Impact
No GFA concession in this PNAP. Facade systems affect prescribed windows, protective barriers, and fire separation at floors/stair lobbies. Cross-design with Glass Code / APP-53 / APP-116 (aluminium windows).

### 3. BD Submission & Certification Procedures
Structural plans + calcs; compatibility with approved GBPs; concurrent approval & consent for curtain wall under ADM-19. Separate RSE paperwork; tempered-glass QAS/supervision plan/reports; sealant certificates; spider/locking proof tests or Data Bank refs; HOKLAS safety tests; spare-glass Schedules A/B (App E) for future repair. Form BA14 / OP milestones.

### 4. Critical Red Flags & AP Liability
Missing fire compartment sections across CW floors; window walls above triggers without structural submission; drilled/bolted fixings without s.31 modification; heat-soak supervision <30% or no QCC logger; FOS/locking layout non-compliant; OP without endorsed test packs; spare glass used without documented Schedule A/B trail.

---

## PNAP APP-38: Bridges over Streets and Lanes — Buildings Ordinance section 31(1)
**Status/Context:** Discretionary BO s.31(1) exemption to permit bridges projecting over streets/lanes; ACABAS aesthetic gatekeeping.

### 1. Core Technical Requirements & Metrics
* Exemption may be given where bridge wholly/partly within private lot or supported/connected to private building, **if**:
  * (a) required under lease / planning permission / consistent with OZP/ODP/Layout Plan; **or** functionally necessary for efficient inter-building pedestrian movement (relieve street-level congestion) and acceptable to LandsD/PlanD/TD/HyD; **or** identified public benefit (pedestrian–vehicle segregation / access to public transport or public footbridge network) acceptable to those departments; **or** other justified special circumstances;
  * (b) pedestrian or vehicular links only — commercial activities generally **not** allowed unless planning permission + justified public benefit, and then **accountable for GFA under OZP**;
  * (c) width and storeys fully justified by pedestrian flow; visual & air ventilation impact studies may be required for bridges > **1 storey** and/or clear width > **6 m**;
  * (d) ACABAS finds aesthetic design acceptable for structures over/under/on/next to public roads.
* **ACABAS submission:** **10** sets A3 stapled + CD/DVD PDF/JPG soft copy direct to ACABAS secretary (ETWB TC(W) 36/2004 materials): general arrangement; elevations + perspective/axonometric with form/texture/colour; comprehensive site photos; for footbridges — anticipated pedestrian flows on plans.
* Free-standing wholly outside private lot: **BO-exempt**; submit to HyD. Resolve maintenance responsibilities with HyD before construction. Read with APP-34 and ETWB TC(W) 10/2005 (planting).

### 2. GFA, Site Coverage, or Design Concession Impact
Link bridges for circulation only typically outside commercial GFA; if commercial activities permitted — GFA-accountable under OZP. Width/storey/air-ventilation affect street canyon and building separation design.

### 3. BD Submission & Certification Procedures
BO s.31(1) exemption application with purpose justification; parallel ACABAS package; departmental acceptability; HyD route if wholly outside lot.

### 4. Critical Red Flags & AP Liability
Commercial bridge uses without planning permission/GFA accounting; bridges >1 storey or >6 m wide without AVA/visual studies; ACABAS rejection blocking exemption; unresolved maintenance.

---

## PNAP APP-39: Inspection and Copying of Plans and Documents
**Status/Context:** Administrative public-records access workflow (BO s.36G); copyright / privacy constraints.

### 1. Core Technical Requirements & Metrics
* Submitted plans/documents are public records; BA may permit inspection/copies under BO s.36G on request and prescribed fee, subject to Personal Data (Privacy) Ordinance, Copyright Ordinance, Code on Access to Information, and confidence.
* **Confidence rule:** no inspection/copies of projects until building/works completed. Available records: latest approved plans/calcs/related docs of completed projects; latest Class I/II MW plans & Class III MW plans/descriptions, photos & related docs of completed MW under simplified requirements.
* **Permitted purposes (applicant declaration):** construction matters; compliance with BO/enactments; or other BA-appropriate public-interest purposes (para. 4(c) needs special justification or copyright-owner authorisation with positive ownership statement).
* **Channels:** BIC in person (Form BIC1 inspect — electronic pledge within **3** working days; BIC2 copies after inspect; BIC-3 one-stop copies within **10** days inform result/fees; BIC4 OP copies); BRAVO online (register Form BIC5 / website — login by registered mail). Fees under B(A)R 42. Free delivery to most HK addresses (excl. P.O. box, Closed Area, Lantau, Outlying Islands).
* **AP/RSE/RGE change:** copyright of plans is on new professional to obtain; BD release does not waive copyright infringement risk.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
Use BIC/BRAVO forms/EFSS; declare purpose; pay fees. New AP/RSE/RGE must secure copyright consent before reusing resigned professional’s plans.

### 4. Critical Red Flags & AP Liability
Seeking incomplete-project records; using plans after AP change without copyright consent; inaccurate lot/address on OP (BIC4) requests.

---

## PNAP APP-40: Hotel Development
**Status/Context:** Discretionary hotel concession under B(P)R 23A (non-domestic treatment + disregard of certain supporting facilities / pick-up-set-down); APP-151 GFA-concession interface.

### 1. Core Technical Requirements & Metrics
* BA considers for B(P)R 23A(2)/(3) treatment:
  * (a) site suitability (OZP Column 1 or s.16 permission; intensity compatible with surroundings; adequate streets; TD parking/loading);
  * (b) basic hotel facilities (reception, linen stores, admin office, staff toilets) + ancillary dining/entertainment/shopping commensurate with patronage;
  * (c) whole hotel / hotel portion has **central A/C** and **centralised hot water**;
  * (d) evidence will operate as Cap. 349 licensed hotel (operator appointment confirmation may suffice).
* Hotels ≥ **100** guest rooms: HKPSG parking & loading normally expected (TD assessment still applies).
* **Unique supporting facilities disregarded under 23A(3)(b):** size reasonable, staff-only access, abuse unlikely; GFA of such facilities expected ≤ **5%** of total hotel GFA unless strong justification. Admin/management offices **not** unique supporting facilities under 23A(3)(b)(iv).
* **App A classification:**
  * BOH unique (may disregard under 23A): linen store*, laundry, carpentry/M&E workshops, dry goods*, food/beverage/furniture stores, staff canteen/changing/rest, staff toilet*† (*required all hotels; dry goods* & admin office* for >10 rooms; †staff toilet not part of admin office may be disregarded).
  * Other BOH (GFA accountable): admin & management office, purchasing/receiving, security.
  * FOH (GFA accountable): reception/lobby*, shopping, dining, business centre, function rooms.
  * Minimum total required BOH & FOH provision: **3%** of total hotel GFA.
* Footnote 1: plant rooms for central A/C and centralised hot water of reasonable size may be disregarded under B(P)R **23(3)(b)** subject to **APP-151** pre-requisites and overall **10%** GFA concession cap.
* Applies to bona fide hotels **only** — not “service apartments”. Applies to new hotels, extensions; A&A adding GFA/bulk reassessed under current 23A. Change-of-use to hotel assessed on same criteria. Sanctions for unauthorised change of use: B(P)R 23A(8)–(9).

### 2. GFA, Site Coverage, or Design Concession Impact
Key GFA/SC tool: treat hotel as non-domestic for SC/PR; disregard unique BOH facilities (≤~5% expected) and pick-up/set-down; plant rooms via 23(3)(b)+APP-151. Reception/shopping/dining/admin generally GFA-accountable. Minimum 3% BOH+FOH provision.

### 3. BD Submission & Certification Procedures
Justify suitability, facilities, central A/C & hot water, Cap. 349 evidence. Schedule BOH/FOH areas vs App A. Coordinate TD on traffic/parking. APP-151 compliance package for plant-room and other GFA concessions.

### 4. Critical Red Flags & AP Liability
Claiming 23A for service apartments; admin office counted as disregarded unique BOH; BOH disregard >>5% without justification; missing central A/C/hot water; no licence-operation evidence; later hotel→residential change triggering 23A(8)/(9) sanctions.

---

## PNAP APP-41: Buildings to be Planned for Use by Persons with a Disability — B(P)R Regulation 72 / Design Manual: Barrier Free Access 2008
**Status/Context:** Mandatory barrier-free access (DDO Cap. 487 s.84; B(P)R 72 + Third Schedule); Design Manual 2008 obligatory + recommended practices; exemption via ACBFA.

### 1. Core Technical Requirements & Metrics
* BA must not approve plans (new or A&A) unless reasonable access for persons with a disability is provided (DDO s.84). Incorporate barrier-free access at design stage.
* Governing provisions: B(A)R 8(1)(m); B(P)R 2(1), 39(3)(e), 72 & Third Schedule; Building (Standards of Sanitary Fitments…) Reg. 61(3).
* Part 4 of Third Schedule: categories with **limited** barrier-free access. Except buildings exempted under B(P)R 72(4), all buildings **not** in Part 4 must comply **fully**.
* Design Manual: Barrier Free Access **2008** (editions through **2025**) incorporates statutory + best practice; amendments Apps C–I (2012–2024) + App J elderly-friendly Chapter 6 recommended design (Task Force ageing-in-place; staged admin then B(P)R amendment).
* **Special circumstances for variation (App A — existing buildings A&A without initial access):** ramp works to common parts where applicant has no control; co-owners/OC consent declined/unavailable; and (if ground beam) spatial/structural constraint.

### 2. GFA, Site Coverage, or Design Concession Impact
No automatic GFA concession in this PNAP. Barrier-free ramps, lifts, sanitary fitments, and elderly-friendly features affect planning efficiency; accessible-lift extensions may seek amenity concessions under **APP-42** paras. 44–45 where criteria met.

### 3. BD Submission & Certification Procedures
Clearly show barrier-free access on plans (B(A)R 8(1)(m)). Exemption/modification applications considered on merits; BA may refer to **ACBFA**. Follow current Design Manual 2008 (2025 Edition) on BD website. Encourage clients to adopt App J elderly-friendly recommended features.

### 4. Critical Red Flags & AP Liability
GBPs without clear BFA provisions; treating Part-4-limited buildings as fully exempt incorrectly; A&A to inaccessible buildings without exploring practical BFA measures; claiming hardship without App A evidence (no control / OC refusal / structural constraint).

---

## PNAP APP-42: Amenity Features
**Status/Context:** Discretionary modification/exemption to encourage amenities; **majority of GFA/SC concessions subject to APP-151** pre-requisites and/or overall GFA concession cap / BEAM Plus interface.

### 1. Core Technical Requirements & Metrics
Objectives: better management; quality of life; reduce UBW temptation; neighbourhood compatibility. Case-by-case; large schemes — pre-discuss BD (± LandsD/PlanD).
* **A/C:** residential wall boxes/platforms permanent features may exclude from SC (APP-19); commercial/industrial — central A/C or set-aside internal areas (no street projection). Floor space for A/C disregarded from GFA under B(P)R 23(3)(b) subject to **APP-151**. Reasonable defaults: A/C plant rooms ≤ **1%** total GFA; AHUs ≤ **4%** GFA of each floor. In-unit plant rooms: access preferably outside unit/common area; if inside unit: floor level difference ≥ **500 mm**; ≥1 open side facing open air (railings/grille/louvre OK to parapet; further enclosure for intake/exhaust or FS Code C11.1); justify size.
* **Security gates:** not obstruct MOE; locks openable from inside without key; may install before OP/BA14 or show positions (unit entrances; main staircase exits; domestic/non-domestic separation).
* **Watchmen / management counters etc. GFA exemption:** not excessive; common parts/DMC undertaking; domestic max **0.2%** domestic GFA or **5 m² per 50 flats** (smaller); non-domestic max **0.2%** non-domestic GFA or **120 m²** (smaller) — subject **APP-151**.
* **OC office / caretakers’ quarters:** favourable GFA exemption (lease size / justification) — subject **APP-151**.
* **Clothes racks / anti-burglar bars / small window hoods:** no SC/PR implication for individual domestic units.
* **Horizontal screens / covered walkways:** open-sided communal G/F or podium; connect lot boundary main access ↔ building main entrance and/or building-to-building; no prescribed-window obstruction; common parts (not commercial); max width **3.5 m**, height **4.5 m** (EVA span may relax); other depts OK — GFA/SC exemption subject **APP-151** pre-reqs.
* **Trellis:** private roof/garden ≤ **5%** of roof/garden or **20 m²** (less); common parts: ≤ **5%** roof / ≤ **10%** garden, each trellis ≤ **20 m²**; open-sided ≤ storey height; bars ≥ **200 mm** apart; no prescribed-window obstruction; **no trellis on refuge roof** — subject **APP-151** pre-reqs.
* **Shelters for outdoor fixed seats:** ≤ **10%** of communal outdoor space, each ≤ **20 m²**; open-sided ≤ **3.5 m** W/H; horizontal clearance ≥ **3.5 m**; common parts; not on refuge roof — **APP-151** pre-reqs.
* **Prestige entrances:** APP-2; protect MOE/fireman’s-lift lobbies — **APP-151** cap/pre-reqs.
* **Communal podium garden / covered landscaped & play under domestic tower:** modify B(P)R 23(3)(a) if open, not encumbered by structure; exempted total ≤ **5%** domestic GFA — **APP-151** pre-reqs.
* **Covered areas at public open space** (lease/planning): resting facilities shown; not commercial; common parts (exceptions for gov-managed POS); LandsD/PlanD no objection — **APP-151** pre-reqs.
* **Recreational facilities** (squash, gym, indoor pool, sauna, function rooms): case-by-case modify 23(3)(a) subject **APP-104** limits and **APP-151**.
* **SMATV:** cabinet ≤ **0.6×0.6×2.2 m** not BO-controlled if no building works; common-parts room ≤ **1.2×1.2 m** GFA-exempt per APP-2.
* **Radio base stations:** cabinet ≤ **1.5×1.0×2.3 m** plant (not BO); larger / rooms — GFA accountable; may need OP as new building; MW Class I for supporting structure.
* **Covered pick-up/set-down:** not excessive; open-sided; common parts; LandsD/PlanD/TD/HyD OK — **APP-151** pre-reqs.
* **Accessible-lift extensions** (existing buildings, not ≤3-storey houses): not excessive; DM:BFA design; common parts; undertaking not to remove existing lifts without BA — GFA/SC exempt.
* **Outdoor prefabricated structures:** ≤ **3 m³** and ≤ **2 m** height not a building (excl. radio base station rule above); larger = building needing approval/consent/OP.
* Para. 46: amenity features in paras 20, 24, 30, 42 (elderly-friendly) apply to residential/composite and elderly-patronaged commercial; cannot retrofit GFA exemption to transfer already-accounted existing features.

### 2. GFA, Site Coverage, or Design Concession Impact
Primary amenity GFA/SC concession PNAP. Almost all concessions tied to **APP-151** (pre-requisites, often BEAM Plus / overall concession cap). Key hard caps: 1%/4% A/C; 0.2% management; 5% podium garden; walkway 3.5×4.5 m; trellis/shelter size limits.

### 3. BD Submission & Certification Procedures
Modification/exemption applications with justifications, DMC/common-parts undertakings, departmental clearances. Show unusual A/C systems detail and operational before OP/BA14. APP-151 package mandatory for listed concessions. Pre-consultation for large/innovative schemes.

### 4. Critical Red Flags & AP Liability
Claiming concessions without APP-151 pre-reqs/cap; in-unit A/C plant without level difference/open side; management rooms in private demise; covered walkways forming commercial premises; trellis/shelter on refuge roof; converting already-accounted amenities into transferable GFA.

---

## PNAP APP-43: Licensing of Child Care Centres, Kindergartens and Restaurants
**Status/Context:** Licensing interface — BD comments on structural safety and MOE; CCC/KG location rules; restaurant certification & discharge-value checks.

### 1. Core Technical Requirements & Metrics
* **CCC / kindergarten above G/F** in non-purpose-built buildings only if location/condition matrix met, including:
  * Conform to MOE CoP;
  * CCC: **12 m / 24 m** max height under Child Care Centre Reg. 19;
  * KG: **24 m** max height under Education Reg. 7;
  * Certain wholly commercial / multi-commercial-floor / single-staircase cases need **two exclusive MOE** or **two extra staircases** with single staircase sealed off;
  * Single-family domestic ≤3 storeys & NT exempted buildings: unconditional.
* Non-compliant “change in use” under BO s.25 will be prohibited. **Not** in industrial buildings (incompatible for fire-fighting and planning).
* **Restaurants — certification:** AP/RSE may certify directly to licensing authority on BD-imposed building safety items; BD audits; negligence/misconduct attract action.
* **UBW:** licensing authorities advised to reject while UBW remain; non-exempted works need prior BA approval/consent (former PNAP 125 / APP-47).
* **Discharge value:** when shops/offices change to restaurants, count **existing restaurants’** utilisation of staircase discharge capacity — surplus may already be used.
* **Structural assessment:** check floors for self-weight, finishes, partitions, plant, minimum imposed loads per B(C)R; submit particulars (App A): raised screeds (core test if not AP/RSE-supervised), brickwalls, fish tanks, large kitchen equipment/walk-in freezers, large central A/C units — sizes, densities, catalogues.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact from this PNAP per se; use change affects MOE capacity and floor loading, potentially constraining tenancy layouts.

### 3. BD Submission & Certification Procedures
Advise clients against prohibited upper-floor CCC/KG locations. For restaurants: structural justification packs; discharge-value analysis including all existing restaurants; direct certification to licensing authority as required; no UBW.

### 4. Critical Red Flags & AP Liability
Licensing CCC/KG above height limits or in industrial buildings; restaurant certification without verifying total building discharge capacity including existing restaurants; load checks omitting fish tanks/screeds/plant; certifying while UBW present.

---

## PNAP APP-44: Streets in relation to Site Area — Building (Planning) Regulation 23(2)(a)
**Status/Context:** Discretionary plot-ratio flexibility where new streets fragment large sites and external planning controls secure open space.

### 1. Core Technical Requirements & Metrics
* New streets may divide land into separate sites under B(P)R 23(2)(a), inhibiting consolidated planning / causing “lost” PR if a large park occupies one island site.
* BO has no explicit PR-transfer mechanism; uncontrolled transfer risk of later park redevelopment overloading neighbourhood/infrastructure.
* Where enforceable lease controls, Master Layout Plans, and/or Town Planning Ordinance s.16 conditions exist, BA may — on Form 29 special circumstances — allow higher PR on another site within the large project (and consequential regulation adjustments) if overall planning improves and specific planning requirements are not significantly impaired.
* If higher PR granted, subsequent change to control drawings/MLP/TP permission that would negate benefits of Form 30 permission will be opposed.

### 2. GFA, Site Coverage, or Design Concession Impact
Potential cross-site PR redistribution within multi-lot large developments, contingent on binding planning/lease/MLP controls. Not a general GFA concession.

### 3. BD Submission & Certification Procedures
Form 29 application citing special circumstances and supporting lease/MLP/s.16 controls; Form 30 permission where granted.

### 4. Critical Red Flags & AP Liability
Seeking PR transfer without enforceable external planning controls; later amending MLP/s.16 to develop the “park” site and negate the concession.

---

## PNAP APP-45: Testing of Reinforcement for Concrete
**Status/Context:** Mandatory verification testing / qualified supervision under BO s.17(1)6; CS2:2012 purchaser’s tests.

### 1. Core Technical Requirements & Metrics
* BA may impose rebar testing at structural approval or consent — verify properties of steel delivered to site/prefabrication factory (additional to mill testing). Random specimens from every batch. Acceptable standard: **CS2:2012**.
* CS2 covers straight bars, coil, decoiled (except cold worked); grades **250** (≤12 mm), **500B**, **500C** — mass/m, chemistry, mechanical, bond; QA Stockists / QA Coil Processors; purchaser’s testing.
* Purchaser’s tests by **HOKLAS**-accredited laboratory. Report must include: Class 1/2 QA Stockist classification; manufacturer/country/grade/size description; deformation pattern & mill marks; batch & delivery date to site/factory; measured mass/m; chemistry (product), tensile, bend, bond if required.
* Coils/decoiled: Amendment No. 2/2018 & Technical Note No. 5; all coil processors to be QA Coil Processors; Approved Yards under DEVB TC(W) 10/2018 recognised.
* Prefabricated rebar from Approved Yards (approved scope) considered conforming to Concrete CoP 2013 (2020 Ed.) if qualified supervision under BO satisfied.
* Approval of RC plans typically imposes s.17(1)6 qualified supervision by RSE + RGBC/RSC for sampling/testing.
* **Streamlined Approved Yard path:** IAT-witnessed QMS batch sampling accepted; RSE/contractor check sampling, witness, HOKLAS reports kept by yard; keep copies on site after delivery; submit list of products + RSE compliance statement to BD within **21 days** of delivery. Alternative: own QCS/QCC arrangements for sampling & testing per CS2.

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
Comply with imposed s.17 testing; HOKLAS reports; for Approved Yard products — on-site records + RSE statement within 21 days of delivery.

### 4. Critical Red Flags & AP Liability
Non-random / incomplete batch sampling; using non-HOKLAS labs; missing 21-day delivery confirmation for prefab rebar; assuming mill certificates alone satisfy purchaser’s tests.

---

## PNAP APP-46: Pollution from Industrial Buildings — Building (Standards of Sanitary Fitments, Plumbing, Drainage Works and Latrines) Regulation 90
**Status/Context:** Mandatory drainage/effluent-treatment provision for industrial buildings; BO ss.24 & 28 / Reg. 90 enforcement tools.

### 1. Core Technical Requirements & Metrics
* BA may invoke BO ss.24 & 28 and Reg. 90 against water pollution from industrial effluent (damage to drains/sewers, overload, worker injury risk).
* For single-occupancy specialised industrial buildings with known processes: consult EPD; allow specific treatment facilities.
* Flatted factories: assume effluent may need facilities beyond Reg. 5(1); failure to provide for future discharge may lead to disapproval under Reg. 90. Clear building-use statements and adequate noxious-effluent treatment at drainage plan stage — failure may reject under BO s.16(1)(i).
* **Unless specific facilities provided, each industrial unit:** individual adequately trapped drainage outlet for treated trade effluent to **foul** system (not storm): usable floor area **<1 000 m²** → **100 mm** dia. outlet; **>1 000 m²** → **≥150 mm** dia. Vertical foul downpipes generally **150–300 mm** dia. depending on floors served. Outlets may be temporarily sealed at floor until needed; assume Reg. 90 effluent treated by occupant before discharge.
* Petrol interceptors where vehicle servicing/parking; other industrial treatments may need specialist advice. Standard petrol-interceptor details attached to note.

### 2. GFA, Site Coverage, or Design Concession Impact
No GFA concession. Drainage risers, treatment plant and interceptors affect basement/services/floor layouts.

### 3. BD Submission & Certification Procedures
State industrial processes/uses on drainage submissions; provide unit outlets sized as above; consult EPD for specialised processes; include petrol interceptors where relevant.

### 4. Critical Red Flags & AP Liability
Connecting trade outlets to storm; missing per-unit foul outlets in flatted factories; vague industrial use on drainage plans → s.16(1)(i) refusal; undersized outlets vs unit UFA.

---

## PNAP APP-47: Unauthorized Alterations and Additions — Buildings Ordinance Section 14
**Status/Context:** Administrative / enforcement — no retrospective approval; exceptions for MW simplified requirements, s.41 exempted works, and Household Minor Works Validation Scheme.

### 1. Core Technical Requirements & Metrics
* BA has **no power** to give retrospective approval or consent for UBW. Except MW under simplified requirements and works exempted under BO s.41, no person shall commence/carry out building works without prior BA approval and consent (s.14(1)). s.42(5): exemption powers **not** applicable to s.14.
* **Household Minor Works Validation Scheme (s.39C; from 31 Dec 2010):** prescribed works in Schedule 3 of B(MW)R completed before that date may be inspected/certified (and sometimes altered/rectified/reinforced) and retained; BA shall not serve s.24 removal order or s.24C warning solely for pre-date s.14 contravention. Legal status remains **unauthorised**; BA may still act if condition becomes dangerous.
* Completed works plan submissions (other than MW simplified): rejected under s.16(1)(a) (not a prior proposal); s.16(1)(c) (Form BA5/BA17 for works “to be carried out” / “to erect”); and if subject of effective demolition order, s.16(1)(d).

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact. UBW cannot be regularised into accountable/concession GFA via retrospective plan approval.

### 3. BD Submission & Certification Procedures
Advise clients: prior approval & consent required; MW via simplified requirements where applicable; do not submit “as-built” UBW plans expecting approval. Validation Scheme procedure under B(MW)R s.62 for eligible pre-2010 household minor works.

### 4. Critical Red Flags & AP Liability
Submitting plans for completed illegal works seeking retrospective approval; client commencing works without consent → BA demolition order and Part IV prosecution (fine/imprisonment); assuming Validation Scheme changes legal status to authorised.

---

## PNAP APP-48: Requirements for Qualified Supervision of Structural Works, Foundation Works and Excavation Works — BO Section 17
**Status/Context:** Administrative BO s.17 qualified supervision for structural/foundation/excavation operations (complement to APP-28 geotech).

### 1. Core Technical Requirements & Metrics
* BA may impose qualified supervision conditions at plan approval or consent for stages/operations such as:
  * major excavation and foundation construction;
  * concreting;
  * compliance testing;
  * prestressing (pre-/post-tensioning, grouting, lock-off);
  * fabrication, erection and examination of key structural steel elements on site;
  * specialist building works.
* Supervisors must have adequate technical knowledge/experience and be fully conversant with the engineering design basis.
* AP, RSE, RGE and RC must ensure qualified supervision under BO ss.4(3) & 9(3) and B(A)R 37 & 41.
* Geotechnical qualified-supervision detail covered by APP-28 (formerly PNAP 83).

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact.

### 3. BD Submission & Certification Procedures
Anticipate/comply with s.17 supervision conditions; assign suitably qualified personnel; coordinate with geotech supervision under APP-28 where overlapping.

### 4. Critical Red Flags & AP Liability
Assigning supervisors unfamiliar with design basis; missing supervision at prestressing, key steel erection, major foundation/excavation, or compliance testing hold points.

---

## PNAP APP-49: Site Investigation and Ground Investigation
**Status/Context:** Mandatory standards / RSC(GIFW) / digital GI-LT reporting for site and ground investigation supporting BO submissions.

### 1. Core Technical Requirements & Metrics
* **Site investigation** (B(C)R s.2): physical characteristics including documentary studies, surveys and GI. **GI:** boreholes, test pits, on-site and laboratory tests.
* Follow GEO TGN No.1 list (Geoguide 2 & 3 etc.) and **Code of Practice for Foundations 2017 (2024 Edition)**.
* **GIFW** (all site GI operations excluding laboratory testing and field density tests): specialised works category; must be by **RSC(GIFW)** (registration/scope in APP-96). Laboratory tests and field density tests by labs accredited for the tests (APP-64).
* RSC(GIFW) responsible for GI reports supporting foundation / site formation / ELS plans (B(A)R 8(1) & 9) and geotechnical assessments with GBP under B(A)R 8(1)(ba) (include plan of GI scope/extent). RSC must ensure correctness even if geophysical surveys by others; keep cores/samples (except those tested) until acknowledgement of related site formation/foundation/works.
* Quality supervision: Technical Memorandum for Supervision Plans 2009 and Code of Practice for Site Supervision 2009 (**2024 Edition**).
* **Digital GI & LT reports required:** PDF + AGS Data Format (ASCII, not split), with GEO local additions; individual GI station PDFs with photos (unique filenames e.g. SSB-BH1).

### 2. GFA, Site Coverage, or Design Concession Impact
No spatial or GFA impact. Adequate GI underpins BEL/foundation choices that affect buildable bulk (esp. Mid-levels APP-30).

### 3. BD Submission & Certification Procedures
Engage RSC(GIFW); submit digital PDF+AGS GI/LT packs; use GI for foundation/site formation/ELS and geotechnical assessments; retain cores for BD/GEO inspection until related works acknowledged.

### 4. Critical Red Flags & AP Liability
Non-RSC(GIFW) carrying out GIFW; paper-only GI submissions without AGS; incorrect lab accreditation; discarding cores before related works acknowledged; geotech assessment without GI scope plan.

---

## PNAP APP-50: Temporary Buildings — Building (Planning) Regulations 50–52
**Status/Context:** Administrative procedural overlay for temporary buildings under B(P)R 50–52; all BO provisions still apply.

### 1. Core Technical Requirements & Metrics
* Temporary buildings = temporary purpose and/or short-lived materials (B(P)R 50(1)(a)(i)/(ii)). **All** BO and subsidiary legislation apply: approval/consent, AP/RSE supervision, registered contractor, completion certification, temporary occupation permit.
* **Procedural precedence:**
  * Submit plans with **Form BA17** (replaces BA5 for approval + BA8 for consent package); **Form BA5** for AP/RSE certificate of preparation; **Form BA4** for appointment notice.
  * On approval, **Form BD107** issued if consent also granted — replaces S.L.9 approval letter and Form BD103; states permitted duration.
* Commencement under BO s.20: works must start within **3 months** of BD107 else renew consent on Form BA9. Building may remain until BD107 expires.
* BA17 processing time limit: **60 days** first submission / **30 days** resubmission (approval + consent clocks concurrent).
* Occupation: temporary OP **Form BD105** via Form BA12. BD107 conditions (max persons, removal on expiry/cancellation, expiry date) become TOP conditions.
* On expiry/cancellation: remove forthwith or face BO s.24(1) order; occupying after TOP expiry/revocation may attract BO s.40(1) prosecution.
* Extension: apply in writing with original BD107 + BD105 and AP/RSE certificate that building can last extended term (max **5 years**) in safe (and sanitary if applicable) condition for stated purposes.

### 2. GFA, Site Coverage, or Design Concession Impact
No lasting GFA/SC concession. Temporary buildings still subject to planning/lease controls for the authorised duration.

### 3. BD Submission & Certification Procedures
Use BA17/BA4/BA5/BD107 pathway; commence within 3 months; obtain TOP (BD105) before occupation; extend only with AP/RSE durability certificate (≤5 years) plus original permits.

### 4. Critical Red Flags & AP Liability
Using BA5/BA8 instead of BA17; failing to commence within 3 months; occupying without TOP; allowing occupation after BD105 expiry; extension without AP/RSE safe-duration certificate.

---

## Completion confirmation

| APP No. | Title (short) | Status |
|---------|---------------|--------|
| APP-26 | Pouring concrete against adjoining walls | Completed |
| APP-27 | Gas water heaters (B(P)R 35A) | Completed |
| APP-28 | Qualified geotech supervision (BO s.17) | Completed |
| APP-29 | Lift & escalator building works | Completed |
| APP-30 | Mid-levels Scheduled Area geotech control | Completed |
| APP-31 | Permanent FSI water supply (OP) | Completed |
| APP-32 | Airport height restrictions (Cap. 301) | Completed |
| APP-33 | PFA in concrete | Completed |
| APP-34 | Bridges & highway structures design | Completed |
| APP-35 | Refuse storage & collection / RCV | Completed |
| APP-36 | — | **Skipped (source file missing)** |
| APP-37 | Curtain wall, window & window wall | Completed |
| APP-38 | Bridges over streets (BO s.31(1)) | Completed |
| APP-39 | Inspection & copying of plans | Completed |
| APP-40 | Hotel development (B(P)R 23A) | Completed |
| APP-41 | Barrier-free access (B(P)R 72 / DM:BFA) | Completed |
| APP-42 | Amenity features (APP-151 linked) | Completed |
| APP-43 | Licensing CCC / KG / restaurants | Completed |
| APP-44 | Streets vs site area / PR transfer | Completed |
| APP-45 | Testing of reinforcement (CS2) | Completed |
| APP-46 | Pollution from industrial buildings | Completed |
| APP-47 | Unauthorized A&A (no retrospective approval) | Completed |
| APP-48 | Qualified supervision structural/foundation/excavation | Completed |
| APP-49 | Site investigation & ground investigation | Completed |
| APP-50 | Temporary buildings (B(P)R 50–52) | Completed |

**APP-151 / BEAM Plus cross-references noted in:** APP-40 (plant rooms; 10% concession cap), APP-42 (pervasive pre-requisites / overall GFA concession cap for amenity exclusions).


<!-- Source: batch_03_APP051-075.md -->

# PNAP Summaries — Batch 03 (APP-51 to APP-75)

Source directory: `PNAP_APPa_e`. All APP numbers in this range are present (APP-51 through APP-75 inclusive; none missing).

---

## PNAP APP-51: Monitoring and Maintenance of Horizontal Drains
**Status/Context:** Formerly PNAP 137; issued November 1990 (GGE); re-issued under new categorization August 2009. Encloses Appendix A guidance note amplifying Geotechnical Manual for Slopes (2nd Ed.) Chapters 4 and 11. Addresses long-term performance of horizontal drains used as slope stabilization (mainly longer drains in soil/mixed rock-soil slopes aiming at overall groundwater pressure reduction).

### 1. Core Technical Requirements & Metrics
* **Purpose of drains covered:** Systems designed so required factor of safety is achieved (Geotechnical Manual Tables 5.1 & 5.4); other drain systems need regular inspection/maintenance but need not follow these procedures.
* **Monitoring frequency:** Piezometric levels and drain flow rates at least once every two months in dry season; weekly in wet season; within two days of heavy rainstorm (e.g. rainfall >100 mm in 24 hours); all drains and piezometers on site.
* **Baseline monitoring:** Prefer coverage of two wet seasons before design finalization; establish wet/dry season “base groundwater levels” prior to drain installation.
* **Performance evaluation (descending significance):** (a) piezometric levels after installation must not rise above design level in heavy rainstorms; (b) post-installation base groundwater level lower than pre-installation; (c) storm-response fluctuation range lower than pre-installation; (d) faster drop after rainstorm, returning to normal within a few days.
* **Maintenance:** At least once during Contract Maintenance period then once annually; flush with clean water jet under controlled pressure (brush if dried deposits); clean from deep end toward outlet until outflow clean; inspect surroundings, remove weeds, clear outlets; replace removable inner liners if blocked/flow reduced.
* **Clogging sources:** plant roots/fungi/algae; fines; precipitates of Ca, Mg, Fe and other compounds.
* **Special case:** Extensive natural hillslope systems with difficult outlet access may rely on piezometer monitoring with flushing only if indicated; routine outlet inspection/clearing still required.
* **Instrumentation:** Scheme at design stage (type/number/location of piezometers; flow measurement); open hydraulic piezometers common; Halcrow buckets often used; allowance for instrument maintenance/replacement.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not a GFA/site coverage concession PNAP. Horizontal drains are a geotechnical design choice; designer must compare monitoring/maintenance cost commitment against other stabilization measures at preliminary design stage.

### 3. BD Submission & Certification Procedures
* **Scheduled Area No. 1 (Mid-levels):** Maintenance subject to additional control under BO ss.28A–28D.
* **Outside Scheduled Area No. 1:** Horizontal drains requiring specific long-term maintenance where significant risk to life only approved with positive undertaking that maintenance will ensure continued effectiveness; acceptable undertakings rare (e.g. major private body developing for own use with ownership not expected to change).
* Designer prepares maintenance programme and as-built details for handover to maintenance authority; appointment of suitably-experienced maintenance officer for inspection records; reactivate monitoring if substantial groundwater changes (large flow variation, new surface seepage).

### 4. Critical Red Flags & AP Liability
* Approving drains without credible long-term maintenance undertaking where life risk is significant.
* Terminating monitoring before effectiveness fully assessed; failing to continue monitoring after remedial works.
* Ignoring adjacent development/pumping that may modify groundwater regime.
* Large unexplained flow increases: discharge should be tested and area inspected for leaking services; notify appropriate authority.
* Designer must be closely involved in monitoring; maintenance authority must alert designer if system not performing.

---

## PNAP APP-52: Supply of Plans to Registered General Building Contractors, Registered Specialist Contractors and Registered Minor Works Contractors
**Status/Context:** Formerly PNAP 139; first issue December 1990; last revision August 2001; this revision December 2010 (AD/Sup). Implements B(A)R reg.36 and B(MW)R s.55.

### 1. Core Technical Requirements & Metrics
* **AP duty (B(A)R 36)** — supply to RGBC, RSC and RMWC:
  * (a) copy of BA-approved plans per B(A)R 30;
  * (b) copy of RSE structural details approved by BA;
  * (c) copy of any supervision plan.
* **Exact reproduction:** Only a copy need be supplied, but approved plans must be exact reproduction of plans as approved, stamped, signed and dated by BA.
* **Promptness:** Regulation does not specify time limit; AP must supply latest plans promptly so contractors can supervise continuously.
* **Class I minor works (B(MW)R 55):** AP must deliver to prescribed registered contractor: (a) copy of prescribed plans/details under s.30(c); (b) if required by technical memorandum, copy of supervision plan under s.30(d) or 48(2)(b)/(3)(b).

### 2. GFA, Site Coverage, or Design Concession Impact
* Procedural only — no GFA, site coverage or design concession content.

### 3. BD Submission & Certification Procedures
* Operational duty of the appointed AP toward contractors; not a BA plan-approval checklist item as such, but failure undermines lawful supervision chain under BO/B(A)R/B(MW)R.

### 4. Critical Red Flags & AP Liability
* Supplying unstamped/unapproved or outdated plans.
* Delaying supply so RGBC/RSC/RMWC cannot supervise continuously.
* For Class I MW: omitting prescribed plans/details or required supervision plan.

---

## PNAP APP-53: Building (Construction) Regulation — Accepted Standards / Technical Criteria
**Status/Context:** Formerly PNAP 140; first issue December 1990; last revision July 2016; this revision April 2024 (AD/NB2). Lists BA-accepted standards/criteria as complying with B(C)R performance requirements. Editions include amendments effective as at December 2023; may not be the latest of each standard.

### 1. Core Technical Requirements & Metrics
* **Design & construction (key HK CoPs accepted):**
  * Concrete: CoP Structural Use of Concrete 2013 (2020 Edition)
  * Fire Safety: CoP Fire Safety in Buildings 2011 (June 2023 Edition)
  * Foundations: CoP Foundations 2017
  * Precast Concrete: CoP Precast Concrete Construction 2016
  * Steel: CoP Structural Use of Steel 2011 (2023 Edition) + Explanatory Materials
  * Wind: CoP Wind Effects in Hong Kong 2019 + Explanatory Notes
  * Dead/Imposed Loads: CoP Dead and Imposed Loads 2011 (2021 Edition)
  * Glass: CoP Structural Use of Glass 2018
  * Aluminium: BS 8118 Part 1:1991 (note: replaced by BS EN 1999 parts; BS 8118 still accepted locally; from 1 Jan 2017 partial load factor 1.4 for wind in lieu of Table 3.1 factor 1.2, except amendment submissions already approved at 1.2)
  * Stainless steel: SCI P291
  * Timber: BS 5268 Parts 2, 3, 4 (specified years)
  * GRC: Practical Design Guide (GRC Association Technical Committee)
  * Elastomeric/mechanical bearings: CEDD General Spec for Civil Engineering Works 2020
  * Masonry / earthworks / stone cladding: BS 5628 Part 1:2005; BS 6031:2009; BS 8298 Parts 1–4:2010
* **Materials / workmanship / testing:** Extensive appendices for concrete, steel, aluminium, timber, glass, stainless steel, masonry, GRC, bearings, sealants, gypsum, natural stone, fire testing, anchors (BS 5080) — HOKLAS-relevant BS EN / ISO / ASTM as listed in source Appendix A.

### 2. GFA, Site Coverage, or Design Concession Impact
* None directly. Sets the acceptable technical baseline for structural/fire/foundation design that underpins PR/SC-compliant schemes.

### 3. BD Submission & Certification Procedures
* Plans based on other versions/standards/criteria may be approved if performance requirements achieved; facilitate processing by detailing full background and compatibility with local conditions.
* Approach BD early for agreement in principle to alternative standards/criteria.

### 4. Critical Red Flags & AP Liability
* Mixing standards without BA agreement.
* Using aluminium BS 8118 wind partial factor 1.2 after 1 Jan 2017 on new designs (must use 1.4).
* Assuming “latest” overseas edition without checking BA’s accepted edition list (as at Dec 2023).

---

## PNAP APP-54: Retaining Wall
**Status/Context:** Formerly PNAP 142; first issue December 1990; last revision April 1998; this revision February 2021 (AD/NB2). Defines retaining walls; cross-references PNAP APP-63 and Geoguide 1 (2nd Ed.).

### 1. Core Technical Requirements & Metrics
* **Definition:** Permanent structure on land retaining earth or fill; anchor plates supporting rock/earth face are **not** treated as retaining walls. Rock faces are not “earth” for earth pressure calculation.
* **Design/construction:** Comply with B(C)R s.23; refer PNAP APP-63 and Geoguide 1.
* **Drainage/filter (other than minor RW under B(C)R s.22):** Per B(C)R s.24; filter of clean, sound, durable material free from clay, organics, impurities; geotextile of resistant synthetic polymers acceptable where site non-aggressive (Geoguide 1 §8.5; GEO Pub 1/93).
* **Backfill prohibited contents:** peat/vegetation/timber/organic/degradable; dangerous/toxic; combustible; metal/rubber/plastic/synthetic; materials susceptible to significant volume change (marine mud, swelling clays, collapsible soils); soluble material; must not be chemically aggressive (e.g. excessive sulphate).
* **Appendix A Table 1 grading/plasticity:**
  * Crushed rock: max size 200 mm; % passing 63 µm = 0; Cu ≥ 5; LL/PI N/A
  * Soil: max size 75 mm (notes allow up to 5% rock fragments ≤200 mm if compaction not interfered/no damage); % passing 63 µm = 0–45; Cu ≥ 5 (weathered rock origin — note 4 for alluvial sands/gravels Cu ≥5, not gap-graded); LL ≤45%; PI ≤20%; LL/PI check not needed if <30% by weight <63 µm; PSD without dispersants; max particle ≤2/3 compacted layer thickness.
* **Remedial/preventive to existing walls:** Geotechnical Manual for Slopes §7.3.3 accepted.
* **Monitoring during construction:** Measure RW performance and effects on groundwater, site, buildings, structures, land, streets, services.
* **Demolition:** Plans and supporting docs per B(A)R 8(3)&(4).
* **Minor works:** Certain routine slope/RW maintenance under MWCS (Schedule 1 B(MW)R; PNAP APP-147).

### 2. GFA, Site Coverage, or Design Concession Impact
* Not a GFA concession PNAP. Affects site formation design that can indirectly constrain building footprints and usable site area.

### 3. BD Submission & Certification Procedures
* Structural/geotechnical compliance via B(C)R ss.22–24 and Geoguide 1.
* Demolition plan approval route under B(A)R 8(3)/(4).
* MW items may use simplified requirements instead of prior approval/consent.

### 4. Critical Red Flags & AP Liability
* Treating anchor-plate rock support as RW (incorrect classification).
* Using rock face pressures as “earth” inappropriately.
* Non-compliant backfill / aggressive chemistry / inadequate filters.
* Demolishing existing RW without prescribed plan submission.
* Failing construction monitoring where effects on adjoining property/services are material.

---

## PNAP APP-55: Procedure for Payment of Fees on Submission of Plans
**Status/Context:** Formerly PNAP 143; first issue March 1991; last revision November 2014; this revision June 2024 (AD/CS) — para 13 added, para 9 amended. Implements B(A)R regs 29, 33, 42.

### 1. Core Technical Requirements & Metrics
* Fees payable on first submissions (including major revisions); all resubmissions free of charge.
* **New buildings (incl. temporary):** Fees on GFA of new building; cover associated site formation/structural/drainage plans.
* **No accountable GFA / A&A / works not resulting in new building:** Charged by total number of submitted plans of A1 or smaller (plans larger than A1 count as multiples); categories include transformer/petrol stations, oil storage, jetties etc.; minor ancillary accommodation otherwise accountable for GFA may be ignored for this purpose.
* **Payment:** Crossed cheque to “The Government of the Hong Kong Special Administrative Region” or “The Government of the HKSAR”; cash/post-dated cheques not accepted; BD 24 (Appendix A) with every first submission/major revision; fees non-refundable if withdrawn.
* **Supplementary fees:** Within 14 days of notification or plans may be disapproved under BO s.16(1)(f); same risk if fee missing or cheque dishonoured.
* **Fee exemption:** Non-profit schools/hospitals/similar community buildings generally favourably considered via Form BA16 (+ documentary support); no cheque needed with plans in such cases.
* **Major revision examples (not exhaustive):** change disposition/number of blocks; change storeys (esp. podium/basements); major floor plan reconfiguration affecting PR/SC/L&V/MOE; principal use change (e.g. office↔residential, hotel↔office); substantial site area/config change; serious access change; substantial mods/exemptions/bonuses needing fundamental review; incorrect ground conditions forcing SF reassessment; changes requiring examination under new legislation or new draft/approved OZP.
* **Localized major revision:** Fee may be based on localized GFA (e.g. per podium / affected podium floors); other variations case-by-case under BO s.42.
* **Orders/notices:** No fee for proposals responding to statutory order/notice or advisory letter on building/fire/slope safety.
* **ESH:** FPS or cheque; cheque with Acknowledgement Receipt copy to Receipt & Dispatch Counter within 14 days of electronic submission completion.
* **BD 24 rates (Appendix A — as printed):** Industrial GFA≤20,000 m²: $2,740 per 100 m² (min $10,400); >20,000 m²: $2,200 per 100 m² (min $547,100). Non-industrial ≤10,000 m²: $4,340 per 100 m² (min $10,350); >10,000 m²: $3,480 per 100 m² (min $434,400). Non-GFA/A&A: $14,200 × number of ≤A1 plans.

### 2. GFA, Site Coverage, or Design Concession Impact
* Fee basis tied directly to accountable **GFA** for new buildings; “buildings without accountable GFA” listed for plan-count charging. Major revisions often triggered by PR/SC/L&V/MOE reassessment — design changes that look minor can reset fee liability.

### 3. BD Submission & Certification Procedures
* AP calculates fee on BD 24; enclose cheque on application for approval.
* Doubt on major revision: consult relevant CBS of New Buildings Division 1 — answer within seven days; new Form BA5 legally required with every major revision submission.
* Keep payment receipt for possible refund of overpayment.

### 4. Critical Red Flags & AP Liability
* Under-declaring GFA / plan count → supplementary fee + s.16(1)(f) disapproval risk.
* Treating extensive redesign as free “resubmission” when it is a major revision (and omitting BA5).
* Missing ESH cheque payment within 14 days.
* Assuming fee exemption without BA16/documentary support.

---

## PNAP APP-56: Exemption Criteria for Site Formation Works associated with Exempted Building Works in the New Territories
**Status/Context:** Formerly related INST:6.4 lineage; first issued August 1991; this revision February 1997 (paras 2–4 revised). Cap.121 Certificates of Exemption; site formation exemption under Cap.121 s.6(a) issued by Director of Lands (District Lands Officer).

### 1. Core Technical Requirements & Metrics
* **Exemption considered only if all met:**
  * (a) max gradient across lot boundary-to-boundary ≤15°;
  * (b) overall gradient of area bounded by lines 10 m outside lot boundary in any direction <15°;
  * (c) no slope within 10 m outside lot steeper than 30° or higher than 1.5 m;
  * (d) no RW/terrace wall within lot or within 10 m outside lot higher than 1.5 m.
* **Conditions on Certificate of Exemption for SF works:**
  * No RW/terrace walls >1.5 m; combined RW+slope height ≤1.5 m;
  * Retaining height:breadth ratio ≤2; RW of masonry or concrete;
  * No slopes steeper than 30° nor higher than 1.5 m.
* **Conditions on Certificate of Exemption for Building Works (Appendix A):** All retaining walls excluded from building works exemption and classified as SF works; any structure retaining earth/fill = RW; investigation of existing slopes/RW may be required (* delete as appropriate).

### 2. GFA, Site Coverage, or Design Concession Impact
* Cap.121 exemption path (not BO PR/SC calc). Failure of criteria forces normal BD site formation submission, affecting programme and professional appointments for NTEH-type developments.

### 3. BD Submission & Certification Procedures
* If criteria/conditions not met → prescribed SF plans to BD in normal way (AP engagement required per flow chart).
* Flow chart (Appendix B): DLO consults GEO; investigation may be required; C of E issued with conditions; adverse effect on existing slopes/RW or LP/remedial needs → BD approval route.

### 4. Critical Red Flags & AP Liability
* Assuming Cap.121 building exemption automatically covers site formation / RWs.
* Constructing walls/slopes exceeding height, steepness or H:B ratio conditions.
* Omitting GEO-required stability investigation where demanded.

---

## PNAP APP-57: Requirements for an Excavation and Lateral Support Plan
**Status/Context:** Formerly PNAP 148; first issue October 1991; last revision August 2011; this revision February 2012 (AD/NB2). B(A)R 8(1)(bc). Appendix A “Notes on Design of ELS Works” (8/2011).

### 1. Core Technical Requirements & Metrics
* **ELS plans required when:**
  * (a) excavation deeper than 2.5 m **and** greater than 5 m in length; **and**
  * (b) liable to affect any road, building, structure, slope steeper than 30°, or water main ≥75 mm dia, within the affected area defined by 45° line up from excavation base to ground surface.
* **Personnel:** RSE prepares/signs plans, structural design, and structural assessment of excavation/dewatering effects on adjoining structures. If excavation **>4.5 m** depth: RGE prepares/signs geotechnical assessment, details, calculations, GI reports etc accompanying ELS submission.
* **Two-stage submission:** Stage 1 — lateral support system (e.g. sheet piles/diaphragm), strutting layout, sequence, geo docs, realistic ground movement estimates for entire works; Stage 2 — structural details of supports/struts per approved stage 1.
* **Design methods:** Global safety factor (unfactored soil strength/loads for stability checks vs B(C)R 15) **or** LSPF per CIRIA C580 as modified by Appendix A — **not mixed**. State method on plans/calcs. Computer programs: prior acceptance per PNAP ADM-6; separate acceptance per design method even if same software.
* **Both methods — hydraulic failure:** GCO Pub 1/90 §6.2.4; min FoS 1.5.
* **LSPF specifics:** Not applicable if wall embedment entirely in soft clays; adopt Geoguide 1 (2nd Ed.) min partial factors/surcharge; structural: min factor **1.4** (not 1.35) on SLS forces/moments from C580; ULS via LE or SSI; no separate global FoS 2.0 for overturning/kick-out if Appendix ULS checks followed; prop level sensitivity ±0.5 m and full/no surcharge for singly propped; progressive failure / mitigation; performance review per PNAP APP-115 on completion.

### 2. GFA, Site Coverage, or Design Concession Impact
* Affects basement/podium excavation feasibility and monitoring costs; no direct GFA concession.

### 3. BD Submission & Certification Procedures
* Consent for ELS works not given if required ELS plans not submitted and approved.
* Design report certified by RSE and RGE stating adequate collapse margin and no unacceptable impacts if assumptions verified and works as specified; list assumptions, monitoring ranges, critical procedures; copy to site supervision personnel.
* Min monitoring: ground settlement/heave and piezometric pressures; also vertical member deflection where significant risk to life/property.

### 4. Critical Red Flags & AP Liability
* Commencing deep excavation without approved ELS where criteria met.
* Omitting RGE for >4.5 m excavations.
* Mixing global FoS and LSPF in one design.
* Using computer programs without prior BD acceptance for the chosen method.
* Inadequate progressive-failure assessment for strut-loss scenarios.

---

## PNAP APP-58: Testing of Drainage Works
**Status/Context:** Formerly PNAP 157; first issued April 1993. B(SSFPDW&L)R 73; BA monitoring role vs AP/contractor responsibility. Concurrent PNRC 11 to contractors.

### 1. Core Technical Requirements & Metrics
* Drain testing must proceed as scheduled, recorded and endorsed **even if BA/representative not present**.
* Tests certified as carried out in compliance with **BS 8301:1985**.
* Within **7 days** of attending test, AP submits “certificate on completion of drain test” (Annex I) with endorsed results/record plans (also cites B(A)R 44).

### 2. GFA, Site Coverage, or Design Concession Impact
* None. Procedural quality-control for drainage works (often OP-critical).

### 3. BD Submission & Certification Procedures
* All B(SSFPDW&L)R 73(1) drain-test applications must be copied to AP at same time.
* AP or representative attends, endorses records/results.
* Annex I certificate to BA within 7 days; copy registered contractor.

### 4. Critical Red Flags & AP Liability
* BA’s attendance does **not** diminish AP/contractor responsibility for prescribed standards.
* OP-stage discovery that drainage never duly tested.
* Site deviations from approved pipe runs/alignment/invert so extensive as to need amended plan — AP may be unaware if not attending.
* Fragmented sectional testing on large projects (>100 tests common) — AP must still maintain endorsed records.

---

## PNAP APP-59: Ban on Hand-dug Caissons
**Status/Context:** Formerly related to 1995 legislative ban; first issued May 1993; this revision February 1995. Buildings (Amendment) Ordinance 1995 (19 Jan 1995); BO s.2(1) definition; BA power under s.16(1A). Effect from **1 February 1996** (12-month grace).

### 1. Core Technical Requirements & Metrics
* **Definition:** Any foundation or earth-retaining structure (or part) whose construction includes excavating a shaft by a person digging inside the shaft, with or without machine tools.
* **Default:** BA refuses approval of plans including hand-dug caissons.
* **Exemption only if BA personally satisfied that:**
  * (a) depth ≤3 m **and** inscribed-circle diameter ≥1.5 m; **or**
  * (b) for that site: only practical construction method, **or** no other safe engineering alternative (e.g. narrow/steep sites where machines not possible/safe).
* If exceptional permission: stringent safety requirements in method statement; RC must comply; observe Construction Site (Safety) Regulations; reference HKIE Guidance Notes and OSHC Code of Safe Working Practices.

### 2. GFA, Site Coverage, or Design Concession Impact
* Foundation methodology constraint (esp. karst/marble sites — also cross-referenced by APP-61). No GFA concession.

### 3. BD Submission & Certification Procedures
* Plans with hand-dug caissons face BA refusal under s.16(1A) unless exceptional case demonstrated to BA personally.
* Method statement with stringent safety requirements where permitted.

### 4. Critical Red Flags & AP Liability
* Specifying hand-dug caissons for convenience rather than genuine impossibility/safety alternative.
* Exempted works without enforced method-statement safety / labour compliance.
* AP/RSE strongly urged to avoid even within grace history — worker safety paramount.

---

## PNAP APP-60: Specified Forms
**Status/Context:** Formerly PNAP 159; first issue August 1993; last revision June 2024; this revision May 2026 (AD/CS) — para 4 & Appendix A amended; paras 5–6 added. Specified under BO s.22(4).

### 1. Core Technical Requirements & Metrics
* Where BO/regulations require specified form, **use forms in Appendix A unaltered**; wrong form may invalidate application/notice/certificate.
* Electronic channels: EFSS / e-Counter (receipt@bd.gov.hk); ESH Stage 1/2/3 (30 Jun 2022 / 31 Mar 2023 / 30 Jun 2024); RMWMS launched **29 May 2026** (https://rmwms.bd.gov.hk).
* Appendix A maps forms BA1–BA26*, MW01–MW32, SC01–SC03 to EFSS/e-Counter, RMWMS, and ESH availability (tick matrix).
* Hardcopy: prefer computer fill so QR/barcode stores data; latest from BD website; hard copies from G/F BD HQ counters.
* MBI/WI schemes: see PNBI-3. Electronic plan format: ADM-17.

### 2. GFA, Site Coverage, or Design Concession Impact
* Procedural. Relevant design/concession forms include BA5 (approval of plans), BA16 (modification/exemption — s.42), BA8/BA8A (consent), BA12/BA13 (OP/TOP), etc.

### 3. BD Submission & Certification Procedures
* Match form number to BO/regulation section; select correct online channel per Appendix A.
* BA8 via EFSS only within office hours (as noted); similarly BA15.

### 4. Critical Red Flags & AP Liability
* Altered/obsolete forms → invalid submission.
* Wrong channel (e.g. submitting MW form only via ESH when RMWMS/EFSS required).
* Incomplete appointments (BA4/BA10) / completion certificates (BA12–BA14C) leading to consent/OP delays.

---

## PNAP APP-61: Geotechnical Control on Developments in Area Numbers 2 and 4 of the Scheduled Areas
**Status/Context:** Formerly PNAP 161; first issue November 1993; last revision December 2005; this revision February 2021 (AD/NB2). Scheduled Areas Nos. 2 (NW NT / Yuen Long) and 4 (Ma On Shan) — marble cavity risk. Complements Foundation Code 2017 and PNAP APP-18.

### 1. Core Technical Requirements & Metrics
* **GI:** Approval required under BO s.41(3); plans under B(A)R 8(1)(l); consent before commence. Stage GI preferred; deep holes to detect marble cavities; if marble encountered, min **20 m penetration into sound marble**; inclined holes where dominant cavity trend near-vertical; geophysics between holes; **grout all holes on completion**; control flushing water (sinkhole induction risk); triple-tube + air foam for high-quality cavity infill cores.
* **Supervision/logging:** CoP Site Supervision 2009; Competent Person (Logging); Geoguide 3; log cavity location/size, wall, infill, discontinuities; TCR/SCR/RQD/FI on logs.
* **Prior notification:** ≥2 weeks prior notice of GI commencement to district CGE (B(A)R 20 context). Retain cores/samples on site until substantial completion for BD/GEO inspection.
* **Foundations:** Prefer driven/machine-bored piles for heavily loaded structures on marble; hand-dug caissons discouraged (dewatering/sinkholes; APP-59). Driven piles: heavy section, modified/strengthened tips; increase pile numbers above minimum for load redistribution; consider in pile cap. Bored/barrettes: cavities under and around each pile in stress zone.
* **Construction records:** Full blow counts (per 500 mm easy / per 100 mm hard; suggest easy/hard divide at 10 blows/100 mm); plot blows/100 mm vs depth; survey pile deviation; assess records at close intervals; trial piling/instrumentation/NDT as needed.
* **Monitoring:** Scheme agreed with BA before foundation completion; monthly results + assessment; unusual settlement → notify BD immediately; GEO may continue post-OP monitoring.
* **Wells:** RGE submission that groundwater extraction will not adversely affect site/surroundings. Flushing water normally supplied in these Areas (APP-4 ref; Yuen Long Town / Ma On Shan).

### 2. GFA, Site Coverage, or Design Concession Impact
* Pre-finalization GI may force relocation of structures for cavity avoidance — impacts massing/PR efficiency before GBP lock-in. No design concession for cavities themselves.

### 3. BD Submission & Certification Procedures
* Foundation plans must be accompanied by supporting docs under B(A)R 8(1)(d)(ii) or may be refused under BO s.16(1)(a) & 16(1)(i).
* Consent for superstructure may be refused under s.16(3)(ba) if performance review (Foundation Code cl.7.8) fails to show adequate inspection/record assessment or necessary design changes/approved amendments.
* GEO TGN 26 (marble foundations); TGN 5 (SI sources); GEO Pub 1/2006 (piles).

### 4. Critical Red Flags & AP Liability
* Finalizing GBP before adequate cavity GI.
* Insufficient marble penetration / ungrouted holes / excessive flush water.
* Missing RGE well assessment.
* Inadequate driven-pile blow-count/deviation records and performance review before superstructure consent.

---

## PNAP APP-62: Protection of Sewage and Drainage Tunnels
**Status/Context:** Formerly PNAP 165; first issue April 1994; last revision May 2013; this revision March 2018 (AD/CS). ST(SE)O; BO s.17A; Scheduled Area No.5; DSD Practice Note 2/2017 for other DSD tunnels.

### 1. Core Technical Requirements & Metrics
* Sewage tunnels typically ≥**30 m rock cover** (exceptions noted for Ap Lei Chau–Aberdeen ends).
* **Circulation:** Building works within **100 m** of centreline of gazetted sewage tunnel route, or GI within Area No.5 → circulated to DSD & GEO. TPZ works for other DSD tunnels similarly circulated.
* **GI in Area No.5:** Building works under BO s.2 / Part II control.
* **Appendix technical limits (site formation / foundation / tunnel-cavern works):**
  * Soil structures: Δ vertical/horizontal pressure ≤20 kPa or ≤5% of total overburden for depths >20 m; rock structures (hydrostatic): Δ ≤50 kPa;
  * Diametric distortion ≤0.1% ID; total movement any plane ≤20 mm;
  * PPV ≤25 mm/s blasting; ≤15 mm/s other prolonged vibration (driving/withdrawing piles etc.);
  * No holes/excavations within 3 m of tunnel structure without BA prior approval of works & method;
  * No pile/foundation/well/soil nail/horizontal drain/rock bolt-dowel within 3 m in any plane;
  * No part of ground anchor within 3 m of any sewage tunnel structure.
* Works within **10 m**: detailed method statements + alignment/depth monitoring; monitoring proposals to BA before commence; ongoing data+interpretation.
* **Dewatering/wells within 100 m:** Assess sewage leakage and gas migration; monitoring programme agreed.
* Rock = Geoguide 3 Grades I–III; soil = Grades IV–VI + reclamation/marine/alluvium.
* Other DSD Tunnels listed: HK West, Kai Tak Transfer, Lai Chi Kok, Tsuen Wan, NWNT Sewage, Tolo Harbour Effluent, Tseung Kwan O Sewage + associated structures — follow DSD PN 2/2017 TPZs.

### 2. GFA, Site Coverage, or Design Concession Impact
* Deep tunnel alignment generally minimizes surface development impact, but foundation/pile/anchor/basement designs inside protection zones may be constrained (depth, standoff, monitoring). May force foundation redesign affecting podium/basement GFA efficiency.

### 3. BD Submission & Certification Procedures
* BA may refuse approval or impose conditions under BO s.17A if incompatible with gazetted sewage tunnel works.
* Monitoring submissions and (if <10 m) method statements required before/during works.
* ST(SE)O compensation enquiries: Director of Lands.

### 4. Critical Red Flags & AP Liability
* Foundations/anchors/GI within 3 m of tunnel structures.
* Exceeding pressure/movement/PPV limits.
* Dewatering near tunnels without gas/sewage migration assessment.
* Ignoring non-gazetted DSD tunnels’ TPZs (DSD PN 2/2017).

---

## PNAP APP-63: Geoguide 1 — Guide to Retaining Wall Design
**Status/Context:** Formerly PNAP 166; first issue August 1994; last revision June 1995; this revision November 2020 (AD/NB2). Accepts Geoguide 1 designs for permanent RWs (RC walls, gravity/crib/gabion/mass concrete, cantilevered RWs).

### 1. Core Technical Requirements & Metrics
* 1st Ed. (1982): limit state with **global** factors of safety.
* 2nd Ed. (1993, continuously updated): limit state with **partial** factors; detailed geotechnical parameter and groundwater pressure guidance; design–construction interrelation. Strongly recommended.
* Designs in **entirety** per either 1st or 2nd edition acceptable; **mixture of editions not acceptable**. Submission must state which edition used.

### 2. GFA, Site Coverage, or Design Concession Impact
* Underpins APP-54 retaining wall compliance. No direct GFA concession.

### 3. BD Submission & Certification Procedures
* State edition of Geoguide 1 on design submissions. Updated 2nd edition from CEDD website.

### 4. Critical Red Flags & AP Liability
* Hybrid 1st/2nd edition design → not acceptable.
* Omitting statement of which edition used.

---

## PNAP APP-64: Methods for Testing Hong Kong Soils (GEOSPEC 3)
**Status/Context:** Formerly PNAP 167; first issue September 1994; last revision May 2004; this revision December 2005. Adopts Geospec 3 — Model Specification for Soil Testing (32 Expanded Phase I + 7 Phase II tests).

### 1. Core Technical Requirements & Metrics
* Recommended standard for specifying soil tests for investigation, design and construction.
* **Laboratories:** Only HOKLAS-accredited for the relevant tests; BA accepts only HOKLAS-endorsed certificates/reports.
* **From 1 July 2004:** Only HOKLAS-endorsed certificates from labs accredited to Geospec 3 for those tests.
* Pre-1 July 2004 Phase I GEO Report 36 tests still acceptable with HOKLAS endorsement (Appendix C mapping to Geospec 3 equivalents).
* Credibility guidelines: proper test schedules/soil type info; supervise sampling/storage/transport/prep; document/vet results; do not reproduce HOKLAS reports except in full; clarify doubts with HKAS before submission.

### 2. GFA, Site Coverage, or Design Concession Impact
* None directly. Quality of fill testing affects acceptance of Certificate of Completion for filling works (PNAP 55 / APP lineage referenced).

### 3. BD Submission & Certification Procedures
* BA may refuse approval/consent under BO s.17(1)(6)(b) context if soil tests not per Geospec 3 when reports support plans/conditions.
* May refuse GI plans in Scheduled Areas, SF plans, or other geo-content plans at variance with Geospec 3.
* Fill relative compaction / in-situ density: Certificate of Completion may not be accepted if tests not per Geospec 3.

### 4. Critical Red Flags & AP Liability
* Non-HOKLAS or non-Geospec-3 accreditation after cut-off date.
* Partial reproduction of HOKLAS reports / knowingly misrepresenting test facts (BA sanction context).
* Poor sample handling invalidating test representativeness.

---

## PNAP APP-65: Natural Lighting to Staircases
**Status/Context:** Formerly related PNAP 169; first issue November 1994; this revision March 2003 (AD/NB1). B(P)R 40 — staircases for common use by more than two tenants require adequate natural lighting.

### 1. Core Technical Requirements & Metrics
* **Design guidelines for B(P)R 40 compliance:**
  * Clear glass;
  * Aggregate glass area per storey ≥ **1/10** of plan area within staircase enclosure;
  * Buildings ≤12 storeys: windows face uncovered space complying with “open air” (B(P)R 2(1));
  * Buildings >12 storeys: windows face uncovered/unenclosed space with base width ≥**2.3 m** and length at right angles ≥**4.5 m** (full width of adjoining service lane can be included);
  * Scissor stairs: even lighting — acceptable examples include end-wall landing window centrally positioned min width **1.3 m**; or side-wall windows min width **650 mm**, ≥2 windows per storey, reduce separating wall so back flight gets light.
* **Artificial lighting waiver alternative (BA prepared to waive natural lighting if satisfied):**
  * Permanent artificial lighting ≥**30 lux** at floor level;
  * Auto emergency backup per FSI CoP, horizontal illuminance ≥**2 lux** in emergency;
  * Proper management: normally accepted if management company maintains system post-occupation **and** regular maintenance requirement in DMC.

### 2. GFA, Site Coverage, or Design Concession Impact
* Affects core design, lightwell/lane adjacency, and scissor-stair planning. No GFA bonus stated; artificial lighting waiver supports compact cores / covered courtyards where natural light hard to achieve.

### 3. BD Submission & Certification Procedures
* Demonstrate B(P)R 40 natural lighting compliance on GBP, **or** seek BA waiver with artificial/emergency lighting + management/DMC evidence.

### 4. Critical Red Flags & AP Liability
* Opaque glass / undersized window area.
* Tall building staircase windows onto inadequate exterior space (<2.3×4.5 m).
* Artificial lighting waiver without emergency backup, 30/2 lux levels, or enforceable DMC/management maintenance.

---

## PNAP APP-66: Metal Refuse Chutes at Construction Sites
**Status/Context:** First issued August 1994 (AD/D); re-categorized August 2009. Safety/environmental advisory on temporary metal barrel refuse chutes.

### 1. Core Technical Requirements & Metrics
* External temporary chutes of old metal barrels unsatisfactory: noise nuisance; weather and debris impact affect stability; collapse hazard to workers and passers-by.
* Prefer safer lowering/removal methods; if chutes used: properly assembled/secured/installed; materials of sufficient strength; prefer internal locations to reduce noise.

### 2. GFA, Site Coverage, or Design Concession Impact
* None (construction site temporary works).

### 3. BD Submission & Certification Procedures
* Not a plan-approval PNAP; supervisory/safety duty of AP/RSE; similar note to RCs.

### 4. Critical Red Flags & AP Liability
* External ad-hoc metal barrel chutes without proper assembly/security — public injury / collapse risk; AP/RSE role in ensuring site safety measures.

---

## PNAP APP-67: Energy Efficiency of Buildings — Building (Energy Efficiency) Regulation
**Status/Context:** Formerly PNAP 172; first issue May 1995; last revision July 2024; this revision September 2025 (AD/NB1) — paras 2, 3, 12 amended. OTTV Code 1995; Energy Saving Plan 2015~2025+.

### 1. Core Technical Requirements & Metrics
* Applies to commercial/hotel building envelopes — suitable OTTV for external walls and roofs.
* **Revised OTTV limits (para 3):**
  * Tower: ≤**20 W/m²** (was 21);
  * Podium: ≤**40 W/m²** (was 50).
* **Notional podium height:** For varying SC under APP-132, podium may be regarded as **20 m** above mean street level (may demarcate lower to simplify).
* **A&A applicability:** (a) horizontal/vertical extension constituting new building; (b) new external walls/facades covering entire tower or podium.
* **Open-front shops G/F:** May disregard from OTTV if UFA ≤50 m² and shop AC separated from main building AC; if UFA >50 m², notional OTTV with clear glass shopfront may demonstrate compliance.
* **Sunshades:** Genuine sunshades assisting OTTV reduction — not accountable for GFA; by B(EE)R 6 not included in SC if project ≤**1.5 m**; quantitative assessment if projection >**750 mm**; ≤750 mm regarded as not obstructing prescribed windows; projection over streets under BO s.31(1) generally not allowed (exemptions case-by-case).
* Innovative designs comparable/better in energy efficiency acceptable; effective innovative OTTV-reduction designs not penalised in PR/SC.

### 2. GFA, Site Coverage, or Design Concession Impact
* **Sunshades ≤1.5 m:** not GFA accountable; excluded from SC (reg.6 B(EE)R) if genuine OTTV benefit.
* Innovative envelope features demonstrated effective: not penalised in PR/SC.
* Implementation of revised 20/40 W/m² standards: new GBP or major revision of GBP for development/A&A submitted for approval **on or after 31 December 2025**.

### 3. BD Submission & Certification Procedures
* First GBP need not include B(EE)R reg.5 OTTV info/calcs.
* After approval, **before consent**: OTTV Summary Sheet (Appendix A) under B(A)R 10.
* Before OP / Form BA14: finalize OTTVs and glass SC on general building plans for record; submit OTTV Report (Forms OTTV1–4, record plans, material test certificates/specs, final Summary Sheet) under B(A)R 10.
* Non-Code materials: document source and local suitability.

### 4. Critical Red Flags & AP Liability
* Post-31 Dec 2025 submissions still using old 21/50 W/m² limits.
* Claiming sunshade GFA/SC exclusion without genuine OTTV benefit / without quant assessment when >750 mm.
* OP application without finalized OTTV Report and record plans.
* Counting open-front shops >50 m² without notional clear-glass calculation.

---

## PNAP APP-68: Design and Construction of Cantilevered Reinforced Concrete Structures
**Status/Context:** Formerly PNAP 173; first issue October 1994; last revision November 2005; this revision September 2012. Appendices A (design/construction/drainage/supervision/maintenance) and B (CJ locations for exposed cantilever slabs). Conforming structural submissions considered to meet B(C)R 4; drainage/plan provisions para.4 App.A → B(P)R 4(b) & 10(3). Weathering carve-out: under permanent solid cover ≤1 storey height and ≥ same plan area — may be treated as not exposed.

### 1. Core Technical Requirements & Metrics
* Prefer beam-and-slab for clear span >**1000 mm** vs pure slab cantilever.
* Span/effective depth per Concrete Code (2004 2nd Ed.) cl.7.3.4.2.
* Assess finishes/parapet/waterproofing DL and maintenance/ponding IL accurately.
* Detail for demolition/replacement without impairing main structure (esp. over streets); comply B(P)R 7 & 10 and APP-19 for projection/clear space.
* Cast monolithically with supporting members; no CJ along external edge of supports unless prior approved alternative of equal strength and watertight.
* Supervision per CoP Site Supervision 2009 Table 9.1.
* **Drainage/waterproofing (exposed):** effective WP; 1:3 CS mortar protect membrane at fall ≥**1:75**; drip/groove at bottom edge; all canopies need surface drainage to building SW system; non-accessible cleaning spans: drainage outlets max **5 m** apart; avoid pipe embedment (APP-105 if unavoidable).
* **Cantilever beams:** overall depth at support ≥**300 mm**; HY stirrups; exposure condition 2+ if external.
* **Cantilever slabs thickness:** ≤500 mm span → ≥110 mm; 500–750 → ≥125 mm; >750 → ≥150 mm. HY both faces both directions; main bars ≥10 mm dia, spacing ≤150 mm, As ≥0.25% Ag; drop-support main bars ≤16 mm dia. Crack/stress: max crack 0.1 mm SLS or deformed HY stress ≤100 N/mm² working; cover exposure 2+.
* **External cantilever slabs span >750 mm exposed:** Construction report + Form BA14; waterproof concrete fcu ≥**35 MPa**; main bars hot-dip galvanized BS EN ISO 1461; WP membrane protected by 1:3 CS mortar max W/C 0.65 or equivalent.
* Construction report contents: as-built dimensions, falls, outlets, screed, WP, CJs, grades, bar dia/spacing, cast date, covermeter covers; photos of bars before concreting and after concreting before finishes.

### 2. GFA, Site Coverage, or Design Concession Impact
* Projuring elements (balconies, canopies, A/C hoods, flowerbeds) affect B(P)R projection/over-street controls (APP-19 / B(P)R 7 & 10). Not itself a GFA concession PNAP; drainage means must be on GBP and drainage plans.

### 3. BD Submission & Certification Procedures
* Show water-accumulation prevention on GBP; surface drainage on drainage plans.
* Supervision/workmanship/construction reports — BA conditions for approval and consent.
* BA14 + construction report for exposed cantilever slabs >750 mm span.

### 4. Critical Red Flags & AP Liability
* Pure long-span slab cantilevers; CJ at support face without approval.
* Missing falls/drips/canopy drainage → ponding and structural degradation.
* Spans >750 mm exposed without galvanizing / WP concrete / construction report / BA14.
* Poor long-term maintenance (clogged drains, A/C loads) — AP should arrange IO/management inspection docs on completion.

---

## PNAP APP-69: Conservation of Historic Buildings
**Status/Context:** Formerly PNAP 175; first issue January 1995; last revision May 2009; this revision January 2016 (general revamp). Monuments Cap.53; graded buildings via AAB; BD Practice Guidebook 2012; Heritage Units process A&A.

### 1. Core Technical Requirements & Metrics
* **Monuments/proposed monuments:** Cap.53 s.6 — no works without Antiquities Authority (SDEV) permit; without permit, plans may be refused under BO s.16(1)(d).
* **Grades 1/2/3:** administrative (Grade 1 outstanding — every effort to preserve; Grade 2 special — selective preserve; Grade 3 some merit — alternative means if preservation not practicable). No Cap.53 statutory protection for graded buildings alone, but BD refers A&A/demolition to CHO & AMO.
* **Pragmatic approach:** Performance-based alternatives if equivalent safety/health; e.g. Loading Code 2011 §4.2 design imposed loads where strengthening for Table min IL would harm heritage.
* **Appendix A — typical s.42 mods/exemptions with required justifications:** verandahs/balconies over street (BO 31(1)) — include in GFA; show critical dimensions; AMO letter. Fee exemption for Revitalising Scheme (B(A)R 29(1A)). Protective barriers height/gap/curb reductions (B(C)R 8). Inadequate floor IL capacity (B(C)R 17(1)) / barrier horizontal IL (17(3)). Window sill height (B(P)R 3A). L&V (B(P)Rs 30–32 via APP-130). EVA deficiency (B(P)R 41D + FS assessment). Roof gutters (SSFPDW&L R 39). Lift pit/machine room deviations. Timber staircases/roofs; staircase width ≥860 mm with population control if multi-stair; winders; 17–18 risers; stairs continuing to basement — compensatory measures per Practice Guidebook sections + management plans/owner undertakings/AMO letters/photos as applicable.

### 2. GFA, Site Coverage, or Design Concession Impact
* Retained verandahs/balconies projecting over street: areas included in **GFA**; need AMO heritage support for s.31(1) modification.
* Revitalising Historic Buildings Through Partnership Scheme: plan fee exemption via B(A)R 29(1A) with DEVB appointment docs (charitable fee exemptions otherwise APP-55).

### 3. BD Submission & Certification Procedures
* Early AMO contact to identify character-defining elements.
* Centralised processing: BD refers historic A&A/demolition to CHO/AMO.
* Heritage Units (New Buildings Divisions) process proposals; pre-submission enquiry ADM-19.
* s.42 applications: use Appendix A checklist of plan-shown vs separately submitted justifications.

### 4. Critical Red Flags & AP Liability
* Works to monument/proposed monument without Cap.53 permit.
* Demolition/A&A of graded buildings without engaging CHO/AMO early.
* Seeking blanket exemptions without management plans, owner undertakings, compensatory FS/structural measures, or AMO letters where required.

---

## PNAP APP-70: Use of Plastic Sheet to Cover Scaffolding Outside Buildings
**Status/Context:** First issued May 1995. Cross-regimes: Construction Sites (Safety) Reg 49(1) Cap.59; Building (Demolition Works) Reg 3(2)(a); Summary Offences Ordinance s.4B(2) Cap.228.

### 1. Core Technical Requirements & Metrics
* Obligation to provide screens/fans/catch platforms etc. to prevent falling objects and dust.
* Full PVC wrapping of scaffolding: FSD concern on fire spread; Labour concern on bamboo scaffold stability in strong winds if poorly fixed; can obstruct natural ventilation/lighting of occupied buildings under renovation.
* Precautions if plastic sheeting used: (a) **flame-retardant** sheeting; (b) reinforce scaffolding for strong winds; (c) avoid obstructing natural ventilation/lighting of occupied buildings as far as practicable.

### 2. GFA, Site Coverage, or Design Concession Impact
* None (temporary protective measures).

### 3. BD Submission & Certification Procedures
* Advisory/regulatory compliance for site works; not a GBP OTTV/design item.

### 4. Critical Red Flags & AP Liability
* Non-flame-retardant PVC full wraps on occupied buildings.
* Sheeting-compromised scaffold stability; blocking occupied-unit L&V during renovation/demolition screening.

---

## PNAP APP-71: Underground Cavern Development
**Status/Context:** First issued April 1995 (AD/SE, GGE). Points to SPUN study (1988) and three primary guidance documents.

### 1. Core Technical Requirements & Metrics
* Viable alternative uses studied: CFS/trailer park, oil/gas storage, sewage treatment, RTS, warehousing, commercial/GIC space — environmental benefit possible.
* Reference standards:
  * Geoguide 4 (Mar 1992) — civil engineering of rock caverns;
  * HKPSG Chapter 11 — planning standards/guidelines for underground rock cavern development;
  * Guide to Fire Safety Design for Caverns 1994 — fire safety design guidelines.

### 2. GFA, Site Coverage, or Design Concession Impact
* Planning/feasibility PNAP; PR/SC treatment of cavern floor space not specified here — consult HKPSG Ch.11 and relevant BO practice separately.

### 3. BD Submission & Certification Procedures
* Follow Geoguide 4 / fire safety guide in design submissions for cavern works; planning compliance via HKPSG Ch.11.

### 4. Critical Red Flags & AP Liability
* Cavern proposals without fire safety design per 1994 Guide or geotechnical design per Geoguide 4.
* Treating as conventional above-ground building without underground-specific precautions.

---

## PNAP APP-72: Control of Blasting
**Status/Context:** Formerly PNAP 178; first issue June 1995; this revision April 2007 (RGE and site supervision; Appendix B added). BO Cap.123 and Dangerous Goods Ordinance Cap.295. Mines Authority = Commissioner of Mines (CEDD).

### 1. Core Technical Requirements & Metrics
* Blasting must not adversely affect services, slopes, RWs, buildings, structures via vibration/other effects; provide preventive/protective/precautionary measures for workers, public, traffic, structures, services, nuisance.
* **Blasting assessment:** By competent person (≥**4 years** design/supervision blasting experience), signed by RGE and/or RSE as appropriate; submit with SF/ELS/foundation plans (or revised plans if need identified later). Appendix A contents: sensitive receivers plans; topo/geology/groundwater/constraints study; condition survey; effects assessment (no injury/damage); preventive measures; action limits (vibration, air-overpressure) with stakeholder agreement evidence; blast design outline; safety management; monitoring stations/criteria; protective measures/evacuation/road closure; explosives delivery logistics; on-site store feasibility if needed.
* Plans must show: blasting areas; geology/GW; sensitive receivers; control criteria; instrumentation; precautionary measures (road closure, evacuation, restricted hours); reporting requirements; note to read with blasting assessment.
* **Supervision (BO s.17 conditions):** Competent supervisor independent of RC assisting RGE/RSE stream TCP T5 (≥4 years); or combined TCP T5 + competent supervisor person; CVs to BA before blast commencement. Appendix B specific tasks for T5 (with supervisor) and T3.
* Demolition blasting exceptional; CoP Demolition + Appendix A items; signed RSE/RGE.
* Mines blasting permit for RC — may impose design/control/monitoring conditions.
* Railway: see PNAP 77 and 279 (legacy numbering in text); GS Civil Engineering Works standards.

### 2. GFA, Site Coverage, or Design Concession Impact
* Site formation constraint. No GFA concession. Affects programme and feasible rock excavation for basements.

### 3. BD Submission & Certification Procedures
* Identify blasting need at GBP geotechnical assessment stage; blast assessment + marked-up plans for SF/ELS/foundation.
* BA acceptance of supervision personnel CVs prior to blasting.
* Mines permit separate from BD approval/consent.

### 4. Critical Red Flags & AP Liability
* Blasting without assessment / without Mines permit.
* Sensitive-receiver limits without agreement evidence.
* Using demolition blasting in dense urban context without exceptional justification and CoP Demolition compliance.
* Supervision by RC staff only (must be independent competent supervisor assisting TCP T5, unless combined qualification).

---

## PNAP APP-73: Service Lanes
**Status/Context:** Formerly PNAP 179; first issued May 1995; last revision November 1995; this revision April 2011 (AD/NB1) — paras 12–13 revised. Private/partly private service lanes (historic scavenging lanes).

### 1. Core Technical Requirements & Metrics
* Before relying on private/partly private lane for BO purposes (L&V, MOE, access): AP must demonstrate permanent or pertinent **rights-of-way**; integrity for all users.
* Exit discharge into private/partly private lane unacceptable unless unfettered RoW demonstrated.
* Lane (public or private) unacceptable as MOE/access if obstructed, incapable of improvement, or in decaying state.
* Long-term improvement objective: upon full abutting development, lane **direct**, unobstructed width ≥**3 m**.
* B(P)R 28: every domestic building generally needs suitable service lane at rear or side (except prescribed circumstances).
* Open space: save B(P)R 28(3), service lane area **excluded** from open space under B(P)R 25 — whether or not included in SC/PR.

### 2. GFA, Site Coverage, or Design Concession Impact
* Abutting private lane owned by developer **not** specifically required for BO purposes of the scheme: BA favourably considers including relevant lane area in **SC and PR**.
* Where RoW established: apply formally for modification of B(P)R **23(2)(a)**.
* Lane area included in SC/PR must on completion be **free of structures** (except structures approved and accounted in calculations).
* Diverted lane needed only for neighbourhood pattern (not specifically for proposed development): BA favourably considers including relevant area in SC/PR.
* Essential public-interest lane improvement **not** specifically BO-required for scheme: BA may grant **PR and SC concessions** for free surrender of such lane (acceptable to Government) provided surrendered area does **not** form part of an existing lane.

### 3. BD Submission & Certification Procedures
* Evidence of RoW on GBP for L&V/MOE/access reliance.
* Formal B(P)R 23(2)(a) modification where needed.
* Surrender: plan + written undertaking to surrender free of cost, pay for paving/channelling/sewering/drainage/(where appropriate) lighting; area free of structures.

### 4. Critical Red Flags & AP Liability
* Counting lane in SC/PR while leaving structures on it.
* Relying on obstructed/decaying lane for MOE.
* Claiming surrender concessions for land that already forms part of an existing lane.
* Using private lane for escape without unfettered RoW for proposed building users.

---

## PNAP APP-74: Alkali-Aggregate Reaction in Reinforced Concrete Structures
**Status/Context:** Formerly PNAP 180; first issued April 1995 (AD/SE). Encourages private projects to adopt Works Branch AAR control specification (Appendix A).

### 1. Core Technical Requirements & Metrics
* AAR needs: reactive minerals in aggregate + sufficient alkali + sufficient moisture → expansive gel → cracking → accelerated rebar corrosion + reduced fc.
* Control measures: limit cement alkali; low-alkali cement; PFA replacement, etc.
* **Recommended limit:** Reactive alkali as equivalent Na₂O ≤ **3.0 kg per m³** concrete (Appendix A method), unless AP/RSE opinion that element will not be subject to moisture ingress throughout design life.
* **Equivalent Na₂O = A + B + C** where: A = acid-soluble alkalis of cement + admixtures + water; B = 1/6 total alkalis of PFA; C = 0.76 × Cl⁻ of aggregate. Test standards: BS 4550 Part 2:1970 (excl. AMD 7285), BS 1881 Part 124:1988, APHA (17ed) 3500-K/Na, BS 812 Part 4:1976 as specified.
* Supplier submits to AP/RSE: HOKLAS certificates ≤6 months old; mix alkali calculation; quarterly new certificates + recalculation.

### 2. GFA, Site Coverage, or Design Concession Impact
* Material durability specification — no GFA/SC impact. Plans for approval should clearly indicate the ≤3.0 kg/m³ Na₂O-eq limit when adopting the clauses.

### 3. BD Submission & Certification Procedures
* When adopting: state on plans that reactive alkali ≤3.0 kg/m³ per Appendix A; AP/RSE approve contractor control measures / require clause compliance except dry-for-life elements.

### 4. Critical Red Flags & AP Liability
* Moisture-exposed members without alkali limit / PFA/low-alkali measures.
* “Not subject to moisture” opinion used for outdoor/retaining/wet-process elements without justification.
* Missing HOKLAS certificates or expired (>6 months) alkali test data.

---

## PNAP APP-75: Means of Access for Firefighting and Rescue in Buildings (B(P)R 41A, 41B, 41C)
**Status/Context:** First issued May 1995 (AD/LM). Building (Planning)(Amendment) Regulation 1995; Code of Practice for Means of Access for Firefighting and Rescue revised accordingly. Application via BO s.39; does **not** apply to works carried out or consented on or before **22 May 1995** (s.39(2)).

### 1. Core Technical Requirements & Metrics
* **Reg 41B revised:** Fireman’s lifts designed and located so that in fire, firemen have **safe and unobstructed access** to lifts and to floors served.
* **Reg 41C revised:** Only fireman’s lifts to be installed in a Firefighting and Rescue Stairway (FRS); access stairway in FRS shall serve **all floors** of the building — so firemen can better use all FRS facilities.

### 2. GFA, Site Coverage, or Design Concession Impact
* Core planning: FRS/fireman’s lift arrangement influences GFA-exempt or accountable staircase/lift core configurations per concurrent FS Code / other PNAPs — this PNAP itself sets mandatory access arrangement, not a concession.

### 3. BD Submission & Certification Procedures
* Demonstrate B(P)R 41A–41C compliance (and revised MoA CoP) on GBP for developments subject to the Amendment Regulation (post 22 May 1995 consent/works threshold).
* Revised MoA Code available from Government Publications Sales Centre (as stated).

### 4. Critical Red Flags & AP Liability
* Ordinary lifts inside FRS (only fireman’s lifts permitted).
* FRS stairway not serving all floors.
* Fireman’s lifts without unobstructed fire-time access path.
* Incorrectly applying pre-22 May 1995 grandfathering to later schemes.

---

## Completed APP number list (Batch 03)

| APP | Title (short) | Present |
|-----|---------------|---------|
| APP-51 | Monitoring and Maintenance of Horizontal Drains | Yes |
| APP-52 | Supply of Plans to RGBC / RSC / RMWC | Yes |
| APP-53 | B(C)R — Accepted Standards / Technical Criteria | Yes |
| APP-54 | Retaining Wall | Yes |
| APP-55 | Payment of Fees on Submission of Plans | Yes |
| APP-56 | NT Exemption Criteria for Site Formation Works | Yes |
| APP-57 | Excavation and Lateral Support Plans | Yes |
| APP-58 | Testing of Drainage Works | Yes |
| APP-59 | Ban on Hand-dug Caissons | Yes |
| APP-60 | Specified Forms | Yes |
| APP-61 | Geotechnical Control — Scheduled Areas 2 & 4 | Yes |
| APP-62 | Protection of Sewage and Drainage Tunnels | Yes |
| APP-63 | Geoguide 1 — Retaining Wall Design | Yes |
| APP-64 | Geospec 3 — Soil Testing Methods | Yes |
| APP-65 | Natural Lighting to Staircases | Yes |
| APP-66 | Metal Refuse Chutes at Construction Sites | Yes |
| APP-67 | Energy Efficiency / OTTV (B(EE)R) | Yes |
| APP-68 | Cantilevered RC Structures | Yes |
| APP-69 | Conservation of Historic Buildings | Yes |
| APP-70 | Plastic Sheet on Scaffolding | Yes |
| APP-71 | Underground Cavern Development | Yes |
| APP-72 | Control of Blasting | Yes |
| APP-73 | Service Lanes | Yes |
| APP-74 | Alkali-Aggregate Reaction in RC | Yes |
| APP-75 | MoA for Firefighting and Rescue (41A–41C) | Yes |

**Total: 25 / 25 (APP-51 through APP-75). No missing numbers in this range.**


<!-- Source: batch_04_APP076-100.md -->

# PNAP Batch 04 Summaries — APP-76 to APP-100

> Source: `PNAP_APPa_e`. APP-77 is absent from the source directory. No invented clauses — summaries track the PNAP text and appendices only.

---

## PNAP APP-76: Keeping Buried Services out of Slopes
**Status/Context:** Formerly PNAP 183; re-issued August 2009. First issued June 1995. Guidelines (not exhaustive) for APs/RSEs on keeping buried services out of slopes/retaining walls and mitigating leakage risk; professional judgement required. Cross-ref: Geotechnical Manual for Slopes §9.7 & Ch.5; PNAP 168 (slope/retaining wall record plans).

### 1. Core Technical Requirements & Metrics
* **Leakage hazard:** Persistent leakage from water-carrying services (stormwater drains, sewers, water mains, catchwater channels, water tunnels) threatens slope/retaining wall stability; telephone/electric cable ducts and disused pipes can also transmit significant water.
* **Design principle:** Keep buried services out of slopes as far as practicable; otherwise provide adequate leakage mitigation.
* **Crest setback rule:** Buried services should not be placed in a slope nearer to the crest than a distance equal to the slope’s vertical height (ref. Geotechnical Manual for Slopes §9.7). Routing close to the crest is poor practice.
* **Resiting:** Consider re-routing existing buried services in existing slopes when slopes within/adjacent to a lot are upgraded or when services are relaid/repaired.
* **If siting outside crest area is impractical:** Design slope to factors of safety in Geotechnical Manual Ch.5 allowing for possible leakage, **or** adopt:
  * (a) Lay services on/above ground surface with aesthetic treatment and corrosion/damage protection;
  * (b) House in ducting system, sealed trench or sleeve drained to surface drainage/natural stream — monitor discharge regularly; provide inspection chambers for access;
  * (c) For water mains in crest area — install stop valves on each side of the slope to isolate leakage.
* **Fill slopes:** Allow for differential settlement of buried services and ancillaries after leakage. For sewers/stormwater drains where settlement may be large — avoid rigid pipelines; use flexible jointings with short pipe pieces; consider non-brittle materials to avoid shearing.
* **As-built records:** Compile accurate as-built of all newly constructed buried services; update building, drainage, site formation and water services plans; incorporate into slope/retaining wall record plans (PNAP 168); distribute copies to developers and owners/building managers for future maintenance.

### 2. GFA, Site Coverage, or Design Concession Impact
* No GFA/SC concessions. Design impact is geotechnical routing/setback and slope FoS — may drive re-routing, surface/ducted services, or flexible pipe systems affecting site layout and drainage plans.

### 3. BD Submission & Certification Procedures
* Guidelines apply through site formation / drainage / building plan design judgement.
* Update statutory plans submitted to government departments with accurate as-built service locations.
* Incorporate into slope/retaining wall record plans per PNAP 168; issue copies to developers and future maintenance parties.

### 4. Critical Red Flags & AP Liability
* Ignoring crest setback / FoS for leakage — slope failure and negligence exposure.
* Rigid pipelines in fill without flexible joints/non-brittle materials — breakage and leakage.
* Ducted systems without monitoring/discharge points/inspection chambers.
* Incomplete as-built / failure to hand over to owners/managers — maintenance liability and leakage risk.
* Disregarding non-water-carrying conduits as potential water paths.

---

## PNAP APP-78: Occupation of New Buildings — Buildings Ordinance section 21
**Status/Context:** Formerly PNAP 188; re-issued August 2009. First issued August 1996. Summarises BA processing of occupation permit (OP) applications under BO s.21. Cross-ref: PNAP 53, PNRC 25 (amendment/record plans and schedules).

### 1. Core Technical Requirements & Metrics
* **Statutory clock:** BA must process OP application within **14 days**.
* **Completeness:** Works must be satisfactorily completed per approved plans and in full compliance with BO and Regulations.
* **Inspection:** All parts of building works must be available for examination. Blatantly incomplete controlled works (e.g. sanitary fitments or fire doors not installed) → summary refusal; fresh BA 13 required.
* **Plant/machinery:** Installations required under BO/Regs to be operational on completion (e.g. extensive A/C) must be available for inspection. User plant/fixtures may generally be installed before OP if structurally safe and do not unduly hamper inspection.
* **Minor defects:** BA may accept AP’s written confirmation and, when appropriate, photographic proof of rectification within the 14-day period — submit early enough for OP preparation.
* **Reinspection after refusal (non-premature):** Formal BA 13 resubmission not required (except premature applications). On AP written notification that refusal items are rectified, BA within 14 days reinspects (if required) and issues OP or formally refuses again.

### 2. GFA, Site Coverage, or Design Concession Impact
* None directly. OP refusal for incomplete fire/sanitary works can freeze occupation irrespective of GFA concessions already granted.

### 3. BD Submission & Certification Procedures
* Formal application: **Form BA 13** with requisite certificates, record plans and schedules.
* Applications without requisite certificates processed as far as practicable but should be avoided.
* Development Division BS arranges early inspection with AP; AP arranges with RGBC.
* Refusal: notified first by fax, then formal letter by post; may include additional comments beyond statutory refusal grounds.
* Cross-ref PNAP 53 / PNRC 25 for amendment plans, record plans and schedules.

### 4. Critical Red Flags & AP Liability
* Premature certification of completion → disciplinary proceedings under BO (serious cases).
* Summary refusal for missing fire doors/sanitary fitments — wasted cycle and disciplinary risk.
* Missing certificates with BA 13.
* Missing the 14-day rectification window for photographic/written proof of minor works.
* Plant/fixtures blocking inspection.

---

## PNAP APP-79: Geoguide 5 — Guide to Slope Maintenance
**Status/Context:** Formerly PNAP 189. First issue January 1996; last revision April 1999; this revision September 2020 (general revision). Adopts Geoguide 5 standards for maintenance of man-made slopes/retaining walls and man-made features on natural hillsides. Available at www.cedd.gov.hk. Cross-ref: B(A)R 8(1)(bb)(E); APP-147; Building (Minor Works) Regulation Sch.1.

### 1. Core Technical Requirements & Metrics
* **Adoption:** Geoguide 5 recommended standards must be adopted when specifying maintenance requirements in site formation submissions under B(A)R 8(1)(bb)(E).
* **Maintenance Manual:** Slope/retaining wall designer should prepare a Maintenance Manual (content per Geoguide 5 Ch.2) to assist owners/maintainers; requirement to submit Manual at Form BA 14 stage must be specified in the site formation submission.
* **Maintenance scope:** Should include review of previous Stability Assessment; Engineer Inspections for Maintenance scope clarified in Geoguide 5 (CEDD website).
* **Layman's Guide:** Abridged version of Geoguide 5 available.
* **MWCS:** Certain routine slope/retaining wall maintenance works are designated minor works under simplified requirements (Sch.1 B(MW)R; APP-147).

### 2. GFA, Site Coverage, or Design Concession Impact
* No GFA/SC impact. Design impact: maintenance access, drainage features and Manual obligations must be designed into site formation.

### 3. BD Submission & Certification Procedures
* Specify Maintenance Manual submission requirement in site formation submission.
* Submit Maintenance Manual **in duplicate** with Form BA 14; upon BA acknowledgement, one copy returned to AP/RSE for onward transmission to owner(s)/maintenance parties.

### 4. Critical Red Flags & AP Liability
* Omitting Maintenance Manual requirement from site formation submission / failing to submit at BA 14.
* Failing to transmit Manual to owners — ongoing slope failure liability.
* Specifying maintenance below Geoguide 5 standards.
* Ignoring MWCS options for routine maintenance works when applicable.

---

## PNAP APP-80: Code of Practice for Fire Resisting Construction 1996
**Status/Context:** Formerly PNAP 192; re-issued August 2009. First issued April 1996. Announces revised FRC Code 1996 (guidance on Part XV Building (Construction) Regulations). Cross-ref: PNAP 163.

### 1. Core Technical Requirements & Metrics
* **Regulatory basis:** Fire resisting construction requirements in Part XV of Building (Construction) Regulations; FRC Code provides guidance.
* **Revision purpose:** Clarifies anomalies/grey areas; upgrades design standards for some components; streamlines duplications between FRC Code and MOE Code.
* **Effective date:** Revised FRC Code effective **1 August 1996**.
* **Transitional:** Requirements do **not** apply to buildings/works being carried out or consented to commence on or before 1 August 1996.

### 2. GFA, Site Coverage, or Design Concession Impact
* No direct GFA/SC. FRC upgrades can affect compartment walls, FRP ratings, openings — may constrain layout.

### 3. BD Submission & Certification Procedures
* Apply 1996 FRC Code to plans for works with consent after 1 Aug 1996.
* Code available at Government Publication Centre; suggestions for improvement welcomed.

### 4. Critical Red Flags & AP Liability
* Applying wrong edition (pre-/post-1 Aug 1996 consent date).
* Assuming 1990 Code still governs post-effective-date works.
* Note: later corrigenda in APP-83; subsequent FS Code 2011 supersedes for newer projects — verify which code applies to the project’s consent/approval timeline.

---

## PNAP APP-81: Places of Public Entertainment (Amendment) Regulation 1996 and Associated Legislative Amendments
**Status/Context:** Formerly PNAP related to PNAP 54 content; first issued June 1996; re-issued August 2009 as APP-81. Amendment Regulation in force **28.6.96** — PPE licensing procedures retained; design/construction matters transferred. Cross-ref: BO s.39(2).

### 1. Core Technical Requirements & Metrics
* **Transfer of design/planning/construction controls from principal PPE Regulation to:**
  * (a) **Building (Construction) (Amendment) Regulation 1996** — defines “cinema”; regulates protective barriers at outer edge of any upper tier in a place of public entertainment;
  * (b) **Building (Planning) (Amendment) Regulation 1996** — new Part VIA for situation, planning, design etc. of places of public entertainment;
  * (c) **MOE Code 1996 Part III** — MOE for places of public entertainment (from repealed PPE Regs; incorporates part of PNAP 54).
* **Application (BO s.39(2)):** Amendment Regs and MOE Code Part III do **not** apply to works being carried out or consented to commence on or before **28.6.96**.

### 2. GFA, Site Coverage, or Design Concession Impact
* No direct GFA/SC. Part VIA planning/design and cinema/protective barrier rules constrain PPE layout, seating tiers and barriers.

### 3. BD Submission & Certification Procedures
* Comply with transferred Regs and MOE Part III for post-28.6.96 PPE works.
* Separate PNAP for revised MOE Code to be issued (see APP-82).

### 4. Critical Red Flags & AP Liability
* Designing PPE under obsolete PPE Regulation safety clauses instead of B(C)R / B(P)R Part VIA / MOE Part III.
* Misapplying effective date under s.39(2).
* Missing cinema definition / upper-tier protective barrier provisions.

---

## PNAP APP-82: Code of Practice for the Provision of Means of Escape in Case of Fire 1996
**Status/Context:** Formerly PNAP 195; re-issued August 2009. First issued June 1996. Explains revised MOE Code 1996 (guidance on B(P)R s.41(1)). Cross-ref: PNAP 163, 192, 194.

### 1. Core Technical Requirements & Metrics
* **Regulatory basis:** B(P)R s.41(1); MOE Code provides compliance guidance.
* **Revision:** Clarifies anomalies; upgrades component design standards; streamlines duplications with FRC Code; adds **Part III** for PPE MOE.
* **Effective dates:**
  * Main Code: **1.12.96**;
  * Part III: already effective **28.6.96** (PNAP 194 / APP-81);
  * Works being carried out or consented on/before 1.12.96 may use earlier MOE edition.
* **Fire Engineering / existing buildings:** BA acknowledges difficulties applying Fire Engineering Approach and new code to existing buildings; further guidelines may issue.

### 2. GFA, Site Coverage, or Design Concession Impact
* No direct GFA/SC. MOE travel distance/exit capacity drives core layout efficiency.

### 3. BD Submission & Certification Procedures
* State which MOE edition applies based on consent date.
* Code sold at Government Publication Centre; suggestions welcomed.

### 4. Critical Red Flags & AP Liability
* Using wrong MOE edition (Part III vs main Code dates differ).
* Assuming new Code automatically applies to pre-1.12.96 consented schemes without checking transitional rules.
* Fire engineering for existing buildings without agreed framework.

---

## PNAP APP-83: Amendments and clarification to Code of Practice for Fire Resisting Construction 1996
**Status/Context:** Formerly PNAP 199. First issue August 1996; last revision August 2011; this revision November 2012 (para. 2(i) amended). Corrigenda to FRC Code 1996 (Jan 1996 edition and post-1996 reprints). Updated FRC Code on www.bd.gov.hk.

### 1. Core Technical Requirements & Metrics
* **Jan 1996 edition corrigenda (in post-1996 reprints):**
  * (i) p.9 para 7.2 — delete “but in no case less than 2 hours”;
  * (ii) p.18 end of para 17.2 — add fire door “to be kept closed” diagram (EN/中);
  * (iii) Table C p.24 — concrete cover for 2 hrs FRP to continuous floors/landings of solid RC: **25 mm** (not 40 mm).
* **Post-1996 reprint corrigenda:**
  * (i) **Para 10.1 revised — openings in compartment walls** for communication (not combination) of adjoining compartments, protected by door/fire shutter:
    * Total opening width ≤ **25%** of compartment wall length → FRP matching wall for **integrity only**;
    * Total opening width > **25%** → FRP matching wall for **integrity and insulation**; insulation FRP may reduce to **30 minutes** if additional sprinkler heads on each side comply with:
      * (1) Part of building sprinkler system; comply with Code of Practice for Minimum Fire Service Installations and Equipment; and
      * (2) Layout substantiates full coverage of each side; spacing per LPC Rules incorporating BS EN 12845:2003.
    * **Applicability of this para 10.1 revision:** Consent on or after **18 August 2011**. For new buildings = consent to commence **foundation works**; for A&A = consent to commence those works.
  * (ii) p.14 fourth line — add “with an FRP as described in (iii) above” after “located”;
  * (iii) p.32 — replace “fixed light;” with “fixed light with FRP ≥ ½ FRPe;”.
* **Raised floors:** Raised floor ≤ **600 mm** from structural floor is **not** an element of construction and does **not** require FRP. Compartment/fire separation walls must start from **structural floor**, not rest on raised floor.

### 2. GFA, Site Coverage, or Design Concession Impact
* No GFA/SC. Opening width % rules and sprinkler trade-offs affect compartment design and FSI coverage.

### 3. BD Submission & Certification Procedures
* Use updated FRC Code from BD website.
* For >25% openings with reduced insulation FRP — substantiate additional sprinklers on plans/FSI submissions.
* Confirm consent date relative to 18 Aug 2011 for para 10.1 applicability.

### 4. Critical Red Flags & AP Liability
* Resting compartment walls on raised floor (≤600 mm) — walls must rise from structural floor.
* Opening width >25% without integrity+insulation FRP (or compliant additional sprinklers).
* Wrong concrete cover (40 mm vs corrected 25 mm) for 2-hr continuous floors/landings.
* Applying revised para 10.1 to pre-18 Aug 2011 foundation consent schemes incorrectly (or vice versa).

---

## PNAP APP-84: Access Facilities for Telecommunications and Broadcasting Services
**Status/Context:** Formerly PNAP 201. First issue November 1997; last revision June 2006; this revision September 2024 (generally revamped; Appendices A & B amended; C, D & E added). Implements B(P)R reg.28A design requirements and MAF for specified buildings under Telecommunications (Amendment) Ordinance 2024 / TO s.14. Spec. date for specified buildings: **1 April 2025** (approval of general building plans).

### 1. Core Technical Requirements & Metrics
* **Statutory trigger (B(P)R 28A):** Access facilities required in every commercial, industrial, residential (other than single-family) and hotel building per BA design requirements.
* **Operators:** FNOs (fixed) under TO s.14; MNOs (mobile) access rights for radiocommunications facilities in **specified buildings** (reg.28A buildings with earliest GBP approval for erection/rebuild/alteration resulting in new building on/after 1 Apr 2025).
* **Fixed services — lead-in ducts, TBE rooms, vertical risers (Appendix A tables by building type / UFS or flats/rooms):**
  * Lead-in ducts: sealable (easy FNO removal); ID typically **100 mm**; counts scale with size (e.g. commercial ≤2×1000 m² UFS: 2 ducts; large commercial up to 8).
  * TBE room min areas & max GFA-exempt areas per Appendix A; clear height **3 m** (commercial/industrial/hotel) or **2.8–3 m** (residential depending on flat count); min vertical risers 1–2 with sizes from 75×75 to 900×250 mm.
  * TBE location: not flood-susceptible; podium+towers → separate TBE for each tower and podium; link to vertical block wiring; **no** water/sewage/drainage/sprinklers/HV (>600V 3φ earth / 1000V 1φ / 1500V dc) cables/transformers inside; lighting, power, ventilation; separate telecom earth; min clear height per App A.
  * Buildings exceeding largest App A range: sum largest-range requirement + remaining-part requirement (example given for 180,000 m² UFS commercial).
* **MAF (App C/D) — specified buildings requiring MAF:**
  * Commercial/industrial **>3,000 m² UFS**; residential **>50 flats**; hotel **>75 rooms**; or if >5 specified buildings but none meet criteria → **one** building gets smallest MAF.
  * Multiple qualifying buildings: no. of MAF buildings = ceil(**25%** of those meeting criteria); podium/towers counted separately; mixed-use: if any use qualifies, building counts as one; if selected, use largest MAF from qualifying use.
  * Select **tallest** building(s); alternatives need OFCA support.
  * Components: TBE_MAF room, RTE room, ITE room (if building height **>175 m** per B(P)R 23(1)), vertical riser_MAF; RTE not combined with ITE; common parts; power connection points; RTE/ITE opaque windows allowing RF propagation; no water/sewage/drainage/sprinklers/HV/transformers; lighting, power, ventilation, maintenance access.
  * RTE elsewhere if rooftop not practicable (non-28A uses / Cap.301 height) — not lower than **90%** of building height.
  * Combined TBE + TBE_MAF: floor demarcation; App A TBE rules apply. If combining impracticable → separate rooms.
  * App D size bands (examples): TBE_MAF / RTE / ITE min areas 10/15/20 m² with max exempt 20/25/30 m²; clear height 3 m (or 2.8/3 m residential); vertical riser_MAF min 1 slot **200×200 mm**.
* **Optional MAF:** Non-required specified buildings may provide TBE_MAF + riser; RTE/ITE only with OFCA support and AP justifications (developer–MNO agreement).

### 2. GFA, Site Coverage, or Design Concession Impact
* **B(P)R 23(3)(b):** BA may disregard floor space solely for access facilities required under reg.28A.
* Fixed TBE: max exemptable area capped per Appendix A (above min required).
* **MAF GFA exemption:** Only for MAF in **specified buildings** under paras 12–13 (and para 14 with OFCA). MAF in non-specified buildings **counts in GFA**.
* **No GFA exemption** if TBE_MAF / RTE / ITE size **< 10 m²**.
* Fixed requirements apply to new/major GBP revision approved on/after **1 Nov 2006**; pre-that may use Sept 2000 practice note.
* MAF requirements apply to new/major GBP of specified buildings approved on/after **1 Apr 2025**, and A&A resulting in new specified building (≥½ volume rebuilt or ≥½ main wall superficial area reconstructed — TO s.14(10A)).

### 3. BD Submission & Certification Procedures
* Consolidate FNO/MNO requirements at planning; appoint >1 FNO for block wiring advisable; lists in CA CoPs.
* Show MAF schedule on GBP per Annex of Appendix C (buildings meeting criteria, 25% count, tallest selection, areas/heights provided vs required/exempt).
* Schematic arrangements: Appendix B (fixed), Appendix E (MAF).

### 4. Critical Red Flags & AP Liability
* Missing reg.28A facilities for multi-family residential / commercial / industrial / hotel.
* Claiming MAF GFA exemption for non-specified buildings or rooms <10 m².
* Wrong 25%/tallest-building selection; combining RTE with ITE; locating RTE below 90% height without justification.
* Water/HV services inside TBE/RTE/ITE; flood-prone TBE.
* Applying MAF rules to pre-1 Apr 2025 GBP approvals incorrectly (or missing them for later approvals).
* Lead-in ducts not properly sealed / non-removable seals.

---

## PNAP APP-85: Application of the Revised Fire Safety Codes
**Status/Context:** Formerly indexing MOA/FRC/MOE. First issued October 1996; re-issued August 2009. Guidance on applying revised fire safety codes (MOA 1995, FRC 1996, MOE 1996) in situations not explicit in Ordinances/Regs. Fire Engineering Approach flagged; separate admin guidelines to follow (see APP-87).

### 1. Core Technical Requirements & Metrics
* **A&A in existing buildings:** Generally only areas affected by proposed A&A (including shared exits) need comply with revised codes; unaffected parts need not.
* **Restaurant licensing:** Only areas under new licence application need revised codes.
* **Consent for plans approved before revised Code effective dates:** Generally no objection to consent if application within **2 years** of approval date and otherwise in order.
* **Occupancy factor:** BD has no objection in principle to population by “head counts” in premises under alteration or suitable comparables — AP must demonstrate suitability:
  * (a) Sufficient demonstration that location, management, patronage, class, type, age etc. are similar;
  * (b) For new buildings, prescriptive population assessment may better protect future A&A headroom.
* **Fire Engineering Approach:** Recognised in the three Codes as alternative to prescriptive provisions; admin procedures PNAP to be issued separately.

### 2. GFA, Site Coverage, or Design Concession Impact
* None directly. Occupancy-factor choice affects MOE capacities and potentially usable planning.

### 3. BD Submission & Certification Procedures
* For A&A/licence — scope compliance to affected areas/shared exits.
* Track 2-year window between plan approval and consent under transitional approach.
* Substantiate head-count population methodology in submission.
* Fire engineering submissions follow later guidelines (APP-87).

### 4. Critical Red Flags & AP Liability
* Forcing entire existing building onto new codes for limited A&A (over-scoping) or omitting shared exits (under-scoping).
* Consent >2 years after approval without checking revised code implications.
* Weak comparable head-count evidence for population.
* Assuming fire engineering acceptance without agreed admin process.

---

## PNAP APP-86: Non-loadbearing Partition Walls
**Status/Context:** Formerly PNAP 203. First issue October 1996; this revision December 2020 (general revision). Safety/performance for non-loadbearing partitions especially in A&A. Cross-ref: APP-53, APP-21, APP-147, B(MW)R Sch.1.

### 1. Core Technical Requirements & Metrics
* **Design/construction:** Per relevant standards/codes; refer **APP-53** — account for slenderness ratio, supports, restraints affecting stiffness/stability.
* **Demolition (APP-21):** (a) appropriate precautionary measures per site; (b) experienced workers; (c) adequate supervision throughout.
* **MWCS:** Certain partition-related works may proceed under simplified requirements (Sch.1 B(MW)R; APP-147).

### 2. GFA, Site Coverage, or Design Concession Impact
* No GFA/SC. Partition layout still affects fire compartmentation, MOE and licensing compliance.

### 3. BD Submission & Certification Procedures
* Normal approval/consent or MWCS simplified requirements as applicable.
* Ensure design considers APP-53 factors even though walls are non-structural.

### 4. Critical Red Flags & AP Liability
* Treating non-loadbearing walls as “non-BO” — public safety still required.
* Demolition without precautions/experienced workers/supervision.
* Ignoring slenderness/restraint → instability.
* Missing MWCS opportunities or conversely using MWCS when full approval required.

---

## PNAP APP-87: Guide to Fire Engineering Approach
**Status/Context:** Formerly PNAP 204. First issued March 1998; re-issued August 2009. Framework for fire engineering as alternative to MOE / MOA / FRC Codes to meet performance of B(C)R 90 and B(P)R 41, 41A, 41B & 41C. Equivalence is paramount. Appendix flow chart: Overview of Fire Engineering Design.

### 1. Core Technical Requirements & Metrics
* **Objective:** Overall safety **equivalent** (or better) to full prescriptive compliance; Codes para 3 recognises FE approach. Compensate deviations with additional measures.
* **Performance requirements to address:**
  * (a) No unacceptable risk of fire developing/spreading given function;
  * (b) Occupants reach temporary/permanent safety without dangerous heat/smoke;
  * (c) No spread to adjacent property;
  * (d) Fire/smoke confined to origin compartment;
  * (e) Firefighters can access/operate without undue risk;
  * (f) Stability, insulation, structural integrity for specified fire intensity/duration.
* **Methodology:** Deterministic FE combining risk & hazard; scenario-based; hazard analysis with defined fire loads, models, computational methods; demonstrate equal performance under given scenarios. Quantitative risk assessment / large-scale tests only for special buildings. HK lacks local stats for indigenous risk factors — full QRA limited.
* **Design procedure (Appendix):** Geometry/construction/use → establish min prescriptive requirements → if non-compliant identify deviations & propose equivalents → agree design → fire scenarios → occupants (max likely number, location, behaviour) → protection features → FE analysis → modify until all scenarios accept → accept design.
* **Fire Safety Strategy Report contents (as relevant):** Intro; development description; sources; MOE; design fires; smoke control; fire spread control; structural performance; sprinklers; alarm; first-aid FF; FF facilities; emergency lighting/signs; role of management; with calculations/sketches (smoke filling, design fire, egress).

### 2. GFA, Site Coverage, or Design Concession Impact
* No automatic GFA concession. FE can unlock atypical atria, travel distances, large compartments otherwise blocked by Codes — still must prove equivalence.

### 3. BD Submission & Certification Procedures
* Early consultation with **BD and FSD** before plan submission for agreement in principle.
* AP assumes pivotal role (no fire engineer accreditation at time of note); other disciplines contribute specialist input.
* Compile Fire Safety Strategy Report; follow Appendix process; practical tests may be required for like-for-like equivalence.

### 4. Critical Red Flags & AP Liability
* Submitting FE without early BD/FSD consultation.
* Claiming FE without demonstrating equivalence to Codes.
* Incomplete scenario coverage or omitted management role / maintenance of FS systems.
* Relying on unverified overseas tools/stats without local justification.
* AP not coordinating multi-discipline FE inputs — pivotal liability remains on AP.

---

## PNAP APP-88: Code of Practice on Inspection and Maintenance of Water Carrying Services Affecting Slopes
**Status/Context:** Formerly related to PNAP 168. First issue November 1996; re-issued August 2009 as APP-88. Announces Works Branch CoP (Government Publications Centre). Read with PNAP 168; similar note issued to Registered Contractors.

### 1. Core Technical Requirements & Metrics
* **CoP scope:** Planning effective inspection/maintenance programmes; options for detecting/inspecting/repairing buried services affecting slopes; recommendations for permanent measures minimising leakage impact on slope safety.
* **BO s.27C:** BA may require building owner to investigate and repair buried water-carrying services in or near a slope.
* **Users:** APs, RSEs, Registered Contractors must refer to CoP when appointed for design, construction and/or maintenance of buried services near slopes.

### 2. GFA, Site Coverage, or Design Concession Impact
* None. Complements APP-76 (keep services out of slopes) with inspection/maintenance regime.

### 3. BD Submission & Certification Procedures
* Apply CoP when responding to s.27C orders or designing/maintaining buried services near slopes.
* Coordinate with PNAP 168 slope record obligations.

### 4. Critical Red Flags & AP Liability
* Ignoring CoP when appointed for services near slopes / s.27C work.
* Disconnect from APP-76 design prevention measures — leakage still slope-critical.
* Failing to respect PNAP 168 record/maintenance handover.

---

## PNAP APP-89: Provision of Better Lift Service
**Status/Context:** Formerly PNAP 207. First issue August 1997; last revision January 2013; this version June 2025 (general revision). Favourable GFA/SC exemption for enlarged lift shafts for better domestic/office lift service. Subject to **APP-151** quality & sustainable environment pre-requisites.

### 1. Core Technical Requirements & Metrics
* **Baseline:** Lift/shaft areas accountable for SC (reg.20) and GFA (reg.23(3)(a)); only fireman’s and accessible lifts have BO size mandates — pressure to minimise shaft area is common.
* **Exemption concept:** Shaft area **above** stated average standard may be excluded from GFA/SC, capped.
* **Domestic/composite including hotels — GFA:**
  * Exempt area over and above **2.5%** of total domestic/hotel GFA;
  * Cap: total exempted ≤ **3.5%** of total domestic/hotel GFA;
  * (If shaft area > **6%** of domestic/hotel GFA → max exempt = 3.5%).
* **Office (<10,000 m² office GFA):**
  * Exempt over and above **5%** of office GFA;
  * Cap ≤ **3%** of office GFA (if shaft >8% → max exempt 3%).
* **Office (≥10,000 m²):**
  * Exempt over and above **3.5%**;
  * Cap ≤ **2.5%** of office GFA (if shaft >6% → max 2.5%);
  * Buildings with office GFA **10,000–12,000 m²**: max exempted area **300 m²**.
* **Shaft definition:** Includes podium floors with lobbies solely serving domestic/hotel/office; excludes shafts serving GFA non-accountable storeys (e.g. refuge). Office GFA includes ancillary office facilities; excludes other commercial uses in office/commercial buildings.
* **SC exemption:** Total GFA-exempt shaft area ÷ number of storeys occupied by such shaft(s).
* **Pre-requisites (para 8):**
  * Domestic/composite: each lift car ≥ **1.82 m²**, shaft ≥ **4.12 m²** internal;
  * Office: car ≥ **2.1 m²**, shaft ≥ **4.4 m²**;
  * Assessment by registered lift engineer (Cap.618) or RPE (building services, Cap.409) certifying above acceptance level per international codes (handling capacity & waiting time) and adequate manoeuvring space for maintenance.
* **Also:** APP-151 pre-requisites/cap. OP-issued buildings not eligible; in-progress projects may apply if enhanced lift service incorporated. Phased development: completed phases get no exemption; no transfer of GFA/SC between completed and incomplete phases (Appendix B examples).

### 2. GFA, Site Coverage, or Design Concession Impact
* Primary concession PNAP: enables larger shafts without full PR/SC penalty within caps above; works with APP-151 overall concession framework.
* Appendix A worked example (office 24,000 m² at 6% shafts → 600 m² GFA exempt; SC exempt = 600/20 = 30 m²).

### 3. BD Submission & Certification Procedures
* Apply for modification for GFA/SC exemption with lift engineer/RPE assessment.
* Demonstrate car/shaft min areas and APP-151 compliance.
* For phased projects — compute exemption per incomplete phase only.

### 4. Critical Red Flags & AP Liability
* Claiming exemption without lift engineer certification or below min car/shaft areas.
* Ignoring APP-151 overall GFA concession cap/pre-requisites.
* Transferring exemption from completed OP phase to later phases.
* Misclassifying retail vs office GFA in composite buildings.
* Applying to buildings already with OP.

---

## PNAP APP-90: Buildings Ordinance section 18(6) — Authority to Enter Buildings
**Status/Context:** Formerly indexed under BO s.18(6)/shoring. First issued June 1997; re-issued August 2009. Procedures for BA authorisation to enter adjacent buildings for necessary shoring (s.18(1)/(6)). Cross-ref: PNAP 71 (shoring for demolition); BO ss.18(4)(5), 18A (compensation / Lands Tribunal).

### 1. Core Technical Requirements & Metrics
* **Preconditions before application:** No other way to provide precautionary measures except shoring inside adjacent buildings; and AP/RSE has failed to obtain owners’/occupants’ consent despite all reasonable steps.
* **Application content (written to BA):** (a) applicant name; (b) HKID/Passport/BRC no.; (c) full address & lot of building to be entered; (d) purpose(s); (e) justification that internal shoring is only possible precautionary means; (f) name of any agent under s.18(6)(b); (g) registration certificate no. if applicant/agent is registered contractor.
* **Authorisation:** If satisfied no alternative, BA issues written authorisation normally within **2 weeks**; copy posted conspicuously on the building.
* **Damage/compensation:** ss.18(4)(5) cover repair of damage and compensation for loss; s.18A — Lands Tribunal for disputes. Rights of affected persons must be respected.

### 2. GFA, Site Coverage, or Design Concession Impact
* None. Site planning should minimise need for invasive adjacent shoring where practicable.

### 3. BD Submission & Certification Procedures
* Written application with all particulars above; await authorisation before entry.
* Follow statutory repair/compensation provisions; see PNAP 71 for demolition shoring.

### 4. Critical Red Flags & AP Liability
* Seeking s.18(6) without exhausting voluntary consent / alternatives.
* Entering without posted authorisation.
* Ignoring damage repair and compensation duties — Lands Tribunal exposure.
* Incomplete application delaying 2-week turnaround.

---

## PNAP APP-91: Maintenance and Replacement Works of Lift Installations
**Status/Context:** First issued July 1997; re-issued August 2009. FRC Code 1996 para 11.2: landing doors FRP ≥ **1 hour** integrity; normally closed unless car at landing. Fire safety during lift M&R — Appendix requirements (to be incorporated into FRC Code). Similar note to Registered Contractors.

### 1. Core Technical Requirements & Metrics
* **Landing doors during works:**
  * (a) Subject to (b), all landing doors remain closed during M&R;
  * (b) If doors need open: normally **no more than one** door open per shaft; openings other than where car levelled attended by lift workers. If >1 open: max **three** open; **no hot works or welding**;
  * (c) Avoid removing >1 landing door per shaft at once;
  * (d) If >1 removed: protect openings with temporary hoarding FRP ≥ **1 hour**;
  * (e)–(f) Hoarding openings: only small vents + access doors; each vent ≤ **5,500 mm²**, upper portion; max **2** vents per liftway, max **4** in the hoarding;
  * (g) Access door same FRP as hoarding; self-closing; lockable from outside, openable from inside without key;
  * (h) Hoarding must not obstruct/reduce escape route width as far as reasonably practicable;
  * (i) Temporary works inside shaft (scaffold, formwork, planking, strutting) — **non-combustible**;
  * (j) Before leaving unattended (lunch/end of day): return open doors to closed or enclose with fire-resisting hoarding.

### 2. GFA, Site Coverage, or Design Concession Impact
* None. Operational fire integrity of shafts during works.

### 3. BD Submission & Certification Procedures
* AP/RSE to observe and brief all parties under their supervision; similar RC practice note exists.
* Requirements intended for incorporation into FRC Code.

### 4. Critical Red Flags & AP Liability
* Multiple open/removed landing doors without FRP hoarding — vertical fire spread path.
* Hot works with >1 door open.
* Combustible temporary works in shaft.
* Leaving openings unattended overnight without protection.
* Escape route obstruction by temporary hoarding.

---

## PNAP APP-92: Amendments and Clarification to Code of Practice for the Provision of Means of Escape in Case of Fire 1996
**Status/Context:** First issued August 1997; re-issued August 2009. Amends MOE Code 1996 para **14(3)(b)** on dead-end travel distance. To be incorporated in next reprint.

### 1. Core Technical Requirements & Metrics
* **Replace original 14(3)(b) with:** Where travel from an exit door of a room to a staircase or discharge to street/open area at ground (para 8.2) is possible in **one direction only (dead-end)**, no point of a room should be more than **18 m** (sum of direct distance + travel distance) from an exit **or** from a point from which travel in different directions to **2 or more exits** is available. In the latter case, maximum distance to one of the exits must not exceed limitations on direct distance and travel distance in paragraph 14.

### 2. GFA, Site Coverage, or Design Concession Impact
* Dead-end 18 m rule critically constrains corridor and unit planning — affects efficiency of domestic/hotel layouts.

### 3. BD Submission & Certification Procedures
* Apply amended 14(3)(b) interpretation on GBP/MOE calculations for schemes under MOE 1996.

### 4. Critical Red Flags & AP Liability
* Misreading dead-end as pure travel distance without “direct distance + travel distance” sum to 18 m.
* Assuming reaching a two-direction point removes para 14 limits to the eventual exit — those limits still apply.

---

## PNAP APP-93: Planning and Design of Drainage Works
**Status/Context:** Formerly PNAP 211. First issue August 1997; last revision September 2012; this revision May 2014 (para 7, Apps B & C added). BA requirements under BO **s.28(1)** for planning/design of drainage for new buildings to enable future maintenance access. Cross-ref: APP-151, ADV-14, FS Code 2011 Part C.

### 1. Core Technical Requirements & Metrics
* **(a) Common underground drains** (except car-park floors): run in sterilised land / common parts.
* **(b) Domestic (not single occupancy) — common soil/waste stacks in common parts;** if pipe-ducts/wells:
  * **Pipe ducts:** access from common parts; ≥ **700 mm** unobstructed working space in front of pipes; doors/panels ≥ **600 × 2000 mm**, FS Code 2011 Part C compliant;
  * **Pipe wells:** size ≥ **1200 × 1500 mm**; openings only for inspection/maintenance from common parts; access ≤ **21 storeys** apart; full-height cat ladder with guard rings; grating platforms ≤ **4 storeys**; access ≥ 600×2000 mm + Part C FRR; ventilation openings at top & bottom each ≥ **1/10** of pipe well horizontal area.
* **GFA:** pipe ducts/wells may be GFA-exempt; open pipe wells also SC-exempt — subject to para 4 (if housing rainwater/soil/waste **and** non-mandatory/non-essential plant pipes → APP-151 pre-requisites & overall GFA concession cap).
* **(c)** Lowest level of re-entrants/light wells with external stacks = common parts with adequate access (cat-ladder if needed).
* **(d)** Multi-unit domestic: no unit’s pipework protruding into lower unit under separate occupancy.
* **(e)** Buildings >3 storeys: separate pipework to manhole for sanitary fitments at floor level with stack bottom.
* **(f)** Soil pipe ND ≥ outlet diameter of WC/slop sinks served.
* **(g)** Bends only where unavoidable; bottom-of-stack bend radius ≥ **4×** stack radius on centreline if practicable, and **never < 200 mm** on centreline.
* **Para 5 modification:** B(SSFPDL)R 25(1) — BA may allow bathtub/shower tray to trap length up to **750 mm** at min gradient **1:40**. Sunken slab voids not to be backfilled with concrete/similar; if unavoidable, provide access panels/cleaning eyes for inspection (CCTV etc.); warn owners floors may need opening for repairs.
* **Para 6:** ADV-14 for external drainage maintenance; consider zoned separate pipes for high-rise.
* **Para 7 — pipes enclosed by architectural features:** Effective visual inspection arrangement from common parts shown on drainage & building plans (App B). Partially screened pipes meeting App C **not** “enclosed”.
  * App C partial screen: exposed ≥1 side; permeable features ≥ **70%** permeability; ≥ **800 mm** high unscreened vertical zone per floor for pipes/branches; projection ≤ **500 mm**.
  * App B enclosed (CCTV regime): feature projection ≤500 mm; vent ≥50% horizontal area top & bottom; access openings ≥300×300 mm; cable-length-based additional openings; vertical camera passage ≥120 mm clear; demountable panels with safety chain for maintenance; OP-stage CCTV inspection under AP; “Certificate on Completion of Inspection…” (Annex 3) with BA 13; DMC/owner undertakings for CCTV device, common parts, regular inspection intervals.
* **Para 8:** Para 3(d) not mandatory for non-domestic but encouraged.

### 2. GFA, Site Coverage, or Design Concession Impact
* Pipe ducts/wells: potential GFA exemption; open wells SC exemption — may be under APP-151 cap when mixed with non-mandatory services.
* Architectural feature enclosures: max **500 mm** depth noted for GFA exemption context in App B diagrams; must not defeat maintenance.

### 3. BD Submission & Certification Procedures
* Comply under s.28(1); show access on drainage/building plans.
* Enclosed pipes: owner/developer letter (DMC undertakings or SPA/tenancy provisions); pre-OP CCTV inspection + Annex 3 certificate with BA 13.
* Modification applications for reg.25(1) length where needed.
* Structural plans for demountable architectural features.

### 4. Critical Red Flags & AP Liability
* Common drains under shops/restaurants/private units — future inaccessible repair crises.
* Pipe ducts without 700 mm clear / undersized access.
* Unit drainage protruding into flat below (para 3(d)).
* Concrete-backfilled sunken slabs without access eyes.
* “Architectural enclosure” without CCTV design, DMC undertakings, or OP inspection certificate.
* Claiming App C “partial screen” when permeability <70% or missing 800 mm exposed zone.

---

## PNAP APP-94: Fire Safety (Commercial Premises) Ordinance, Cap. 502
**Status/Context:** Formerly PNAP 212. First issue August 1997; last revision October 2007; this revision October 2010 (para 5 amended; para 12 ACFSO added). FS(CP)O in force 2 May 1997; amendment Ordinance 1 June 1998. Upgrades fire safety for Prescribed Commercial Premises (PCP) and Specified Commercial Buildings (SCB).

### 1. Core Technical Requirements & Metrics
* **PCP:** Building/part used (or proposed) for banking (not merchant), off-course betting, jewelry/goldsmith with security area, supermarket/hypermarket/department store, or shopping arcade; **and** total floor area **>230 m²** (floor area per FS(CP)O ss.3(3)–3(6); App A shopping arcade examples).
* **SCB:** Used as office/business/trade/entertainment; **and** plans first submitted for BA approval on/before **1 Mar 1987**, or constructed on/before that date with no plans submitted by then.
* **Measures (any/all):** Construction — adequate MOE; MOA for firefighting/rescue; measures inhibiting fire spread & ensuring structural integrity. FSI — automatic sprinklers; MV automatic cut-off; emergency lighting; manual alarms; portable extinguishers; FH/HR; CoP for Minimum FSI & Equipment 1994 requirements.
* **Construction detail sources:** Schedules 2 (PCP) & 5 (SCB) of FS(CP)O; detailed standards in MOE 1996, FRC 1996, MOA 1995.
* **Enforcement:** Director of Buildings — planning/design/construction fire safety measures; Director of Fire Services — FSI/equipment. BD Fire Safety Section (CBS/Fire Safety) administers construction side.
* **Directions/orders:** FSDn (PCP) / FSIDn (SCB) under ss.5(1)/5(1)(A); on conviction for non-compliance, magistrate compliance orders under s.6(1).
* **Alternatives:** Genuine difficulties → fire safety engineering alternatives achieving FS(CP)O primary objectives; considered via **ACFSO** (est. 1 Jun 2010) — see APP-145 App A for TOR/membership.

### 2. GFA, Site Coverage, or Design Concession Impact
* No GFA concession. Upgrade works may affect planning; voluntary or FSDn/FSIDn-driven works still need BO approval if non-exempted.

### 3. BD Submission & Certification Procedures
* Non-exempted upgrade works: approval under BO as usual; FSD requires **three** (not two) sets of FSI plans.
* **No fee** under B(A)R 42 if proposals are entirely for FSDn/FSIDn fire safety improvement.
* Clarify PCP status with BD Fire Safety Section if demarcation difficult.

### 4. Critical Red Flags & AP Liability
* Misclassifying premises (≤230 m² or wrong activity) → wrong Ordinances.
* Ignoring SCB 1 Mar 1987 plan-submission trigger.
* Non-compliance with FSDn/FSIDn → conviction and compliance orders.
* Submitting FE alternatives without ACFSO channel consideration.
* Wrong fee/plan set count for FS-driven submissions.

---

## PNAP APP-95: Sale Offices and Show Flats on Construction Sites
**Status/Context:** First issued August 1997; re-issued August 2009. Public safety rules for sale offices/show flats on active sites. Index: TOP.

### 1. Core Technical Requirements & Metrics
* **Principles:**
  * (a) No part of new building (under construction or substantially completed) as sale office/show flat without **temporary occupation permit**;
  * (b) No temporary building on site as sale office/show flat without **temporary building permit** and TOP for that purpose.
* **BA satisfaction for temporary occupation:**
  * (a) Structurally suitable;
  * (b) Adequately segregated from construction by fire resisting construction;
  * (c) Adequate independent protected means of access/escape with **direct street connection**;
  * (d) Adequate FSI to FSD Director’s satisfaction.
* **Possible conditions:** Limit occupation period; restrict concurrent persons; require partial/total suspension of site works during occupation.

### 2. GFA, Site Coverage, or Design Concession Impact
* None directly. TOP does not equate to OP; sales use must remain temporary and segregated.

### 3. BD Submission & Certification Procedures
* AP application with information justifying para 2 criteria; specify period and expected population.
* Violation of requirements/conditions → TOP revocation + prosecution under BO **s.40(1) and (5)**.

### 4. Critical Red Flags & AP Liability
* Running sales gallery in unfinished tower without TOP.
* Inadequate FR segregation or shared escape with construction areas.
* No direct protected street escape connection.
* Exceeding permitted occupancy / ignoring work-suspension conditions — criminal liability.

---

## PNAP APP-96: Registration of General Building Contractors and Specialist Contractors
**Status/Context:** Formerly PNAP 214. First issue November 1997; last revision September 2013; this revision September 2020 (paras 4, 6, 10 amended). Covers RGBC/RSC registration under BO ss.8–8F. Minor works contractors → APP-148. Procedures detail → PNRC 38. Appendix A scope demarcation (Rev. 9/2013).

### 1. Core Technical Requirements & Metrics
* **Registers (s.8A):** RGBC, RSC (sub-registers), minor works contractors. Gazette annually; particulars on BD website (contractor, AS, reg no., expiry).
* **Specialized works categories (currently five):** Demolition; Foundation; Ground investigation field works; Site formation; Ventilation.
* **Scope:** RGBC — general building/street works excluding specialized categories; also all MW types in B(MW)R Sch.1 Part 2. RSC — only their category (and MW per B(MW)R s.28(1)(b)–(ea)).
* **Registration criteria (s.8B(2)):** Corporate management structure; personnel experience/qualifications; plant/resources access; AS ability to understand works and statutory requirements.
* **Key personnel:** ≥1 AS; for corporation ≥1 Technical Director (TD) with board authority on plant, technical/financial support, decisions & supervision of AS; if TD lacks quals → Other Officer (OO) or AS to assist. Suitable qualified staff also required.
* **Eligibility/sharing:** Individual = only AS; partnership = partner AS; corporation = board-appointed AS; TD must be Companies Ordinance director. Same person may be AS+TD if both criteria met. OO assists one TD only; AS cannot be that OO. AS/TD/OO generally cannot dual-register with another contractor except holding/subsidiary sharing arrangement.
* **CRC:** Must recommend inclusion (s.8B(10)); may advise on AS/TD/OO addition, renewal (s.8C(4)), restoration (s.8D(3)). Membership compositions per s.8(3)/(3A).
* **Appendix A highlights:**
  * **RSC(D):** Not specialized if all: not Scheduled Area 1; height ≤10 m; clear spans ≤6 m / cantilevers ≤1 m; not prestressed; earth retaining ≤1.5 m; no buildings within 5 m.
  * **RSC(F):** All foundations except penetration ≤3 m.
  * **RSC(GIFW):** Exploratory drilling/boring/excavation/probing, instruments/sampling/field tests; pre-drilling; proof-drilling for CIP/mini/socketed H; field testing of treated ground (examples listed).
  * **RSC(SF):** All site formation unless gentle gradients (<15° across lot and 10 m surrounds), no steep/high slopes/walls (>30° or >1.5 m), no construction of walls/slopes/combined exceeding 1.5 m as detailed.
  * **RSC(V):** Works under Building (Ventilating Systems) Regulations.
  * **Shared scopes:** Temporary works generally by RGBC/RSC(F)/RSC(SF)/RSC(D) for their works; pile caps RGBC or RSC(F); basement (non-pile-cap) RGBC; diaphragm walls >3 m penetration → RSC(F); landscape/street RGBC (some RSC(SF)); retaining with DW/piles/caissons → RSC(F); mini-piles ≤400 mm → RSC(F) or RGBC if <3 m deep, not RSC(SF); dredging/reclamation typically RSC(SF) if within para 6 triggers; trial pits normally RSC(GIFW) with limited RGBC exceptions; fire dampers install RGBC or RSC(V) — if RGBC installs, RSC(V) must inspect/certify (FS Code E8.3; APP-13).

### 2. GFA, Site Coverage, or Design Concession Impact
* None. Wrong contractor category can invalidate consent/supervision and delay GFA-related stages.

### 3. BD Submission & Certification Procedures
* Owner appoints correct register category; AP/RSE/RGE select by competence principles; grey cases → case-by-case BA consideration on AP/RSE/RGE proposal.
* Registration/renewal/restoration procedures: PNRC 38.

### 4. Critical Red Flags & AP Liability
* Appointing RGBC for specialized works (e.g. piles >3 m, demolition outside exceptions, steep SF).
* Dual AS/TD across unrelated contractors.
* Fire dampers installed by RGBC without RSC(V) certification.
* Assuming mini-piles are site formation works for RSC(SF).

---

## PNAP APP-97: Consent Procedures for Building Works and Street Works
**Status/Context:** First issue November 1997; last revision December 2005; this revision May 2023 (para 9 & Appendix A first-consent checklist added). Normal vs fast-track consent under BO s.14(1)(b) and B(A)R regs 31 & 33. Sanctions: BO ss.7 & 40.

### 1. Core Technical Requirements & Metrics
* **Type I works:** No first BA consent yet (first consent = first time for those works; not amendment-plan consent, but **includes** major revisions / material deviations approved subsequently). Use **normal** procedure (separate approval then consent). Fast-track **not** available.
* **Type II works:** Approval + first consent already given; amendment to approved plans proposed; **excludes** major revisions / material deviations. May use **fast-track** (approval + consent together) or opt for normal.
* **Fast-track plan endorsement (lower right):** Statement that works are Type II (e.g. curtain wall) seeking Fast Track consent under B(A)R 33. Statement accepts in lieu of Form BA8 for Type II consent.
* **Misclassification:** BA may refuse consent under s.16(3)(a)/(b).
* **Compatibility:** Fast-track consent limited to approved plans; if corresponding structural amendments needed, do not execute until those are approved **and** consented.
* **Terminology for work types:** Demolition; GI; site formation; slope/RW; ELS; foundation; cap/footing/basement; superstructure; curtain wall/cladding; A&A; street/access road; drainage; tunnel; general building works — optional phase detail in brackets.
* **Validity / review:** No statutory plan validity period, but on consent BA may invoke **s.16(3)(d)** if plans approved **>2 years** ago and works don’t meet current BO standards (not used to enforce OZP changes after building plan approval).
* **New regulations (s.39(2)):** Pre-new-reg law applies if works ongoing or consented before new reg. If new-reg works not shown on any plans approved within 2 years at first consent — BA may refuse under s.16(3)(a). If not refused, AP/RSE/RGE must still bring works to new-reg standards before OP (amendment plans as needed); non-compliance → OP refuse under s.21(6).
* **Appendix A first-consent checklist (not for submission):** Site preparation (party wall safety, shoring, ADV-12 site board); documents (BA8/BA8A, supervision plan, GFA concession docs — BEAM Plus provisional, energy performance, APP-151/156 reports, ownership proof, MOD condition docs); ADM-19/ADV-33 GBP Stage II; APP-67 OTTV; ADM-21 site parameters; s.17(1) conditions; corresponding structural/drainage approvals; APP-12 anchors; GEO conditions; new codes/PNAPs; AMO if heritage; MOD validity; APP-23 hoarding; s.113 party wall consent; BA 14 foundation completion; ADM-19 deferral of minor amendments.

### 2. GFA, Site Coverage, or Design Concession Impact
* First consent often hinges on APP-151/APP-2/APP-150 BEAM Plus provisional results and energy reports tied to GFA concessions — incomplete packages delay superstructure consent.

### 3. BD Submission & Certification Procedures
* **Normal:** Separate approval application then consent (all Type I; optional Type II).
* **Fast-track Type II steps:** Mark statement → simultaneous approval+consent outcome (or simultaneous disapproval+refusal; or approval with consent refusal → then normal consent path).
* Use App A checklist before first superstructure/drainage consent.
* Ensure all consents obtained before commencing — ss.7 & 40 sanctions.

### 4. Critical Red Flags & AP Liability
* Labelling major/material amendments as Type II to fast-track.
* Starting works on Type II architectural amendments before corresponding structural consent.
* First consent on >2-year-old plans without checking current standards (s.16(3)(d)).
* Missing APP-151 / ownership / supervision plan packages at first consent.
* Commencing without consent — BO s.40 offences; disciplinary under s.7.

---

## PNAP APP-98: Lighting and Ventilation for Bathrooms and Lavatories in Domestic Buildings
**Status/Context:** Formerly PNAP 219. First issue December 1997; last revision February 2010; this revision June 2013 (general revamp). Favourable modification of **B(P)R reg.36** for internal bathrooms/lavatories in domestic buildings (new and existing).

### 1. Core Technical Requirements & Metrics
* **Modification criteria:** (a) Room part of domestic unit; (b) reasonable size; (c) unlikely to compromise public health/safety.
* **Imposed conditions when modification granted:**
  * (a) Artificial lighting + mechanical ventilation producing **5 air changes/hour** whenever room in use; air change with outside; ventilation ducting with cleaning access acceptable;
  * (b) Additional permanent ventilation to “open air” (reg.2) or “external air” (reg.31) or to another room with window sized for combined rooms — via ventilation duct with cleaning access, or wall/door aperture permanently open/louvred, min size **1/20** of floor area;
  * (c) Unless demountable/replaceable duct: access door/panel min **150×225 mm** (duct ≥150×150) or **100×225 mm** (smaller ducts) every **4 m**, at changes of direction, adjacent turning vanes/dampers, easily accessible;
  * (d) Comply B(P)R **35A** and **APP-27** (water heating) where applicable;
  * (e) Each unit has own lighting/MV/ducting — or communal system with **proper management** (property management company accepted as evidence of proper management for new buildings / completed A&A).
* Prefer annual duct inspection and cleaning.

### 2. GFA, Site Coverage, or Design Concession Impact
* Enables internal wet rooms — significant design freedom for residential efficiency without claiming GFA exemption per this PNAP.

### 3. BD Submission & Certification Procedures
* Apply for modification of B(P)R 36 meeting para 2 criteria; expect para 3 conditions on permit.
* Applies to bathrooms/lavatories in new **and** existing domestic buildings.
* Demonstrate management arrangements if communal MV used.

### 4. Critical Red Flags & AP Liability
* Internal bathrooms without modification or without 5 ACH + permanent ventilation.
* Shared MV without management arrangements.
* Inaccessible ventilation ducts (missing access panels every 4 m / at bends).
* Non-compliance with APP-27/reg.35A for water heaters in internal bathrooms.

---

## PNAP APP-99: Flushing Volume for Flushing Cisterns
**Status/Context:** Formerly PNAP 220. First issue May 2000; this revision February 2012. Relaxes B(SSFPDL)R **reg.19** discharge range (9–14 litres) to conserve water where performance maintained.

### 1. Core Technical Requirements & Metrics
* **Reg.19 default:** WC cistern discharge **9–14 litres**.
* **Acceptance of reduced discharge:** BA and Water Authority have no objection if design flushing volume is compatible with toilet bowl for effective waste clearance by single flush **and** apparatus meets WA requirements.
* **Waterworks vs non-waterworks flush water:**
  * Per reg.91: regs 19–23 **do not apply** to soil fitments flushed with **waterworks** water → **no modification of reg.19 needed** for reduced discharge; AP must ensure Water Works Ordinance/Regs and WA circulars compliance.
  * If flushed with water **other than** from waterworks → BA prepared to grant modification of reg.19 for individual WC systems meeting para 2 requirements.

### 2. GFA, Site Coverage, or Design Concession Impact
* None. Water conservation / WA apparatus approval focus.

### 3. BD Submission & Certification Procedures
* Waterworks-fed low-flush: no BD modification; comply with WA.
* Non-waterworks-fed low-flush: apply for reg.19 modification with performance/WA compatibility evidence.

### 4. Critical Red Flags & AP Liability
* Assuming reg.19 modification always required (not for waterworks supply).
* Low-flush cistern incompatible with bowl — clearance failure / WA rejection.
* Non-waterworks systems without obtaining BD modification.

---

## PNAP APP-100: Structural Plans of Glass Reinforced Polyester (GRP) Water Tanks
**Status/Context:** Formerly PNAP 222. First issue March 1998; this revision December 2010 (para 7 amended; para 9 MWCS added). GRP tanks are building works under BO. Cross-ref: APP-147; B(MW)R Sch.1.

### 1. Core Technical Requirements & Metrics
* **Material behaviour:** High strength / low stiffness → design dominated by stiffness; allow for creep and environmental effects to avoid premature failure.
* **Full structural plan particulars (non-small tanks):** (a) design standards; (b) material specs (types, standards, mechanical properties); (c) max designed capacity, principal dimensions/thicknesses; (d) major component fabrication details; (e) fixing arrangements & tank supports — plus calculations for tank and base support adequacy.
* **Pre-consent documents:** (a) recognised lab/organisation test reports — fibre glass panel mechanical properties and withstand **6× design hydrostatic pressure**; (b) manufacturer’s QC details for panels and tank fabrication.
* **Performance tests (fill to overflow at ambient):**
  * Leakage: no visible leakage after standing ≥ **48 hours**;
  * Deflection: side deflection ≤ **1.0%** of tank depth; bottom ≤ **10 mm** after full load ≥ **2 hours**.
* **Post-test:** Submit reports with AP/RSE statement confirming performance met.
* **Small tanks (volume ≤9 m³ and water head ≤2 m):** Paras 3–5 normally not required; plans need location, principal dimensions, capacity, weight; design standards & material specs; fixing details + support calculations.
* **Indoor very small (volume ≤4 m³ and head ≤1.2 m):** Only location/dimensions/capacity/weight plus calculations for **floor structure** supporting tank.
* **MWCS:** Certain GRP tank works in existing buildings designated minor works (Sch.1 B(MW)R; APP-147).

### 2. GFA, Site Coverage, or Design Concession Impact
* Tank weight/support design affects roof/floor structure; tank rooms themselves may interact with other plant-room GFA rules elsewhere — not addressed in this PNAP.

### 3. BD Submission & Certification Procedures
* Structural plans + calcs for approval; lab 6× hydrostatic & QC docs before consent; post-completion leakage/deflection reports with AP/RSE confirmation.
* Small/indoor thresholds determine reduced submission scope.
* Existing-building works may use MWCS simplified path.

### 4. Critical Red Flags & AP Liability
* Designing for strength only — ignoring stiffness/creep/environment.
* Missing 6× hydrostatic substantiation before consent.
* Failed leakage/deflection tests or missing AP/RSE signed confirmation.
* Stretching “small tank” limits to avoid full testing submission.
* Inadequate support/fixing calcs leading to structural failure of floors.

---

## Completed APP Number List

| Covered | Title (short) |
|--------|----------------|
| **APP-76** | Keeping Buried Services out of Slopes |
| **APP-78** | Occupation of New Buildings (BO s.21) |
| **APP-79** | Geoguide 5 — Guide to Slope Maintenance |
| **APP-80** | Code of Practice for Fire Resisting Construction 1996 |
| **APP-81** | Places of Public Entertainment (Amendment) Regulation 1996 |
| **APP-82** | Code of Practice for Means of Escape 1996 |
| **APP-83** | Amendments/clarification to FRC Code 1996 |
| **APP-84** | Access Facilities for Telecommunications and Broadcasting Services |
| **APP-85** | Application of the Revised Fire Safety Codes |
| **APP-86** | Non-loadbearing Partition Walls |
| **APP-87** | Guide to Fire Engineering Approach |
| **APP-88** | CoP Inspection & Maintenance of Water Carrying Services Affecting Slopes |
| **APP-89** | Provision of Better Lift Service |
| **APP-90** | BO s.18(6) — Authority to Enter Buildings |
| **APP-91** | Maintenance and Replacement Works of Lift Installations |
| **APP-92** | Amendments/clarification to MOE Code 1996 (dead-end) |
| **APP-93** | Planning and Design of Drainage Works |
| **APP-94** | Fire Safety (Commercial Premises) Ordinance Cap. 502 |
| **APP-95** | Sale Offices and Show Flats on Construction Sites |
| **APP-96** | Registration of General Building Contractors and Specialist Contractors |
| **APP-97** | Consent Procedures for Building Works and Street Works |
| **APP-98** | Lighting and Ventilation for Bathrooms and Lavatories in Domestic Buildings |
| **APP-99** | Flushing Volume for Flushing Cisterns |
| **APP-100** | Structural Plans of GRP Water Tanks |

**Missing from source (not summarised):** APP-77

**Total summarised:** 24 PNAPs (APP-76, APP-78–APP-100).


<!-- Source: batch_05_APP101-130.md -->

# PNAP Batch 05 Summaries — APP-101 to APP-130

**Source:** `PNAP_APPb_e/_extracted_txt`  
**Scope:** APP101, APP104–APP112, APP114–APP130 (existing files only)  
**Absent in range:** APP102, APP103, APP113  
**Completed APP list:** 101, 104, 105, 106, 107, 108, 109, 110, 111, 112, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130

---

## PNAP APP-101: Podium Height Restriction under Building (Planning) Regulation 20(3)
**Status/Context:** Re-issued August 2009 under APP categorisation; first issued April 1998 (previously related to PNAP series; index also cites B(P)R 23(3)). Advises how BA considers applications to relax the 15 m full-site-coverage podium height limit under B(P)R 20(3).

### 1. Core Technical Requirements & Metrics
* **Statutory podium height:** B(P)R 20(3) restricts full site coverage of non-domestic podium to a height of **15 m**.
* **BA consideration factors:** Functional requirements, site constraints, environmental impact, public interest, and likelihood of abuse.
* **Favourable examples:** Buildings with public transport terminus (or similar); increase in podium height giving better aesthetic/environmental effect; buildings of special design or use; buildings subject to special floor-height requirements under lease conditions.
* **General rules when modification granted:** Not more than **4 storeys** in the podium; podium height not more than **20 m** from ground level.

### 2. GFA, Site Coverage, or Design Concession Impact
* Directly concerns **site coverage** of non-domestic podiums (full SC allowed only within the regulated podium height envelope).
* Relaxation from 15 m to up to 20 m / ≤4 storeys is a modification that expands the vertical extent of full-SC podium—APs must still reconcile OZP, lease, and other SC/PR constraints.

### 3. BD Submission & Certification Procedures
* Application for relaxation/modification of B(P)R 20(3) podium height restriction under BA discretionary consideration as framed in this PNAP.
* Ref: GP/BREG/P/2.

### 4. Critical Red Flags & AP Liability
* Exceeding 15 m without approved modification is a fundamental B(P)R breach.
* Even with favourable examples, BA may refuse if abuse risk, environmental harm, or weak functional justification.
* Modified cases still capped at **4 storeys / 20 m**—do not assume open-ended podium height.

---

## PNAP APP-104: Exclusion of Floor Areas for Recreational Use
**Status/Context:** Previously PNAP 229; first issue January 1999; last major design-concession alignment January 2011; **this revision July 2025** (para 5 elderly facilities added; paras 1, 4, 6, 8 & 12 amended; former paras 12–13 and Appendix B deleted). Cross-links PNAP APP-42 and **APP-151** GFA concession pre-requisites/cap (except covered landscaped/play areas under para 8).

### 1. Core Technical Requirements & Metrics
* **Basis:** Case-by-case GFA exclusion of residential recreational facilities by modification of B(P)R 23(3)(a), under s.42 BO, for facilities benefiting owners/residents generally (APP-42 para 32).
* **Elderly facilities (from 31 Aug 2025 for new GBP / major revisions):** At least **one elderly-friendly toilet** and **elderly fitness equipment** per Design Manual: Barrier Free Access; if the elderly-friendly toilet also serves as the required accessible toilet, provide **another elderly-friendly facility** plus the fitness equipment; show on plans. Provision commensurate with recreational design (DM Chapter 6 examples).
* **Sliding scale cap (Table 1) — GFA of recreational facilities including voids, plant rooms (incl. swimming-pool filtration), covered courts, etc. serving solely recreational use** must not exceed (whichever is greater of % of total Domestic GFA or absolute m² where stated):

| Total Domestic GFA | Max % / Max area |
|---|---|
| up to 25,000 m² | 5% |
| >25,000–50,000 m² | 4.5% / 1,250 m² |
| >50,000–75,000 m² | 4.0% / 2,250 m² |
| >75,000–100,000 m² | 3.5% / 3,000 m² |
| >100,000–125,000 m² | 3.0% / 3,500 m² |
| >125,000 m² | 2.5% / 3,750 m² |

* **Covered landscaped / children’s play areas under domestic tower footprint:** Not subject to Table 1; limited to **5% of total domestic GFA** (APP-42); still subject to **APP-151 pre-requisites**.
* **Appendix A — commonly accepted active facilities:** Swimming pool; multi-purpose/squash; basketball/football; tennis/badminton; children’s play; games room; indoor golf; table-tennis; fitness; gymnasium; weight training/aerobic/exercise; bowling; skating; volleyball; rock climbing; dance/yoga.
* **Passive:** Sitting/lounge; billiard; sauna/jacuzzi/spa; reading/study/library; function room; computer/video; music/karaoke; club management office/reception; staff room; snack bar/mini-bar/pantry (**≤10 m²** total); first-aid; kitchen (**≤15 m²**, sites without commercial floor space); changing/shower; lavatories; stores.
* **Excluded from concession:** Substantially luxury clubs with restaurants/facilities for exclusive membership/commercial undertakings; commercial undertakings generally. Kitchen of reasonable size ancillary to recreational use on sites **without commercial floor space** may be considered.

### 2. GFA, Site Coverage, or Design Concession Impact
* Core GFA concession PNAP for clubhouse/recreational floors; subject to **APP-151 pre-requisites and overall GFA concession cap** (except para 8 covered landscape/play).
* Table 1 is a hard sliding cap on recreational GFA package size relative to domestic GFA.
* Use must remain exclusive to owners, residents and bona fide visitors—commercialisation voids the concession basis.

### 3. BD Submission & Certification Procedures
* Applications must substantiate need, overall size, headroom, facility mix, and operation/control for exclusive owner/resident use.
* **Prerequisite for plan approval:** Developer/owner letter of undertaking designating recreational facilities as **common area in DMC**, with use/location and binding terms for control, operation, financial support and maintenance. Amendments need revised undertaking and layout plan.
* Exemption via modification of relevant B(P)Rs; condition: undertakings registered in Land Registry **before OP application**; recreational area exclusive use only as on approved plans; no other use/persons without prior BA consent.
* **OP will not issue** without evidence of Land Registry registration of undertaking/layout and GFA concession dissemination in Approved Building Plans per **PNAP ADM-2**.
* Para 5 elderly requirements apply to new GBP or major revisions submitted on/after **31 August 2025**.
* Ref: BD GP/BORD/48 (II).

### 4. Critical Red Flags & AP Liability
* Luxury/membership club commercialisation → concession refusal or enforcement.
* Missing APP-151 compliance for capped items.
* OP blockage if DMC undertaking not registered or ADM-2 disclosure incomplete.
* BA will prosecute contravention of exemption conditions; APs must warn developers/purchasers.
* Omitting elderly toilet/fitness (from implementation date) risks plan rejection.

---

## PNAP APP-105: Water Seepage
**Status/Context:** Previously PNAP 230; first issue October 1999; last revision December 2010; **this revision September 2024** (general revision; Appendix B enhanced guidelines added). Parallel practice note issued to registered contractors. Enhanced guidelines apply to new GBP / major GBP revisions and A&A submitted after **31 March 2025**.

### 1. Core Technical Requirements & Metrics
* **Statutory performance:** B(C)R s.3 (materials); s.27 (external walls impervious); ss.32–33 (damp walls / wet floors); s.34 (weatherproof roof).
* **High-risk locations:** Roofs, external walls, curtain walls, windows, balconies, UPs, bathrooms, kitchens, plumbing/drainage, car park floors, basements.
* **Embedded pipes (Appendix A):** Generally **not permitted** in columns, slabs, structural walls, beams, transfer plates, pile caps, footings (except para 2 piercings). Permitted piercings where no adverse effect and easily accessible—prefer **pipe sleeves** cast into structure:
  * **Vertical through slab/transfer plate:** Hole ≤ **150 mm** dia. or min. bar spacing (whichever less); no severed main reinforcement; trimming bars ≥ main slab rebar size.
  * **Horizontal through beams:** Hole ≤ **150 mm** or **1/3 beam depth** (lesser); at **neutral axis**; vertical & horizontal trimming ≥ **16 mm** each side; no severed shear reinforcement.
  * **Horizontal through structural walls:** Hole ≤ **150 mm** or min. vertical bar spacing (lesser); trimming ≥ vertical wall rebar both sides.
* **Roof waterproofing (App B):** System over entire roof; turn-up ≥ **300 mm** above finished level; angle fillets at V/H junctions; flood/water tests; roofs ≥C35 waterproof concrete recommended in Annex 1; min. structural roof slab thickness **150 mm**; dual-face/dual-direction HY bar ≥10 mm @ ≤150 mm; steel ≥0.25% of concrete section (Annex 1).
* **Bathrooms:** Membrane entire floor + wall turn-up ≥**300 mm**; bathtub/shower walls ≥**2,200 mm**; basin/sink walls ≥**1,100 mm** FFL or **300 mm** above fixture (higher). Sunken slabs monolithic with floor; waterproof entire sunken area; access panels/inspection chambers.
* **Kitchens (incl. open kitchen):** Floor membrane + **300 mm** turn-up; sink/countertop wall membrane ≥**1,100 mm** or **300 mm** above countertop.
* **Pipe penetrations:** Waterproof dress-up ≥**20 mm** above raised platform; dress-down ≥**50 mm** into floor outlet; **100 mm** horizontal around pipes overlapping wet-area membrane.
* **Car parks / basements:** Falls, intercepting channels at ramp top/bottom; water-stops at movement joints; basement (excl. pile caps, thick footings, diaphragm panels) advised as water-retaining structure; no backfill until tanking water test satisfactory.

### 2. GFA, Site Coverage, or Design Concession Impact
* BA prepared to grant modification to exclude from GFA calculation **genuine pipe ducts** designed per **PNAP APP-93** (to keep water-borne pipes off structure).
* Favourable consideration for modification of B(P)R 23(3)(a) for genuine pipe ducts with adequate inspection/maintenance access under **PNAP APP-2** (smart monitoring/access devices encouraged).

### 3. BD Submission & Certification Procedures
* Structural and drainage plans must **explicitly state** that no water-borne piping (other than Appendix A para 2) will be embedded in structural elements; if embedding proposed, submit routing details and justification—omission → disapproval under **BO s.16(1)(i)**; B(C)R s.14(4)(a) relevant.
* Compliance testing (flood tests, precast/curtain wall water penetration tests per codes) required.
* App B guidelines apply to submissions after **31 March 2025**.
* Refs: BD GR/1-55/173; GP/BORD/92; GP/BREG/P/9 (III).

### 4. Critical Red Flags & AP Liability
* Embedding water-borne pipes in structure without approval/justification → plan disapproval.
* Inadequate waterproofing / supervision → latent seepage liability for AP/RSE/RC (health nuisance if foul water; structural deterioration).
* External tanking after backfill is practically unmaintainable—test before backfill.
* AP/RSE/RC must ensure materials, design, workmanship and supervision meet BO performance requirements.

---

## PNAP APP-106: Fire Resisting Construction — Kitchens in Restaurants
**Status/Context:** Re-issued August 2009; first issue October 1998. Clarifies FRC treatment of restaurant kitchens pending incorporation into FRC Code; mean time para 6 of FRC Code to be read with this PNAP.

### 1. Core Technical Requirements & Metrics
* Kitchen regarded as **ancillary accommodation** to restaurant for FRC assessment.
* For Building (Construction) Regulations Part XV:
  * Kitchen enclosed by walls FRP **≥ 1 hour**; openings defended by doors FRP **≥ ½ hour**.
  * **Protected lobby** between each kitchen door and: any escape route from the main building; **and/or** the dining area where kitchen usable floor area **> 45 m²** and door opens onto dining exit route.
* Hold-open devices for kitchen doors may be installed subject to FRC Code para 17.1.

### 2. GFA, Site Coverage, or Design Concession Impact
* No direct GFA/SC concession. Affects compartmentation layout and area planning of F&B premises.

### 3. BD Submission & Certification Procedures
* Demonstrate FRC wall/door ratings and protected lobbies on fire strategy / GBP as applicable; reference this PNAP with FRC Code.
* Ref: BD GP/BREG/C/19/L (VII).

### 4. Critical Red Flags & AP Liability
* Kitchen >45 m² opening directly onto dining exit route without protected lobby → FRC non-compliance.
* Treating kitchen as unrelated room type without 1-hour enclosure is incorrect under this clarification.

---

## PNAP APP-107: Precautionary Measures for Construction Sites
**Status/Context:** Re-issued August 2009; first issue December 1998. Reminder PNAP on protecting adjoining property and public amenity during construction.

### 1. Core Technical Requirements & Metrics
* Attention areas: (a) demolition; (b) dewatering in foundation/basement excavation; (c) lateral support for excavation; (d) pouring concrete against walls of adjoining buildings; (e) structural works.
* Cross-references then PNAPs 71, 74, 81, 148, 224; Draft Code of Practice for Demolition of Buildings; environmental nuisance control (then PNAP 144).

### 2. GFA, Site Coverage, or Design Concession Impact
* None.

### 3. BD Submission & Certification Procedures
* Measures to be planned and implemented as appropriate to site circumstances; follow related practice notes/codes for each work type.
* Ref: BD GR/ACT/20.

### 4. Critical Red Flags & AP Liability
* Failure to provide adequate protective/precautionary measures → damage to adjoining properties, public nuisance, potential BO/common-law liability for AP/RSE/contractor.

---

## PNAP APP-108: Dedication of Land/Area for Use as Public Passage
**Status/Context:** First issue November 1999; revised December 2002; **this revision June 2003**. Sets guidelines for dedication concessions (GFA exemption and/or bonus PR/SC) for public passage.

### 1. Core Technical Requirements & Metrics
* **Category (i) — setback at street level for public passage:** Permitted SC and PR may be exceeded per B(P)R; **maximum additional PR = 5 × dedicated area or 20% of permissible PR, whichever less**. BA may also exempt dedicated areas from GFA.
* **Category (ii) — public passage within/through building at G/F or other floors:** Concessions by modification on merits—from GFA exemption of dedicated area up to bonus PR/SC. Bonus SC normally per B(P)R 22(1). **Max bonus PR (additional GFA):** generally **5×** dedicated area at ground level; **2×** at other floor levels; **total bonus ≤ 20%** of permissible PR, with dedicated area exempted from accountable GFA.
* B(P)R 22(2) applies to surrender for street widening shown on town plans / street improvement plans.
* Resultant intensity must not exceed OZP restrictions unless plan provides otherwise.
* Dedication may be accepted if it: alleviates vehicular/pedestrian congestion; links to public footbridge/subway enhancing safety/convenience; improves road safety/public convenience; or provides suitable greenery compatible with the passageway.
* Mixed public + building-user space: exempted/bonus GFA assessed **proportionally** to traffic generation.
* Notices of dedication, opening hours, and responsible party to be displayed conspicuously; owner responsible for provision, maintenance and repair.

### 2. GFA, Site Coverage, or Design Concession Impact
* Direct PR/SC bonus and GFA exemption engine for public passages/setbacks.
* **GFA exemption** of dedicated area is more readily available once dedication is accepted as desirable; **bonus PR/SC** only if dedication is considered **essential** by government (considering alternative passages nearby).

### 3. BD Submission & Certification Procedures
* Applications with suitable justification of genuine public need and reasonableness of dedicated area.
* **TOP/OP will not issue** before execution of **Deed of Dedication** with all terms fulfilled—advise clients early.
* Ref: BD GP/BREG/P/3(III).

### 4. Critical Red Flags & AP Liability
* Claiming bonus without “essential” dedication justification.
* Exceeding OZP intensity despite bonus formula.
* OP delay from late Deed of Dedication.
* Failure to display notices / maintain dedicated areas breaches dedication conditions.

---

## PNAP APP-109: Geotechnical Manual for Slopes — Guidance on Interpretation and Updating
**Status/Context:** Re-issued August 2009; first issue June 1999 (was PNAP 234). Appendix A clarifies interpretation of Geotechnical Manual for Slopes (2nd Ed., 1984) and supersedes obsolete terminology/sections.

### 1. Core Technical Requirements & Metrics
* **Terminology:** “Risk” → “consequence”; consequence-to-life Categories **1 / 2 / 3** (was high/low/negligible); economic consequence Categories **A / B / C**; combined notation e.g. **2A**.
* **Table 1 — Min FoS for new slopes (10-year return rainfall):**

| Economic \ Life | Cat 1 | Cat 2 | Cat 3 |
|---|---|---|---|
| A | 1.4 | 1.4 | 1.4 |
| B | 1.4 | 1.2 | 1.2 |
| C | 1.4 | 1.2 | >1.0 |

  * Cat 1 also requires FoS **≥ 1.1** for predicted worst groundwater.
* **Table 2 — Existing slopes / remedial-preventive (rigorous investigation + history):** Life Cat 1 → FoS **1.2**; Cat 2 → **1.1**; Cat 3 → **>1.0** (10-year rain). Back-analysis may assume existing FoS **1.0** for worst known loading/groundwater.
* **Temporary works:** Same FoS as permanent new works (Table 1), considering life-of-temporary conditions (category may be lower during construction).
* **Fill compaction:** Exceptional large platforms not supporting structures may use **90%** MDD interior if formation level fill compacted to **95%** for ≥**1.5 m** vertical thickness and peripheral slopes to **95%** for ≥**3 m**.
* **Existing loose fill standard treatment:** Recompact surface fill to **3 m** depth—may be waived for life Cat 3, “too small” hazard (judgement), or mature vegetation with reasonable alternative solution.
* **Consequence examples (Table 3):** Cat 1 — occupied buildings (incl. **bus shelters** with cover), DG stores; Cat 2 — heavily used open spaces, high-traffic roads, uncovered bus stops/petrol stations; Cat 3 — country parks, low-traffic roads, non-DG storage.
* Many Manual chapters superseded by Geoguides / GEO publications (Ch.1, 2, 7 largely, 11, etc.—see App A §10).

### 2. GFA, Site Coverage, or Design Concession Impact
* None directly; governs site formation / slope design affecting development feasibility and setbacks from features.

### 3. BD Submission & Certification Procedures
* Designers apply Tables 1–4 and interpretation guidance in slope assessments/designs; follow current Geoguides where Manual superseded.
* Ref: BD GR/GEO/11(III).

### 4. Critical Red Flags & AP Liability
* Using obsolete “high/low/negligible” risk language or superseded Manual chapters.
* Applying Table 2 lower FoS without rigorous geology/groundwater/performance history.
* Misclassifying bus shelters as non-buildings (must treat as occupied buildings for life Cat 1).
* Owner (advised by designer) chooses economic FoS—document balance of cost vs consequence.

---

## PNAP APP-110: Protective Barriers
**Status/Context:** Previously PNAP 235; first issue September 2000; last revision June 2024; **this revision January 2026** (paras 3, 5, 6 & 11 amended; paras 8 & 9 added). Implements B(C)R ss.36–37, 9, 38 and B(P)R 3A.

### 1. Core Technical Requirements & Metrics
* **Height:** Barrier ≥ **1.1 m** from finished floor of surface where people could step on (adjoining floor level).
* **Toe:** Lowest **150 mm** built solid (except staircases enclosed with walls and without open stair-well—APP-119 relevant).
* **Gaps:** Inhibit passage of particles > **100 mm** in smallest dimension.
* **Curb vs measuring level:** Top of curb not adjoining floor level if: curb height > **500 mm**; or (non-railing) protruding width < **75 mm**; or (railing, curb <500 mm) lowest horizontal rail top ≤ **250 mm** above adjoining floor, or vertical balustrades only with curb ≤ **250 mm** high and protruding width < **75 mm**. Protruding width excludes splay steeper than **45°**.
* **Places of public entertainment:** Outer edge of upper tier—horizontal surface inclined **30°** toward seating and concave, or other manner allowing only small articles and preventing fall to tiers below.
* Design loads per B(C)R s.9; glass barriers per Code of Practice for Structural Use of Glass 2018; tempered glass / structural sealant / spider fixing also per **APP-37**.
* Inaccessible roofs/areas for maintenance only: above barrier rules do not apply, but observe Access for External Maintenance 2021 CoP and OSH Reg s.6.

### 2. GFA, Site Coverage, or Design Concession Impact
* None directly; barrier geometry affects usable balcony/roof edge conditions and safety compliance.

### 3. BD Submission & Certification Procedures
* Structural plans for barriers to include: framing/elements; anchors/supports; design loads/standards; material specs; workmanship for connections/protection; calculations (parent structure check, adequacy/stability, element design, deflection).
* **Streamlined alternative:** Include typical barrier details/layout/general notes in **superstructure plans** (not separate barrier structural submission); location/layout/elevation still on GBP; AP/RSE ensure BO compatibility. Checklist App B5 and samples App B8 of **PNAP ADV-33**.
* Site supervision by suitably qualified person.
* Certain barrier MW items under B(MW)R Schedule 1 / **APP-147**.
* Ref: BD GR/1-55/71/2 (III).

### 4. Critical Red Flags & AP Liability
* Measuring barrier height from curb that should not count as adjoining floor → height shortfall.
* Gaps >100 mm or missing solid 150 mm toe (where required).
* Glass barriers omitting Glass Code / APP-37 requirements.
* Incompatibility between GBP barrier locations and structural details.

---

## PNAP APP-111: Design of Car Parks and Loading/Unloading Facilities
**Status/Context:** Previously PNAP 236; first issue March 2000; last revision January 2011; **this revision July 2019** (Appendix A amended). BA checks layout convenience/safety; C for T advises on road safety/traffic management/run-ins.

### 1. Core Technical Requirements & Metrics
* **Stall dimensions (Table 1 — key):** Motorcycles L 2.4 (min 2) × W 1 × HR 2.4 m; private cars/taxis 5 × 2.5 × 2.4; coaches/buses 12 × 3.5 × 3.8; LGV 7 × 3.5 × 3.6; MGV/HGV 11 × 3.5 × 4.7; containers 16 × 3.5 × 4.7; light buses 8 × 3 × 3.3; disability 5 × 3.5 × 2.4. Align with latest HKPSG Ch.8 Table 11.
* **Private car one-way aisles (desirable):** 0° 3 m; 30° 3; 45° 3.6; 60° 4.2; 70° 4.7; 80° 5.3; 90° desirable 6 / min 5.5 (**absolute min 5.0**); two-way 90° desirable 7.5 / min 6.0 (**absolute min 5.5**).
* **Driveway widths:** Residential one-way desirable 5.5 / min 4.0 / abs min 3.0 (cars only); two-way 7.3 / 5.5 / 5.0. Industrial/mixed one-way 6.0 / 5.5 / 3.5; two-way 10.5 / 7.3 / 6.0.
* **Gradients:** Straight ramp cars desirable 1:10 / max 1:7 / abs 1:6; goods 1:10 / 1:8. Helical cars 1:12.5 / 1:8; goods 1:12.5 / 1:10.
* **Vertical clearance** over driveway (all vehicles): **5.1 m** min (may lower if vehicle-type limited); horizontal clearance **500 mm** (or ≥200 mm from railings/sign posts if impracticable).
* **Bend widening:** e.g. ≤6 m width, R<18 m → +1.2 m widening (see full Table 2 matrix).
* **MSCP ramps (cars/taxis):** Straight one-way min width 3.0 m; helical 3.65 m; two-way straight 6.0 m (min 5.5, no central kerb). Horizontal clearances 300 mm straight / 600 mm helical. Min inner radius bends 5.5 m; helical outer radius 9.0 m one-way. Two-way ramps not recommended.

### 2. GFA, Site Coverage, or Design Concession Impact
* For GFA disregard under B(P)R 23(3)(b) / **PNAP APP-2**, BA must be satisfied as to car park design quality before disregarding floor space from GFA.
* Appendix A deviations are generally **not** treated as fundamental disapproval issues but must be justified and rectified in subsequent submissions if advised.

### 3. BD Submission & Certification Procedures
* Plans show stall dimensions, L/UL bays, run-ins/outs; ramp gradients/radii/swept paths/turning circles; notes on standards used.
* Highlight and justify deviations with swept paths/data; absolute minimum only under exceptional circumstances with full justification.
* C for T continues advice on run-ins and traffic aspects; BA owns general car-park standard compliance.
* Ref: BD GP/BOP/6 (IX).

### 4. Critical Red Flags & AP Liability
* Substandard geometry jeopardising APP-2 carpark GFA disregard.
* Inadequate reverse/manoeuvre space for goods bays (approx. one vehicle length recommended; hammerhead preferred; turn-table if constrained).
* Cycle/motorcycle layout conflicts with run-in or lack of segregation.

---

## PNAP APP-112: Disposal of Condensate from Air-conditioners
**Status/Context:** Previously PNAP 238; first issue March 2000; **this revision March 2019** (revamped).

### 1. Core Technical Requirements & Metrics
* Proper condensate disposal system for A/C required as part of the building’s **surface water drainage** system.

### 2. GFA, Site Coverage, or Design Concession Impact
* None.

### 3. BD Submission & Certification Procedures
* Indicate condensate disposal system on **drainage submission**; failure → plans **disapproved under BO s.28(1)**.
* For existing buildings without system, strongly recommend communal system during comprehensive maintenance.
* Refs: BD GP/BREG/VS/2(II); GP/BORD/92.

### 4. Critical Red Flags & AP Liability
* Omitting condensate drainage from drainage plans → s.28(1) disapproval.
* Uncontrolled discharge causes nuisance and enforcement risk for owners/AP advisors.

---

## PNAP APP-114: Waste Minimization — Provision of Fitments and Fittings in New Buildings
**Status/Context:** Re-issued August 2009; first issue July 2000; revision December 2000 (para 4 amended). Addresses discarding of pre-OP sanitary fitments.

### 1. Core Technical Requirements & Metrics
* Basic sanitary fitments required under building regulations should generally be installed **before OP**.
* BA may favourably modify Building (Standards of Sanitary Fitments, Plumbing, Drainage Works and Latrines) Regulations where: (a) restaurants/hotels will undergo extensive post-OP renovation that would dismantle fitments; or (b) developer offers purchaser-choice fittings.

### 2. GFA, Site Coverage, or Design Concession Impact
* None.

### 3. BD Submission & Certification Procedures
* Modification application detailing extent of deferred fitments, with undertaking that outstanding fitments: (a) installed prior to actual occupation of relevant part; (b) comply with Sanitary Fitments Regs and Water Authority requirements; (c) installed under AP supervision by RGBC employing licensed plumber; (d) WA notified via form **WW046**.
* Refs: BD GP/BREG/RC/2; GP/BREG/SF/1 (II).

### 4. Critical Red Flags & AP Liability
* Deferring fitments without modification/undertaking.
* Occupation before installation of outstanding fitments breaches undertaking.
* Plumbing works without licensed plumber / WA notification.

---

## PNAP APP-115: Performance Review — Item 6(g)(ii) in Column B, Section 17(1) of the Buildings Ordinance
**Status/Context:** First issue September 2000; **this revision December 2005** (paras 1–3 amended; para 4 deleted). Implements BO s.17(1) Column B item 6(g) performance review for certain works **outside** scheduled areas.

### 1. Core Technical Requirements & Metrics
* Performance review demonstrates: adequate inspection/monitoring during construction; validity of geotechnical design assumptions; review of ground conditions encountered; evidence that consequential design changes were made and plans amended/approved.
* Likely imposition sites (besides Scheduled Area Nos. 1, 2, 4):
  * (i) Geology to be verified—slopes with significant continuous ground movement history; abnormal geological weakness (e.g. persistent weak kaolinitic clay in weathered rock).
  * (ii) Groundwater regime adversely affected—damming by congested foundations below GWL or cutoff by bored pile/diaphragm walls (e.g. downslope of Mid-levels Area No.1; hilly HK Island; Kowloon foothills).
  * (iii) Unconventional design (examples section incomplete in extracted text).

### 2. GFA, Site Coverage, or Design Concession Impact
* None directly; can gate occupation of the development.

### 3. BD Submission & Certification Procedures
* BA may impose as condition of approval or consent.
* Performance review to BA’s satisfaction **before OP/TOP**; otherwise application may be refused under **BO s.21(6)(f)**.
* Refs: BD GP/BORD/A/41; GP/BORD/75.

### 4. Critical Red Flags & AP Liability
* OP/TOP refusal if performance review outstanding or unsatisfactory.
* Unvalidated geotechnical assumptions on complex/unconventional sites → public safety liability.

---

## PNAP APP-116: Aluminium Windows
**Status/Context:** Previously PNAP 248; first issue July 2001; last revision March 2006; **this revision February 2021**. Compliance with paras 4–9 accepted as meeting B(C)R s.3; deviations need separate substantiation.

### 1. Core Technical Requirements & Metrics
* Large windows under **APP-37** criteria require structural submission; others still must meet B(C)R performance/safety (standards in App A of APP-37 and APP-53).
* **Fixing lugs:** Stainless steel or hot-dip galvanised; min thickness **1.5 mm**; max **300 mm** centres (greater spacing needs AP/RSE justification that stability/waterproofing uncompromised).
* Aluminium structural members min thickness **2 mm**; mullion depth ≥ **38 mm**.
* Side-hung sash width ≤ **700 mm**; top-hung sash size ≤ **2.5 m²**.
* **4-bar hinges (App A):** Stainless steel, adjustable friction shoe; bars ≥ **2.5 mm** thick; ≥ **3** SS rivets ≥4.8 mm dia. or SS screws ≥5 mm dia. each top and bottom bar; SS plates/bars/angles ≥ **3 mm** for anchorage **or** local thickening ≥ **5 mm**; hinge length ≥ **60%** of sash width; prevent dissimilar-metal contact.
* Recommended drip-nose projecting fin on top frame member (App B).
* Locking devices per APP-37. Cleaning: corrosive agents only if immediately washed with clean water.
* Field water penetration tests advised (Glass Code 2018 Annex A methods).

### 2. GFA, Site Coverage, or Design Concession Impact
* None.

### 3. BD Submission & Certification Procedures
* Structural submission where APP-37 thresholds met; otherwise AP/RSE/RC duty of care for design/installation QA.
* Window repair/replacement may be MW under B(MW)R / APP-147.
* Similar PNAP issued to RCs.
* Refs: BD GP/BORD/105 (II); GP/BREG/P/38 (II).

### 4. Critical Red Flags & AP Liability
* Undersized aluminium sections, oversize openable sashes, inadequate lug spacing → fall-out / seepage risk and public safety liability.
* Aluminium rivets on SS hinges (corrosion).
* Inadequate site supervision of lug fixing.

---

## PNAP APP-117: Structural Requirements for Alteration and Addition Works in Existing Buildings
**Status/Context:** Re-issued August 2009; first issue December 2000. Guidance on structural A&A submissions.

### 1. Core Technical Requirements & Metrics
* New structural elements: design to **current** Building Regulations and codes.
* Existing adequacy may be checked to **then-prevailing** regulations/codes to which building was designed, subject to:
  * **Wind:** If major wind-resisting walls/frames reduced in stiffness by **≥5%**, or wind exposure area increased by **≥10%** → check to **current wind code**.
  * **Storage floors:** Check to current B(C)R minimum imposed loads.
  * **Flat slabs (working-stress originally):** If altered or additional load → check shear to Concrete Code **1987**.
* If approved plans unavailable: compare new vs original loading/BM/shear; open-up for reinforcement/concrete strength if needed. Show reinforcement details when available (then PNAP 121).

### 2. GFA, Site Coverage, or Design Concession Impact
* None directly; structural viability gates A&A proposals that may include GFA changes.

### 3. BD Submission & Certification Procedures
* Structural plans accompanied by assessment of structural viability; AP/RSE inspect affected existing elements; submit site photos where possible; include test results and planned remedial works as appropriate.
* Fire resistance: refer then PNAPs 202 and 231 (FRC/MOE codes application).
* Ref: BD SED/T/48.

### 4. Critical Red Flags & AP Liability
* Using old wind code after significant stiffness reduction/exposure increase.
* Storage conversion without updating imposed loads.
* Proceeding without knowledge of existing reinforcement/capacity.

---

## PNAP APP-118: Testing of Building Materials
**Status/Context:** Previously PNAP 251; first issue October 2001; **this revision May 2012**. Clarifies BA does **not** certify materials; relies on AP/RSE/RGE and independent labs.

### 1. Core Technical Requirements & Metrics
* Normally test via **HOKLAS** or MRA-partner accredited labs within scope: concrete cube/core; steel reinforcement; splices/couplers; curtain wall systems; fire-rated products/materials/components.
* Fire-rated products must meet B(C)R 90 performance via **FS Code 2011**; tests/assessments per FS Code; reports per Clauses **E16.1 / E16.2**; **expired validity not accepted**. Certification bodies via HKCAS / multilateral partners.

### 2. GFA, Site Coverage, or Design Concession Impact
* None.

### 3. BD Submission & Certification Procedures
* Material/product compliance certification on completion per **PNAP APP-13**.
* APs/RSEs/RGEs/RCs supervise selection/application and certify BO compliance.
* Refs: BD GR/BM/5(2)(II) & GR/1-10/461.

### 4. Critical Red Flags & AP Liability
* Relying on BA “approval” of materials (no such power).
* Using non-accredited labs or out-of-scope tests.
* Expired fire test/assessment reports.

---

## PNAP APP-119: Stair-well and Open Wells in School and Other Buildings Used by Youngsters
**Status/Context:** Re-issued August 2009; first issue May 2001. Responds to Coroner's recommendation after fatal fall through school stairwell.

### 1. Core Technical Requirements & Metrics
* Avoid open wells/stairwells in new schools where practicable; elsewhere for children/youngsters evaluate hazard of proper/improper use; provide additional measures (safety nets, higher railing) where appropriate.
* Handrail: MOE Code 1996 para 17.6 and B(P)R Third Schedule para 8.
* Balustrade height ≥ **1,100 mm** (B(C)R 8).
* Protective barriers where level difference > **600 mm**.

### 2. GFA, Site Coverage, or Design Concession Impact
* None.

### 3. BD Submission & Certification Procedures
* Design GBP to demonstrate protective barriers and handrails for open stairwells/wells.
* Ref: BD GP/LEG/26 (III).

### 4. Critical Red Flags & AP Liability
* Open stairwells in schools without enhanced child safety measures—Coroner's recommendation and AP duty of care.
* Barrier height <1.1 m or unprotected >600 mm drops.

---

## PNAP APP-120: Concrete Batching Plant
**Status/Context:** Re-issued August 2009; first issue March 2002. Establishes when CBPs are “buildings” under BO and approval/consent regime.

### 1. Core Technical Requirements & Metrics
* CBP fixed to ground, connected to utility supply, with control room → **buildings** under BO; approval and consent required before erection.
* Fast-track simultaneous approval+consent for common type in App A if: production lines **≤ 4**; total GFA of all control rooms **≤ 100 m²**.
* Longer-term note: possible self-certification exploration for silo capacity **< 50 tonnes** and overall height **< 15 m** (feasibility statement, not enacted in this PNAP).
* App C: 30-day structural processing for relocation of approved CBP with RSE certifications of identical framing/foundations and non-referral conditions.

### 2. GFA, Site Coverage, or Design Concession Impact
* Control rooms count toward GFA thresholds for streamlined processing (≤100 m² aggregate).
* Must comply with town plan / land use.

### 3. BD Submission & Certification Procedures
* New CBP: AP/RSE building plans under BO before erection; OP/TOP on completion.
* Enforcement against new CBP/associated structures after **31 March 2002** without approval/consent.
* Existing pre-**1 May 2002**: no BA action if RSE structural appraisal by **30 October 2002** and proper maintenance (other departments may still enforce).
* Ref: GP/BORD/73 (II).

### 4. Critical Red Flags & AP Liability
* Treating fixed utility-connected CBP with control room as mere “machinery” to avoid BO control.
* UBW enforcement for post-cutoff unapproved plants.
* Ignoring Lands/lease and other department requirements even if BA appraisal accepted for old plants.

---

## PNAP APP-121: Amendment to Code of Practice for Provision of Means of Escape in Case of Fire 1996 (MOE Code)
**Status/Context:** Re-issued August 2009; first issue June 2001. Softens MOE Code para 14.5(e) vision panel rule for inner rooms.

### 1. Core Technical Requirements & Metrics
* MOE Code para 14.5(e): vision panel required in a room (other than toilet) whose only exit is through another room.
* May substitute alternatives (e.g. fire alarm audible in the inner room) alerting occupants of fire/smoke danger.
* Does **not** apply to habitable rooms with MOE through living/dining or kitchen in domestic flats.

### 2. GFA, Site Coverage, or Design Concession Impact
* None; aids planning flexibility for inner rooms without vision panels.

### 3. BD Submission & Certification Procedures
* Document alternative alerting provisions when omitting vision panels.
* Ref: BD GP/LEG/6/A (VII).

### 4. Critical Red Flags & AP Liability
* Omitting both vision panel and equivalent alerting system for non-domestic/inner rooms.
* Misapplying para 14.5(e) to standard domestic flat living-room–bedroom layouts.

---

## PNAP APP-122: Provision of Sky Garden in Refuge Floor
**Status/Context:** Previously PNAP 258; first issued December 2001; **this revision September 2010**. Enables communal sky gardens in refuge floors with FSD concurrence; links **JPN No. 1**.

### 1. Core Technical Requirements & Metrics
* Comply with MOE Code para 21 and FRC Code para 18 (except stated specials). **Net refuge area / min dimension:** disregard space occupied by planters, equipment, furniture.
* Garden furniture/equipment firmly fixed; furniture, equipment, rubbish bins, artificial features and finishes **non-combustible**, no toxic gas; must not obstruct exit routes/lift openings; bins with self-closing lids.
* No naked-fire activities (e.g. barbecue); notices posted.
* Meet other JPN No. 1 communal sky garden criteria.
* **Wholesale conversion existing buildings:** may accept refuge/main-roof refuge not meeting MOE 21.2/21.3 and/or FRC 18.2 if enhanced FSI to FSD satisfaction **and** suitable greenery. Main roof as refuge: **≥50%** of total roof area planted greenery (footnote: short grass turf suitable for foot traffic counts toward net refuge area); comply with paras 2(b)–(d).
* **Lift openings onto refuge+sky garden:** Protected lobby—doors FRP ≥ **1 hour**, walls ≥ **2 hours**; non-fireman’s lift landing doors auto-locked when fire alarm on.
* Example enhanced FSI: drencher flow > **10 L/min/m²** over external openings; fast-response sprinklers where sprinklers required.
* Live plants preferred; avoid artificial plants; highly flammable live plants (resinous/volatile oils) with caution. Maintenance/management manual required.

### 2. GFA, Site Coverage, or Design Concession Impact
* Aligns with JPN No. 1 sky garden incentives / environmental enhancement—APs must still apply JPN GFA treatment separately.
* Greenery on roof refuge supports conversion concessions under constrained envelopes.

### 3. BD Submission & Certification Procedures
* Early consultation with BA/FSD for special designs.
* Demonstrate MOE/FRC/JPN compliance and FSI enhancements where technical waivers sought.
* Ref: BD GP/LEG/6(II).

### 4. Critical Red Flags & AP Liability
* Counting planter/furniture footprint toward net refuge area.
* Combustible furniture/finishes or obstructed exits.
* Lift doors onto refuge without protected lobby / auto-lock logic.
* Relying on artificial plants for “greenery” under para 3 (≥50% live plants only).

---

## PNAP APP-123: Alternative Designs — Paragraph 12.3 of the Code of Practice for Fire Resistance Construction 1996 (FRC Code)
**Status/Context:** Re-issued August 2009; first issue October 2001. Spandrel alternatives between storeys.

### 1. Core Technical Requirements & Metrics
* FRC Code para 12.3: external wall at any floor separated from floor next below by spandrel ≥ **900 mm** high.
* Alternative: horizontal apron projected width **900 mm** where 900 mm vertical separation not practicable.
* BA prepared to **waive** para 12.3(a) for balconies **open on at least two sides** (ventilated balconies, lower fire risk). Remainder of unit must still fully comply with para 12.3 separation.

### 2. GFA, Site Coverage, or Design Concession Impact
* Facilitates continuous glazing / balcony facade designs without 900 mm spandrels; apron alternative has massing impact.

### 3. BD Submission & Certification Procedures
* Show spandrel or 900 mm apron; for open balconies document openness (≥2 sides) and compliance for remainder of unit.
* Ref: BD GP/BREG/C/19/L (VII).

### 4. Critical Red Flags & AP Liability
* Claiming balcony waiver for balconies not open on ≥2 sides.
* Ignoring separation for non-balcony remainder of the unit.

---

## PNAP APP-124: Streets for Site Classification
**Status/Context:** First issue October 2001; **this revision November 2005** (totally revamped for B(P)R 18A effective **31 December 2005**). Defines “specified street” ≥4.5 m for Class A/B/C sites.

### 1. Core Technical Requirements & Metrics
* Site class (hence permitted SC/PR) depends on number of streets ≥ **4.5 m** wide abutting site.
* Street must have street characteristics (passage/access; factors include lighting, paving, drainage). **Not** streets: public amenity open car parks, public open spaces, nullahs, sea, etc.
* Physical separation by intervening strip: abutting depends on function, status, ownership of intervening land.
* **Specified street under B(P)R 18A(3)** if any of:
  * (a) Vested in Government and maintained by HyD (public streets);
  * (b) On land under same GL as site, lease requires surrender of street land when required;
  * (c) Required to be constructed on unleased GL pursuant to lease of the site;
  * (d) Land over which site owner has express right of way exercisable at all times (instrument);
  * (e) On land held by site owner under GL (private street owned by owner)—undertaking that street remains street for lifetime, e.g. LR-registered assignment as common area;
  * (f) Parts under (a)–(e) together constituting the street; intervening non-qualifying strips split into separate specified streets.
* New specified street must be **completed before OP**; remain a street for life of buildings relying on it for SC/PR. Building over/extinguishing → BO breach; disapproval under s.16(1)(d).

### 2. GFA, Site Coverage, or Design Concession Impact
* Foundational to **maximum SC and PR** via site class. Misclassification can wrongly unlock Class B/C intensity.

### 3. BD Submission & Certification Procedures
* Substantiate with lease/land grant, HyD confirmation, ROW deed, or LR undertaking as applicable.
* Incomplete street at OP stage → refuse OP under **BO s.21(6)(a)**.
* Ref: BD GP/BORD/80 (VI).

### 4. Critical Red Flags & AP Liability
* Counting nullahs, open spaces, car parks as “streets.”
* Relying on informal access without express ROW instrument (18A(3)(a)(iv)).
* Private street without lifelong common-area undertaking (18A(3)(a)(v)).
* Subsequent extinguishment/building-over of classification street.

---

## PNAP APP-125: External Area and Floor Adjoining External Ground or Roof
**Status/Context:** Previously PNAP 266; first issue December 2001; last revision January 2005; **this revision February 2021**. Guidance on B(C)R ss.33(2), 34(2), 33(3) against ingress from external ground/roof.

### 1. Core Technical Requirements & Metrics
* Deemed-comply options for ss.33(2)/34(2):
  * Internal floor ≥ **150 mm** above adjoining external ground or roof; **or**
  * Additional drainage channels each with ≥ **2 outlets**, external surface falling ≥ **1:80** away from internal floor.
* If neither practicable: kerb with waterproof construction, total height **150 mm** above external level—case-by-case.
* External paving (s.33(3), except landscaped area): fall ≥ **1:80** to gully trap or drainage channels to surface water drain.

### 2. GFA, Site Coverage, or Design Concession Impact
* None; step/kerb details affect accessible thresholds (coordinate with BFA).

### 3. BD Submission & Certification Procedures
* Show levels, falls, channels/outlets or kerb details on GBP/drainage as appropriate.
* Ref: BD GP/BREG/C/23 (VIII).

### 4. Critical Red Flags & AP Liability
* Level flush thresholds without equivalent drainage performance → water ingress non-compliance.
* External paving without ≥1:80 fall to SW drainage.

---

## PNAP APP-126: Erection of Signboards
**Status/Context:** Previously PNAP 269; first issue May 2003; last revision September 2013; **this revision July 2021** (para 20 & Appendix N added for legal/validated signboard database). Comprehensive control of signboards as building works under BO.

### 1. Core Technical Requirements & Metrics
* **Projection over street (BO s.31(1)(aa))** permitted only if no structural danger, traffic/fire hazard, obstruction of traffic signs/signals/markings/monitoring, obstruction/reduction of MOE/MOA, obstruction reducing required L&V, or public danger.
* Must meet App A construction; **App B positional/dimensional**; FSD/TD/HyD Apps C–E; airport height controls/OZP; railway, harbour-facing illuminating, monument controls.
* **Headroom clearances (App B):** ≥**5.8 m** if within 1 m of footpath outer edge or over carriageway; over footpath ≥**3.5 m** (or ≥**2.5 m** if projects ≤600 mm); over tramway ≥**7 m**.
* Horizontal: ≥**1.5 m** from vertical line at street centreline; ≥**3 m** between opposing signboards; if projects >600 mm from wall → ≥**2.4 m** laterally from adjacent projecting signboards throughout building height; ≥**1.2 m** from common site boundary.
* **SBD setbacks (APP-152):** No signboard projecting >**600 mm** within setback area up to **15 m** above street level where building set back for SBD Guidelines.
* **Wall signboard:** Projection ≤ **600 mm**; shopfront head signboards independent of roller shutters/AC units; enclosed space not for storage.
* **Projecting signboard:** Projection ≤ **4.2 m** from external wall; contained in virtual prism: vertical planar surface area ≤ **40 m²**, horizontal width ≤ **600 mm**; for multiple in same vertical plane, aggregate planar areas ≤ **40 m²** and aggregate prism heights ≤ **20 m** (including existing).
* **Roof signboards:** ≥ **1.5 m** from inside face of parapet/curb; setback area accessible.
* Must not fix to unauthorised structures or to another signboard; **no support from cantilevered slabs**; projecting structures/balconies generally not supporting members (limited App G exception). Full wind pressure on supporting frame; overall parent-building stability check if projecting signboard area ≥ **10%** of wind exposure area of building.
* Signboard >**3 m** high on ground/roof must not create enclosed/partially enclosed floor space unless that space included in GFA & SC or occupied by machinery/ductwork.
* Wall/projecting signboards exceeding App B dimensions/projection → treated as **new building** for BO (incl. GFA & SC accountability).

### 2. GFA, Site Coverage, or Design Concession Impact
* Oversize/out-of-limit signboards accountable for **GFA and SC**.
* Enclosed floor space under tall signboards accountable unless machinery/duct exception.
* Must not consume SBD setback (APP-152) with deep projections below 15 m AGL.

### 3. BD Submission & Certification Procedures
* Unless MWCS (B(MW)R Sch.1 / APP-147) or Schedule 2 exempted works: prior approval and consent; works by RGBC.
* Fast-track: ≥11 plan sets + App I certificate + App F checklist; **30-day** processing if App G info complete; concurrent consent per ADM-19. Unconventional / non-conforming excluded (AP advised within 28 days).
* Supervision plan generally not required (unless “new building” under para 4) but AP/RSE/RGBC must assure public safety (shoring/platform against fall).
* On Form BA12/13/14 completion (from **1 Sep 2021**): provide signboard info per App N for GeoInfo database.
* Display BD reference numbers recommended (aligned with APP-147 / APP-155).
* Annual + post-typhoon maintenance inspections; issue maintenance manual (App M).
* Consider LandsD lease (esp. projection over GL)—App J; EMSD/lighting—Apps K/L; ENB external lighting guidelines.
* Refs: GR/1-125/33/0 Pt. 2.

### 4. Critical Red Flags & AP Liability
* Misrepresentation / misconduct: BA serious view; AP/RSE duties under BO s.4; sanctions ss.7 & 40.
* Common-part fixing without DMC/BMO/OC consent → civil liability.
* Supporting on cantilevers/UBs; obstructing MOE/L&V/EVA; encroaching SBD setbacks.
* Exceeding virtual prism 40 m² / 4.2 m projection without treating as new building (GFA/SC).

---

## PNAP APP-127: Contractor’s Sheds
**Status/Context:** Re-issued August 2009; first issue November 2002; revision October 2007 (para 5 & Form BA18). Permit regime under B(P)R 53 with self-certification track.

### 1. Core Technical Requirements & Metrics
* **RGBC/RSC self-certification (App A):** Single storey; storey height < **3 m**; floor area < **230 m²**; if stilted, base ≤ **1.5 m** above ground; no geotech concern (gradient across site ≤**15°**; overall gradient 10 m outside footprint <**15°**; no slope within 10 m steeper than **30°** or higher than **1.5 m**; no retaining/terrace wall >**1.5 m** within site or 10 m outside); not on cantilever or above hoarding/covered walkway; within site; not readily accessible to public.
* Otherwise: AP + RSE certification (Form BA18 Parts I & III) with structural docs comparable to B(A)R 8(1)(d)&(i); RGE geotechnical docs if geotech concern (B(A)R 8(1)(bb) standard).
* Combustible sheds: ≥ **3 m** clear of adjoining buildings or site boundary.
* No permit if shed support depends on hoarding/walkway structure or obstructs clear width of walkway.
* **Fire safety (App B):** Extinguisher 4.5 kg CO₂ or 9 L water at each entrance; multi-storey <230 m² also ≥1 open stair; single-storey >230 m² also fire-engine access within **30 m** travel; other designs case-by-case by FSD. Travel distance inside per MOE Code 1996.

### 2. GFA, Site Coverage, or Design Concession Impact
* Temporary works; not development GFA—but control-room-like misuse must not become permanent UBW.

### 3. BD Submission & Certification Procedures
* Form **BA18** + plans; BA issues permit, audits randomly.
* Renewal: original BD 108 + written confirmation certification still valid.
* Ref: BD GP/BREG/P/16 (IV).

### 4. Critical Red Flags & AP Liability
* Certifying App A eligibility when geotech/slope criteria fail.
* Combustible shed without 3 m separation.
* Relying on hoarding structure for shed support.
* Certification of structural safety despite BA audit risk—RGBC/RSC/AP/RSE remain responsible.

---

## PNAP APP-128: Geotechnical Design Information
**Status/Context:** First issue January 2003; **this revision December 2005**. Good-practice PNAP for organising geotechnical plans/reports/calculations and computer-program submissions.

### 1. Core Technical Requirements & Metrics
* Designs must maintain adequate margin of safety of works and remainder of site during construction and thereafter; must not impair stability of adjacent ground/facilities (align B(C)R 23 for foundations near features/slopes).
* Reports: executive summary; schedule of geotechnical design assumptions/parameters with justifications (GI, lab, GWL monitoring).
* Incorporate design-review provisions during construction (link performance review—then PNAP 246 / APP-115).
* Computer analyses (pre-accepted programs—then PNAP 79): name/version/developer/BD ref/validity; accepted scope & limitations; model justifications; assumptions/parameters; input from ground conditions; salient outputs (FoS, envelopes, displacements); interpretation for design. RGE completes App A proforma.

### 2. GFA, Site Coverage, or Design Concession Impact
* None directly; early geotechnical assessment (B(A)R 8(1)(ba) / then PNAP 78) protects development feasibility affecting buildable SC/PR massing.

### 3. BD Submission & Certification Procedures
* Geotech feasibility at GBP stage where assessment criteria met.
* Site formation: B(A)R 8(1)(bb); ELS: 8(1)(bc) & related PNAPs; Scheduled Areas: then PNAPs 85, 161; Northshore Lantau: then PNAP 283.
* Differentiate proposed vs existing works (B(A)R 14); avoid common deficiencies listed (survey, rainfall precautions, sequence, plan/report discrepancies).
* Refs: BD GR/OA/71/1; GP/BORD/75.

### 4. Critical Red Flags & AP Liability
* Unjustified soil/groundwater parameters; missing executive summary / assumption schedule.
* Computer output without validation scope/limitations/BD programme acceptance.
* Demolition of buildings supporting ground without adjacent stability provisions; debris stockpiling near features.

---

## PNAP APP-129: Use of Recycled Aggregates in Concrete for Minor Structures and Non-structural Works
**Status/Context:** Previously PNAP 275; first issue February 2003; **this revision February 2022**. Technical guidelines for C20–C35 concrete with recycled coarse aggregates.

### 1. Core Technical Requirements & Metrics
* **C20 with 100% recycled coarse aggregate (App A):** Minor/non-structural only (on-grade slabs, blinding, U-channels, pipe bedding/haunching, fence post footings, mass fill without appreciable load). Mix per 100 kg OPC : 180 kg fine : 180 kg 20 mm : 90 kg 10 mm. Slump **75 mm**; cube **14 MPa / 20 MPa** at 7/28 days; lab trials each of 3 cubes ≥ **26 MPa** at 28 days. Fine aggregate: grading M CS3—**no recycled fines**. Aggregate Table 1: dry density ≥**2000 kg/m³**; water absorption ≤**10%**; wood/light material ≤**0.5%**; foreign materials ≤**1%**; fines ≤**4%**; sand <4 mm ≤**5%**; sulphate ≤**1%**; flakiness ≤**40%**; 10% fines **100 kN**; chloride per CS3 5.2.3 (**0.05%**); wet thoroughly before use.
* **C25–C35 with max 20% recycled coarse (App B):** Landscape RC features, fence/mass walls & footings for landscape, stormwater manholes/sand traps, footways, cycle tracks, RC infill walls, mass concrete under footings/rafts. OPC only (BS EN 197-1); 80% natural coarse; weekly source tests; separate storage/compartment; min slump 75 mm; lab + plant trials (Annex criteria). Same recycled aggregate Table 1 limits.
* **Not permitted:** Liquid-retaining, prestressed, transfer, or hanger structures.
* Precast paving units: follow HyD Guidance Notes / particular specifications.
* Concrete Code 2013 QC generally applies.

### 2. GFA, Site Coverage, or Design Concession Impact
* None.

### 3. BD Submission & Certification Procedures
* State recycled aggregate use on structural general notes and Part I structural calculations (**PNAP ADM-8**); affirm compliance with Apps A/B; show scope on relevant structural plans. Other concrete structure rules still apply.
* Ref: BD GP/BREG/RC/4(V).

### 4. Critical Red Flags & AP Liability
* Using 100% recycled C20 in structural members.
* Using recycled fines; or 20% mix in transfers/prestressed/liquid-retaining.
* Omitting plan statements / trial compliance documentation.

---

## PNAP APP-130: Lighting and Ventilation Requirements – Performance-based Approach
**Status/Context:** First issue December 2003; last revision February 2015; **this revision December 2016** (App A para 6 amended). Accepts alternative performance standards to B(P)R regs **30, 31, 32** for natural lighting and ventilation in habitable rooms and domestic kitchens.  
**Note for practitioners:** This APP-130 is **not** the Sustainable Building Design Guidelines document. Building separation / street setbacks / greenery SBD content is in **PNAP APP-152** (cross-referenced from APP-126 App B para 9). Summarise only what this extracted APP-130 contains.

### 1. Core Technical Requirements & Metrics
* **Performance standards (para 1):**
  * Natural lighting — Vertical Daylight Factor (VDF) at centre of window pane: Habitable room **8%**; Kitchen **4%**.
  * Natural ventilation — Habitable room **1.5 ACH** (natural); Kitchen **1.5 ACH natural + 5 ACH mechanical**.
* **Simplified method (App A) “deemed to meet”** if windows pass UVA lighting tests (Part II) and ventilation rules (Part III).
* **UVA method key rules:**
  * Cone of **100°** centred normal to glazing (50° each side); max cone length = **height of facade** (window head of lowermost storey with window → main roof parapet top).
  * Measure UVA to lot boundary, or include full street width if abutting street; sector beyond common boundary/street centreline may use **×4** multiplying factor capped so as not to exceed UVA measurable to facade height.
  * Adjacent same-site obstruction: if vertical obstruction ≤ **30°**, area above that structure within cone countable.
  * Window only counts if: faces uncovered space not bounded opposite by building obstruction; window top ≥ **2 m** above floor; glass area (effective glazing) ≥ **10%** of room floor area.
  * **Table 1 (habitable, 8% VDF) & Table 2 (kitchen, 4% VDF):** minimum UVA (m²) vs facade height for glazing ratios 10% / 15% / 20% of floor area (examples: habitable @10 m facade → 50 / 30 / 20 m² UVA; @100 m → 2,400 / 1,800 / 1,300 m²; kitchen @10 m → 20 / 15 / 10 m²). Interpolate between 10–15–20% glazing and intermediate facade heights; glazing >20% still uses 20% column.
* **Ventilation (simple):** Primary openings ≥ **1/16** of floor area facing open-air-compliant clear area; kitchen also needs **5 ACH** mechanical.
* **Cross ventilation relaxation:** Primary ≥ **2%** floor area; secondary ≥ **2%** in rear half on different plane facing open air; room depth from primary may extend to max **12 m** (relaxes reg 32 depth restriction).
* For B(P)R 31(2), base may be measured at angle ≤ **15°** from external wall.
* Hybrid: project may mix prescriptive regs and performance standards.
* APs may use validated lighting simulation / CFD instead of simplified method (Apps B & C validation notes).

### 2. GFA, Site Coverage, or Design Concession Impact
* No direct GFA concession; enables tighter site massing / deeper rooms / reduced prescribed window facing where VDF/ACH / UVA or simulation proven.
* **Wholesale conversion to office (para 6):** Favourable modification of regs 30 & 31 if adequate artificial lighting + mechanical ventilation **and** energy-efficient design achieving **40%** in BEAM Plus **EU** and **IEQ** categories (HKGBC).

### 3. BD Submission & Certification Procedures
* Apply for modification of B(P)R 30/31/32 when using performance path; prove UVA tables or validated simulation/CFD.
* Wholesale IB conversion path—on plan approval application: HKGBC letter acknowledging project registration + undertaking to submit: (a) BEAM Plus Provisional Assessment showing 40% EU & IEQ **before consent**; (b) Final Assessment showing 40% EU & IEQ within **6 months** of BA acknowledgement of Form BA14.
* Refs: BD GP/BREG/P/42; P/18/1(E)(VII); P/18/1(G)(II).

### 4. Critical Red Flags & AP Liability
* Counting windows that fail 2 m head / 10% glass / open-air facing tests toward UVA.
* Wrong facade height definition (must to main roof parapet, not intermediate).
* Applying ×4 boundary sector without capping to facade-height cone.
* Claiming cross-ventilation relaxation without true secondary openings on different plane in rear half.
* Wholesale conversion without BEAM Plus registration/undertaking milestones → modification/consent risk.
* Do not confuse this PNAP with **APP-152** SBD (building separation, 15 m setbacks, greenery)—those metrics are not in this file.

---

## Completed APP Number List (this batch)

**101, 104, 105, 106, 107, 108, 109, 110, 111, 112, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130**

**Skipped (not present in `_extracted_txt`):** 102, 103, 113


<!-- Source: batch_06_APP132-155.md -->

# PNAP Summaries — Batch 06 (APP-132 to APP-155)

Source: `PNAP_APPb_e/_extracted_txt` (APP132.md–APP155.md). All files in range exist; none skipped. Summaries are drawn only from the extracted PNAP text; no invented clauses.

---

## PNAP APP-132: Site Coverage and Open Space Provision
**Status/Context:** Flexibility under B(P)R Regs 20 and 25 for innovative design. Formerly PNAP 280; this revision December 2012 (paras. 2–4 & 7 amended; paras. 5–6 added). Site coverage concessions subject to APP-151 GFA-concession pre-requisites. Town-plan site coverage controls and lease modification (Lands D PN 1/2004) still apply.

### 1. Core Technical Requirements & Metrics
* **Legal basis:** BA may modify B(P)R Regs 20 and 25 case-by-case.
* **Set Back Approach (para. 3):** Criteria (a)–(f) must all be met:
  * Setback area ≥ **8%** of site area (non-domestic); ≥ **18%** (domestic). Composite: apply 8%/18% to respective portions.
  * Length ≥ half of frontage and ≥ **10 m**, or full frontage if frontage < 10 m.
  * Satisfactory control/maintenance of setback, flat roofs, covered areas.
  * Setback properly landscaped and/or paved; open, uncovered; no permanent building structures other than landscaped features and perforated boundary walls.
  * Improves street environment.
  * Excludes areas dedicated/surrendered for public passage under Reg 22.
* **If criteria met – SC by height:** Appendices A (domestic) and B (non-domestic) tables apply. Total covered area (footprint including JPN1/2 SC-exempt features; excluding APP-19 projections) must not exceed **63%** (domestic) or **80%** of site area or Appendix B percentage, whichever greater (non-domestic).
* **Excludable from SC assessment at a level (para. 4):** (a) unexcavated/backfilled area under footprint on sloping site; (b) open-sided covered areas of non-domestic buildings as green features under JPN1/2, as common areas, accessible to all occupants, no commercial activities.
* **Open Space Approach (para. 5):** Volume of un-built open space ≥ viable notional scheme; GFA ≤ notional scheme; max SC any level: domestic / domestic part **63%**; non-domestic / non-domestic part **92%** ≤24 m from street, **80%** >24 m. Innovative design required (full max SC on every floor may not qualify). Un-built volume measured from mean level of lowest abutting street to mean roof height over highest usable floor of the notional scheme.
* **Appendix A key SC% (domestic, from street level):** ≤24 m → 63%; 25→62 … decreasing to over 61 m → 40%.
* **Appendix B key SC% (non-domestic):** ≤24 m → 92%; decreasing to over 61 m → 65%.

### 2. GFA, Site Coverage, or Design Concession Impact
* SC concessions under paras. 3–5 are subject to **same pre-requisites as GFA concessions in APP-151**.
* Total covered area / open-space volume controls interact with Regs 20/25 modification; statutory OZP SC must still be observed.

### 3. BD Submission & Certification Procedures
* Case-by-case modification applications demonstrating setback or open-space criteria and (for open-space approach) viable notional scheme compliant with BO/regulations and OZP.
* Lease modification via Lands D procedures if needed; premium may be payable.

### 4. Critical Red Flags & AP Liability
* Missing APP-151 pre-requisites → SC concessions not available.
* Setback counting dedicated public passage (Reg 22) invalidates criterion (f).
* Assuming every-floor maximum SC qualifies as “innovative” without design merit.
* Ignoring OZP SC controls or lease modification / premium implications.

---

## PNAP APP-133: Cast Iron Pipes for Drainage Works
**Status/Context:** Formerly PNAP 282; guidelines on quality of cast iron (C.I.) drainage pipes. First issue November 2003. Mandatory for drainage plan approvals after **1 November 2004**.

### 1. Core Technical Requirements & Metrics
* Pipes/fittings per relevant BS or equivalent (e.g. BS 416:Part 1 or BS EN877 above-ground; BS 437 or BS 4622 underground / >150 mm above-ground).
* Suitable internal and external anti-corrosion coating; cold-applied bitumen-based coatings to BS 3416 or equivalent; external coating with anti-corrosion inhibitors.
* Pipes in a state permitting additional external finishing coatings.
* Corrosion-resistant fixings (e.g. stainless steel brackets); properly anchored into solid wall.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not applicable (materials/drainage specification).

### 3. BD Submission & Certification Procedures
* BA requires compliance under **BO s.28(1)** for drainage plan approvals after 1 Nov 2004.
* C.I. pipes to be included in Schedule of Building Materials and Products under PNAP 53 (APP materials schedule) at OP application.

### 4. Critical Red Flags & AP Liability
* Specifying uncoated/inadequately coated C.I. or non-corrosion-resistant fixings.
* Omitting C.I. pipes from materials schedule at OP.

---

## PNAP APP-134: Development in the Designated Area of Northshore Lantau
**Status/Context:** Formerly PNAP 283; complex geology (metasedimentary rocks/cavities, soft deposits, deep/steep rockhead). First issue January 2004; revision February 2006 (RGE added). Boundary plan in Civil Engineering Library GIU / Appendix A; GEO TGN No. 12.

### 1. Core Technical Requirements & Metrics
* GI preferably in stages; adequacy to assess effects on development; some deep drillholes required; early GI before finalising GBPs advised (layout adjustment may be most economical).
* Foundation plan submissions in Designated Area must include: (i) explanatory guide; (ii) GI report with equipment/procedures; (iii) critical examination/interpretation, design assumptions schedule, anticipated problems, geotechnical requirements for design/construction/testing/inspection/maintenance; (iv) foundation design calculations.
* Guidance: PNAP 66, Code of Practice for Foundations; GEO Publication 1/96; Guide to Site Investigation.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not a GFA PNAP; geological risk may force layout change / abandonment affecting bulk/GFA realisation.

### 3. BD Submission & Certification Procedures
* Follow Code of Practice for Site Supervision for GI supervision.
* Strongly encouraged to seek CGE/Mainland West (GEO) advice on GI proposals before commencement.
* AP/RSE/RGE supervise foundations per Supervision Code.

### 4. Critical Red Flags & AP Liability
* Inadequate staged deep GI before locking layout → costly/abandoned towers (historical precedent cited).
* Incomplete foundation submission package for Designated Area.

---

## PNAP APP-135: Quality Supervision of Soil Nailing Works
**Status/Context:** Formerly PNAP 284; supervision, testing, certification of soil nails. First issue October 2003; revision February 2006 (RGE; NDT; paras 7–18/apps deleted; new para. 7).

### 1. Core Technical Requirements & Metrics
* Buildability: nails >**20 m** increase risk of collapse, high grout loss, poor grout quality; adverse ground may require RGE buildability assessment and site trial (include pull-out where possible) before working nails.
* Difficult ground examples: loose fill/colluvium, rockfill, soil pipes, buried streams, open discontinuities, alternating soil/rock, groundwater flow.
* Site formation submission must include: site trial details/locations (if required); pull-out test procedures; NDT methodology for verifying installed nail length with provisions to allow testing.
* Reference: CEDD LPM specs/drawings; GEO Report 133 (NDT of steel soil nail lengths).

### 2. GFA, Site Coverage, or Design Concession Impact
* Not applicable.

### 3. BD Submission & Certification Procedures
* RGE includes trial/pull-out/NDT particulars in site formation approval package.
* Quality supervision, TCP qualifications, NDT details: Technical Memorandum for Supervision Plans and Code of Practice for Site Supervision.

### 4. Critical Red Flags & AP Liability
* Installing working nails before trial/pull-out where long nails or adverse ground exist.
* Inadequate NDT provisions built into design for length verification.

---

## PNAP APP-136: Building (Planning) Regulation 41D — Emergency Vehicular Access
**Status/Context:** Formerly PNAP 288; EVA for new buildings from B(P)R 41D (effective 31 Dec 2004). First issue May 2005; revision July 2006. Design standards in Part VI of MOA Code.

### 1. Core Technical Requirements & Metrics
* Application: does not apply to works underway or consented before 31 Dec 2004 (foundation often the relevant consent).
* EVA meeting MOA Code = compliance with B(P)R 41D.
* Major façade measurement (para. 6): simple contours use actual perimeter length for one-fourth major façade; complex contours may use notional building contour line (Appendix A).
* Projections accepted by BA **excluding** balconies/UPs under JPN1/2 disregarded for façade length calculation.
* Exemption grounds (41D(3)): impracticable due to topography; or low fire risk by use.
* Appendix B relaxation examples (fire-safety report generally **not** required for these items): dead-end reverse ≤30 m; run-in width ≥4.5 m; horizontal distance 10–30 m with FSI enhancement (e.g. hose reel); >30 m for ≤3-storey domestic/family with FSI (e.g. sprinkler); Class A/B/C redevelopment road width ≥4.5 m; Class A major façade min. = side-boundary distance within 10 m of EVA.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not a GFA/SC concession PNAP; EVA layout affects site planning and major façade geometry.

### 3. BD Submission & Certification Procedures
* Separate EVA plan on GBP with: extent/alignment (coloured); width, turning radii, loading, gradient; signage/crash gates; clear headroom section if overhead; block plan of major façade; façade length % calculation; non-hard paving if any.
* Public street EVA: items 4(a)(b)(e)(f) only; loading capacity not required for public street portion.
* Non-compliant / no EVA: Form BA16 exemption + justification; fire-safety report per MOA Code para. 27.2 where appropriate; BA consults DFS.

### 4. Critical Red Flags & AP Liability
* Incomplete EVA plan / wrong façade % (counting JPN balconies/UPs).
* Relying on Appendix B relaxations without case-specific FSI enhancements when required.
* Consent more than 2 years after plan approval risk under BO s.16(3)(d) context for related works.

---

## PNAP APP-137: Ground-borne Vibration and Ground Settlement arising from Pile Foundation and Excavation and Lateral Support Works
**Status/Context:** Formerly PNAP 289; vibration/settlement control for pile installation & ELS. Latest revision November 2024 (general revision). Cross-refs Foundation Code 2017 cl.7.2; APP-18; APP-24 railway/settlement engineering approach.

### 1. Core Technical Requirements & Metrics
* Plan submissions should address Foundation Code monitoring/assessment; BA may require: pre-construction condition survey (photos); preliminary vibration & settlement assessment; control limits + monitoring proposal; detailed assessment if limits > Appendix A (refs BS ISO 4866, CIRIA TN142); trial piles near vulnerable receptors.
* Percussive/vibratory piles near vibration-sensitive receptors (Foundation Code 7.2.6) normally not accepted without trial piles; precautionary shoring may be needed before trials.
* ELS with temporary pile walls: same 3(a)–(d) monitoring proposal; trial piles if nearby vulnerable receptors.
* Test/trial monitoring: max **ppv** recorded every metre of penetration, at final set, and at obstructions; three orthogonal axes at ground level of receptors.
* Enhanced **5A** trigger system (Appendix A empirical, if no sensitive receptors):

| Criterion | Alert | Alarm | Action L1 | Action L2 | Action L3 |
|-----------|-------|-------|-----------|-----------|-----------|
| Ground settlement | 12 mm | 18 mm | 20 mm | 22 mm | 25 mm |
| Services settlement / angular distortion | 12 mm or 1:600 | 18 mm or 1:450 | 20 mm or 1:400 | 22 mm or 1:350 | 25 mm or 1:300 |
| Building tilting (angular distortion) | 1:1000 | 1:750 | 1:600 | 1:550 | 1:500 |

* **ppv guide (mm/s)** — robust buildings: transient Alert/Alarm/A1/A2/A3 = 9/12/13/14/15; continuous 4.5/6/6.5/7/7.5. Vibration-sensitive/dilapidated: half of those (transient 4.5…7.5; continuous 1.8…3).
* Action Level 3 also if: 5 mm increase between consecutive daily readings; or distress/damage observed.
* Site-specific engineering limits via APP-24 Appendix C need owner/authority acceptance before BA plan approval.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not applicable.

### 3. BD Submission & Certification Procedures
* Include assessment/monitoring/trial pile proposals with foundation/ELS/site formation plans.
* Before works: RSE confirm method, concurrent pile numbers, plant; re-assess if amended; PR Plan advised (Foundation Code 7.2.7).
* Trial pile reports (2 sets; 1 set if ESH) to BA before consent for working piles; post-trial condition survey.
* Exceedance → stop works; review precautionary measures; resume only after BA-satisfactory review.

### 4. Critical Red Flags & AP Liability
* BO duty: works must not impair stability or damage buildings/structures/land/services.
* Adopting >Appendix A vibration limits without rigorous assessment / cumulative pile effects.
* Continuing works after ppv/settlement exceedance or observed damage.
* Railway protection area: APP-24 Appendix B vibration controls.

---

## PNAP APP-138: Appointment of Authorised Signatory to Act for Registered Contractor and Temporary absence of Authorised Signatories
**Status/Context:** Formerly PNAP 290; AS duties for RGBC/RSC. First issue May 2004. Cross-refs PNRC 38, PNRC 59.

### 1. Core Technical Requirements & Metrics
* One AS only accepted per project for the RC; AS signing Form BA10 is deemed the responsible AS.
* Forms BA 7, 10, 11, 12, 13, 14, 14A, 18, 20 — signing AS is responsible for RC BO duties.
* From **1 July 2004**, AS name must appear on specified forms or form incomplete/unacceptable.
* Change of AS (multi-AS RC): notify BA on PNRC 59 App A, AP countersign, ≥**7 days** before change.
* Temporary AS: App B to PNRC 59; ≥7 days notice (or 3 days documentary proof for sudden illness/accident); nominee = another AS of same RC on same register/sub-register, or AS of another RC with authorisation; max **14 days** acting, total max **30 days** with special proof.
* Temporary AS may sign inspection records only — **not** supervision plans or specified forms.
* Absence >30 days → formal AS change or add AS to registration.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not applicable.

### 3. BD Submission & Certification Procedures
* AS name on all forms and matching supervision plan; change/nomination notifications as above.
* Single-AS firm (not sole prop): cannot change project AS without adding new AS via PNRC 38 first.

### 4. Critical Red Flags & AP Liability
* Mismatched AS on supervision plan vs BA10/13/14 → rejection.
* Temporary AS signing forms/plans → invalid.
* Works continuing with no AS acting → B(A)R 22(2) cessation obligation.

---

## PNAP APP-139: Code of Practice on Wind Effects in Hong Kong
**Status/Context:** Implements Wind Effects Code 2019 (+ Dec 2023 amendments to Code and Explanatory Notes). Revision December 2023. Grace for 2004 Code ended **31 March 2021**.

### 1. Core Technical Requirements & Metrics
* After 31 Mar 2021: only 2019 Code accepted for new foundation/superstructure submissions (unless earlier approval used same Code for subsequent related submissions including loading allowance for future structures).
* A&A after grace period: APP-117 for new elements / existing adequacy.
* Wind tunnel: Section 6 of 2019 Code; if not per Code, methodology proposal to BD (normally determine within **45 days**); pre-submission enquiry ADM-19; Appendices C & D list essential methodology and QA plan contents.
* Witness: RSE or independent engineer (HKIE Corporate or equivalent, ≥**5 years** relevant experience); not staff/employee of tunnel lab.
* Report must include procedures, full readings, structural/dynamic properties, RSE statement on supervision and raw data/results meeting 2019 Code.
* Dec 2023 amendments among others: wind tunnel trigger figures; size factor; EN cl.2.2.3 multi-tower-over-podium fundamental frequency assumptions; hoarding/covered walkway design net pressures (≤2.5 m → 0.63 kPa; 5 m → 0.70; 10 m → 0.77); shelter benefit limited to 80% of Standard Method base moments if no building-removal investigation.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not a GFA PNAP; wind loading drives structural form and cladding pressures.

### 3. BD Submission & Certification Procedures
* Foundation/superstructure to 2019 Code after grace expiry.
* Wind tunnel methodology + QA plan before/with structural submissions as applicable; RSE-certified tunnel report for structural incorporation.
* BO s.16(3)(d): consent refusal if >2 years since plan approval.

### 4. Critical Red Flags & AP Liability
* Using 2004 Code after grace without grandfathered approved package.
* Tunnel test without accepted methodology deviation / inadequate QA / unsupervised lab run.
* Independent witness who is lab staff.

---

## PNAP APP-140: Registration of Authorized Persons and Registered Structural Engineers as Registered Geotechnical Engineers
**Status/Context:** Formerly transitional path (BO Amendment Ordinance 2004) for AP (engineers list)/RSE to register as RGE by **30 December 2005**. First issue December 2004. Read with PNAP 43.

### 1. Core Technical Requirements & Metrics
* Window: within 12 months from RGE register commencement **31 Dec 2004**.
* Conditions: within 7 years preceding application — engaged in/took part in site formation works completed under BO; was the AP or RSE for those works; satisfies BA of appropriate geotechnical experience/competence (detailed project engagement from plan prep through completion; AP certifies / RSE reports to certifying AP; no BO contravention record).
* RGE registration valid **5 years**, renewable while remaining on AP/RSE register.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not applicable (registration).

### 3. BD Submission & Certification Procedures
* Application with justifying information/documents as BA may require under BO s.53I transitional provisions.

### 4. Critical Red Flags & AP Liability
* Historical transitional note only — current RGE registration follows prevailing BO routes (not this window).

---

## PNAP APP-141: Division of Responsibilities between Authorized Person, Registered Structural Engineer and Registered Geotechnical Engineer
**Status/Context:** Implements RGE appointment from **31 Dec 2005** (BO s.4(1)(c)). Formerly PNAP 294; this revision February 2009. Cross-refs APP/PNAP geo series (50, 75, 77, 83, 85, 132, 148, 161, 200, 283, 284). Sanctions: BO ss.40 & 7.

### 1. Core Technical Requirements & Metrics
* **RGE executive role** (prepare/sign geo plans & reports; certify geo works completed per approved plans & geotechnically safe): Task 2A GI Scheduled Areas; 2B GI Non-scheduled; 4 Site Formation; 7A Groundwater drainage Scheduled Area 1; 7B Water supply & wells; 10 Remedial works to dangerous hillsides; 11 Long-term monitoring post-OP.
* **RGE advisory role** (sign geo reports/docs; AP/RSE sign non-geo plans): Task 1 Demolition affecting slopes/RWs; 3 Geo assessment for GBP; 5A Foundations in Scheduled Areas 1,2,4 & Northshore Lantau Designated Area; 5B Foundations affecting slopes/RWs; 6 ELS; 8 Superstructure geo design parameters; 12 Hoardings/covered walkways/gantries affecting nearby slopes/RWs.
* Key sign-off patterns (Appendix B examples): Demolition — AP+RSE plans, RGE geo reports, RGE geo supervision, AP+RSE certify; Site formation — AP general layout, RGE site formation (non-structural), RSE structural details, AP+RGE (+RSE if structural) certify; Foundation in geo-sensitive areas — RSE plans, RGE geo reports/performance review, shared supervision; ELS — RSE plans incorporating RGE recommendations, RGE geo reports.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not applicable (responsibility matrix).

### 3. BD Submission & Certification Procedures
* Prescribed plans/documents per B(A)R 12; resolve RSE–RGE differences **before** BD submission.
* Performance reviews / monitoring reports for specified works prepared/signed by RGE.

### 4. Critical Red Flags & AP Liability
* AP remaining “statutorily responsible” for geo elements after RGE regime — incorrect after 31 Dec 2005.
* Submitting plans with unresolved RSE/RGE conflicts or missing RGE signatures on geo docs.
* Prosecutions/disciplinary action expose RGE similarly to AP/RSE.

---

## PNAP APP-142: Code of Practice for Structural Use of Concrete 2013
**Status/Context:** Promulgates amendments to Concrete Code 2013 (2020 Edition) via Appendices A (Feb 2022), B (Jun 2023), C (Apr 2024). Latest PNAP revision April 2024. Full technical text is in the Code amendments on BD website; this PNAP is the amendment vehicle.

### 1. Core Technical Requirements & Metrics
* **Feb 2022 (key):** New cl.6.2.3 plain concrete linings (tunnels/caverns) with interaction curve Fig.6.18b; for ec≤0.1h: nLT ≤ 0.32 h fcu; for 0.1h < ec ≤ 0.3h: nLT ≤ 0.4(h−2ec)fcu; max ecc. 0.3h; shear per Code clauses cited. Cube tests: **100 mm** cubes default; **150 mm** if max aggregate >20 mm. Maturity method guidelines Table 11.2 / ASTM C1074.
* Subsequent Appendices B & C incorporate further TC-agreed Code updates (June 2023 / April 2024) — APs/RSEs must use consolidated Code on BD website.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not applicable (structural Code).

### 3. BD Submission & Certification Procedures
* Structural submissions to current Concrete Code 2013 (2020 Edition) as amended.
* QC testing/maturity monitoring per amended clauses during construction.

### 4. Critical Red Flags & AP Liability
* Designing plain concrete linings outside compression/rock criteria or beyond 0.3h eccentricity.
* Wrong cube size relative to aggregate; ignoring maturity-method correction factors.

---

## PNAP APP-143: Quality Control and Supervision of Precast Concrete Construction
**Status/Context:** Formerly PNAP 299; QA/supervision/audit for key precast elements (excludes minor non-structural blocks, architectural features, planters). Latest text in extracted file references Precast Concrete Code 2016 and Supervision Code 2009 (2021 Edition). Cross-ref APP-158 for QCS frequency baseline for in-situ RC.

### 1. Core Technical Requirements & Metrics
* Factory **ISO 9001** QA certification required (BO s.17(1) item 6 condition).
* QAS to cover: material QC tests; lab equipment calibration; casting yard equipment; production process; testing procedures; inspection frequency/extent (in-house + independent HKAS certification/inspection bodies); audit frequency/extent.
* RSE QCS ≥ **T3** TCP (RSE stream); frequency ≥ **once/week**.
* RC QCC ≥ **T1** TCP (RC stream); continuous factory supervision.
* Quality audits: first visit by RSE and AS in person for first batch; thereafter ≥ monthly (quarterly in-person; intervening months may use videotelephony ≥480p colour on non-rewritable DVD-ROM).
* Alternative: RSE first factory visit then on-site audits of delivered elements (1-month prior written notice to BA).
* Separate RSE allowed for precast not affecting parent stability (façade/stair); Forms BA4/BA5; project RSE written acknowledgment; separate RSE certifies under B(A)R 25(3).

### 2. GFA, Site Coverage, or Design Concession Impact
* Not a GFA PNAP; MiC/precast interfaces with JPN8 (see APP-151 list item 38) are separate.

### 3. BD Submission & Certification Procedures
* QAS + RSE confirmation ≥**14 days** before factory production start.
* Precast Concrete Supervision Plan ≥14 days before production.
* Quality audit reports to BD within **14 days** of each audit (incl. first visit); DVD if videotelephony.
* Separate RSE: assessment report on parent structure effects + project RSE statement on connections.

### 4. Critical Red Flags & AP Liability
* Production before QAS/supervision plan submission and ISO9001 factory confirmation.
* AS/RSE skipping audits or inadequate videotelephony records.
* Demarcation gaps between project RSE and separate RSE on connections pre-installed in parent structure.

---

## PNAP APP-144: Design and Construction of Run-in and Run-out on Public Road
**Status/Context:** Formerly PNAP 300; HyD standards + self-certification. Effective **1 January 2007**. First issue September 2006.

### 1. Core Technical Requirements & Metrics
* Match adjoining footpath: concrete with concrete; pavers with pavers + visual contrast/pattern change.
* HyD Standard Drawings / GS (Sections 9–11 etc.); concrete: H1113–H1116; pavers: H1103, H5101–2, H5114–H5116.
* Saw-cut method required; damage outside run-in needs separate HyD Excavation Permit + reinstatement.
* Protect utilities: HyD TC 3/90 (or update) minimum cover.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not applicable.

### 3. BD Submission & Certification Procedures
* Design details on GBP for HyD circulation; early utility diversion + Excavation Permit.
* Before OP (encouraged early): Certificate of Completion of Vehicular Run-in and Run-out (App B) — AP Part A + RC Part B; c.c. HyD with block plan.
* BD notifies HyD for inspection/takeover; defects may ground OP refusal under **BO s.21(6)(a)**.
* HyD-entrusted works: entrustment letter + fee receipt; temporary run-in may allow OP processing before permanent works complete.

### 4. Critical Red Flags & AP Liability
* Incomplete/defective run-in at OP → HyD objection → OP refusal.
* Damaging adjoining pavement without separate excavation permit.

---

## PNAP APP-145: Fire Safety (Buildings) Ordinance, Cap. 572
**Status/Context:** Formerly PNAP 302; FS(B)O in force **1 July 2007**. Revision October 2010 (Advisory Committee). Enforcement: BD (fire safety construction); FSD (FSI/equipment).

### 1. Core Technical Requirements & Metrics
* Target buildings: composite or domestic (>3 storeys if wholly domestic) with plans first submitted ≤**1 Mar 1987** or constructed ≤ that date without plans; excludes Cap.121 NT buildings; domestic excludes hotel/guesthouse/elderly home/child care/nursery for “domestic purposes” definition; composite excludes wholly factory/industrial/godown/warehouse/bulk storage as non-domestic part.
* Fire safety construction Schedules 1 (non-domestic parts of composite) & 2 (domestic/domestic parts); Codes: MOE 1996, FRC 1996, MOA 1995 (for FS(B)O upgrading).
* FSI examples: sprinklers; MV auto cut-off; emergency lighting; manual alarms; FH/HR; COP Minimum FSI 1994.

### 2. GFA, Site Coverage, or Design Concession Impact
* Improvement works pursuant to FSDn: no B(A)R 42 fee if entirely for FSDn compliance.

### 3. BD Submission & Certification Procedures
* Fire Safety Directions (ss.5(1)/(2)); Fire Safety Compliance Orders after conviction (s.6).
* ACFSO advises on alternatives (s.5(10)); structural integrity / technology constraints; fire engineering alternatives to primary objectives.
* Voluntary / FSDn A&A: usual BO approval; **three** sets of FSI plans for FSD (vs normal two).

### 4. Critical Red Flags & AP Liability
* Applying Cap.572 codes to Cap.121 village houses incorrectly.
* Ignoring ACFSO path where structural/tech constraints make Schedule items unreasonable.
* Under-providing FSI plan sets to FSD.

---

## PNAP APP-146: Metal Gates
**Status/Context:** Formerly PNAP 304; design/installation/maintenance of fence-wall/entrance metal gates. Latest revision March 2025 (welding NDT, anchors, Appendices A/B).

### 1. Core Technical Requirements & Metrics
* New buildings: show on plans for approval/consent. Height >**3.2 m**: structural details + calculations for approval. Existing buildings: if >3.2 m, building + structural plans before install. MWCS may apply for certain existing installations (APP-147 / B(MW)R Sch.1).
* Performance: B(C)R s.3; recognised standards; solid construction for intended life.
* Structural submission focus: wind Code; framework/posts/foundation; connection to supporting structure; swing hinges; sliding end stoppers & multi-pass connections; guides against lift-off/derailment.
* Swing gates: ≥3 hinges/post; if >3.2 m, stainless hinges ≤**1000 mm** c/c and ≤**300 mm** from top/bottom; anti-lift hinge orientation.
* Sliding: ≥2 pairs guiding wheels, min spacing **1000 mm**; ≥1 leaf stopper + additional stopper(s) on ground/column/wall; rubber cushion; derailment safeguards.
* Drilled-in anchors: ≥**5** of each type/size pull-out tested to APP-169 App B; capacity ≥**1.5×** manufacturer recommended tensile; pass = no separation/plastic/deleterious effect.
* NDT all welded joints at supports and mechanical end stoppers; HOKLAS/mutual-recognition labs; direction by AP/RSE (approved) or PBP (Class I MW) or RGBC/RMWC (Class II/III without PBP).
* Electrically operated: EMSD COP Sliding Gates/Glass Doors/Rolling Shutters.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not applicable.

### 3. BD Submission & Certification Procedures
* Prior approval/consent or MWCS simplified path as applicable.
* Qualified supervision by RGBC/RMWC; inspect and trial-operate on completion.
* Anchor/weld tests directed and documented as above.

### 4. Critical Red Flags & AP Liability
* Large gates without structural approval; missing end stoppers / anti-derailment.
* Skipping HOKLAS pull-out/weld tests; unprotected hinge welds preventing inspection.
* Maintenance: defects on hinges/wheels/track/steel → owner/IO documentation every **3 months** routine check recommended.

---

## PNAP APP-147: Minor Works Control System
**Status/Context:** MWCS simplified procedures without prior BA approval/consent. First issue Dec 2010; this revision Sep 2021. **187** minor works items: Class I 58, Class II 68, Class III 61 (B(MW)R Sch.1). Free of charge submissions. No referral to other departments (except Area No.3 railway-adjacent footing/excavation/drainage → BD forwards to MTRCL).

### 1. Core Technical Requirements & Metrics
* Class I: PBP (AP + RSE/RGE/RI as required) design/supervise + PRC carry out; notice of commencement + completion certificate.
* Class II: PRC prepares/submits/plans/supervises/carries out; notice + completion.
* Class III: PRC; combined notice and certificate of completion.
* Plans scales: ratio ≥1:100 for plan/section; block plan ≥1:500.
* Signboards: display MW submission numbers (App D); black on white; letters/digits ≥**35 mm** Arial; yellow background for alteration of previously unauthorised signboards.
* Validation schemes: HMWVS (pre-31 Dec 2010 PBW in Sch.3 Part 2); MAFVS (from 1 Sep 2021 — 21 amenity feature types pre-1 Sep 2020 designation, Sch.3 Part 4); Signboard Validation → APP-155.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not a GFA-concession PNAP; validates certain unauthorised amenity features (enforcement deferred if certified safe/compliant except BO s.14(1) & B(A)R 25).

### 3. BD Submission & Certification Procedures
* Forms MW01–MW12 and standards MW31–33, PR1–6 (App C).
* Class I/II commencement: form, photos, coloured plans/details, supervision plan (Class I), other docs.
* Minor deviations not changing design assumptions / quantity increase → revised plans with completion; otherwise new notice (≥7 days) or MW11/12 additional items.
* PBW certification Forms MW06-1/2/3; alteration/strengthening via simplified MW before re-certify.
* Cessation notices within **7 days**.
* Radio base stations/antennas: MW items listed in App E; OFTA declaration/guidance note.

### 4. Critical Red Flags & AP Liability
* Commencing works before acknowledgement / assuming BD referral covers Lands/PlanD/etc.
* DMC/common-parts liabilities ignored.
* Area No.3 works without MTRCL agreement (Railways Ord. / Cap.276 risks).
* Wrong class/PBP appointments; supervision plan requirements under TM/Supervision Code.

---

## PNAP APP-148: Minor Works Contractors Registration
**Status/Context:** Registration of RMWC (Ind) and RMWC (Co) under BO s.8A(1)(c) / B(MW)R. First issue December 2010. Detailed procedures in PNRC 69.

### 1. Core Technical Requirements & Metrics
* RMWC (Ind): individual for Class III items specified — qualifications/experience; personal ability/skills; recognised Class III training course; suitability.
* RMWC (Co): key personnel quals; plant/resources; adequate corporate management; AS understanding of applied MW; suitability. Min **1 AS**; corporations also min **1 TD** (access to plant/resources; technical/financial support; supervise AS).
* One person may be both AS and TD if both criteria met. Key personnel cannot simultaneously be AS/TD/Other Officer for another contractor firm (conflicts).
* Class I registration / addition of MW / AS/TD → MWCRC interview/recommendation mandatory before BA can allow in whole or part.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not applicable.

### 3. BD Submission & Certification Procedures
* Specify items (Ind) or types/classes (Co) in application; BA registers only those found qualified.
* MWCRC: examine quals, inquire into experience, interview, advise allow/defer/refuse, review decisions.
* Aggrieved applicants: s.26 review request on specified form + fee (refunded if BA substitutes decision).

### 4. Critical Red Flags & AP Liability
* Carrying out MW outside registered class/type/item.
* Dual key personnel roles across firms.
* Incomplete documentary proof → BA refusal.

---

## PNAP APP-149: Appointment of Authorized Signatory to Act for Prescribed Registered Contractor and Temporary absence of Authorized Signatories in respect of Minor Works commenced under the Simplified Requirements
**Status/Context:** Companion to APP-138 for MWCS PRCs. First issue December 2010. Forms Appendices via PNRC 72.

### 1. Core Technical Requirements & Metrics
* One AS per MW submission; AS signing MW01 or MW03 is deemed responsible.
* AS must appear on all related forms / match supervision plan.
* Change (multi-AS PRC): App A PNRC 72; AP countersign for Class I; ≥**7 days**.
* Temporary AS: App B; Class I AP countersign; 7-day notice / 3-day proof for sudden incapacity; nominee must be BA-accepted AS for same classes/types of MW under the submission; max **14 / 30 days** total.
* Temporary AS: site inspection records only — not plans or specified forms.

### 2. GFA, Site Coverage, or Design Concession Impact
* Not applicable.

### 3. BD Submission & Certification Procedures
* Notifications to BA; Class I involves AP countersignature.
* >30 days absence → change AS or add AS to registration.

### 4. Critical Red Flags & AP Liability
* Temporary AS signing MW forms → invalid.
* Continuing MW with no acting AS → works must cease.
* Class I temporary nomination without AP countersignature.

---

## PNAP APP-150: Wholesale Conversion of Industrial Buildings
**Status/Context:** Supports Govt industrial building revitalisation (Lands D measures). First issue Sep 2010; revision June 2013. Pragmatic modifications for A&A wholesale conversion.

### 1. Core Technical Requirements & Metrics
* Favourable modification factors (examples):
  * Refuge floor difficulty → greenery design + enhanced FSI (APP-122); DFS no adverse comment.
  * Office conversion lighting/ventilation → B(P)R 30/31 mod if artificial L&V + energy design achieving **40%** in EU and IEQ under BEAM Plus (APP-130).
  * Oversized A/C boxes/platforms / over street → energy efficient / environmentally friendly A/C units (APP-19).
  * Curtain wall projecting over street (BO s.31(1) exemption) → low-energy glazing/materials with EU & IEQ **40%** BEAM Plus (APP-2).
* PPE in non-domestic: revised requirements in FS Code Clauses B19.2 & B20.9.
* Redundant carparks disregarded under Reg 23(3)(b) convertible to transformer rooms / mandatory or essential plant rooms (APP-151 App A types) under Reg 23(3)(a) mod with stakeholder support; **undertaking** that on cessation of facilities, plant rooms demolished and carparks reinstated per original approved plans.

### 2. GFA, Site Coverage, or Design Concession Impact
* Plant room swap from disregarded carpark GFA → modification pathway with reversion undertaking.
* Greenery/energy features support other SC/GFA-related modifications (refs APP-2, 19, 122, 130).

### 3. BD Submission & Certification Procedures
* A&A modification applications with BEAM Plus / FSI / energy justifications as applicable.
* Owner+operator undertaking letter + justifications at plan submission for carpark-to-plant conversions.

### 4. Critical Red Flags & AP Liability
* Claiming Reg 23(3)(a) plant room GFA without reversion undertaking / department support.
* Partial industrial-building columbarium/PPE fire-risk contexts (see also APP-154 for columbarium).

---

## PNAP APP-151: Building Design to Foster a Quality and Sustainable Built Environment
**Status/Context:** Core GFA-concession control PNAP. First issue Jan 2011; enhanced BEAM Plus / specific-standards mechanism. This revision **July 2025** (Apps A & C amended). Pre-requisites in paras. 6–9 apply to new GBP / major revisions / resubmitted disapproved GBP on or after **30 June 2024**. Earlier approvals refer to August 2022 version (Appendix D) subject to BO s.16(3)(d).

### 1. Core Technical Requirements & Metrics
* Three pillars: SBD Guidelines (APP-152); **GFA concessions**; energy efficiency.
* **Overall cap:** total GFA concessions for capped features ≤ **10%** of total GFA of the development (domestic and non-domestic parts calculated separately in composites, each at 10% of that part’s GFA).
* **Not subject to overall 10% cap** (para. 5) — may still have own criteria: (a) mandatory/essential plant rooms (e.g. refuse storage, TBE); (b) communal podium/sky gardens improving permeability; (c) parking/LUL floor space (separately controlled); (d) voids for cinema/arcades etc. with operational need (non-domestic); (e) bonus GFA / dedication-surrender / setback exemptions per SBD Guidelines; (f) hotel concessions under B(P)R Reg 23A.
* **Pre-requisites for GFA concessions (para. 6)** for App A green/amenity & non-mandatory plant:
  1. APP-152 SBD Guidelines (where applicable);
  2. Domestic/composite: APP-156 energy efficiency requirements (where applicable);
  3. Official HKGBC letter acknowledging satisfactory project registration for **BEAM Plus New Buildings Version 2.0 or above**;
  4. State in GBP the **target CA rating** under BEAM Plus NB and any required specific standards:
     * Anticipated **Gold** — no specific standard;
     * Anticipated **Silver** — **one** specific standard;
     * Anticipated **Bronze** — **two** specific standards;
  5. Document cascade: BSL Provisional Assessment credit summary (aligned with target) before superstructure consent; App B energy performance form before consent; update at OP; BSL CA result at OP achieving target on approved GBP; provisional & final energy efficiency reports per APP-156 where applicable;
  6. Overall 10% cap (where applicable);
  7. Individual feature acceptance criteria.
* **Specific standards (App C):** (a) enhanced greenery; (b) health & well-being; (c) enhanced natural ventilation; (d) BIM in plan submission; (e) MiMEP; (f) elderly-friendly building. Selection may change before OP application.
* **Enhanced greenery (App C1) — additional over APP-152 SCG:**

| Site area | Min additional greenery | Min no. of feature types (skyrise / green buffer / tree cluster) |
|-----------|-------------------------|------------------------------------------------------------------|
| < 1,000 m² | 5% of site | 1 |
| ≥1,000 & <20,000 m² | 5% of site | 2 |
| ≥20,000 m² | 7.5% of site | 2 |

  * Small site ≤1,000 m² meeting App E setback alternative: additional 5% may be waived if green buffer **or** tree cluster provided.
  * Green buffer: ≥2 m wide tree-pit strip along full street frontage; each pit ≥1.5×1.5×1.2 m; ≥6 m² greenery/pit; ≥1 pit; **zero irrigation**; greenery area ×**2** multiplier.
  * Tree cluster: ≥2 adjoining pits; min 12 m²; zero irrigation.
* **MiMEP (App C5):** coverage ≥ **50%** of qualifying plant/services area (calculation methodology in App C5).
* Conditions (para. 7): submit pre-consent items before consent; OP items at OP; modification **revoked** if consent sought before pre-consent submissions.
* AP must consult registered professional engineer (relevant discipline) for energy form (para. 8).
* Public disclosure after OP: energy data; BEAM Plus CA result; finalised RTTV/OTTV for residential recreational facilities.

### 2. GFA, Site Coverage, or Design Concession Impact
* **Appendix A — List of GFA Concessions** (✓ = subject to para.6/7 pre-reqs and/or 10% cap as marked in source table columns):

| # | Feature | Pre-reqs | 10% cap |
|---|---------|----------|---------|
| 1 | Carpark & LUL (excl. public transport terminus) | — | — |
| 2.1 | Mandatory/essential plant (area limited by PNAP/reg) e.g. LMR, TBE, RSMRC | — | — |
| 2.2 | Mandatory/essential plant (area not limited) e.g. FSI rooms, meters, transformers, water tanks | — | — |
| 2.3 | Non-mandatory plant e.g. A/C, AHU | ✓ | ✓ |
| 3 | Hotel pick-up/set-down | — | — |
| 4 | Hotel supporting facilities | — | — |
| 5 | Balcony (residential) JPN1 | ✓ | ✓ |
| 6 | Wider common corridor & lift lobby JPN1 | ✓ | — |
| 7 | Communal sky garden JPN1&2 / APP-122 | ✓ | — |
| 8 | Communal podium garden (non-res) JPN1 | ✓ | — |
| 9 | Acoustic fin JPN1 | ✓ | — |
| 10 | Wing wall, wind catcher, funnel JPN1 | ✓ | — |
| 11 | Non-structural prefabricated external wall JPN2 | ✓ | ✓ |
| 12 | Utility platform JPN2 | ✓ | ✓ |
| 13 | Noise barrier JPN2 | ✓ | — |
| 14 | Caretaker/guard/OC office etc. APP-42 | ✓ | ✓ |
| 15 | Residential recreational facilities (+voids/plant serving them) | ✓ | ✓ |
| 16 | Covered landscaped/play area, covered POS | ✓ | — |
| 17 | Horizontal screen/covered walkway/trellis/shelter/pick-up | ✓ | — |
| 17A | Accessible lift H/V extension at existing building | — | — |
| 18 | Larger lift shaft APP-89 | ✓ | — |
| 19 | Chimney shaft | ✓ | ✓ |
| 20 | Other non-mandatory plant (boiler, SMATV etc.) | ✓ | ✓ |
| 21 | Pipe/air duct/vertical riser for mandatory plant | — | — |
| 22 | Pipe/air duct for non-mandatory plant | ✓ | ✓ |
| 23 | Plant/duct for environmentally friendly systems | ✓ | — |
| 24 | High headroom/void (cinema, arcade etc.) non-domestic | ✓ | — |
| 25 | Prestige entrance void (non-domestic) | ✓ | ✓ |
| 26 | Void in duplex flat/house | ✓ | ✓ |
| 27 | Sunshade & reflector | — | — |
| 28 | Projecting planter/window/minor projecting features (A/C box etc.) | — | — |
| 29 | Maintenance walkway & projections not under APP-19 §3(b)(c) | ✓ | ✓ |
| 30 | Refuge floor (incl. refuge cum sky garden) | — | — |
| 31 | Covered area under large projecting/overhanging feature | — | — |
| 32 | Public transport terminus | — | — |
| 33 | Party structure & common staircase | — | — |
| 34 | Horizontal area of stair/lift/vertical duct serving non-accountable floors | — | — |
| 35 | Public passage APP-108 | — | — |
| 36 | Covered setback area APP-152 | — | — |
| 37 | Bonus GFA APP-108 | — | — |
| 38 | Buildings adopting MiC (JPN8) | (Additional green feature under JPN) | — |

* Notes (1)–(9) define room types under Reg 23(3)(a)/(b); unlimited-area essential plant still only **minimum** GFA necessary (APP-2).
* Filtration plant for water features may be GFA-exempt but still subject to APP-151 pre-reqs and overall cap where applicable (cross-ref APP-152 App D note).

### 3. BD Submission & Certification Procedures
* GBP must state target BEAM Plus rating and selected specific standard(s) (sample drawing C042 / ADV-33).
* Pre-superstructure consent: HKGBC registration letter; BSL provisional credit summary; App B energy form; APP-156 provisional energy report (if applicable); SBD compliance proof.
* At OP: updated energy form; BSL CA result matching approved target; APP-156 final energy report; Land Registry undertakings for applicable specific standards (e.g. greenery).
* Consent before pre-consent package → modification revoked.

### 4. Critical Red Flags & AP Liability
* Claiming capped concessions (balconies, UPs, prefab walls, recreational facilities, non-mandatory plant, etc.) without SBD + BEAM Plus + rating/specific-standards path + 10% math.
* Bronze/Silver without enough specific standards documented on GBP.
* Target rating change without GBP amendment before OP.
* Missing energy engineer collaboration on App B.
* Assuming carpark / mandatory plant / podium & sky gardens / bonus / hotel / PTT are “free” of all controls — they escape **overall 10%** but still have own PNAPs and transport policies.
* Using pre-30 Jun 2024 mechanism after applicable GBP cutoff without Appendix D grandfathering.

---

## PNAP APP-152: Sustainable Building Design Guidelines
**Status/Context:** SBD Guidelines referenced by APP-151 as GFA-concession **pre-requisite**. First issue Jan 2011; this version **September 2023** (Apps A & D amended). Three elements: building separation, building setback, site coverage of greenery.

### 1. Core Technical Requirements & Metrics
* **Building Separation — applies if:** site ≥ **20,000 m²**, **or** site <20,000 m² with continuous projected façade length Lp ≥ **60 m**.
* Assessment zones from Level Zero (mean of lowest abutting street): Low ≤20 m; Middle 20–60 m; High >60 m.
* **Design Requirement (1) — Lp:** for buildings within **30 m** of street centreline, max Lp = **5 × U** (mean street canyon width). Portions in low zone ≤**6.67 m** high may be disregarded for Lp. Not applicable if site has no street or no building within 30 m of street centreline in the zone.
* **Design Requirement (2) — S & P:** orthogonal (75°–105°) projection planes; one low-zone plane parallel to a street. P by ≥2/3 Intervening Space + ≤1/3 Permeable Element.

| H of tallest building | Site <20,000 m² & Lp≥60 m (each plane) | Site ≥20,000 m² Plane 1 | Plane 2 |
|----------------------|----------------------------------------|-------------------------|---------|
| H ≤ 60 m | 20% | 20% | 25% |
| H > 60 m | 20% | 20% | 33.3% |

  * IS S ≥ **7.5 m** to boundary/street centreline (mean ≥7.5 m; no part within **3 m** of boundary if S varies); additional IS between buildings ≥ **15 m**. IS height ≥2/3 of zone or open-to-above. PE clear W&H ≥ **3 m**.
  * Lp = continuous projected façade if separations <15 m. Standalone residential ≤**15 m** high exempt and disregarded in assessment of others.
* **Building Setback — if fronting street <15 m wide:** either (a) maintain 15 m × 15 m ventilation corridor — no building part ≤15 m above street within **7.5 m** of street centreline; or (b) cross-ventilated communal podium garden clear height ≥**4.5 m** and keep below 45° inclined plane from opposite street boundary. Structures >15 m may build over setback; canopies Reg 10; minor features/signboards ≤**600 mm** projection at ≥**2.5 m** clear height; footbridges; columns per Fig C2; setback landscaped/paved open common area. Exemption if building height < **2×** mean street width. Covered setback under footprint/canopy may be GFA-exempt if common, no commercial activity.
* **Site Coverage of Greenery — Table 2:**

| Site area | Primary zone (15 m vertical) | Overall |
|-----------|------------------------------|---------|
| 1,000–20,000 m² | 10% | 20% |
| ≥20,000 m² | 15% | 30% |

  * N/A to single-family-house-only sites.
  * Greening features may contribute ≤**30%** of required overall greenery (after reduction factors): covered greenery (primary zone, 50%); water features (primary/uncovered communal roof, 50%); grass paving (50%, excl. carpark/LUL); inaccessible-roof planters in primary zone (50%); vertical greening (nil reduction); landscape-treated slopes/RW >45° (nil). Green buffer per APP-151 C1 uses ×2 multiplier for APP-152 SCG too.
  * Removable pots not counted; covered greenery above primary zone generally not counted (limited exceptions). Vertical climbing frames: parts >**7.5 m** not accountable. All greenery as common parts; irrigation/drainage; roof imperviousness & structural load.
* **Alternatives (App E):** less bulk (SC ≤65%) + street setback (frontage ≥50% of boundary & ≥10 m / full if <10 m; setback area ≥15% site) may waive low-zone separation; performance AVA (wind tunnel/CFD) if min P in Table 1 still met and equivalence to compliant baseline shown; BC may review.

### 2. GFA, Site Coverage, or Design Concession Impact
* Compliance is APP-151 pre-requisite for listed GFA/SC concessions.
* Covered setback GFA exemption (footnote) and APP-151 Item 36 covered setback; bonus/dedication still under APP-108 pathways.
* Greenery letter of undertaking → LR registration before OP when GFA mods granted (conditions).

### 3. BD Submission & Certification Procedures
* Submit separation, setback, greenery information per Appendix F; greenery plans uploaded to BD website after OP.
* Section 42 modification conditions may lock greenery common-parts / DMC restrictions.

### 4. Critical Red Flags & AP Liability
* Claiming GFA concessions on large/long façades without meeting Lp/P/S for every assessment zone.
* Counting PE >1/3 of required P; inadequate IS widths; counting removable pots / above-primary covered gardens.
* Street <15 m without setback/45° option and no height-based exemption.
* Greenery not designated common / no LR undertaking when required by approval conditions.

---

## PNAP APP-153: Code of Practice for Fire Safety in Buildings 2011
**Status/Context:** FS Code replaces MOE 1996, FRC 1996, MOA 2004. Operative **1 April 2012**. PNAP revised September 2024 consolidating amendments (Apps B–H) into **FS Code (2024 Edition)** on BD website. This PNAP is primarily an applicability and amendment vehicle — detailed technical fire design is in the FS Code itself.

### 1. Core Technical Requirements & Metrics
* FS Code Parts A–G + Annex A (licensing authority codes).
* Effective regime: works consented before 1 Apr 2012 may continue on old MOE/FRC/MOA Codes (for new buildings, relevant consent = **foundation** consent). Pre-1 Apr 2012 submissions may use FS Code **only in entirety**. Cap.502 / Cap.572 upgrading remains on APP-94 / APP-145 basis — FS Code **not** applicable to those improvement regimes.
* A&A / licensed premises: generally only **affected areas** (+ affected exit routes) need FS Code; remainder need not.
* Consent for plans approved pre-FS Code: generally OK if consent within **2 years** of first approval; then amended plans for FS Code before OP as necessary; otherwise OP refusal BO s.21(6) and/or consent refusal BO s.16(3)(d).
* Appendix A PNAP list **not applicable** when FS Code governs (APP-14, 75, 80–83, 85, 87, 91, 92, 106, 121, 123). Those PNAPs still apply to old-Code designs and Cap.502/572 works.
* Consolidated amendments through Sep 2024 include (non-exhaustive examples from early corrigenda): swimming pool occupant capacity based on water surface (Use 5d); fire door/shutter insulation rules with sprinkler option if openings >25% wall length; combustibility classifications for linings (BS EN 13501-1 / Table E1 equivalences) — **full current text must be taken from FS Code 2024 Edition**.

### 2. GFA, Site Coverage, or Design Concession Impact
* Fire safety design (MOE/MOA/FRC) constrains permeable elements, refuge floors, sky gardens, EVA, and voids that interact with APP-151/152 concessions — concessions never override FS Code.

### 3. BD Submission & Certification Procedures
* Design entire building works to FS Code (or entire applicable old Codes under grandfather rules).
* For A&A: limit FS Code upgrade scope to affected areas/exit routes unless otherwise required.
* Track TC amendments Apps B–H; use BD website 2024 Edition.

### 4. Critical Red Flags & AP Liability
* Mixing old Codes with FS Code partially.
* Applying FS Code to Cap.572/502 upgrading incorrectly (or conversely applying obsolete PNAPs to new FS Code buildings).
* Consent >2 years after old-Code approval without addressing FS Code before OP.
* Relying on this PNAP’s amendment extract tables instead of the consolidated Code.

---

## PNAP APP-154: Design Requirements for Columbarium Facilities
**Status/Context:** Design/construction requirements under BO for columbaria. First issue August 2012.

### 1. Core Technical Requirements & Metrics
* **MOE:** FS Code Part B; Table B1 Item 5d occupancy **2 m² UFA/person**. Include corridors of balcony approach, circulation, lift lobbies etc. in UFA; **exclude** niche accommodation areas and staircases from that UFA calculation.
* **FRC:** FS Code Part C; Use Classification “Other Assembly Premises” (Table C1). Burner/offering facilities = special hazard (Subsection C13 separation).
* **MOA/EVA:** B(P)R 41A–D + FS Code Part D; non-standard EVA → BA16 + APP-136.
* **Sanitary fitments (Table 1):** population at 2 m²/person; M:F = **1:1.5**; Male: 1 WC + 1 urinal /150; 1 basin /300; Female: 1 WC /75; 1 basin /300; separate rooms.
* **BFA:** B(P)R s.72 + DM 2008; aisle space for worship in addition to min. passageway/MOE clearances.
* Loads: Dead and Imposed Loads Code 2011.
* Conversion: material change of use (BO s.25); non-domestic buildings only; industrial buildings — **entire building** conversion only (FSD fire safety); partial conversion undesirable.

### 2. GFA, Site Coverage, or Design Concession Impact
* Occupancy-driven MOE/sanitary provision affects planning efficiency; not itself a GFA concession tool.

### 3. BD Submission & Certification Procedures
* Plans demonstrating MOE/FRC/MOA/sanitary/BFA/loads; other departments (planning, hygiene, traffic, FSD, Lands lease) separately.
* Change-of-use notifications where conversion.

### 4. Critical Red Flags & AP Liability
* Under-counting UFA for MOE by excluding circulation.
* Partial industrial-building columbarium conversion.
* BO compliance alone without lease/OZP/licensing.

---

## PNAP APP-155: Signboard Validation Scheme
**Status/Context:** Validation of existing unauthorised signboards under Signboard Control System from **2 September 2013**. Revision December 2020. 5-year re-validation cycle. Free submissions; no departmental referral.

### 1. Core Technical Requirements & Metrics
* Eligible: unauthorised signboards erected **before 2 Sep 2013** matching MW Sch.3 Part 3 / corresponding Sch.1 MW items (projecting, wall/shopfront, roof, on-grade, spread footing, balcony/canopy soffit).
* Key dimensional limits (App A examples):
  * Projecting: Class I >10–≤20 m² display, projection ≤4.2 m, thickness ≤600 mm; Class II ≤10 m², ≤1 m projection, ≤300 mm thick; Class III ≤1 m², any part ≤6 m from ground; no stone; no extra load to cantilevered slab; no structural element alteration.
  * Wall: LED >5–≤20 / ≤5 m²; non-LED >10–≤40 / ≤10 / ≤5 m² by class; stone restriction if >6 m from ground.
  * Roof: ≤20 m²; thickness ≤600 mm; ≤6 m above roof; not projecting beyond external wall.
  * On-grade: ≤20 / ≤10 m²; ≤6 m / ≤2 m from ground by class.
  * Spread footing: ≤1 m²; ≤300 mm thick; ≤3 m high; excavation ≤500 mm.
  * Balcony/canopy soffit: ≤2 m²; height ≤600 mm; thickness ≤100 mm; no projection beyond balcony/canopy.
* Positional: APP-126 spacings (e.g. min lateral spacing to opposite signboards; clearances over walkway/carriageway/tramway as diagrammed). Failure to show required lateral spacing → ineligible.
* Person appointments: Class I — AP (+RSE if not specified construction under B(MW)R s.37(4)); Class II/III — PBP or PRC registered for corresponding type C MW. Strengthening by PRC (Class I under AP/RSE supervision as necessary).

### 2. GFA, Site Coverage, or Design Concession Impact
* Not applicable (signboard validation / enforcement deferral).

### 3. BD Submission & Certification Procedures
* Forms SC01 / SC01C (Class I), SC02 / SC02C (Class II), SC03 (Class III) + photos, fixing details, plans, calculations (Class I), safety inspection checklists (App C).
* Alteration/strengthening notified and completion certified on related forms.
* Recommend display of validation submission numbers (App D).
* Re-validate or remove at **5-year** intervals.
* Common parts: DMC / Cap.344 consent and third-party insurance advised.

### 4. Critical Red Flags & AP Liability
* Validating post-2 Sep 2013 unauthorised signboards under this scheme.
* Spacing conflicts with approved/validated neighbours.
* Wrong class professional appointments; assuming BD submission notifies other departments.
* Letting validated frames pass 5-year cycle without re-certification or removal → enforcement risk.

---

## Completed APP List (Batch 06)

| APP | Title (exact from source) | Status |
|-----|---------------------------|--------|
| APP-132 | Site Coverage and Open Space Provision | Summarised |
| APP-133 | Cast Iron Pipes for Drainage Works | Summarised |
| APP-134 | Development in the Designated Area of Northshore Lantau | Summarised |
| APP-135 | Quality Supervision of Soil Nailing Works | Summarised |
| APP-136 | Building (Planning) Regulation 41D Emergency Vehicular Access | Summarised |
| APP-137 | Ground-borne Vibration and Ground Settlement arising from Pile Foundation and Excavation and Lateral Support Works | Summarised |
| APP-138 | Appointment of Authorised Signatory to Act for Registered Contractor and Temporary absence of Authorised Signatories | Summarised |
| APP-139 | Code of Practice on Wind Effects in Hong Kong | Summarised |
| APP-140 | Registration of Authorized Persons and Registered Structural Engineers as Registered Geotechnical Engineers | Summarised |
| APP-141 | Division of Responsibilities between Authorized Person, Registered Structural Engineer and Registered Geotechnical Engineer | Summarised |
| APP-142 | Code of Practice for Structural Use of Concrete 2013 | Summarised |
| APP-143 | Quality Control and Supervision of Precast Concrete Construction | Summarised |
| APP-144 | Design and Construction of Run-in and Run-out on Public Road | Summarised |
| APP-145 | Fire Safety (Buildings) Ordinance, Cap. 572 | Summarised |
| APP-146 | Metal Gates | Summarised |
| APP-147 | Minor Works Control System | Summarised |
| APP-148 | Minor Works Contractors Registration | Summarised |
| APP-149 | Appointment of Authorized Signatory to Act for Prescribed Registered Contractor and Temporary absence of Authorized Signatories in respect of Minor Works commenced under the Simplified Requirements | Summarised |
| APP-150 | Wholesale Conversion of Industrial Buildings | Summarised |
| APP-151 | Building Design to Foster a Quality and Sustainable Built Environment | Summarised (full GFA/BEAM focus) |
| APP-152 | Sustainable Building Design Guidelines | Summarised (full SBD metrics) |
| APP-153 | Code of Practice for Fire Safety in Buildings 2011 | Summarised |
| APP-154 | Design Requirements for Columbarium Facilities | Summarised |
| APP-155 | Signboard Validation Scheme | Summarised |

**Missing in range:** none (APP132–APP155 all present in `_extracted_txt`).

**Output file:** `_PNAP_summaries/batch_06_APP132-155.md`


<!-- Source: batch_07_APP156-174.md -->

# PNAP Batch 07 Summary: APP-156 to APP-174

**Source:** `PNAP_APPb_e/_extracted_txt`  
**Skipped (not in source dir):** APP-160, APP-161  
**Completed list:** APP-156, APP-157, APP-158, APP-159, APP-162, APP-163, APP-164, APP-165, APP-166, APP-167, APP-168, APP-169, APP-170, APP-171, APP-172, APP-173, APP-174

---

## PNAP APP-156: Design and Construction Requirements for Energy Efficiency of Residential Buildings
**Status/Context:** First issue September 2014; last major content revision July 2024; this revision September 2025 (AD/NB1) — paragraphs 5, 6(b) and 17 amended (OTTVRRF standards and implementation date). Applies to “residential building” as domestic building under BO s.2(1), excluding hotels, guesthouses, RCHE/RCHD and similar AC-profile premises. Does **not** apply to A&A or change in use that does not produce a new residential building. Detail metrics also set out in BD “Guidelines on Design and Construction Requirements for Energy Efficiency of Residential Buildings” and CoP for OTTV in Buildings 1995.

### 1. Core Technical Requirements & Metrics
* **RTTVWall (prerequisite for APP-151 GFA concessions):** Must not exceed **12.5 W/m²** (previously 14 W/m²).
* **RTTVRoof:** Must not exceed **3.5 W/m²** (previously 4 W/m²).
* **OTTVRRF (residents’ recreational facilities):** Must not exceed **20 W/m²** for a building tower (previously 21) or **40 W/m²** for a podium (previously 50), calculated per CoP OTTV 1995.
* **Glazing — VLTGlass:** Not less than **50%** for glass forming part of building envelope (curtain wall, cladding, skylight, window, door) of the residential building and RRF; VLT requirement applies only to glass in prescribed windows under B(P)R regs 30 and 31.
* **Glazing — ERGlass:** External reflectance not more than **20%**.
* **NVTC (natural ventilation for thermal comfort):** Extent of compliance (percentage of habitable space area complying with Guidelines) must be submitted; collected for research/benchmarking, not published on BD website.
* **Sunshades:** Genuine sunshades that reduce RTTV/OTTV are not accountable for GFA and not included in site coverage; projection >750 mm from external walls requires quantitative assessment; projection >1.5 m generally not envisaged; ≤750 mm regarded as not obstructing prescribed windows; projection over streets under BO s.31(1) generally not allowed (case exemptions possible).

### 2. GFA, Site Coverage, or Design Concession Impact
* Compliance with para 6 (RTTVWall/Roof, OTTVRRF, NVTC submission, VLT/ER) is a **pre-requisite** for granting GFA concessions for green/amenity features and non-mandatory/non-essential plant rooms and services in a residential building under **PNAP APP-151**.
* Genuine energy-beneficial sunshades: **not GFA-accountable** and **excluded from site coverage** calculations (subject to projection rules above).

### 3. BD Submission & Certification Procedures
* **First GBP submission:** Full RTTV/OTTV calcs need not accompany first plans, but plans must include a **statement** of intended compliance with RTTVWall, RTTVRoof, OTTVRRF, VLTGlass and ERGlass.
* **After GBP approval, before consent to commence building works:** Submit Summary Sheets — Appendix A (RTTV) and Appendix B (OTTVRRF) demonstrating para 6(a), (b) and (d).
* **Before OP:** Incorporate finalised RTTVWall, RTTVRoof, OTTVRRF, VLTGlass, ERGlass and glass shading coefficients into GBP for record.
* **At OP application:** Submit Energy Efficiency Report including: RTTV calcs (Guidelines Appendix III forms); OTTVRRF Forms OTTV 1–4 if applicable; record plans; material test certificates/published specs; finalised Appendices A & B; NVTC compliance extent (Guidelines Appendix VI).
* Non-listed materials: obtain RTTV/OTTV properties from reliable sources; detailed source background and local suitability aids consent/OP processing.
* Post-OP: RTTV and OTTVRRF of individual developments uploaded to BD website for public disclosure; NVTC extent not uploaded.
* **Implementation of revised OTTVRRF (para 6(b)):** Applies to all new GBP or major revision of GBP submitted for approval **on or after 31 December 2025**.

### 4. Critical Red Flags & AP Liability
* Failure to meet RTTV/OTTV/VLT/ER thresholds jeopardises **APP-151 GFA concessions**.
* Omitting the compliance statement on first plans, or missing Appendix A/B before consent, risks delay/refusal of consent or OP.
* False or incomplete Energy Efficiency Report / material certificates at OP is a direct AP/RSE documentary liability.
* Sunshade projections over streets or >750 mm without assessment; RRF treated wrongly under residential RTTV instead of OTTV hotel/commercial-type control.
* Scope trap: hotel/guesthouse/RCHE-type AC profiles are outside this PNAP’s “residential building” definition.

---

## PNAP APP-157: Code of Practice for Site Supervision 2009
**Status/Context:** First issue May 2015; last revision December 2023; this revision August 2024 (AD/NB2) (general revision). Points APs/RSEs/RGEs to Supervision Code **2024 Edition** on BD website, incorporating 2021 Edition plus Appendix A (December 2023) and Appendix B (August 2024) amendments. Similar PN issued to registered contractors.

**⚠ EXTRACTION INCOMPLETE:** Source PDF is large/scanned (~99 pages); extracted text covers main body §§1–6 fully, but Appendices A & B are largely **empty page frames** (legends only; amendment tables of 2021 vs 2024 text not OCR’d). Summarise only what exists; do not invent Supervision Code clause text from blank appendix pages. Refer to BD-published Supervision Code (2024 Edition) and APP-157 appendices on BD website for full amendment matrices.

### 1. Core Technical Requirements & Metrics
* **Temporary works supporting tower cranes:** In addition to Supervision Code (2021 Edition) para 4.9, RGBC/RSC must appoint a **design engineer** to prepare plans, construction drawings and design justifications, and an **independent checking engineer** to check those documents for compliance with BO, regulations and relevant CoPs.
* **Applicability trigger:** All development projects with specified Form **BA 10** submitted **on or after 1 November 2024**.
* **Certification forms:** TW1, TW2, TW3 soft copies on BD website (APP-157 page).
* **TCP academic qualifications:** Paras 8.18–8.24 of Supervision Code (2021 Edition); BD publishes accepted course list (local and non-local) as ready reference on BD website.
* **Corresponding recognition (Appendix X) repealed:** Circular letter 8 May 2015 repealed TCP recognition based on membership of particular professional institutions (Appendix C of this PNAP for reference). Members previously accepted may continue as TCPs if evidence of previous recognition is provided with supervision plan submissions.

### 2. GFA, Site Coverage, or Design Concession Impact
* No direct GFA/site coverage concession provisions in the extracted text.

### 3. BD Submission & Certification Procedures
* Use Supervision Code **2024 Edition** (BD website) as the operative code incorporating Appendices A & B amendments.
* Tower-crane temporary works: design engineer + independent checking engineer certifications (TW1/TW2/TW3).
* Supervision plans: if relying on pre-repeal institutional TCP recognition, supply evidence of previous acceptance with the plan.

### 4. Critical Red Flags & AP Liability
* BA 10 on/after 1 Nov 2024 without design engineer + ICE for tower-crane support temporary works = non-compliance with enhanced Supervision Code controls.
* Appointing TCPs on obsolete “corresponding recognition” without documentary evidence risks rejection of supervision plan.
* **Content gap:** Detailed December 2023 / August 2024 clause-by-clause amendments are **not usable from this extraction** — verify against BD PDF/HTML before citing specific Supervision Code 2024 deltas.

---

## PNAP APP-158: Quality Supervision of Building Works
**Status/Context:** First issue November 2016; last revision February 2021; this revision September 2024 (AD/NB1) — paragraph 3 and Appendix A amended. Complements Code of Practice for Site Supervision 2009. Similar PN issued to RCs.

### 1. Core Technical Requirements & Metrics
* Quality supervision is part of the supervision plan: works must be in general accordance with BO/regulations, approved plans, and approval/consent conditions.
* AP/RSE/RGE/AS must devise TCP checklists from typical items plus project-essential items, including BA-imposed quality/qualified supervision conditions.
* Appendix A tables (non-exhaustive) cover inspection items for:
  * **Superstructure — in-situ RC (QC1–QC11):** locations/sizes; steel bar delivery/sampling per CS2; bar fixing/cover per PNAP ADV-15; concrete delivery/cubes per CS1 / high-strength coring conditions; placing/compaction/curing; transfer structure sequence/temporary works; formwork/falsework stability (division of RSE/RC responsibility per Supervision Code clauses 4.7–4.9); post-strip concrete condition; couplers; cast-in embeds/anchors; in-situ strength (coring/rebound).
  * **General building works (QB1–QB8):** setting-out basements/G/F and upper floors (lanes, EVA, setbacks, dedicated areas, storey height, FS staircases, smoke vents, refuge, barriers, etc.); interior/fitting-out including exit routes, fireman’s lift lobbies, temporary refuge spaces, GFA-concession features (balconies, UPs, wider corridors, plant rooms, RRF), fire barriers/FRR products, roof waterproofing; windows (prescribed areas/openable areas; PNAP APP-116; modification conditions); BFA dimensions/DM:BFA; waterproofing application/performance testing for roofs/balconies/UPs/wet areas/basements; curtain wall mock-up and on-site water penetration tests (Glass Code 2018 Annex A standards); precast façade water penetration tests (Precast CoP 2016 clauses 2.8.2.8 and 4.3).
  * **ELS (QE1–QE9):** temporary planking location/install; grout curtain; pumping/ground treatment tests; strut erection/removal sequence; preloading; staged excavation (no over-excavation/stockpile risk); backfilling/compaction; instrumentation/monitoring (movement, GW drawdown, ingress). RGE stream only when geotechnical qualified supervision is an approval condition. AP stream often coordinating (*) roles.
  * **Site formation:** monitoring (QSF1); drainage/rainstorm protection; cut/fill (APP-15); rock slopes (APP-17); retaining walls (including reg.48 domestic cases for waterproofing/insulation); reinforced fill (APP-54 drainage/filter; APP-15 backfill).
* Record sample Appendix B: TCP name/grade, frequency, item nos., location, S/NS/NA results, remedial remarks, photos; Form B where non-conformity has material safety concern or cannot be verified due to cover-up.

### 2. GFA, Site Coverage, or Design Concession Impact
* No direct new concession formula; however QB3 specifically requires checking dimensions/conformity of **features subject to GFA exemptions/modifications** (balconies, UPs, wider corridors/lift lobbies, plant rooms, pipe ducts/wells, RRF, etc.) — failure here can invalidate previously granted concessions at audit/OP.

### 3. BD Submission & Certification Procedures
* Keep all checklists and inspection records **on site** for Site Monitoring Section / BA inspection.
* Devise project-specific quality supervision records (Appendix B sample is reference only).
* Coordinate streams; AP (*) ensures RSE/RGE/RC checking where marked; AP (#) checks layout conformity to approved plans.

### 4. Critical Red Flags & AP Liability
* Incomplete checklists omitting curtain wall/glass/prestress/steel/waterproofing where relevant.
* Missing site records → BD audit failure against supervision duties under BO.
* NS findings without Form B when required (material safety concern or covered-up works).
* Overlooking GFA-concession geometry / fire door FRR / prescribed window areas during interior fitting-out stage.

---

## PNAP APP-159: Measures to Deter Misuse of Industrial Buildings for Residential Use
**Status/Context:** First issue October 2016 (AD/NB1). Targets new IB proposals including A&A, to deter unauthorised residential conversion at design stage. Unauthorised residential use of IBs poses high risk (dangerous/inflammable goods) and contravenes BO.

### 1. Core Technical Requirements & Metrics
* Workshop servicing arrangements must be clearly shown on GBP: loading/unloading areas, cargo lifts, and their **segregation** from communal circulation of occupiers/visitors.
* Modification for **non-provision of natural lighting and ventilation to toilets** generally not granted except for **communal** toilets.
* **Excessive storey height:** for small workshop units, storey height **>3.5 m** must be fully justified.
* **Small workshop unit:** usable floor area **<80 m²**.
* For IB with small workshop units and curtain walls: **outer face of curtain walls** taken as external wall for measuring GFA and site coverage.
* Designs/facilities not commonly found in IBs or not commensurate with industrial use require justification; may be refused as IB development.

### 2. GFA, Site Coverage, or Design Concession Impact
* Internal pipe ducts for toilets: **not exempted from GFA** except for communal toilets in common parts (consequence of refusing private toilet NL&V modifications).
* Curtain-wall IBs with small workshops: GFA and site coverage measured to **outer face of curtain wall** (tighter envelope).

### 3. BD Submission & Certification Procedures
* Measures applied in BD processing of new IB proposals (including A&A).
* Servicing/segregation must be explicit on GBP; excessive height and non-industrial facilities need documented justification.

### 4. Critical Red Flags & AP Liability
* Designing IB layouts that facilitate residential misuse (private toilets without NL&V, excessive storey heights without justification, domestic-type facilities without industrial servicing).
* Claiming GFA exemption for private toilet pipe ducts.
* Undermeasuring GFA/SC by not taking curtain wall outer face where small units apply.

---

## PNAP APP-162: Conditions and Requirements Imposed under the Buildings Ordinance upon Granting Approval and/or Consent
**Status/Context:** First issue September 2020; this revision March 2025 (AD/NB2) (general revision). Explains BO s.17 conditions/requirements typified in Appendix A; cross-ref APP-158 for quality supervision. Similar PN to RC. Common material/works-specific conditions also on BD website (“Codes and references”).

### 1. Core Technical Requirements & Metrics
* BA may impose case/task-specific conditions under BO s.17 covering quality supervision, qualified supervision, QA/QC, material testing, instrumentation, record documentation — to be complied with before consent, during works, and/or at completion certification.
* **Qualified supervision — Mobile Plant Alert System & Tower Crane Alert System (4S):** From **1 July 2025**, for projects with estimated total cost of building works **> $30 million**, conditions under s.17(1) item 6(e) for adoption of both alert systems will be imposed on first approval (or major revision) and/or first consent for demolition, site formation, ELS, foundation, pile cap, superstructure involving mobile plants and/or tower cranes; also for A&A with structural works meeting the cost threshold. (Superstructure: circular letter 28 Mar 2024 already mandated alert systems from **1 July 2024** on first superstructure approval/major revision and subsequent consent.)
* **Qualified supervision personnel (typical):** RSE assigns QCS (≥ weekly inspection; min T3 RSE stream); RGBC/RSC assigns QCC (full-time on site; min T1 RC stream); log book on site. Enhanced for Type 2 mechanical couplers: QCC raised from T1 to **T3**.
* Materials: B(C)R s.3 — nature/quality, mixing, installation; recognised tests; manufacturer’s recommendations; if used before testing, **full traceability** required.
* Monitoring: vibration, tilting, movements of adjacent buildings/land/streets/services; groundwater where appropriate.
* Continuous supervision footnote: e.g. Type 2 coupler connecting requires **full-time RC TCP** during the task; bar fixing may be inspected at hold points if readily checkable.

### 2. GFA, Site Coverage, or Design Concession Impact
* No direct GFA/SC concession content.

### 3. BD Submission & Certification Procedures
* **AP declaration** under B(A)R reg.10 at **first consent application** (whichever works type earlier): whether estimated total cost of building works (incl. demolition, SF, ELS, foundation, pile cap, superstructure, A&A) **exceeds $30 million**. Failure → possible refusal under BO s.16(3)(b). Subsequent consents need no further declaration. If declared >$30M, BA imposes 4S conditions on first consent for all para-4 works types.
* Typical B(A)R reg.10 document requirements: QSP; manufacturer’s QA scheme; pre-construction surveys/monitoring; material certificates; strength/performance tests; RSE & AS audit reports; RSE confirmation statement; record plans/reports; $30M cost declaration.
* Keep approval/consent letters on site; brief supervision team on imposed conditions.
* Streamlined: quote BD common conditions on website for specific materials/methods; pre-accepted method statements elsewhere (e.g. APP-169).

### 4. Critical Red Flags & AP Liability
* Missing $30M declaration at first consent → consent refusal risk.
* Understating estimated cost to avoid 4S conditions (AP liability).
* Using materials before test results without traceability; ignoring QCS/QCC log books; treating “continuous supervision” as casual intermittent visits on critical coupler works.

---

## PNAP APP-163: Code of Practice on Access for External Maintenance 2021
**Status/Context:** First issue February 2021; this revision September 2024 (AD/NB1) — paragraphs 3–5 amended, paragraph 6 and Appendix A added. Code (2024 Edition) consolidates TC amendments. Supersedes Code of Practice on Design for Safety – External Maintenance 2019. Statutory basis: B(C)R ss.27(2), 28(5), 31(3), 34(3) for means of access for M&R of external building elements (external walls, curtain walls, claddings, roofs and projections). BO s.39(2) grandfathering for works under way or consented as at **31 January 2021** (foundation works of proposed development generally count).

### 1. Core Technical Requirements & Metrics
* Submit **M&R access plans** per Code procedures (details, supporting documents, developer/owner’s letter of undertaking).
* **Appendix A item 1 — new para 3.2.4 (anchors at balconies/UPs):** At least **one anchor** for personal fall arresting system at every balcony and UP; readily accessible from adjoining floor; height **not less than 1.5 m and not more than 1.8 m** above finished floor of adjoining floor; comply with Appendix D para 7; structural/fixing detail per Appendix F. Outer surface M&R access still by power-operated elevating work platform or suspended working platform (para 3.2.3).
* **Inaccessible roof edge protection (amended 4.2.3 / new 4.2.4):** Where permanent guard-rails around whole perimeter impracticable, alternatives: proprietary collapsible guard-rail (loads/wind not inferior to B(C)R, Loading Code, Wind Code) and/or temporary edge protection with platform/ladder after LD “Five Steps to Risk Assessment”; with anchorage points or horizontal lifeline ≥2 m from edge/fragile area (or at roof access), attachable before fall-risk zone; if access within 2 m of edge or onto pitched roof, permanent rails at least around access/landing. GBP general notes required as specified.
* Other Appendix A items: LD references updated (add “Overview of Work-at-Height Safety”, “Five Steps to Risk Assessment”; renumber subsequent items).

### 2. GFA, Site Coverage, or Design Concession Impact
* No direct GFA concession formulae in this PNAP; M&R features still subject to normal BO/B(P)R accounting unless separately exempted elsewhere.

### 3. BD Submission & Certification Procedures
* M&R access plans with undertaking letter per Code.
* **Implementation:** All Appendix A items except new para 3.2.4 — immediate effect. Para 3.2.4 applies to new GBP or major revision (and previously disapproved GBP resubmitted) for approval **on or after 1 December 2024**. APs advised to provide balcony/UP anchors in ongoing projects anyway.

### 4. Critical Red Flags & AP Liability
* New GBP on/after 1 Dec 2024 without balcony/UP fall-arrest anchors at 1.5–1.8 m.
* Relying solely on collapsible/temporary roof edge protection without lifeline/anchor before entering fall-risk zone, or without LD risk assessment notes on plans.
* Ignoring Code for A&A to existing buildings without exploring feasible M&R access (LD OSH references still apply).

---

## PNAP APP-164: Enhanced Design Standards of Aboveground Drainage System
**Status/Context:** First issue April 2021; last revision April 2023; this revision November 2023 (AD/NB1) — paragraph 9 added and Appendix A amended. Issued under BO s.28(1) pending legislative amendment of Drainage Regulations. Covers floor drain, anti-syphonage pipe, branch discharge, ventilating pipe, rainwater pipe design.

### 1. Core Technical Requirements & Metrics
* **Floor drain seal replenishment (kitchens in domestic units, toilets, pantries):** Divert used water from lavatory basin, bath or shower bath to replenish floor drain trap seal without backflow; trap to comply with Drainage Reg. 25.
* **Main anti-syphonage connections to drainage stack:**
  * Connecting pipes slope upwards at angle **≤67.5°** from stack; internal diameter **≥ main anti-syphonage pipe**.
  * Buildings **>5 and ≤20 storeys:** connections at intervals **≤5 storeys**; **>20 storeys:** intervals **≤3 storeys**; starting from lowest storey with branch discharge to stack (podium/basement stacks: use podium/basement storey count).
  * Connection required below lowest branch and above bend of an **offset**; not required between offsets with no branches.
* **Restricted zone at every offset:** No drainage pipe connection within up to **600 mm** (≤5-storey) or **1 000 mm** (>5-storey) above bend invert, and within **2 500 mm** horizontally from bend.
* **Lowest-floor sanitary fitments vs stack discharge to manhole:**
  * **>3 and ≤20 storeys:** fitments on discharge floor must not connect to stack — separate pipework to manhole.
  * **>20 storeys:** same for discharge floor **and floor above**.
* **Ventilating pipe open ends (roof):** Not less than **3 m** from common boundary, and from any window/opening/fresh air intake; APs also advised to carry vents **≥3 m above accessible roofs**.
* **Rainwater pipes ≤100 mm ID (advisory, DSD-aligned):** Max horizontal roofed-over area — 40 mm: 9 m²; 65 mm: 33 m²; 80 mm: 58 m²; 100 mm: 106 m².
* **Modification of Drainage Reg. 30(2)(b)(ii):** BA prepared to favourably consider anti-syphonage connection to branch soil/waste at **≤750 mm** from trap outlet (Appendix A Fig. 8).
* Hopper heads: APs advised **not** to provide (debris/vegetation blockage).

### 2. GFA, Site Coverage, or Design Concession Impact
* No GFA/SC provisions.

### 3. BD Submission & Certification Procedures
* New drainage plans or major revisions for development projects and A&A submitted for approval **after 31 August 2021** must comply.
* Projects with superstructure consent **after 31 August 2021:** para 2(b), (c), (f) to be complied with; amend drainage plans (or deferred minor amendments per PNAP ADM-19 paras 22–24).
* Also applies to aboveground drainage under **Minor Works Control System** commenced after 31 August 2021.
* Appendix B maps A&A/MW examples to which para 2 requirements apply (new floor drain; new stack; new offset; new connection; new fitment at lowest/second-lowest floors; new/altered roof vent).

### 4. Critical Red Flags & AP Liability
* New stacks without correct anti-syphonage interval regime (5 vs 3 storeys) or offset restricted-zone connections.
* Connecting lowest (or 2nd lowest for tall buildings) floor fitments into the stack discharging to manhole.
* Roof vents <3 m from boundary/openings; continuing open hopper-head systems without considering closed trapped systems on repairs.

---

## PNAP APP-165: Product Certification System
**Status/Context:** First issue September 2021 (AD/CS). Promotes third-party Product Conformity Certification Schemes (PCCS); currently accepts CoCs for fire doorsets and non-loadbearing fire partition walls as alternative to lab test/assessment reports.

### 1. Core Technical Requirements & Metrics
* Product certification: accredited CB issues CoC confirming product meets specified PCCS; factory audit + independent accredited lab (HOKLAS/MRA) sample testing; periodic surveillance; CoC typically valid **3 years**; suspension/withdrawal on non-compliance.
* **Currently accepted under BO as alternative to test/assessment reports:** Valid CoCs of **fire rated doorsets** and **non-loadbearing fire partition walls** under **PCCS for Passive Fire Protection Products (Fire Door and Non-loadbearing Fire Partition) (Issue 3)** issued by HKCAS-accredited (or MRA) CBs. Scheme owner: Hong Kong Institute of Steel Construction.
* List of PCCSs: Hong Kong Council for Testing and Certification website; accredited CBs: HKAS HKCAS directory.

### 2. GFA, Site Coverage, or Design Concession Impact
* No GFA/SC impact.

### 3. BD Submission & Certification Procedures
* On completion: AP/RC may submit CoCs with Certificate and Schedule of Building Materials and Products per **PNAP APP-13**; then **test/assessment reports for those products not required**.
* BD randomly audits CoCs from Schedule; data transferred to Central Data Bank per **PNAP ADM-20**.
* APs should require suppliers to provide relevant test reports (para 2 evaluation) for record and BD submission if needed.
* BD prepared to advise other PCCS scheme owners on BO compliance.

### 4. Critical Red Flags & AP Liability
* Submitting expired, suspended, or scheme-mismatched CoCs.
* Using CoC route for products outside the Issue 3 fire door / non-loadbearing partition acceptance without BD confirmation.
* Failing to retain supplier test reports for audit.

---

## PNAP APP-166: Metal Grille and Louvre
**Status/Context:** First issue December 2021; this revision January 2026 (AD/NB2) — paragraphs 4 & 5 added, paragraph 7 amended. Defines grille vs louvre; structural submission triggers by function Type 1–3.

### 1. Core Technical Requirements & Metrics
* **Type 1 (external cladding):** Structural submission required if any part installed **above 6 m** from adjoining ground/floor (ref. APP-16 para 4); design ref. ADV-33 Appendices B6 & B9.
* **Type 2 (wholly/partly external wall):** Submission if structural span **>6 m**, **or** design wind pressure **≥2.86 kPa** and structural opening area **>6 m²** or least dimension **>1.8 m** (ref. APP-37 paras 4–7); design ref. ADV-33 B7 & B10.
* **Type 3 (protective barrier):** Structural submission **always**, except when also Type 2 and meeting Type 2 exemption criteria; design ref. APP-110 para 5.
* Interior facing/architectural decoration on interior structure: structural submission **not** required.
* Other materials (concrete/glass): follow relevant CoPs.

### 2. GFA, Site Coverage, or Design Concession Impact
* No specific GFA concession rules in this PNAP.

### 3. BD Submission & Certification Procedures
* Structural plans must include: framing/elements; anchors/supports; design loads/standards/CoPs; material specs; workmanship for connections/protection; calculations (parent structure check, system stability, element design, deflection if applicable).
* **Streamlined alternative:** RSE may put typical details/layout/general notes in **superstructure plans** instead of separate grille/louvre structural plans; location/layout/elevation still on GBP; AP & RSE ensure compatibility with approved GBP and BO/regulations (ADV-33 B7 checklist / B10 samples).
* Where submission not required: AP & RSE still responsible for safe design/fabrication/installation.
* **DEW:** B(MW)R Sch.2 Part 2 item 27 — metal window security grille or metal wind guard for external wall opening meeting description = designated exempted works.
* **Minor works:** No specific grille/louvre MW item; may fall under MW 3.31 (cladding), 2.8/3.6 (window/window wall), 1.6 (protective barrier) — see APP-147 / Sch.1 B(MW)R.

### 4. Critical Red Flags & AP Liability
* Omitting structural submission for Type 1 above 6 m, Type 2 span/wind-opening triggers, or Type 3 barriers.
* Relying on streamlined superstructure notes without GBP location/elevation consistency.
* Misclassifying protective-barrier louvres as “decoration” to avoid submission.

---

## PNAP APP-167: Quality of In-situ Reinforced Concrete Works at an Early Age
**Status/Context:** First issue March 2022 (AD/NB2). Early-age quality control for structures using different concrete grades; alert system via rebound hammer tests (RHT). Similar PN to RC. Cross-ref APP-158 QC items.

### 1. Core Technical Requirements & Metrics
* Where different concrete grades used: BA will impose s.17(1) item 6 condition on **first approval of superstructure plans** requiring RHT on higher-grade elements at early age (Appendix A).
* **Timing:** Between **7th and 10th day** after casting (if holiday, next working day); method **BS EN 12504-2:2021**.
* **Minimum testing frequency (RSE randomly selects elements):**
  * Vertical elements of higher grade than immediate supports at base (pile cap/footing/raft/transfer plate/transfer beam): **50%** (kickers included if present).
  * Vertical elements higher grade than adjoining beams/slabs at top: **10%**.
  * Transfer beams: **50%**.
  * Beams higher grade than adjoining beams/slabs on same floor: **10%**.
* **Supervision:** RSE decides elements/frequency (≥ table minima); RSE’s TCP **T3** witnesses **≥10%** of RHTs; RHT by RC’s TCP **T1+** trained in rebound hammers (or HOKLAS lab); records on Annex form; kept on site for RSE TCP.
* **Alert levels (empirical, absent engineering assessment):**
  * With PFA or GGBS: RHT equivalent **<55%** of minimum characteristic strength → follow-up.
  * Without PFA/GGBS: **<65%** → follow-up.
* **Follow-up:** Examine approved plans, order/delivery, method/curing, supervision records; additional RHT/coring; enhance supervision of similar elements; keep review and if necessary **report to BD and suspend concrete works** until follow-up complete.
* **Alternative:** Maturity method on **7th day** per Concrete Code 2013 clause 11.7.5.4; same measuring points and alert levels as RHT.

### 2. GFA, Site Coverage, or Design Concession Impact
* No GFA/SC impact.

### 3. BD Submission & Certification Procedures
* Condition attached at first superstructure approval for multi-grade structures.
* Maintain Annex RHT records on site; ongoing projects: RSE/RC should advise clients to consider implementing the system even if not imposed.

### 4. Critical Red Flags & AP Liability
* Skipping early RHT on transfer systems / higher-grade verticals when multi-grade design used.
* Missing T3 witnessing ≥10%; inadequate follow-up/reporting when below alert thresholds — structural safety liability.

---

## PNAP APP-168: Code of Practice for the Structural Use of Steel 2011
**Status/Context:** First issue March 2023; this revision April 2026 (AD/NB2). Points to Steel Code **2023 Edition** and promulgates Appendix A amendments (**April 2026**) with **immediate effect**. Prior amendments Nov 2016 / May 2021 / Mar 2023 summarised in BD old-versions zip link.

### 1. Core Technical Requirements & Metrics
* April 2026 amendments (subjects — full text in Appendix A / Steel Code 2023 Edition as amended) include among others:
  * Cl. 3.1.3 — clarify Ys and Us for ultra high strength steels (>690 N/mm²) by reference to cl. 3.1.2.
  * Cl. 3.1.5 — delete duplicated paragraph.
  * Cl. 3.4 — welding different steel grades clarification.
  * Cl. 5.3.4 — building acceleration limits revised.
  * Eqs 9.9 / 9.10 — lap joint typo; net cross-sectional area clarification.
  * Cl. 10.1.2 / Table 10.1 — short-term elastic modulus of concrete added.
  * Fig. 10.17 — composite column classification; Cl. 10.5.1(3) — allowable concrete/steel grades in composite columns revised; Cl. 10.5.2(5) — QC for CFST composite columns; Table 10.11 — geometric ratios; Cl. 10.5.3.2 — design strengths; Table 10.13 — buckling curves/imperfections; Cl. 10.5.3.3 — buckling strength checks.
  * Cl. 13.6.4 — footbridge vibration response requirements.
  * Cl. 14.3.2 / 14.3.3 / Table 14.2b / Annex A1.4.2.2 — mechanised/automatic welding requirements and carbon equivalent definition; Annex A2.5 — vibration reference for steel-framed systems.

### 2. GFA, Site Coverage, or Design Concession Impact
* No GFA/SC provisions.

### 3. BD Submission & Certification Procedures
* Design structural steelwork to Steel Code 2023 Edition as amended April 2026 (immediate).
* Composite column and welding/automation QC updates may affect quality supervision / documentation expected at consent/completion.

### 4. Critical Red Flags & AP Liability
* Designing CFST/composite columns or UHSS to pre-April 2026 clauses without checking revised strengths, geometric limits, buckling curves, and concrete QC.
* Ignoring new mechanised/automatic welding acceptance standards and footbridge vibration criteria.

---

## PNAP APP-169: Strength Tests for Structural Fixings in Concrete
**Status/Context:** First issue October 2023 (AD/NB2). Pre-accepted proof load method statements for drilled-in anchors and grouted bolts/dowels/rebars / T-bolts with cast-in channels; BA may impose strength tests under BO s.17(1) item 6.

### 1. Core Technical Requirements & Metrics
* Verify manufacturer’s recommended tensile and/or shear loads by proof load tests; test load **≥1.5 × recommended load**.
* **Appendix A — drilled-in anchors for cantilevered structure / hanger / curtain wall remedial works:**
  * Sampling: **≥5% or 5 nos.** (whichever more) of each type and size.
  * Full apparatus rules (frame supports ≥8A; displacement gauge ≥12A for tension accuracy 0.02 mm; shear steel block 5d diameter etc.; PTFE ≤2 mm; load accuracy 2%).
  * Procedure: visual check; preload ≤1%; load continuously 9–11 N/(mm²·s) or ≥10 equal increments; hold **≥1 hour** at max load; unload ≥5 decrements; record recovery.
  * Acceptance: no separation/plastic deformation/deleterious effect; **recovery of deformation ≥80%** of total deformation at max load; plot force vs displacement; record failure modes.
* **Appendix B — drilled-in anchors for other works:** Sampling **≥1% or 5 nos.**; simplified procedure — load at constant rate, hold **≥2 minutes**, unload; acceptance = no adverse signs (no 80% recovery criterion); apparatus similar but tension displacement independent gauge not mandated as in A.
* **Appendix C — cementitious/polymer grouted bolts/dowels/rebars or steel T bolts with cast-in channels for curtain wall/cladding:** Sampling **≥1% or 5** of each type/size/embedment (or assemblies); supports ≥8A or **2hef** for cast-in channels; load/hold **≥2 minutes**; acceptance = no adverse signs; record extended failure modes including cast-in channel leg failure.

### 2. GFA, Site Coverage, or Design Concession Impact
* No GFA/SC impact.

### 3. BD Submission & Certification Procedures
* If tests follow Appendix A, B or C: RSE may **quote the relevant Appendix** on submitted plans — **method statement submission not required**.
* Alternative method statements: must be submitted to BD for agreement.

### 4. Critical Red Flags & AP Liability
* Using Appendix B sampling/hold criteria for cantilever/hanger/curtain-wall remedial anchors (must use Appendix A 5%/1-hour/80% recovery).
* Inadequate reaction distances or measurement accuracy; failing to report premature failure loads/modes.

---

## PNAP APP-170: Code of Practice for Demolition of Buildings 2004
**Status/Context:** First issue October 2023 (AD/NB2). Promulgates Appendix A (September 2016) and Appendix B (October 2023) amendments; uploaded to BD website. Similar PN to registered contractors.

### 1. Core Technical Requirements & Metrics
* **Sept 2016 major themes (Appendix A summary):** Incorporate RGE statutory role and MWCS Type G demolition; scaffold catchfan/typhoon stability; extra heavy-duty nylon net layer; machinery/aged LCC building demolition guidance; update waste disposal facilities/debris procedures. Key metrics from amendment table include: bamboo scaffold ties ≤4 m H&V; scaffolds >15 m need steel brackets ≤15 m intervals; unbraced scaffold after demolition ≤2 m above nearest anchor; optional extra heavy-duty nylon net **min 3.5 mm dia**, mesh **≤50 mm**; tarpaulin fire performance Type B per BS 5867.
* **Oct 2023 major themes (Appendix B summary):**
  * Table 3.4 — propping for lightweight mechanical plant max **5,800 kg**.
  * Cl. 3.8.1 — Hong Kong Institute of Construction (formerly CITA).
  * New 3.8.8 — precautionary measures at interface of adjacent demolition/construction sites.
  * New 3.8.9 — floor openings and free edges.
  * New 3.8.10 — control conveying debris through floor openings.
  * Cl. 3.10.7 — C&D material disposal clarification.
  * Exterior column demolition method/Fig 4.5 revisions.
  * Form BA20 personal information posting near site front entrance.
  * Appendices F/G figures — temporary platforms required unless cantilevered structures demolished by cut-and-lift or similar (cl. 3.5.1(B)).

### 2. GFA, Site Coverage, or Design Concession Impact
* No GFA/SC provisions.

### 3. BD Submission & Certification Procedures
* Demolition design/method statements and plans must reflect amended Code (RGE involvement where geotechnical aspects; MWCS Type G follow Technical Guidelines, not this Code’s prior-approval path).
* Continuous supervision by RSC (Demolition); safety features designed by AP/RSE/RGE as applicable.

### 4. Critical Red Flags & AP Liability
* Demolition with slopes/RW without RGE input.
* Unsecured cantilevered bamboo above top floor / floor being demolished under typhoon.
* Missing temporary platforms for cantilevers not using cut-and-lift.
* Inadequate interface precautions with adjoining sites; uncontrolled debris through floor openings.

---

## PNAP APP-171: Code of Practice for the Structural Use of Glass 2018
**Status/Context:** First issue February 2024 (AD/NB2). Promulgates Appendix A (July 2020) and Appendix B (February 2024) amendments to Glass Code 2018; on BD website.

### 1. Core Technical Requirements & Metrics
* **July 2020 — Cl. 7.1.1 retaining devices for four-sided structural sealant glazing:** Applies where any point of glass pane is **≥5 m** above finished floor of accessible area on either side; design to prevent fall on bond failure; retaining devices (feature capping, angle, bracket, insert, etc.) at **any two opposing edges**; device and associated glass must resist **37% of design wind pressure × γ=1.0**, where design wind pressure = Wind Code 2019 **reference pressure without adjustment factors**; self-weight on setting blocks.
* **July 2020 — Annex C C2:** Torsional inertia J uses depth d and thickness t: \(J = d\,t^3/3\,(1-0.63\,t/d)\); G=28,700 N/mm², E=70,000 N/mm² for glass fins.
* Other 2020: gaskets on both sides of “glass pane” (typo fix); deglazing test wording or/and factory quality.
* **Feb 2024:** Fig. 6.1 — delete 8 mm dia. weep holes for external application in typical glass balustrade details; Cl. 8.3.1(b) — repeated ± pressure test **p2** = net wind pressure **P** on mullion of representative performance-test portion per Wind Code **2019** (≥5 pulses); if Wind Code 2004 used for curtain wall, p2 = cp × qz for that part; Annex B failure load symbol revised to \(W_{max}\).

### 2. GFA, Site Coverage, or Design Concession Impact
* No GFA/SC provisions.

### 3. BD Submission & Certification Procedures
* Curtain wall/structural sealant designs and performance tests must reflect amended Glass Code clauses.
* Structural sealant retaining-device strength check and wind reference basis should be explicit in RSE submissions.

### 4. Critical Red Flags & AP Liability
* Four-sided SSG ≥5 m without opposing-edge retaining devices sized for 37% wind reference pressure.
* Performance tests still using obsolete p2 definition under Wind Code 2019 projects.
* Relying on Fig. 6.1 weep-hole detail that was deleted.

---

## PNAP APP-172: Residential Care Homes for the Elderly and Residential Care Homes for Persons with Disabilities
**Status/Context:** First issue April 2024 (AD/NB1). Facilitating BO modifications for RCHE/RCHD; plus higher PR under time-limited LandsD/SWD incentive schemes for new private developments.

### 1. Core Technical Requirements & Metrics
* Although habitation = domestic under BO, BA may modify to treat RCHE/RCHD premises as **non-domestic** (or non-domestic part of composite) for B(P)R regs **19, 20, 21, 22**, and allow **non-provision of open space** under reg. **25**, if **all** criteria met:
  * (a) No adverse SWD comments (including ambulant resident access);
  * (b) No FSD objection;
  * (c) Comply with BO/regs including structure, fire safety, adequate headroom, natural lighting & ventilation;
  * (d) Comply with B(P)R regs **49(1)** and **49B** (modification for genuine hardship possible case-by-case);
  * (e) Comply with Cap. 459A s.20 or Cap. 613A s.21; **not in basement**;
  * (f) **Not** in an industrial building.
* Incentive schemes (LandsD PN 5/2023 & 10/2023; SWD Guidance Notes): during pilot period, BA prepared to modify for **higher plot ratio** to accommodate additional GFA of eligible RCHE/RCHD, considering PlanD advice on OZP/planning approval; must also meet para 2 criteria. GFA calculation guideline in LandsD/SWD annexes.
* Para 2 measures: new buildings and A&A for new/additional RCHE/RCHD. Para 4 higher PR: **new developments only** under the two incentive schemes.

### 2. GFA, Site Coverage, or Design Concession Impact
* RCHE/RCHD remain **accountable for GFA** under B(P)R; facilitation is domestic→non-domestic treatment for SC/PR (regs 19–22) and open space, plus possible **higher PR** for eligible new-development incentive premises — not a blanket GFA exemption of the care home itself.

### 3. BD Submission & Certification Procedures
* Apply for modifications with supporting SWD/FSD clearances and Cap. 459A/613A compliance evidence; align GBP with OZP/planning for incentive PR.
* Demonstrate regs 49(1)/49B and NL&V/fire/structure compliance on plans.

### 4. Critical Red Flags & AP Liability
* Seeking non-domestic treatment for RCHE/RCHD in **IBs** or **basements**.
* Claiming higher PR outside incentive schemes or without PlanD/OZP alignment.
* Incomplete SWD/FSD clearances while relying on facilitation.

---

## PNAP APP-173: Hostels in the City Scheme
**Status/Context:** First issue July 2025; this revision September 2025 (AD/NB1) — paragraph 3 amended; paragraphs 13–15 added (newly built hostels per 2025 Policy Address). Facilitation for EDB-confirmed eligible student hostels under Scheme (www.studenthostel.gov.hk). Does not override LandsD/PlanD/FSD/TD etc.

### 1. Core Technical Requirements & Metrics
* **Conversion (existing commercial/hotel) — eligible hostels:** BA prepared to:
  * Treat as non-domestic (or part) for **SC & PR** under B(P)R 19–22;
  * Allow non-provision of open space (reg.25) and service lane (reg.28 case merits, e.g. no existing lane + acceptable servicing);
  * Permit non-provision of kitchens in individual units (reg.45) subject to **communal canteen/kitchen/pantry**.
* Still must comply with other domestic requirements (e.g. NL&V) and hostel/dormitory fire safety.
* **Hostel facilities GFA exemption (Appendix):** linen store; laundry; study/collaboration/leisure room; gymnasium/sports; communal kitchen/pantry/canteen; staff rest/toilet; other EDB+BA-accepted support facilities.
* **Redundant previously exempted/disregarded GFA:** may convert to mandatory features, plant rooms, green/amenity, hostel facilities favourably (APP-151 pre-requisites if A&A results in new building). Former hotel Cap.349 pick-up/set-down and BOH disregarded under reg.23A(3) may convert to hostel facilities with reg.23(3)(a) modification. Redundant <5% of hostel GFA → hostel facilities up to 5%; redundant >5% → may convert all redundant to hostel facilities; exemption of hostel facilities **>5%** considered case-by-case.
* **Partial conversion:** allowed if Scheme Application Guidelines met (EDB + DevB DPFO); “total GFA of student hostel” = hostel-portion GFA only.
* **Newly built hostels (from this PN issuance):** same SC/PR non-domestic treatment; open space/lane; kitchen non-provision; exempt hostel facilities **up to 5%** of total hostel GFA — subject to **APP-151 pre-requisites** but **not** overall GFA concession **cap**; treated as non-residential for JPN 1 & 2, APP-42, APP-104.
* **Loss of Scheme status:** exemptions revoked; owner must appoint AP to submit change-in-use demonstrating BO compliance or face BD enforcement.

### 2. GFA, Site Coverage, or Design Concession Impact
* Non-domestic SC/PR treatment; open space/lane and kitchen modifications; Appendix hostel facilities GFA-exempt (caps and APP-151/overall-cap rules differ for conversion vs new-build as above). Previously disregarded hotel BOH/pick-up can roll into hostel facilities. New-build hostel facilities concessions not subject to overall APP-151 GFA cap (but still need APP-151 pre-requisites).

### 3. BD Submission & Certification Procedures
* Eligibility confirmation by EDB under Scheme required before relying on facilitation.
* Apply for specific B(P)R modifications/exemptions; document communal catering if no unit kitchens; list hostel facilities for GFA exemption; coordinate LandsD/PlanD/FSD/TD.
* New-build facilitation applies to new GBP or major revision submitted **on or after** issuance of this PN (Sept 2025 revision content for paras 13–15).

### 4. Critical Red Flags & AP Liability
* Claiming facilitation without EDB Scheme eligibility.
* Omitting communal canteen/kitchen/pantry when seeking unit kitchen exemption.
* Exceeding 5% hostel-facility GFA exemption without case approval (or without counting redundant conversion correctly).
* Continuing to operate under revoked Scheme status after cessation as student hostel.

---

## PNAP APP-174: Code of Practice for Precast Concrete Construction 2016
**Status/Context:** First issue June 2026 (AD/NB2). Promulgates Appendix A (November 2020) and Appendix B (June 2026) amendments to Precast CoP 2016; on BD website.

### 1. Core Technical Requirements & Metrics
* **Nov 2020 (Appendix A) highlights:**
  * Cl. 2.4.3 — corrosion cover: follow **Concrete Code 2013** (not Building (Construction) Regulations alone for corrosion).
  * Cl. 2.4.4.1 — connection fill also to prevent **water seepage**.
  * Cl. 2.6.1 — materials per B(C)R **and** Concrete Code 2013.
  * Cl. 2.6.2.1 ASR — expanded mitigation: expert advice before alkali-reactive aggregates; non-reactive aggregate per CS1; reduce moisture ingress; retain ≤**3.0 kg/m³** equivalent Na₂O and supplier mix design + HOKLAS certificates.
* **June 2026 (Appendix B) highlights:**
  * New Table **2.7a** — on-site water-tightness testing of completed panel joints and window joints per **AAMA 501.2**: **100%** samples; nozzle pressure **205–240 kPa**; hose dia **19 mm**; **5 min** per **1.5 m** joint length; nozzle distance **305±25 mm**; failure = dampness/leakage on interior during test or within **2 hours**; remedy and **retest** failed joints.
  * Cl. 2.7.9.4 redesign of ultimate bearing: \(f_{cb}=0.27\,m\,f_{cu}\) (dry), \(0.40\,m\,f_{cu}\) (bedded), \(0.80\,m\,f_{cu}\) (steel plate ≤40% corresponding concrete dimension); \(m=\sqrt{A_2/A_1}\le 2\) confinement factor (new Fig. 2.5a); symbol \(f_{cb}\) added.
  * Cl. 2.8.2.8 Testing rewritten to mandate AAMA 501.2 procedures for completed joints; Annex A references updated (AAMA 501.1–501.3, ASTM C719, C794, C920, C1087, E283, E330, E331, E547, ANSI Z97.1, BS 6213).

### 2. GFA, Site Coverage, or Design Concession Impact
* No GFA/SC provisions.

### 3. BD Submission & Certification Procedures
* Design precast bearing and connections to amended cl. 2.7.9.4.
* Plan/demonstrate AAMA 501.2 field joint testing (100% of completed panel/window joints) with failure/remeasurement protocol; retain HOKLAS ASR package where applicable.

### 4. Critical Red Flags & AP Liability
* Using old 0.4/0.6/0.8 \(f_{cu}\) bearing stresses without confinement factor \(m\).
* Relying on hose spray description without AAMA 501.2 parameters / 100% joint coverage / 2-hour post-test observation.
* ASR control without 3.0 kg/m³ reactive alkali documentation.

---

## Batch completion note

| APP | Title (short) | In batch |
|-----|----------------|----------|
| 156 | Residential energy efficiency (RTTV/OTTV/NVTC) | Yes |
| 157 | Site Supervision Code 2009 (2024 Ed.) | Yes — **appendices OCR incomplete** |
| 158 | Quality supervision of building works | Yes |
| 159 | Deter IB misuse for residential use | Yes |
| 160 | — | **Missing** |
| 161 | — | **Missing** |
| 162 | BO s.17 approval/consent conditions (incl. 4S >$30M) | Yes |
| 163 | Access for External Maintenance Code 2021 | Yes |
| 164 | Enhanced aboveground drainage standards | Yes |
| 165 | Product Certification System | Yes |
| 166 | Metal grille and louvre | Yes |
| 167 | Early-age in-situ RC quality (RHT) | Yes |
| 168 | Structural Use of Steel Code 2011 (2023 Ed./2026 amd) | Yes |
| 169 | Strength tests for structural fixings in concrete | Yes |
| 170 | Demolition of Buildings Code 2004 | Yes |
| 171 | Structural Use of Glass Code 2018 | Yes |
| 172 | RCHE / RCHD facilitation | Yes |
| 173 | Hostels in the City Scheme | Yes |
| 174 | Precast Concrete Construction Code 2016 | Yes |

**Completed APP list:** APP-156, APP-157, APP-158, APP-159, APP-162, APP-163, APP-164, APP-165, APP-166, APP-167, APP-168, APP-169, APP-170, APP-171, APP-172, APP-173, APP-174.
