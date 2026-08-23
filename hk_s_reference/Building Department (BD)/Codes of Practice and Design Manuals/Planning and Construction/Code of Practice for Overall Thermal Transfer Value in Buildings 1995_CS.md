# Code of Practice for Overall Thermal Transfer Value in Buildings 1995
**Architect critical summary for schematic design**  
April 1995 | Building Authority / Buildings Department

> Scope note: Deemed-to-satisfy technical method for a **suitable OTTV** under the **Building (Energy Efficiency) Regulation (Cap. 123M)** — commercial buildings and hotels only. This Code still supplies the **calculation formulas, coefficient tables, and Forms OTTV1–4**. Numeric caps and podium practice are amended by **PNAP APP-67** (current tower **≤ 20 W/m²**, podium **≤ 40 W/m²** for new / major-revision plans submitted on or after **31 Dec 2025**). Do **not** design to the 1995 printed caps of 35 / 80. For statute + APP-67 process (consent / OP, open-front shops, sunshade GFA/SC), see Cap 123M and APP-67 Architect Critical Summaries. Residential RTTV is **APP-156**, not this Code.

---

## Regulatory Overview

This Code applies to **hotels and commercial buildings** under Cap 123M and sets how to calculate OTTV of external walls and roofs so the envelope meets a “suitable” overall thermal transfer value — compliance with the Code may be deemed to satisfy Cap 123M.

Limits are **overall envelope averages** for the **building tower** and the **podium** separately (walls + roofs together as applicable); they do **not** apply elevation-by-elevation or to a single wall/roof in isolation.

---

## Critical main topics and subtopics

### 1. Does this Code apply? Lock the calculation boundary first (§§1.6–1.8, 2, 4)

| In scope | Out of Cap 123M / this Code |
|---|---|
| Commercial buildings (offices, shops, F&B, entertainment, assembly, etc.) | Domestic, industrial, schools, bulk storage, utility buildings |
| Hotels (Schedule item 2 — separate from “commercial”) | Residential RTTV track (APP-156) |
| Schedule-use parts + ancillary spaces on mixed-use | Pure domestic / industrial floors |

**Envelope assumptions that change the model:**
- Building envelope is treated as **completely enclosed** (§1.7).
- **No credit** for internal blinds/drapes, or solar reflection / shading from **adjacent buildings** (§1.8).

| Include in OTTV calc | Exclude (§4.1) |
|---|---|
| All external walls & roofs of tower / podium (unless listed right) | External walls of a **refuge floor** |
| **Party walls** — whether an adjoining building exists or not (§4.2); **no** adjoining-building shade credit | External walls **and roof** of a **carparking** floor |
| | External walls of a **lightwell** with plan area **≤ 21 m²** |
| | **Any wall on any roof** |

**Key definitions (§2):**

| Term | Meaning for SD |
|---|---|
| **Building tower** | Part of the building **above the podium** |
| **Podium** (1995 Code) | Part within **15 m** above ground level (with B(P)R 20(3) / s.42 modification nuance for excess SC) |
| **Fenestration** | Any glazed aperture in the envelope (windows, glass walls, skylights) |
| **Opaque** wall/roof | Solid portion that is **not** fenestration |
| **Lightwell** | Vertical open-air shaft enclosed on all sides by the building |
| **Refuge floor** | As in MOE Code — protected assembly floor |

**APP-67 overlay (not in 1995 text):** for APP-132 varying site coverage, notional podium height for OTTV may be regarded as **20 m** above mean street level (may demarcate lower). Lock the podium / tower cut-line early — it assigns area to the tighter tower band vs the looser podium band.

**SD takeaway:** Draw the OTTV boundary on GAs at schematic: carve out carpark, refuge, small lightwells, roof parapet walls; keep party walls in with no neighbour-shade credit.

---

### 2. Suitable OTTV caps — printed 1995 vs what you design to today (§3 + APP-67)

