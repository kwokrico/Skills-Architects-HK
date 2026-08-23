# Code of Practice on Wind Effects in Hong Kong 2019
**Architect critical summary for schematic design**  
First issue September 2019 | Amendments December 2023 | Buildings Department  
Companion: *Explanatory Notes to the Code* (Sep 2019) + EN Amendments (Dec 2023) — **integrated below**

> Scope note: **Standard Method** for calculating wind loads on buildings and building elements for structural design. Deemed to satisfy relevant Buildings Ordinance / regulation provisions. Apply this Code’s `γw` = **1.4** with **SUC / steel / concrete / glass** load factors. Dec 2023 Code + EN amendments revise tunnel flowcharts (Figs 2-1 / 2-2), across-wind frequency guidance, hoarding net pressure note, Table 4-1 podium cross-refs, App. A2 / size-factor / damping text — use **amended** documents.

---

## Regulatory Overview

This Code (with EN) sets the **wind actions envelope** for structural design of buildings and parts of buildings in Hong Kong: design pressure `Qz`, along-wind / across-wind / torsional forces, cladding and attachment pressures, occupant comfort accelerations, temporary-works reductions, and when the Standard Method must be abandoned for **wind tunnel testing** (Section 6).

It is intended for **normal / typical constructions** generally **≤ 200 m**. Codified shapes are mostly rectangular blocks and shapes treatable as rectangles; free-form, highly 3D topography, high across-wind response, or **B/D > 6** push the project into tunnel scope at schematic design — lock height, plan aspect, corner strategy, podium–tower relationship, and tunnel fee before freezing massing and façade budgets.

---

## Critical main topics and subtopics

### 0. What changed in 2019 (vs older HK wind practice) — why architects care

| New / emphasised feature | SD consequence |
|---|---|
| Across-wind + torsional forces codified | Slender / tall towers no longer “along-wind only” |
| Load combination factors (lateral + torsion) | Core layout and plan eccentricity matter early |
| **Displacement height** shelter from neighbours | Dense urban sites may reduce effective height — with floors |
| Acceleration / occupant comfort | Residential & Grade-A office comfort can govern structure |
| Wind **directionality** factor `Sθ` | Orientation still matters; circular plans get no relief |
| Updated vertical distribution via **Sq,z** (rises with height) | Top floors / roof plant see higher dynamic amplification |
| Attachment coefficients (fins, balconies, canopies, walls) | Façade extras are structural wind items, not decoration |
| Expanded wind-tunnel rules + shelter minimum loads | Tunnel is not a free reduction licence |

---

### 1. Scope gate — Standard Method vs wind tunnel (§1.1, Figs 2-1 / 2-2 as amended Dec 2023)

Users must satisfy themselves that guidance is **rationally applicable** to the form under consideration. Standard Method covers typical buildings **up to 200 m**. Wind tunnel **should be used** for any of:

| Ref | Trigger | Architect implication |
|---|---|---|
| (a) | **H > 200 m** | Tunnel mandatory — budget + programme from day one |
| (b) | **Unusual shape** not covered by §4 | Free-form, twisted, porous mega-frames, non-codified wings → tunnel |
| (c) | Locations where **complicated topography or surroundings** adversely affect wind | Hillside clusters, channelled valleys, unusual neighbour geometry |
| (d) | Codified across-wind moment **substantially larger** than along-wind (§2.2.3) | If across/along factor **> 1.5** → **must** tunnel |
| (e) | **B/D > 6**, except where §2.2.4 allows torsion cases to be neglected | Very elongated plans / slabs |

**Decision tree (SD):**

```
H > 200 m?                         → TUNNEL
Unusual shape / not in §4?         → TUNNEL
Adverse topography / surrounds?    → TUNNEL (often + topo model)
B/D > 6 and torsion not waived?    → TUNNEL
Else run Standard Method:
  Across-wind needed? (§2.2.3)
    across/along > 1.5?            → TUNNEL
    across > along but ≤ 1.5?      → uprate along-wind forces; stay code
  Else                             → Standard Method OK
```

**SD takeaway:** Height, plan aspect, and “is this a rectangle (or codified wing)?” decide consultant fees in week one. Do not freeze a 210 m free-form tower without tunnel + RSE in the fee proposal.

**EN (special attention):**
- Code rules mostly envelope **simple rectangular** test cases — extended judicially to shapes treatable as rectangular (incl. slight trapezoids; critical wind may **not** be exactly orthogonal).
- **Complex topography** = where App. A3 2D hill/cliff rules cannot be clearly applied (esp. highly 3-dimensional hills) → topo tunnel.
- Where deeper understanding of loads or movements is desirable → tunnel recommended even if Standard Method is formally available.

---

### 2. Definitions & symbols that lock geometry (§1.2 + EN 1.2)

#### 2.1 Building geometry

| Symbol | Meaning — why it matters at SD |
|---|---|
| **H** | Height to **top roof** above ground for the approaching wind. **EN:** on sloping / multi-level ground, take H above **average ground on each face**; for **Qh** it is easier (and not particularly conservative) to use the **greatest** H. Varying H by direction has more value for surroundings / Cf |
| **Hb** | Height excluding irregular roof features that do **not** continue the prismatic form (sloping roofs, small plant crowns) — used for across-wind & acceleration. **EN:** vortex shedding is strong for prismatic forms and weakens for non-prismatic crowns |
| **He** | **Effective** building height after shelter (App. A2); used for Qo, turbulence, Cf |
| **B** | Breadth — horizontal dimension **normal** to wind |
| **D** | Depth — horizontal dimension **parallel** to wind |
| **B/D** | Plan aspect — drives torsion eccentricity `e` and tunnel trigger (e) |
| **b** | Scaling length for pressure zones = **smaller of B or 2H** |
| **d** | Diameter of circular cylinder |
| **w** | Width of wedge in re-entrant or chamfered corners |
| **r** | Corner radius (rounded corners) |
| **h** (unsubscripted) | Parapet / free-standing wall / canopy / signboard height |
| **φ** | Solidity ratio of walls or frames |
| **Xp** | Separation from upwind obstructing building (shelter) |
| **Hi** | Height of obstructing building in surroundings |
| **Hd** | Displacement height (reduction in reference height due to shelter) |

#### 2.2 Pressures, forces, dynamics

