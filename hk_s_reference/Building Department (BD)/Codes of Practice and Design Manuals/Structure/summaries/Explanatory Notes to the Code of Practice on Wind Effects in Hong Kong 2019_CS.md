# Explanatory Notes to the Code of Practice on Wind Effects in Hong Kong 2019
**Architect critical summary for schematic design**
First issue September 2019 | Buildings Department

> Scope note: These notes explain the 2019 wind code and the situations where its rules need care. They are **not** the Code, and they are **not** the December 2023 amendment sheets to the Code or to these notes.

## Regulatory Overview
The notes set how Hong Kong wind loads are built from a gust reference pressure, size and dynamic factors, torsion, and an across-wind check, for buildings that can be treated as rectangular and for a limited set of other shapes. Wind-tunnel testing is the route where the shape, the plan ratio, or the across-wind scaling falls outside those rules.

## Critical main topics and subtopics

### 1. Reference system and building height (sections 1.1, 1.2, 2.1, 3.1)

| Item | Rule in the notes |
|---|---|
| Load basis | Peak gust pressure with force and pressure coefficients. The 2004 reference pressures are retained. Along-wind response uses one size and dynamic factor, Sq,z, in place of the old static and dynamic split |
| Load factor | The formulations include the current Hong Kong wind load factor γw of 1.4. Multiplying the reference pressures by 1.4 would give the same ultimate loads with a future factor of 1.0 |
| Reliability | Used with γw = 1.4 and the direction factors, ultimate loads are calibrated to at least a 1,000–1,500 year return |
| Wind climate behind the formula | Open-sea exposure, mean speed 59.5 m/s at 500 m. Peak factor 3.7 on the turbulence, described as about a 0.35 s average. The change of description does not change the Code pressures |
| Height H | Height above the average ground level on each face. For the reference pressure Qh, use the greatest height |
| Height Hb | For accelerations and across-wind base moments. Excludes sloping roofs and irregular roof plant that are a small part of the height and do not continue the prismatic form |
| Cladding of usual elements | Quasi-static gust pressure only, with no dynamic amplification |
| Unusual elements | Overhanging roofs, long-span facades, and small-diameter members that may shed vortices need a specialist review |

**SD takeaway:** Take H as the greatest height for Qh, strip roof plant out of Hb, and keep γw = 1.4 on these reference pressures.

### 2. Torsion and load combinations (sections 2.2.2 and 2.2.4)

Eccentricity for torsion increases linearly with plan ratio B/D, from ±0.05B for a square plan to ±0.2B when B/D is 6.0. Wind-tunnel data are required when B/D is larger than 6.0.

The envelope is 24 combinations:

| Case | Factors |
|---|---|
| (a) | ±1.0 Fx with ±0.55 Fy and ±0.55 Mz |
| (b) | ±0.55 Fx with ±1.0 Fy and ±0.55 Mz |
| (c) | ±0.55 Fx with ±0.55 Fy and ±1.0 Mz |

Torsion may be neglected, which cuts the set from 24 to 8, for:

| Building | Condition |
|---|---|
| Single storey | Up to 10 m high |
| Up to 70 m | Peripheral lateral system on all faces (masonry or concrete shear walls, or braced steel). A bi-directional multi-bay moment frame may be included. Any column set-back, measured from the column centre, must not exceed 5 m or 1/10 of the building dimension in the set-back direction, whichever is smaller |
| Torsional regularity | A check similar to ASCE 7-16. For a tall building, compare shear strains from torsion with shear strains from lateral shear, because the ASCE check was written for low-rise buildings |

If torsion is only moderate, omit case 3 in Table 2-1 and use 16 combinations. Taking every component at 1.0 also reduces 24 combinations to 8. Neglect inside the limit does not mean torsion is absent.

**SD takeaway:** Keep all 24 combinations unless the building is a single storey up to 10 m, or up to 70 m with a peripheral lateral system and set-backs no greater than 5 m or 1/10 of the plan.

### 3. Across-wind base moment and when a tunnel test is required (section 2.2.3)

The across-wind moment uses the National Building Code of Canada method, scaled so the ultimate moment is divided by γw before it enters the structural codes. The moment rises with wind speed to the power 3.3, not 2.

| Check | Limit |
|---|---|
| Calibration range | Rectangular prism, mode shape about linear with height, mass fairly uniform over the top half, and 0.5 < B/D < 2. Experience extends similar reliability to about 1:4. Beyond that, a tunnel test may be appropriate |
| Exemption | With natural periods of H/46 in both directions, no across-wind check when H / min(B, D) < 5, H < 100 m, and N > 0.5 Hz |
| Scaling | If the across-wind base moment exceeds the along-wind moment in that direction, scale the along-wind force up to the across-wind moment. If across-wind is smaller, ignore it |
| Tunnel trigger | If the scale-up is larger than 50%, a wind-tunnel test is required. The worked example treats 1.43 and 1.27 as inside the Standard Method because both are below 1.5 |
| Very slender towers | For preliminary strength, wind speed may be capped at Vcrit ≈ 10 Ny B, where vortex shedding peaks, but the response is to be verified in a tunnel. Otherwise follow the Code formula |
| Irregular plans | The formula is conservative for strongly tapered, stepped, or irregular plans |

**SD takeaway:** Skip the across-wind check only when H is under 100 m, H / min(B, D) is under 5, and the frequency is above 0.5 Hz; otherwise test in a tunnel if across-wind exceeds along-wind by more than 50%.