| Envelope zone | 1995 Code (§3.1) | Current APP-67 (plans on/after 31 Dec 2025) |
|---|---|---|
| **Building tower** | ≤ **35** W/m² | ≤ **20** W/m² |
| **Podium** | ≤ **80** W/m² | ≤ **40** W/m² |

- Caps apply to the **overall average** of all external walls and roofs of that tower or podium — **not** to individual elevations (§3.2).
- Assess OTTV per methods in this Code (§3.3); sample calc in Appendix.

**SD takeaway:** Use **20 / 40** as the BA floor for current submissions. Client / BEAM Plus targets may be stricter. The 1995 35 / 80 figures are historical method-document caps only.

---

### 3. Schematic design levers the Code expects you to trade (§1.2–1.5)

| Lever | Why it matters |
|---|---|
| Glazing type (SC, and VLT balance) | Dominates solar term through fenestration |
| Window size / **WWR** | Scales both conduction and solar terms |
| **External** shading (overhangs / sidefins) | ESM multiplies the solar term — paramount (§7.6) |
| Wall / roof colour (**α**) | Multiplies opaque heat gain |
| Wall / roof type (U + mass / density) | U and \(TD_{EQ}\) both move with build-up |

**Orientation cue (§1.3):** avoid extensive glazed façades with a **southerly** aspect; if used, provide external shading and/or low-heat-gain glazing.

**Daylight vs cooling (§1.4):** size/place windows for daylight to cut artificial lighting heat, but select glass balancing **visible light transmittance** against thermal transmittance.

**SD takeaway:** Own orientation, WWR by elevation, glass SC, overhang/fin strategy, and opaque colour/mass **before** freezing the façade system — not as late GS polish.

---

### 4. Wall OTTV formula (§5)

\[
OTTV_w = \frac{(A_w \times U \times \alpha \times TD_{EQw}) + (A_{fw} \times SC \times ESM \times SF)}{A_{ow}}
\]

| Symbol | Meaning | Source |
|---|---|---|
| \(A_w\) | Opaque wall area (m²) | GA / elevation take-off |
| \(U\) | Opaque wall U-value (W/m²°C) | §7.1 + Tables 1–3 |
| \(\alpha\) | Opaque wall absorptivity | Table 4 |
| \(TD_{EQw}\) | Equivalent temp. difference for wall (°C) | Table 5 (density × orientation) |
| \(A_{fw}\) | Fenestration area in wall (m²) | Window schedule |
| \(SC\) | Shading coefficient of fenestration | Manufacturer (normal incidence) §7.5 |
| \(ESM\) | External shading multiplier | Tables 6–7 |
| \(SF\) | Solar factor, vertical (W/m²) | Table 8 |
| \(A_{ow}\) | Gross wall area = \(A_w + A_{fw}\) | — |

**SD takeaway:** Opaque term is mass- and colour-sensitive; glazed term is almost always the driver — WWR × SC × ESM × SF. No ESM credit without real external projections measured as OPF / SPF.

---

### 5. Roof OTTV formula (§6)

\[
OTTV_r = \frac{(A_r \times U \times \alpha \times TD_{EQr}) + (A_{fr} \times SC \times SF)}{A_{or}}
\]

Same logic as walls, but:
- **No ESM** term for roof fenestration / skylights
- \(TD_{EQr}\) from **Table 9** (density only — not orientation)
- \(SF\) for **horizontal** surface from Table 8 (= **264** W/m²)

**SD takeaway:** Skylights sit on a high SF (264). Opaque roof mass and light-coloured / low-α finishes are early RTTV/OTTV tools; green / insulated roofs need Code-table or BA-accepted properties.

---

### 6. Opaque U-value build-up (§7.1–7.2)

\[
U = \frac{1}{R_i + \sum (x_i / k_i) + R_a + R_o}
\]