| Symbol | Meaning |
|---|---|
| **Qo,z** | Wind reference pressure at effective height Ze, open exposure, flat terrain (Table 3-1) |
| **Qz** | Qo,z corrected for topography (`St`) and directionality (`Sθ`) |
| **Qh** | Qz at effective building height He |
| **Ze** | Effective height after shelter; floor **Ze ≥ 0.25 Z** |
| **Cf** | Force coefficient (overall building) |
| **Cp** | Net / total pressure coefficient (elements) |
| **Cpe / Cpi** | External / internal pressure coefficients (dominant openings) |
| **Ss** | Size effect factor on half-perimeter L0.5p (may be **> 1** for small elements) |
| **Ss,p** | Size factor for internal pressure under dominant openings |
| **Sq,z** | Size and dynamic factor on overall building forces (varies with height) |
| **Wz** | Along-wind load per unit height |
| **ΔTz** | Variable torsional load per unit height about vertical axis through centre of width |
| **e1, e2** | Eccentricity for variable torsion |
| **Fx / Fy** | Along-wind / across-wind forces |
| **Mx y,base** | Peak across-wind moment at base |
| **Az** | Peak acceleration at height Z |
| **γw** | Ultimate wind load factor = **1.4** |
| **ρa** | Air density = **1.2 × 10⁻³ T/m³** (= 1.2 kg/m³) |
| **N, Nx, Ny** | Fundamental frequencies (along / across). Typical construction **< 100 m**: may use **N = 46/H**; otherwise modal analysis with best-estimate stiffness & mass |
| **Mh** | Mass of building above **2 Hb / 3**. May add **25% imposed** with dead loads for mass. E&M rooms: same rule **or** actual imposed + dead |
| **ξx, ξy** | Damping ratios (App. C2) |
| **Iv,z / Io,z** | Turbulence intensity at Z / Ze |
| **St** | Topographic multiplier on pressure, evaluated at **2H/3** |
| **Sθ** | Directionality factor on pressure |
| **Sr** | Return-period factor on pressure (accelerations) |
| **ηy** | Mode deflection ≈ (Z/H)^ηy; typically **1.0–2.0**; default **1.5** in top quarter for acceleration if no modal analysis |
| **(BD)b** | Average plan area of enclosing rectangle over **top third** of building (exclude upper cut-backs for acceleration). Cap: if (BD)b > **H²/9**, take **H²/9** |
| **R** | Return period (years) |
| **L0.5p** | Half-perimeter of loaded / tributary area |

**SD takeaways:**
- Agree **H vs Hb** with RSE before quoting “storeys” — roof plant, crowns, and sloping sites move the numbers.
- **B** and **D** swap with wind direction; elongated plans drive torsion (`e` up to **±0.20 B** at B/D = 6).
- Mass above 2/3 height (Mh) feeds comfort — lightweight top plant rooms / transfer cut-backs can worsen acceleration.

**EN — elements that break the “quasi-static cladding” assumption (§2.1):** usual cladding / attachments are quasi-static only. Flag specialist review for **flexible overhanging roofs**, **long-span façades** (dynamic amplification), and **small-diameter** members (vortex-shedding vibration).

---

### 3. Calculation procedure overview (§2.1)

#### 3.1 Overall structure (Fig. 2-1)

1. Along-wind forces (§2.2.1)
2. Torsional forces (§2.2.2)
3. Across-wind base moment if required (§2.2.3)
4. Combine two orthogonal directions + torsion (§2.2.4 / Table 2-1)
5. Branch to tunnel where flowchart / §1.1 triggers apply (as amended Dec 2023)

#### 3.2 Building elements (Fig. 2-2)

- Enclosed envelope without dominant openings → Eq. 2-3a + Table 4-1
- With dominant openings → Eqs 2-3b–d + App. B1
- Frameworks / attachments / free-standing walls → Tables 4-2, B2, B3

#### 3.3 Occupant comfort

- Peak acceleration (§2.4.1) vs limits Fig. 2-6 (§2.4.2)

---

### 4. Overall wind forces on buildings (§2.2)

#### 4.1 Along-wind (§2.2.1)

```
Wz = Qz · Cf · Sq,z · B
```

| Term | Source |
|---|---|
| Qz | §3 (shelter + topography + directionality) |
| Cf | §4.2 |
| Sq,z | §5.2 (increases toward top) |
| B | Breadth normal to wind |

Components may vary with height. Additional variable torsion at the same height by offsetting Wz (§4.2 below).

#### 4.2 Variable torsion (§2.2.2, Fig. 2-3 + EN)

For buildings that may be treated as rectangular, apply along-wind force at eccentricity from geometric centre of area:

| B/D | Eccentricity e |
|---|---|
| ≤ **1** | **±0.05 B** |
| = **6** | **±0.20 B** |
| Between | Linear interpolation |
| Outside this range | Extrapolate only with **tunnel data** |

**EN why it grows with B/D:** tunnel studies for this Code show increased torsion with elongation from a **trapped vortex** behind the windward end under **diagonal** wind — slab-like plans are torsion-sensitive by physics, not just code conservatism.

```
ΔTz = e1 · Wz,x1    OR    ΔTz = e2 · Wz,x2
```
Take whichever has **greater magnitude**.

For non-rectangular shapes treated as rectangular, use B and D from §4.2 / Figs 4-4.

#### 4.3 Across-wind base moment (§2.2.3 + EN) — tall / slender gate

**Skip across-wind check** (use along-wind without modification) if **all** of:
- H < **100 m**, and
- **H/B < 5** for **all** directions, and
- Fundamental frequency > **0.5 Hz**

Otherwise, for rectangular-treated buildings, compute across-wind base moment (Eq. 2-2) for two orthogonal wind directions. Key inputs: γw = 1.4, ξy (App. C2), Ny, (BD)b over top third, Qh, Iv,h, Hb. (Dec 2023 EN adds guidance on determining fundamental frequency for this check.)

**If across-wind base moment > along-wind base moment** → factor the relevant along-wind force sets upward so along-wind base moments match across-wind (rules (a)–(d) in Code for ±X1 / ±X2).

**Hard tunnel trigger:** if the factor

```
max(|M−y2|, |M+y2|) / max(|M−x1|, |M+x1|)
```
or the analogous X2/Y1 ratio **> 1.5** → **wind tunnel must be conducted**.

**EN — when the Standard Method formula is trustworthy:**
| Calibration / limit | Implication |
|---|---|
| Rectangular **prismatic** form; approx. **linear** mode; mass **relatively uniform** over top half | Formula domain |
| Originally **0.5 < B/D < 2**; experience extends similarly to about **1:4 / 4:1** | Beyond ~4:1, also weigh torsion significance → often tunnel |
| **Tapered / stepped / irregular plan** | Formula often **conservative** (less coherent vortex shedding) — tunnel may unlock better loads |
| Formula does **not** fully capture buffeting by neighbours | Dense clusters: tunnel still valuable |

**EN — critical vortex speed (very slender):**
```
Vcrit ≈ 10 · Ny · B
```
If factored ultimate wind speed at roof > Vcrit, loads do **not** keep rising with Eq. 2-2 — may cap at Vcrit for **preliminary** strength, but **must verify by tunnel**. Otherwise follow Code calculation.

**SD takeaway:** Towers near H ≥ 100 m, H/B ≥ 5, or soft frequency are across-wind candidates. Very slender residential towers often hit the **1.5** tunnel gate. Stepped / tapered massing can reduce across-wind excitation vs a pure prism.

#### 4.4 Load combinations (§2.2.4, Table 2-1)

Lateral loads in two orthogonal directions **and** torsion are applied **simultaneously** with combination factors:

| Case | Wx1 = max(W+x1, W−x1) | Wx2 = max(W+x2, W−x2) | ΔTz |
|---|---|---|---|
| **1** | ±**1.00** | ±**0.55** | ±**0.55** |
| **2** | ±**0.55** | ±**1.00** | ±**0.55** |
| **3** | ±**0.55** | ±**0.55** | ±**1.00** |

Resultant at each level must act through the **centre of area** at that level (may vary with height). Co-ordinate system: Fig. 2-5.

**All buildings** should be designed to resist these torsional loads with lateral loads. Table 2-1 yields **24** signed combinations of Fx / Fy / Mz. Torsion loadcases may be **formally ignored / reduced** only if:

| Waiver | Condition | Loadcase count (EN) |
|---|---|---|
| (a) | Single storey up to **10 m** height | — |
| (b) | Up to **70 m** with a **peripheral** lateral load-resisting construction | — |
| (c) | Torsional regularity: max inter-storey drift due to torsion < **25%** of lateral drift (check base + capacity drops > **25%**) | Full neglect → **8** cases |
| (d) | Torsional drift ≤ **50%** of lateral → omit **Case 3** | **16** cases |

**EN caveats:**
- Neglecting torsion loadcases does **not** mean torsion wind loading is absent — only that combinations may be simplified under Code rules.
- Tall-building torsion regularity is about comparing **shear strains** from torsion vs lateral shear (not naive storey drift alone).
- Conservatively taking full factors (always 1.0) reduces case count (24→16 or 8) when wind is not governing — useful for low buildings.

**SD takeaway:** Central-core-only towers and transfer structures rarely get (b) or (c) — assume full Table 2-1 until RSE proves a waiver. Peripheral tube / mega-frame helps (b).

---

### 5. Wind forces on building elements (§2.3)

#### 5.1 Enclosed building — no dominant openings

```
P = Qz · Cp · Ss
```

- Qz per §3.1; reference height Z defined with Cp, normally **building height H** (Table 4-1 notes: use **Qh**)
- Cp = net pressure coefficient including internal effects (§4.3.1 / Table 4-1)
- Ss = size factor from L0.5p of tributary area (§5.1)

Same equation used for open frameworks, attachments, free-standing walls.

#### 5.2 With dominant openings

```
P = Pe − Pi
Pe = Qz · Cpe · Ss
Pi = Qz · Cpi · Ss,p
```

- Cpe / Cpi from App. B1.2 / B1.3
- Ss,p from size of dominant opening(s) (§5.1 / Fig. 5-3)

---

### 6. Occupant comfort — acceleration (§2.4)

#### 6.1 Peak acceleration (§2.4.1)

Assess separately for orthogonal wind directions at any height Z and return period R (Eq. 2-4). Uses Sr, Qh, Ny, ξy, (BD)b, Iv,h, Hb, Mh, ηy.

Defaults / caps useful at SD:
- ηy ≈ **1.5** for accelerations in **top quarter** if no modal analysis
- (BD)b = enclosing-rectangle plan area averaged over top third, **excluding upper cut-backs**; if (BD)b > **H²/9**, take **H²/9**
- Mh = mass above **2 Hb / 3**

#### 6.2 Acceptance limits (§2.4.2, Fig. 2-6 + EN)

Comfort is acceptable if **1-year** and **10-year** peak accelerations are below Fig. 2-6 limits (frequency-dependent — **ISO 10137** office/residential curves adopted by Code; read with RSE).

Return-period factors on pressure (Table A1-2):

| R (years) | Sr |
|---|---|
| **1** | **0.25** |
| **10** | **0.55** |

**EN shortcuts:**
- Code method: 10-yr / 1-yr acceleration ratio is locked at **≈ 3.67** via NBCC scaling → checking **one** return period is enough for the Standard Method.
- **Tunnel:** check **both** 1-yr and 10-yr — ratio may differ from 3.67.
- Very slender: if Vcrit for vortex shedding is below the 10-yr wind, also check comfort **at Vcrit** (interpolate Fig. 2-6). EN uses `Vcrit ≈ 10 Ny` for prismatic section in the comfort note (strength note uses `10 Ny B` — confirm with RSE which form applies to the case).
- Occasional extreme moves matter less than frequent events; higher frequency → more sensitive (ISO logic).
- If (BD)b would exceed H²/9, Code caps it — reduces risk of under-predicting vs along-wind; comfort rarely governs stocky plans.

Alternatively (tunnel): Storm Passage / Up-crossing with combined X, Y, rotational responses (§6.5.3).

**SD takeaways:**
- Residential and Grade-A office → comfort often governs before strength.
- Plan aspect, mass distribution (Mh), damping (RC vs steel), and height drive Az — coordinate with RSE before promising floor plate / height.
- Tuned mass dampers / viscous dampers are a real SD option when aspect ratio is aggressive.

---

### 7. Temporary structures (§2.5 + EN / Dec 2023 EN)

| Case | Design wind |
|---|---|
| Temporary buildings & associated constructions **not for residency**, remaining ≤ **1 year** | Minimum **70%** of permanent-building design loads |
| Hoarding, covered walkway, contractor shed, bamboo shed, tent or marquee (**non-residential**) | Qz = **37% of Qo,z** (§3.2) — **no other adjustment** (no St, Sθ, etc.). Dec 2023 EN adds design **net pressure** guidance for site hoarding / covered walkway |

**EN risk framing:** higher risk is accepted because people on site can be **evacuated** after storm warning — risk is mainly **economic**. Designer must still take measures so disintegration does **not** create significant additional **life-safety** hazard or **highly disproportionate** economic damage.

**SD takeaway:** Sales offices used as residency, or temporary buildings > 1 year, fall back toward permanent rules — check use and duration with RSE / AP.

---

### 8. Design wind pressures (§3)

#### 8.1 Basic equation (§3.1)

```
Qz = Qo,z · St · Sθ
```

| Factor | Role | Default if inactive |
|---|---|---|
| **Qo,z** | Open-exposure reference at Ze (Table 3-1) | — |
| **St** | Topography (App. A3) | **1.0** if topography not significant |
| **Sθ** | Directionality (App. A1) | Max in 90° sector; circular → **1.0** |

#### 8.2 Reference pressure Table 3-1 (§3.2 + EN)

| Ze (m) | Qo,z (kPa) | Ze (m) | Qo,z (kPa) |
|---|---|---|---|
| ≤ **2.5** | **1.59** | **100** | **2.86** |
| 5 | 1.77 | 150 | 3.05 |
| 10 | 1.98 | **200** | **3.20** |
| 20 | 2.21 | 250 | 3.31 |
| 30 | 2.36 | 300 | 3.41 |
| 50 | 2.56 | 400 | 3.57 |
| 75 | 2.73 | **500** | **3.70** |
| | | > 500 | Specialist advice |

Interpolation (2.5–500 m):

```
Qo,z = 3.7 (Ze / 500)^0.16
```

Turbulence intensity (open exposure):

```
Io,z = 0.087 (Ze / 500)^(−0.11)
```

For across-wind moment and acceleration, if **0.25 ≤ He/H ≤ 0.5**, modify:

```
Io,z = [4 − (6 He/H)] · 0.087 (Ze / 500)^(−0.11)
```

**EN calibration backdrop (architects need the consequence, not the meteorology):**
- Open-sea storm profile ≈ **59.5 m/s** mean at 500 m; with γw = 1.4 + Sθ → ULS roughly **1,000–1,500 year** reliability band.
- **No** detailed terrain-roughness fetch factors in the Code (HK near sea + tall buildings + complex topography) — **topography dominates** over roughness.
- Climate-change intensity uncertainty retained as existing conservatism — do not invent ad-hoc uplifts without RSE / BA path.

**SD takeaway:** 50 m → 200 m raises Qo,z by ~**25%**. Cladding uses **Qh** — tall towers are not “same Cp, higher Q only a little”.

#### 8.3 Sheltering — displacement height (§3.3, App. A2)

May reduce height to **Ze** for wind pressure, turbulence intensity, **and** force coefficient. Conservatively take **Ze = Z** (no credit).

**Effective height:**

```
Ze = max(Z − Hd, 0.25 Z)
```

**Hd** may be taken as zero, or the **minimum** of:
1. **0.8 Hi**
2. **1.2 Hi − 0.2 Xp** (but ≥ 0)
3. **0.75 H**

Where:
- **H** = proposed building height
- **Hi** = obstructing building height above ground within **±45°** of considered wind (Fig. A2-1); Hi ≤ H
- **Xp** = horizontal distance from **upwind edge** of proposed building to obstructing building (Fig. A2-2)
- Consider obstructors with **Xp < 6H**

**Critical rules:**
- **Only one** upwind obstructing building → **no shelter allowed**
- ≥ two obstructors → use building giving **second-most** sheltering (second-largest Hd) — Fig. A2-3 / Dec 2023 clarification
- Varying heights across ±45° sector → weighted average Hd across sector (Fig. A2-4); divide into **≥ 4** equal divisions
- Obstructor height = actual height **or** height reduced to proposed building’s base level — take whichever gives **smaller** shelter benefit

Also:

```
Ze = Z − Hd     when Z ≥ 1.33 Hd
Ze = 0.25 Z     when Z < 1.33 Hd
```

**Link to tunnel floors (§6.4):** even with shelter, new buildings must resist ≥ **80%** of Standard Method loads (relaxable to 70% along-wind with removal testing — see §14).

**EN (shelter physics + traps):**
- Ze ≥ **0.25 Z** caps pressure reduction at about **20%** under the Code open-sea profile (`0.25^0.16 ≈ 0.8`).
- Accelerated flow occurs near the base of buildings **much taller** than displacement height. For **low-rise next to tall towers**, App. A2 shelter credit is **not necessarily conservative** — use BS EN A.4 methods / other standards / tunnel.
- Urban surroundings will change over building life — do not bank heavily on today’s neighbour shelter (ties to §6.4 floors).

**SD takeaway:** “We’re in a canyon” is not automatic. Need **two** meaningful upwind buildings; credit is capped; tunnel still has an 80% floor; low podium next to a super-tall neighbour may see **speed-up**, not shelter.

#### 8.4 Topography (§3.4, App. A3)

Method applies to hills/ridges or cliffs/escarpments that may be taken as reasonably **2-dimensional**.

**Topography is significant** when **ψu > 0.05** **and** site is in the significant zone:

| Condition | Meaning |
|---|---|
| **Zt / Ht ≥ 0.5** | Site high on the feature |
| Downwind: **Xt < 1.5 Ht / ψe** | Close enough downwind of crest |

Definitions:
- **ψu** = max slope for a quarter of hill-height in top half on windward side
- **ψe** = min(ψu, **0.3**)
- **Ht** = hill height from windward side above surrounding ground with mean slope ≤ **5%**
- **Zt** = height of highest part of site from same datum (Zt ≤ Ht)
- **Xt** = distance downwind from crest

If not required: **St = 1.0**. Otherwise:

```
St = [1 + 2 ψe · s / (1 + 3.7 Iv,z)]²
```

Evaluate **s** and **Iv,z** at **Z = 2H/3**. Location factor **s** from Figs A3-2(a–c) or Eqs A3-2 to A3-11 (upwind hills/cliffs; downwind hills; downwind cliffs/escarpments). Downwind of crest: use **lower** of hill/ridge vs cliff/escarpment **s**.

**SD takeaway:** Mid-Levels, Peak, hillside and cliff-top sites → flag St day one. Complex 3D topography → topo tunnel (≥ 1:5000, §6.1.3) rather than 2D App. A3 alone.

#### 8.5 Directionality (App. A1.1, Table A1-1)

| Direction | Sθ | Direction | Sθ |
|---|---|---|---|
| N | 0.82 | S | 0.85 |
| NE | 0.84 | SW | 0.84 |
| E | 0.85 | W | 0.82 |
| SE | 0.85 | NW | **0.80** |

- Interpolate between the eight directions.
- Standard Method: adopt **maximum Sθ in the 90° studied sector**.
- **Circular buildings: Sθ = 1.0** (no directionality relief).
- Tunnel alternative: Storm Passage / Up-crossing etc. may use **Sθ = 1.0** on forces/pressures (§6.5.2).

---

### 9. Force coefficients for overall buildings (§4.2)

#### 9.1 General

- Rectangular plans: §4.2.1–4.2.3
- When plan may be treated as rectangle: §4.2.4 (wings)
- Circular plan with **H/d ≤ 6** → **Cf = 0.75**
- **EN:** circular **H/d > 6** → use international provisions (e.g. BS EN 1991-1-4 Cl. 7.9.2) **and** check vortex-induced vibration (e.g. Vickery / Basu methods for isolated cylinders)

#### 9.2 Rectangular prism (§4.2.1, Fig. 4-1 / 4-2)

Cf is a function of **He, B, D** (Eq. 4-1). Valid for **He/D ≤ 12**.

```
Cf = 1.1 + exp{ |ln[(0.6 B/D)(1 − 0.011 He/D)]| · [1.7 − 0.0013 (He/B)²] }
     · (form as printed; use Code / Fig. 4-2 for application)
```

For overall loads (cumulative shear, torsion, moments), Qz may vary with height, or conservatively use **Qh**.

**EN:** high Cf on slender towers with **limited** surroundings drove the update — isolated slender towers pay more than 2004 intuition suggested.

#### 9.3 Variation of plan with height (§4.2.2)

- At a given height, compute Cf with **local B and D**, He/D ≤ 12.
- Steps affecting < **10% of H** → ignore for Cf calculation.
- Pressures still applied to the **actual** projected area.
- Large setbacks / transfers change Cf **and** centre-of-area for torsion.

#### 9.4 Corner shaping — architectural lever (§4.2.3, Fig. 4-3)