### 4. Occupant acceleration (section 2.4)

The Code uses the National Building Code of Canada across-wind acceleration. People feel motion most in slender buildings, where across-wind acceleration usually governs.

| Item | Rule |
|---|---|
| Along-wind may govern | If (BD)b > H²/9. The Code sets (BD)b ≤ H²/9 so the across-wind formula is not used where along-wind motion would be larger |
| Comfort criteria | ISO 10137 frequency-dependent peak accelerations for office or residential use under a one-year wind |
| Ten-year check | Those one-year limits are scaled by 3.3 × √(0.55/0.25) = 3.67, using the return-period factors Sc of 0.55 at 10 years and 0.25 at 1 year. Under the Code method, check only one of the two periods |
| Wind tunnel | Check both return periods, because the ratio need not be 3.67 |
| Vortex critical speed | If Vcrit ≈ 10 Ny for a prismatic section is below the 10-year wind, also check comfort at that speed by interpolating Figure 2-6 |

**SD takeaway:** Hold (BD)b at or below H²/9 for the Code acceleration method, and plan a two-period tunnel check if comfort is not taken from the Code's 3.67 scaling.

### 5. Temporary structures (section 2.5)

| Structure | Minimum pressure |
|---|---|
| Temporary building, or a building in position for not more than one year | Not less than 70% of the Code pressures |
| Hoarding and covered walkway at a construction site, contractor shed, bamboo shed, tent, or marquee, not for residential use | Not less than 37% of the Code pressures |

The designer must keep these structures from breaking up in a way that adds a serious life-safety hazard or highly disproportionate economic damage. The December 2023 amendment sheet adds a net-pressure table for hoarding and covered walkways; that table is not in these 2019 notes.

**SD takeaway:** A structure that stays up for no more than a year may use 70% of the Code pressure, and a non-residential site hoarding or shed may use 37%.

### 6. Shelter and topography (sections 3.2 to 3.4, Appendix A2)

| Item | Rule |
|---|---|
| Effective height | Not less than 25% of the relevant reference height. With the open-sea exposure that limits the pressure reduction to 20% (0.25^0.16 = 0.8) |
| Future change | The most beneficial sheltering building is ignored. Benefit may be taken from the second most sheltering building |
| Same lot | Buildings in the same lot are treated as one when deciding which sheltering building is removed |
| Low buildings beside a tall neighbour | Effective-height relief may be unconservative. Assess accelerated flow by BS EN 1991-1-4 clause A.4, another standard, or a tunnel test |
| Topography | Factors are spreadsheet equations based on an updated EN 1991-1-4, adjusted for Hong Kong. Terrain-roughness fetch factors are not provided |
| Complex topography | Where the rules cannot be applied clearly, especially a strongly three-dimensional hill, use further guidance or a tunnel test |
| Irregular building shape | Same: further guidance or a tunnel test. Slightly trapezoidal plans may be treated with judgement; the critical directions may not be orthogonal |

**SD takeaway:** Do not take shelter below 25% of the reference height, ignore the single most helpful neighbour, and test a low block that sits in the accelerated flow of a much taller neighbour.

### 7. Overall force coefficients (section 4.2)

| Form | Coefficient |
|---|---|
| Rectangular, or a shape that can be treated as rectangular | Code formula from aspect ratio H/D and plan ratio B/D |
| Circular, height / diameter not larger than 6 | Force coefficient 0.75 |
| Circular, height / diameter larger than 6 | Use an international standard such as BS EN 1991-1-4 clause 7.9.2, and check vortex-induced vibration |

**SD takeaway:** A circular tower uses 0.75 only while height / diameter is 6 or less; above that, add a vortex check.

### 8. Cladding, openings, balconies, and canopies (sections 2.3, 4.3, Appendix B)

| Item | Rule |
|---|---|
| Enclosed cladding | Net pressure, as in the 2004 code. Reference height Qz is the top of the building, not the element's own level |
| Size factor Ss | Applied to the net pressure. That is conservative when Ss is greater than 1, because internal pressure is scaled as well |
| Dominant opening | An opening, or openings on the same side, with area greater than 1.5 times the sum of the areas of the other openings. External and internal pressures are then separate. The internal size factor follows the opening size, not the loaded-area size |
| Balcony balustrade | The notes record AWES values of ±1.8 at corners and the top floor and ±1.5 elsewhere. The Code takes ±1.8 throughout. Balcony slabs: −1.8 uplift and +0.9 downward |
| Balcony reference height | The building height. A balcony within half the displacement height may take a 20% reduction |
| Fins on a long plan | If B/D > 3, friction on vertical fins is to be evaluated. Section 7.5 of BS EN 1991-1-4 is named as a reference |
| Canopy on the lower half | Downward on the windward face, uplift on a side face. The notes record +0.9 and −1.3 as the most onerous values for a canopy from the bottom to mid-height |
| Canopy on the upper half, or free-standing | Use the free-standing canopy rules in BS 6399 or the BS EN |

**SD takeaway:** Treat an opening larger than 1.5 times the rest as dominant, and take balcony balustrades at ±1.8 on the building height unless the balcony sits within half the displacement height.

### Source

`ExplanatoryNotesWindEffects2019e.pdf`

Read with the Code of Practice on Wind Effects in Hong Kong 2019 and the December 2023 amendments (`WindEffects2019e_Amend2023e.pdf` and `ExplanatoryNotesWindEffects2019e_Amend2023e.pdf`).