| Symbol | Meaning | Source |
|---|---|---|
| \(x\) | Layer thickness (m) | Spec / detail |
| \(k\) | Thermal conductivity (W/m°C) | **Table 1** |
| \(R_i\), \(R_o\) | Internal / external surface film resistance | **Table 2** |
| \(R_a\) | Air-space resistance | **Table 3** |

**Table 2 — film resistance highlights (m²°C/W):**

| Surface | Value |
|---|---|
| Wall \(R_o\) (external) | **0.044** |
| Wall \(R_i\) (α ≥ 0.5) | **0.120** |
| Wall \(R_i\) (α < 0.5) | **0.299** |
| Roof \(R_o\) (external) | **0.055** |
| Flat roof \(R_i\) (α ≥ 0.5 / α < 0.5) | **0.162** / **0.801** |

**Table 1 — k-value cues for common HK build-ups (W/m°C):** normal concrete **2.16**; mosaic tile **1.50**; cement/sand plaster **0.72**; glass fibre quilt **0.035**; expanded polystyrene **0.034**; polyurethane foam **0.026**; aluminium alloy **160**; steel **50**.

**Non-listed materials:** k (and α) subject to **BA acceptance**; submit source of values (§7.2 note / Table 4 note). APP-67 also wants suitability for **local conditions**.

**SD takeaway:** Spandrel / roof insulation thickness and cavity air space are quantitative OTTV tools. Exotic cladding needs a properties dossier before consent.

---

### 7. Absorptivity α — colour is a code parameter (Table 4 / §7.3)

α multiplies the opaque \(TD_{EQ}\) term. Simulation studies for HK: surface colour has a **significant** effect on chiller energy.

| Finish cue | Typical α (Table 4) |
|---|---|
| Black glass / flat black paint | ~1.0 / 0.95 |
| Red brick / dark paints | ~0.88–0.91 |
| Uncoloured concrete | **0.65** |
| White mosaic / white marble | **0.58** |
| White gloss / silver paint | **0.25** |
| Polished aluminium reflector | **0.12** |

**SD takeaway:** Light / reflective external finishes cut opaque heat gain. Spec colour early enough that α in the OTTV model matches the tender façade.

---

### 8. Wall \(TD_{EQw}\) — density × orientation (Table 5 / §7.4)

Heavyweight construction resists heat better than lightweight. Use **gross wall mass** (kg/m²) including finishes.

**Full Table 5 — \(TD_{EQw}\) (°C):**

| Orientation | < 22 kg/m² | 23–199 | 200–379 | 380–569 | ≥ 570 |
|---|---:|---:|---:|---:|---:|
| N | 3.70 | 3.38 | 2.72 | 2.05 | 1.70 |
| NNE | 4.65 | 4.21 | 3.30 | 2.36 | 1.88 |
| NE | 5.60 | 5.03 | 3.86 | 2.67 | 2.05 |
| ENE | 6.55 | 5.86 | 4.44 | 2.98 | 2.23 |
| E | **7.50** | 6.68 | 5.01 | 3.28 | 2.40 |
| ESE | 7.05 | 6.26 | 4.65 | 3.00 | 2.15 |
| SE | 6.60 | 5.85 | 4.30 | 2.71 | 1.90 |
| SSE | 6.15 | 5.43 | 3.95 | 2.43 | 1.65 |
| S | 5.70 | 5.01 | 3.60 | 2.15 | **1.40** |
| SSW | 6.15 | 5.42 | 3.92 | 2.37 | 1.58 |
| SW | 6.60 | 5.82 | 4.23 | 2.59 | 1.75 |
| WSW | 6.55 | 5.81 | 4.29 | 2.73 | 1.93 |
| W | 6.50 | 5.79 | 4.35 | 2.86 | 2.10 |
| WNW | 5.80 | 5.19 | 3.94 | 2.66 | 2.00 |
| NW | 5.10 | 4.59 | 3.54 | 2.45 | 1.90 |
| NNW | 4.40 | 3.98 | 3.13 | 2.25 | 1.80 |