| Device | Reduction factor on Cf | Limits |
|---|---|---|
| Symmetric cut-outs / chamfers | `[1 − 2 (w/B) (1 − cos θ)]` | 0 ≤ w/B ≤ **0.31**; if w/B > 0.31 take 0.31 **or** treat as X-shaped |
| Rounded corners | `[1 − 2.5 r/B]` | 0 ≤ r/B ≤ **0.1**; if r/B > 0.1 take **0.1** |
| Unsymmetric corners | Use corner that produces **least** reduction | — |

**SD takeaway:** Modest chamfers / rounding can cut overall wind force — coordinate with curtain-wall module, sight-lines, and GFA before freezing the envelope. Deep “X” re-entrants change the equivalent rectangle path (§9.5).

**EN expectation management:** measured tunnel reductions for corners are often **relatively small** — useful trend, not a miracle massing lever.

#### 9.5 Wings: U, X, Y, L, Z (§4.2.4, Figs 4-4(a)–(f) + EN)

| Shape | Method |
|---|---|
| **U** | Equivalent rectangle per Fig. 4-4(a) |
| **X** | Equivalent rectangle per Fig. 4-4(b); corner effects as shown |
| **Double Y / single Y** | Figs 4-4(c) / 4-4(d) |
| **L / Z** | Figs 4-4(e) / 4-4(f) |

Force coefficients calculated as for rectangular building on the **equivalent rectangle** dimensions. Free-form / twisted / porous forms outside these figures → tunnel.

**EN — judicial extension for shapes not drawn in the Code:**
1. Enclosing rectangle → effective **B** for each wind direction.
2. If **H/B ≥ 1**, ignore re-entrant surfaces — straight line between extremes of each cross-section.
3. Apply corner rules (§4.2.3) where windward faces are not normal to wind.
4. Effective **D** = minimum depth near extremes of breadth; if surfaces not parallel to wind, take **min(enclosed-rectangle depth, B/1.8)** when judging the rough B/D where Fig. 4-2 Cf peaks.
5. Check at least **four** roughly orthogonal wind directions.

Largest loads for approx. rectangular-cornered buildings track **simple rectangular** forms — Code wing rules are helpful but slightly **conservative**.

---

### 10. Cladding & envelope pressures (§4.3, App. B1)

#### 10.1 Enclosed envelope — no dominant openings (Table 4-1)

Net Cp includes internal pressure effects. Use **Qh**.

| Surface | Zone | Description | Cp (−) | Cp (+) |
|---|---|---|---|---|
| Wall | **A** | Edge zone | **−1.4** | **+1.1** (A & B) |
| Wall | **B** | Elsewhere | −1.0 | +1.1 |
| Flat roof or pitch **< 30°** | **C** | Corner | **−2.2** | +0.3 |
| | **D** | Edge | −1.6 | +0.3 |
| | **E** | Elsewhere | −1.0 | +0.3 |
| Pitch **> 60°** | **C** | Corner | −1.4 | +1.1 |
| | **D** | Edge | −1.4 | +1.1 |
| | **E** | Elsewhere | −1.0 | +1.1 |

**Notes that drive SD:**
- (a) Use **Qh** for net pressures — **EN:** changed from mid-height elevation in 2004 Code; above displacement height, side/rear suctions are fairly uniform and positive pressures are deflected downward by the building (matches tunnel).
- (b) Ss depends on tributary / structural span — may be **> 1.0**. **EN:** applying Ss to **net** Cp (incl. internal) is conservative when Ss > 1.
- (c) Cladding pressures may be reduced **20%** below height **0.5 (H − He)**.
- (d) Significant steps / podiums → height rules for tower & podium (Figs 4-5 / 4-6; Dec 2023 cross-ref update — follow amended figure references).
- (e) Linear interpolate roof pitch **30–60°**.
- (f) Low-rise roof Cp may also come from reliable published sources — **EN:** complex roof Cp from BS EN low-rise tests are **not** adopted for HK mid/high-rise; if using foreign external Cp for low-rise, bring internal via App. B.

**EN — internal walls (RSE / AP judgment):**
| Situation | Guidance |
|---|---|
| No dominant openings | Foreign codes cite ~**0.3–0.5** net Cp on partitions; Code leaves judgment to RSE/AP when internal walls need wind design |
| Between occupied units | Consider accidental cladding breach / dominant opening — **out of Code scope** for accidental cases, but still a real unit-to-unit risk to brief |

**Zone geometry (Figs 4-6(a)/(b)):**
- Scaling length **b = min(B, 2H)**
- Edge / corner zones sized from b (read figures for extents of A–E)
- Worst cladding usually **wall edge A** and **roof corner C**

#### 10.2 Podium + tower — freeze before GBP (§4.3.1, Figs 4-5 / 4-6)

| Layout | Rules |
|---|---|
| Tower **set back** from podium edge | Fig. 4-5(a): separate wind reference height and zone scaling for tower vs podium |
| Tower at **podium edge** | Fig. 4-5(b): zone key still Figs 4-6; for podium design pressure use **max(b1t, b1p)** and **max(b2t, b2p)** for Zone A extent; reference height per Fig. 4-5(b) |
| Podium roof under tower influence | Pressures on podium = pressures on **adjacent tower elevation(s)** |

**SD takeaway:** Podium roof plant, skylights, landscape decks, and glass next to the tower face inherit **tower-level** intensity — not low-rise roof Cp. Flush vs setback tower position changes zone extents on the podium.

#### 10.3 Dominant openings (App. B1) — internal pressurisation

**Definition (B1.1):** dominant if **Ao > 1.5 Atot**, where:
- **Ao** = area of largest opening, **or** sum of openings of similar size in same/similar pressure zone(s) on the **same** face
- **Atot** = sum of openings on **other** faces, including leakage
- Default leakage contribution to Atot = **0.1%** of total external surface area of the other surfaces (other values with justification / specialist advice)

Non-dominant openings → internal pressures from airflow balance (see EN).

**External Cpe (Table B1-1)** — note these are **lower magnitude** than net Table 4-1 because internal is separate:

| Surface | Zone | Cpe (−) | Cpe (+) |
|---|---|---|---|
| Wall | A | −1.2 | +0.8 |
| Wall | B | −0.8 | +0.8 |
| Flat / pitch < 30° | C / D / E | −2.0 / −1.4 / −0.8 | 0.0 |
| Pitch > 60° | C / D / E | −1.2 / −1.2 / −0.8 | +0.8 |

Same Qh, Ss, 20% shelter reduction, podium rules, 30–60° interpolation notes as Table 4-1. Note (g): Table 4-1 net ≈ Table B1-1 with internal **+0.2 / −0.3**.

**Internal Cpi (Table B1-2):**

| Case | Cpi |
|---|---|
| Dominant opening | `Cpe / [1 + (Atot/Ao)²]`  *(use Code formula structure with local Cpe at opening)* |
| Not dominant | See EN |

Combine external + internal for **worst net** (Figs B1-1 to B1-4: external walls; internal walls with opening not in corner / upwind corner / downwind corner).

**SD triggers for dominant-opening design:**
- Loading docks, warehouse / hangar doors
- Large operable walls, garage doors, industrial shutters
- Phased occupation / incomplete enclosure
- Cladding breach scenarios (coordinate with façade engineer)