**SD takeaway:** Worst opaque \(TD_{EQ}\) is **lightweight East** (7.50). Best is **heavy South** (1.40). Do not run curtain-wall spandrels as “light” without checking density band.

---

### 9. Glass SC and external shading ESM (§§7.5–7.6)

#### 9.1 Shading coefficient (SC)

SC = solar heat gain through the glass ÷ solar heat gain through double-strength sheet **clear** glass under the same conditions. HK latitude / solar effects are already in **SF** — use manufacturer SC at **normal angle of incidence** without further latitude modification (§7.5).

#### 9.2 Overhangs — OPF and Table 6

\[
OPF = \frac{A}{B}
\]

- **A** = horizontal depth of overhang (outer face of glass → tip of overhang)
- **B** = vertical distance (window sill → underside of overhang)

| OPF | ESM N | ESM NE/NW | ESM S/E/W | ESM SE/SW |
|---:|---:|---:|---:|---:|
| 0.00 | 1.000 | 1.000 | 1.000 | 1.000 |
| 0.25 | 0.883 | 0.853 | 0.823 | 0.823 |
| 0.50 | 0.781 | 0.726 | 0.672 | 0.672 |
| 0.75 | 0.693 | 0.621 | 0.549 | 0.549 |
| 1.00 | 0.621 | 0.537 | 0.453 | 0.453 |

**Table 6 rules:** if OPF falls between listed 0.05 steps → use ESM for the **next larger** OPF; OPF **> 1.0** not covered (estimation error too large); S/E/W combined because figures are similar.

#### 9.3 Sidefins — SPF and Table 7

\[
SPF = \frac{C}{D}
\]

- **C** = depth of sidefin projection
- **D** = clear distance between opposing sidefins (plan)

| SPF | ESM N | E | S | W |
|---:|---:|---:|---:|---:|
| 0.00 | 1.000 | 1.000 | 1.000 | 1.000 |
| 0.20 | 0.828 | 0.898 | 0.855 | 0.897 |
| 0.50 | 0.613 | 0.766 | 0.673 | 0.765 |
| 1.00 | 0.370 | 0.599 | 0.459 | 0.604 |
| 1.50 | 0.271 | 0.499 | 0.359 | 0.517 |

**Table 7 rules:** SPF **> 1.5** not covered; between increments → adopt ESM for **next larger** SPF. Full 8-orientation grid is in the Code (N, NE, E, SE, S, SW, W, NW).

#### 9.4 Combined overhang + sidefin (§7.6(c))

Calculate overhang ESM and sidefin ESM **separately**; use the **smaller** of the two — do **not** multiply or stack both credits.

**SD takeaway:** Overhangs help S/E/W more than N. Deep fins help N strongly. Combined systems take the **better single** ESM only. Cap 123M s.6 / APP-67 sunshade GFA–SC concessions (≤ 1.5 m; quantitative proof if > 750 mm) are separate from ESM — design shading as a real OTTV device documented in the calc.

---

### 10. Solar factor SF (Table 8 / §7.7)

| Orientation | SF vertical (W/m²) | Orientation | SF vertical |
|---|---:|---|---:|
| N | **104** | S | **191** |
| NNE | 121 | SSW | 197 |
| NE | 138 | SW | **202** |
| ENE | 153 | WSW | 189 |
| E | 168 | W | 175 |
| ESE | 183 | WNW | 157 |
| SE | 197 | NW | 138 |
| SSE | 194 | NNW | 121 |

**SF horizontal (roofs / skylights) = 264**

Sloping walls/roofs: resolve into vertical + horizontal components; apply respective SF (§7.7).

**SD takeaway:** Highest vertical SF is **SW (202)** then SE/SSW (197). Horizontal **264** makes roof/skylight glass expensive in OTTV terms.

---

### 11. Roof \(TD_{EQr}\) (Table 9 / §7.8)