#### 10.4 Open frameworks (Table 4-2)

For planar frameworks (e.g. exposed lattice beams attached to buildings):

| Solidity φ | Cp |
|---|---|
| 0.01 | **2.0** |
| 0.1 | 1.8 |
| 0.2 | 1.7 |
| 0.3 | 1.6 |
| 0.5 | 1.5 |
| 0.8 | 1.5 |
| 0.9 | 1.6 |
| 1.0 | **2.0** |

- φ = effective projected area / area enclosed by frame boundary normal to wind
- Linear interpolate; apply pressure to **solid area only**
- Free-standing walls with φ < **0.8** → use Table 4-2, not B3

---

### 11. Attachments & free-standing walls (App. B2–B3)

Unless noted: use **Qh**; often **Ss = 1.0**; −20% below 0.5(H − He) where stated.

#### 11.1 Sunshades, architectural fins, signboards (Table B2-1, Fig. B2-1)

| Fixing | Edge zones of building | Other zones |
|---|---|---|
| **Case 1** — directly attached to façade | **±1.8** | ±0.9 |
| **Case 2** — spaced away from façade | **±3.0** | ±1.5 |

- Gap < **2/3** of element width → treat as Case 1 (gap closed); load at centre of area
- Case 2: take lesser magnitude of `Cp_case1 × Agross` vs `Cp_case2 × Anet`
- Edge zone definition: **b = min(B, 2H)** — Fig. B2-1(c)
- Ss = **1.0**
- Overall structural force effects still per §4

**SD takeaway:** Projected / floating fins and large signboards at corners are among the highest local wind items in the Code (±3.0).

#### 11.2 Balconies (Table B2-2)

| Element | Cp |
|---|---|
| Balcony walls and balustrades | **±1.8** |
| Balcony slabs | **+0.9 and −1.8** |

Reference pressure = **roof height** of host building. Ss = 1.0. −20% below 0.5(H − He) allowed.

**SD takeaway:** High-rise balcony glass, cantilevers, and open-side balustrades are wind-critical — size connections and glass early; do not treat as pure architecture.

#### 11.3 Canopies attached to buildings (B2.3)

Codified Cp **+0.9 / −1.3** (positive = **downward**) only if **both**:
- Attached below mid-height: **h/H < 0.5**, and
- Below a height of **twice the canopy projection**

Use Qh. Outside these limits → specialist advice / tunnel / EN.

**SD takeaway:** High entrance canopies on tall towers often fall **outside** B2.3 — flag early.

#### 11.4 Free-standing walls & parapets (Table B3-1, Fig. B3-1)

Reference area = **gross** area. Reference height = **top of wall** above ground. For wall cantilevering from continuous base, Ss uses **L0.5p = 2h**.

**φ = 1 (solid), without return corners:**

| ℓ/h | Zone A | B | C | D |
|---|---|---|---|---|
| ≤ 3 | **2.3** | 1.4 | 1.2 | — |
| = 5 | **2.9** | 1.8 | 1.4 | 1.2 |
| ≥ 10 | **3.4** | 2.1 | 1.7 | 1.2 |

**With return corners of length ≥ h:** A = **2.1**, B = 1.8, C = 1.4, D = 1.2 (interpolate returns 0 to h).

**φ = 0.8:** all zones **1.2**. φ < 0.8 → Table 4-2.

**EN:** Zone A/B peaks are from **oblique** wind on walls **without** returns. **~20% porosity** (≤ 80% solid) in high-suction regions drops those peaks to Zone D level — a cheap SD lever vs long solid parapets.

**SD takeaway:** Long solid boundary walls and continuous roof parapets without returns attract Zone A Cp up to **3.4**. Introduce returns ≥ h, breaks, or porosity.

---

### 12. Size factor and size & dynamic factor (§5, App. C1–C2)

#### 12.1 Size factor Ss (§5.1, Fig. 5-1 / 5-2, App. C1)

Depends on size and location of loaded area via half-perimeter **L0.5p**:
- Measured around tributary area making main contribution to the load effect
- Complex shapes: half length of taut string around extremities (circle diameter d → L0.5p = πd/2)
- Corner / edge / “Other” curves on Fig. 5-2 (zones per Fig. 4-6(a) & Table 4-1)

Equations (App. C1):

| Case | Formula |
|---|---|
| Other zones & overall wind loads | `Ss = exp(0.17 − 0.07 L0.5p^0.32)` |
| Edge zones, L0.5p < 15 m | `Ss = 1.3 − logn(L0.5p)/9.0` (> 1.0) |
| Corner zones, L0.5p < 15 m | `Ss = 1.5 − logn(L0.5p)/5.4` (> 1.0) |

Dominant-opening internal size factor **Ss,p**: half-perimeter of largest opening or notional perimeter around several openings forming Ao (Fig. 5-3); use **“Other”** curve.

**SD takeaway:** Small corner / edge panels see **Ss > 1** — curtain-wall performance specs must state zone + tributary size, not a single “design wind pressure”.

**EN:** Ss = 1.0 is set at **L0.5p ≈ 15 m** (HK typhoon / tall-building correlation higher than European practice). Typical façade panel sizes → **Ss > 1.0**. Small tunnel-model attachments (< ~6 mm at model scale) may be too small to instrument — estimate from edge speed-up (Bernoulli from surface pressures) even when a tunnel is run.

#### 12.2 Size and dynamic factor for buildings Sq (§5.2)

At top of building:

```
Sq,h = 0.5 + √[ (Ss(L0.5p=B) − 0.5)² + 0.25 / (B^0.5 · H · Nx² · ξx) ]
```
(Use Code Eq. 5-1; Ss from “Other” curve with L0.5p = B.)

Reduce over height:

```
Sq,z = Sq,h − 1.2 (Sq,h − (10/H)^0.14) (1 − Z/H)
```

Units: metres and Hertz.

**Buildings < 50 m** — simplified, all heights:

```
Sq = 1.1 · Ss(L0.5p = H/1.5 + 2B)
```

#### 12.3 Damping (App. C2) — comfort & across-wind

Establish from reliable measurements on similar structures where possible. Tables give fundamental-mode damping for typical buildings. Composite steel/concrete → intermediate values. Particularly slender buildings → lower values; seek specialist advice.

**Aspect ratio for damping** = total tower height above foundation ÷ dimension of tower **lateral load-resisting structure** in vibration direction. With plan set-backs, also check height above set-back ÷ depth above set-back — take **largest**. Towers on shared podium: similarly check **above podium**.

**Table C2-1 — typical RC (ξx, ξy)**

| Aspect ratio | Max damping — accelerations | Max damping — structural loads |
|---|---|---|
| ≥ **8** | **0.010** | 0.015 |
| 7 | 0.011 | 0.017 |
| 6 | 0.013 | 0.020 |
| 5 | 0.016 | 0.024 |
| < **4** | **0.020** | 0.030 |

**Table C2-2 — typical steel**