| Density of roof construction | \(TD_{EQr}\) (°C) |
|---|---:|
| < 22 kg/m² | **18.60** |
| 23–199 kg/m² | 16.88 |
| 200–379 kg/m² | 13.37 |
| 380–569 kg/m² | 9.75 |
| ≥ 570 kg/m² | **7.90** |

**SD takeaway:** Heavy roofs cut \(TD_{EQ}\) hard. Lightweight metal roofs without mass sit in the worst band.

---

### 12. Windows and doors — entrance air leakage (§8)

| Rule | SD implication |
|---|---|
| No **unenclosed** doorways / entrances | Vestibule / door strategy required |
| High-traffic commercial entrances | **Self-closing** doors (no hold-open restrainers), **revolving** doors, or equivalent |
| Windows | Detail sealing to limit air leakage in service |

**SD takeaway:** Open lobby / permanently open shopfront strategies conflict with §8 unless Cap 123M / APP-67 open-front carve-outs apply and A/C is separated — coordinate early with retail and BS.

---

### 13. Submission package — Forms OTTV1–4 (§9 + APP-67 sequencing)

| Code requirement (§9) | Detail |
|---|---|
| First GBP | Simplified OTTV calcs acceptable |
| Before **consent** | **Detailed** calcs required |
| Forms | **OTTV 1** — U-values of composite walls/roofs + component coefficients |
| | **OTTV 2** — window & rooflight schedule |
| | **OTTV 3 & 4** — OTTV calculations |
| Precision | Calculate to **two decimal places** |

**APP-67 practice overlay (current):**
- First GBP may omit full Cap 123M s.5 pack
- **OTTV Summary Sheet** (APP-67 App. A) before consent (B(A)R reg. 10)
- Before OP / BA14: final OTTVs + glass SC on record plans; full **OTTV Report** (detailed calcs, Forms OTTV1–4, record plans, material test certs / published specs, final Summary Sheet)

**SD takeaway:** Programme façade consultant + glass procurement against **consent** and **OP** gates. Forms OTTV1–4 are still the calculation vehicle this Code defines.

---

### 14. Schematic go / no-go checklist

Before freezing massing, orientation, WWR, or façade system:

1. Confirm **commercial and/or hotel** Schedule use — otherwise this Code / Cap 123M is off (check APP-156 if domestic).
2. Draw OTTV boundary — **exclude** carpark, refuge walls, lightwells ≤ **21 m²**, roof-top walls; **include** party walls with no neighbour shade.
3. Lock **podium vs tower** cut-line (Code 15 m / APP-67 notional ≤ 20 m for APP-132) and design to **≤ 20 / ≤ 40 W/m²** (current APP-67), not 35 / 80.
4. Set strategy: orientation, WWR by elevation, glass **SC**, overhang **OPF** / sidefin **SPF**, opaque **α** and mass band.
5. Remember combined shading takes the **smaller** ESM only; OPF ≤ 1.0 and SPF ≤ 1.5 for Code tables.
6. Roof / skylight: SF **264**; pick roof density band and insulation early.
7. Commercial entrances: self-closing / revolving / equivalent — no permanent open doorway.
8. Non-Code materials: BA-accepted k / α source + local suitability narrative.
9. Plan documentation path: Summary Sheet → Forms **OTTV1–4** (2 d.p.) → OP report.
10. Do not confuse Cap 123M / this Code with **EMSD BEC**, **BEAM Plus**, or **APP-156** RTTV.

---

### Source

*Code of Practice for Overall Thermal Transfer Value in Buildings 1995*, Building Authority, Hong Kong, April 1995 (Forms OTTV1–4; Tables 1–9; Appendix sample calc).

Companion practice (caps, podium height, consent/OP, open-front shops, sunshade GFA/SC):
- PNAP **APP-67** Energy Efficiency of Buildings (rev. Sep 2025)
- Cap **123M** Building (Energy Efficiency) Regulation
- Cap 123A / B(A)R **reg. 10** (Summary Sheet / Report vehicle)
- Parallel only: PNAP **APP-156** (residential RTTV — not this Code)