| Aspect ratio | Max damping — accelerations | Max damping — structural loads |
|---|---|---|
| ≥ **8** | **0.005** | 0.008 |
| 7 | 0.006 | 0.009 |
| 6 | 0.007 | 0.010 |
| 5 | 0.008 | 0.012 |
| < **4** | **0.010** | 0.015 |

**SD takeaway:** Slender steel towers have half (or less) the damping of stocky RC — comfort and across-wind amplify. Aspect ratio uses **structural depth**, not architectural width of wings.

---

### 13. Wind tunnel testing requirements (§6)

#### 13.1 When and what (§6.1 general)

Guidance for modelling complete buildings for overall forces, accelerations, and surface pressures — typical HK testing.

| Sub-clause | Requirement (practical minimum / guide) |
|---|---|
| **6.1.1 Wind modelling** | Represent hourly mean speed vs height, turbulence intensity & length scales for site. Peak loads of reliability compatible with Code. Vortex-shedding frequencies modelled physically; lower-frequency turbulence may be analytical. **EN:** typically **1–2 hours** full-scale-equivalent data; cladding tap density **≥ 120 m²** surface per tap |
| **6.1.2 Dynamic response** | Accurate mass & stiffness (physical or analytical); appropriate damping. Near-prismatic with H/B and H/D < **15** → may consider only lowest 3 modes (2 lateral + torsion). **EN:** resonant response ∝ 1/√damping — damping errors hit **across-wind** hardest; very slender → higher modes |
| **6.1.3 Topography** | If significant: small-scale tunnel or reliable published data. Model usually ≥ **1:5000**; if smaller, see EN (frequency-response corrections). Include majority of influencing features. ≥ **18** directions @ **20°**. St from Eq. 6-1 comparing topography vs approach profiles |
| **6.1.4 Proximity** | Include surroundings that significantly affect windiness; general guide ≥ **400 m** radius. Large topography handled per 6.1.3. Normally ≥ **36** directions @ **10°** for pressures/loads. **EN:** test **existing + likely future**; if one building looks specially sheltering → **removal** case |
| **6.1.5 Model scale** | Building model usually ≥ **1:500** (EN also cites practical **1:200–1:600**). Sharp corners: Re based on typical breadth ≥ **1×10⁴**. Rounded shapes need further evidence (e.g. larger scale / trip features). Blockage normally ≤ **10%** incl. surroundings; if visual blockage > 10%, measurement evidence required |
| **6.1.6 Wind profiles** | Match Harris–Deaves / ESDU 01008 after scaling. Code §3 profile ≈ ESDU open-sea. Topo study profiles feed building tests. **EN:** turbulence intensity within **10%** of target (±15% of ref height); length scales within **×2** for structure (×3 may be OK for cladding panels ≤ 15 m) |
| **6.1.7 Match pressures** | Eq. 6-2 links Qz to Vz and Iv,z. **Matching height:** built-up — greater of **150 m above upwind surroundings (effective)** or **2H/3**; open — **2H/3**; intermediate — check both. Correct tunnel peak gust at match height to target Qz from Eq. 3-1 |

#### 13.2 Target reliability (§6.2)

Structural design wind loads ↔ expected peak response in **one hour** of exposure to ultimate wind pressures = code reference pressures × **Sθ** (§6.5.2) × **γw** from relevant structural CoP.

#### 13.3 Cladding from tunnel (§6.3 + EN)

- Derive for typical panel sizes, e.g. L0.5p **2–5 m**
- **80%** chance of non-exceedance in one hour
- Significantly larger panels may justify reduced loads
- Internal pressures from consideration of measured external pressures
- **EN:** common practice uses **0.5–1 s** time-average filter for typical panels; large areas → area- or time-averaging under experienced wind engineer

#### 13.4 Minimum loads in sheltered locations (§6.4, Fig. 6-1 + EN)

Where adjoining/surrounding buildings provide significant shelter (most sheltering per direction per App. A2), also consider effect of **their possible removal**.

| Building type | Floor |
|---|---|
| New buildings **within** Code scope | ≥ **80%** of Standard Method load. May relax to **70%** of along-wind Standard Method if additional **Removal Testing Configuration** is run and adopted loads ≥ **80%** of removal-test results |
| New buildings **beyond** Code scope | ≥ **80%** of Removal Testing Configuration; and not lower than **70%** of along-wind Standard Method |

Removal principle: building / lot providing **most significant shelter** in each wind direction considered for removal (procedure App. A2). Otherwise use maximum loads with existing and **likely future** surroundings.

**EN:** always also consider **100%** of loads with existing **and likely future** surroundings. Planning restrictions on neighbours may inform removal risk — do not assume today’s canyon forever.

**SD takeaway:** Tunnel cannot be used to undercut the Code by claiming temporary neighbour shelter — removal testing and 70–80% floors apply.

#### 13.5 Directionality & accelerations in tunnel (§6.5 + EN)

- Ultimate loads: directionally adjusted speeds × √γw, then divide by γw for unfactored loads to combine with material-code factors (§6.5.1)
- Directionality: Sector Method Sθ (App. A1) **or** Sθ = 1.0 with Storm Passage / Up-crossing (§6.5.2)
- Accelerations: Sr from Table A1-2 **or** combined directional probability methods (§6.5.3)
- **EN:** Code Sθ is for **typhoon** winds (NW weakest). Frequent-wind comfort may use Waglan-type data + topographic steering (or fall back to typhoon Sθ). Monte-Carlo Up-crossing / Storm Passage: target Code pressure × γw with **Sθ = 1.0**, then divide by γw; for comfort target Code speed × Sr with Sθ = 1.0

#### 13.6 Verification (§6.6 + EN)

Enough detail of test conditions and results for **independent verification** of modelling applicability.

**EN deliverables that matter to AP/RSE briefing:** wind properties and measured data in **electronic tabulated** form — **images alone are not sufficient**. Asymmetric forms may need load combinations beyond Code 24 cases; complex diaphragms / linked towers may need specialist third-party advice on load applicability.

---

### 14. December 2023 amendments — Code + EN

| Item | Change |
|---|---|
| **Figs 2-1 & 2-2** (Code) | Revised tunnel-trigger flowcharts — **use amended** |
| **Table 4-1 note (d)** (Code) | Podium height-rule figure cross-references updated |
| **Fig. 5-2 & App. C1** (Code) | Size-factor calculation elaborated |
| **App. A2 / Fig. B3-1** (Code) | Second-most obstructing building wording clarified |
| **EN Cl. 2.2.3** | Extra guidance on **fundamental frequency** for across-wind assessment |
| **EN Cl. 2.5** | Design **net pressure** for site hoarding / covered walkway added |
| **EN Cl. 4.3.1, 6.4, Fig. B-1, App. C2, E3.1** | Textual refinements |

---

### 15. EN special-attention situations (freeze before SD massing)

Use this as the EN “gotcha” list when the Code text alone looks fine:

| Situation | Why it bites | SD action |
|---|---|---|
| Sloping / multi-level site | H differs by face | Agree greatest H for Qh; vary H for Cf / surrounds if material |
| Crown / plant / sloping roof | Across-wind assumes prism | Define Hb vs H with RSE early |
| Free-form / twisted / porous | Outside rectangular envelope | Tunnel + fee day one |
| B/D ≳ 4 (esp. > 6) | Across-wind + torsion | Expect tunnel; slab plans = torsion |
| Isolated slender tower | High Cf in open exposure | Don’t assume dense-urban Cf |
| Low-rise beside super-tall | Speed-up, not shelter | Tunnel / EN A.4 methods |
| Mid-Levels / Peak / cliff | Topography dominates | St or topo tunnel (≥1:5000) |
| Central core only | Full 24 torsion combos | Peripheral structure helps waiver |
| Spaced fins / corner signage | Cp ±3.0 | Treat as structure, not décor |
| High canopy on tall tower | Outside B2.3 window | Specialist / tunnel early |
| Long solid parapet / boundary | Zone A up to 3.4 | Returns ≥ h or ~20% porosity |
| Typical CW panel | Ss > 1.0 | Spec by zone + L0.5p |
| Flexible roof / long-span façade | Dynamic beyond Code cladding | Specialist |
| Circular H/d > 6 | Vortex vibration | Not just Cf = 0.75 |
| Temporary sales pavilion as residence | Falls out of §2.5 relief | Use permanent wind path |
| Tunnel claiming deep canyon shelter | 70–80% floors + removal | Brief future-neighbour cases |

---

### 16. Schematic design checklist (architect ↔ RSE ↔ façade)

**Massing & tunnel gate**
1. H, Hb, He; plan B×D; H/B; B/D — both orthogonal directions
2. Any §1.1 tunnel trigger (height, shape, topography, across-wind, B/D)?
3. Can plan be rectangular-treated or codified U/X/Y/L/Z — or free-form tunnel?

**Form & structure**
4. Corner strategy (chamfer w/B, radius r/B) vs Cf reduction and CW module — don’t over-promise
5. Peripheral vs central core → torsion waiver prospects (§2.2.4)
6. Aspect ratio for damping (structural depth, set-backs, podium)
7. Tall residential/office → comfort path (1-yr / 10-yr Az; tunnel: both) + damper option
8. Tapered / stepped massing vs pure prism (across-wind)

**Site**
9. Hillside / cliff / escarpment → St / topo tunnel
10. Neighbour shelter → App. A2 credit vs 80% floor / removal / future neighbours
11. Low-rise next to tall → check speed-up, not only shelter
12. Orientation → Sθ sector (circular: no relief)

**Envelope & attachments**
13. Podium–tower setback vs flush edge → Figs 4-5 / 4-6 zones
14. Roof pitch bands (<30 / 30–60 / >60) for Cp
15. Large doors / operable walls / phasing → dominant opening case
16. Internal partitions between units → wind / breach brief with RSE
17. Fins, sunshades, signage (±3.0 if spaced at edges)
18. Balconies (±1.8; slabs −1.8)
19. Canopies — inside or outside B2.3 limits (h/H < 0.5 and ≤ 2× projection)?
20. Parapets / site walls — length, returns, solidity / porosity
21. Curtain-wall brief: zone A–E + L0.5p / Ss, not a single pressure

**Programme / temporary / tunnel QA**
22. Temporary works / hoarding / sheds → §2.5 (70% or 37% Qo,z) + disintegration duty
23. If tunnel: 400 m proximity, topo scale, cladding panel size / tap density, electronic verification pack, removal cases

---

### 17. What this Code / EN does **not** set

| Outside this Code | Go to |
|---|---|
| Member design; DL/IL/wind combinations | SUC / steel / concrete material codes (apply γw with those) |
| Pedestrian-level wind / AVA | AVA studies, PNAP, lease / planning conditions |
| Envelope thermal / OTTV / RTTV | Energy / OTTV codes |
| Typhoon EOT / contract risk allocation | Contract (NEC / GCC / etc.) |
| Accidental dominant openings (cladding breach) | Out of Code scope — still brief unit-to-unit walls with RSE |
| Older pre-2019 wind practice | Superseded — do not mix coefficients |

---

### 18. Quick reference — critical numbers for SD

| Item | Value |
|---|---|
| Standard Method height limit | **≤ 200 m** |
| Across-wind exemption | H < **100 m** and H/B < **5** and f > **0.5 Hz** |
| Across/along tunnel hard stop | Factor **> 1.5** |
| Across-wind B/D comfort zone (EN) | ~**0.5–2** (extend ~**1:4**); beyond → caution / tunnel |
| Vcrit (strength, EN) | ≈ **10 Ny B** |
| Torsion eccentricity | **0.05 B** (B/D≤1) → **0.20 B** (B/D=6) |
| Load combo factors | 1.00 / 0.55 / 0.55 → **24** signed cases |
| Torsion ignore (examples) | ≤10 m single storey; ≤70 m peripheral; drift tests 25% / 50% |
| γw | **1.4** |
| Qo,z at 10 / 50 / 100 / 200 m | **1.98 / 2.56 / 2.86 / 3.20** kPa |
| Shelter floor on Ze | **≥ 0.25 Z** (~**20%** pressure floor); need ≥2 obstructors; 2nd-most shelter |
| Shelter search radius | Xp < **6H** |
| Topography trigger | ψu > **0.05** + significant zone |
| Wall edge / roof corner Cp (enclosed) | **−1.4 / −2.2** |
| Dominant opening | Ao > **1.5 Atot**; leakage **0.1%** |
| Spaced fin at edge | **±3.0** |
| Balcony wall / slab | **±1.8** / +0.9 & **−1.8** |
| Canopy codified window | h/H < **0.5** and height ≤ **2×** projection |
| Free-standing wall Zone A (long, solid) | up to **3.4** (cut with returns / ~20% porosity) |
| Temporary ≤1 yr non-residential | **70%** permanent |
| Hoarding / shed / tent | **37% Qo,z**, no other factors |
| Sr for comfort | **0.25** (1-yr) / **0.55** (10-yr); code Az ratio ≈ **3.67** |
| Circular Cf shortcut | H/d ≤ **6** → **0.75**; taller → EN + vortex VIV |
| Tunnel proximity / topo / model | **400 m** / ≥**1:5000** / ≥**1:500** |
| Tunnel cladding taps / duration | ≥ **120 m²**/tap; **1–2 h** full-scale equiv. |
| Tunnel shelter floor | **80%** (or 70% along-wind + removal rules) |
| Cladding tunnel non-exceedance | **80%** in one hour; L0.5p ~ **2–5 m** |
| Ss = 1.0 reference size (EN) | L0.5p ≈ **15 m** |

---

*Sources: Code of Practice on Wind Effects in Hong Kong 2019 (BD) + December 2023 Code amendments; Explanatory Notes to the Code (Sep 2019) + EN Amendments (Dec 2023). Figures, equations, and flowcharts in the Code/EN remain authoritative; this summary is for schematic-design scanning and coordination only.*
