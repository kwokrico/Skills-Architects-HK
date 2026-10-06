# Explanatory Materials to the Code of Practice for the Structural Use of Steel 2011
**Architect critical summary for schematic design**
Explanatory Materials to the 2011 steel code | Buildings Department

> Scope note: These Explanatory Materials give the background, limits, and worked-example context for the Code of Practice for the Structural Use of Steel 2011, and they are to be read with that Code. They are **not** the Code, and they do **not** cover rail or road bridges, articulated access walkways, nuclear power stations, pressure vessels, or fibre-composite structures.

## Regulatory Overview
The Materials explain when the Code's steel grades, second-order analysis, robustness ties, and tall-building comfort rules apply to building structures, including composite beams and columns and cold-formed sections. The Responsible Engineer for a private building is a Registered Structural Engineer, and the assumed design working life for a normal building is 50 years.

## Critical main topics and subtopics

### 1. Scope, design life, and second-order analysis (E1.1, E1.2.7)

| Item | Lock in these Materials |
|---|---|
| Code coverage | One volume for building structures: stability, tall buildings, composite beams and columns, long spans, and steel grades. Section 10 does not cover fibre composites |
| Out of scope | Rail or road bridges, articulated access walkways, nuclear power stations, and pressure vessels. General steel principles may still be used for preliminary design of some special types |
| Design working life | 50 years for normal buildings and other common structures. Discuss a longer life for hospitals, police stations, fire stations, government headquarters, power stations, and fuel depots. Bridge codes use 120 years |
| Second-order analysis | If the elastic critical load factor is less than 5, do not use manual methods. Use a non-linear second-order analysis that includes P-Δ and P-δ and member and frame imperfections, for both sway and non-sway frames |
| Design documents | State the design assumptions, the structural system, and whether loads or reactions are factored |

**SD takeaway:** Lock a 50-year life unless the building is an essential or civic facility, and switch to non-linear second-order analysis once the elastic critical load factor drops below 5.

### 2. Steel class and strength cap (E1.1, E3.1, E3.1.4)

| Class or range | Design strength |
|---|---|
| Normal steel | Yield from 190 N/mm², or 215 N/mm² (170 N/mm² for thick plates), up to 460 N/mm². Design strengths py are in Tables 3.2 to 3.6 of the Code |
| Class 1H | Above 460 N/mm² and not greater than 690 N/mm², under an acceptable quality-assurance system, with the restrictions in clause 3.1.3. Sulphur not above 0.015% and phosphorus not above 0.025%, unless a listed standard is deemed to satisfy |
| Above 690 N/mm² | Not covered. Performance-based design is the route if it is proposed |
| Plastic analysis | Not permitted where the yield strength is greater than 460 N/mm² |
| Class 3 uncertified steel | Discouraged. Permitted with restrictions, including a 6 m span limit. py not exceeding 170 N/mm² and tensile strength not exceeding 300 N/mm². Coupon tests typically 170 N/mm² yield, ultimate 1.2 times yield, Charpy, and 15% elongation. If welded, chemical tests and a carbon equivalent within BS EN 10025 |
| Grade 43C chemistry | Sulphur and phosphorus set at 0.03% in clause 3.1.2. Weldability in that clause is to be observed |
| Elastic modulus | Reinforcement in composite construction is taken as 205 kN/mm², the same as structural steel sections |
| Thermal expansion (E3.1.6) | The text layer prints 14 x 106 /°C to match section 12, and 12 x 106 /°C for steel below 100°C |

**SD takeaway:** Stay at or below 460 N/mm² if plastic design is intended; Class 1H stops at 690 N/mm², and uncertified steel is capped at 170 N/mm² and a 6 m span.

### 3. Material factors and overturning (E2.3.2.2, E4.2)

| Item | Factor |
|---|---|
| Class 1 and Class 1H | γm1 = 1.0 and γm2 = 1.2, so py = Ys / 1.0. Ultimate design strength is also limited to ultimate tensile strength divided by 1.2 |
| Class 2 | May be used if tested and found to comply, with γm1 = 1.1 and γm2 = 1.3 |
| Serviceability | Load factors typically 1.0. The material factor on Young's modulus is 1.0 |
| Overall stability | Factored loads for sliding, overturning, and uplift. The Building (Construction) Regulations prevail where they are more onerous: Code combination 2 uses 1.0 dead ± 1.4 wind; the Regulations use 1.0 dead ± 1.5 wind |
| Diaphragm | Floor and roof slabs that form part of the lateral system need strength and fixings to deliver horizontal force to the collectors. Cladding must be strong enough to deliver wind load to the frame |
| Earth and water (E2.5.4) | If worst-credible earth and groundwater loads are used, the partial load factor may be 1.2 instead of 1.4 |

**SD takeaway:** Check overturning to the Building (Construction) Regulations' 1.5 wind factor, which is stricter than the Code's 1.4, and keep Class 1 steel at γm1 = 1.0.

### 4. Robustness and key elements (E2.3.4)

The Materials follow the tie, element-removal, and key-element routes used in BS 5950 and BS 8110.

| Route | Requirement |
|---|---|
| Ties | Horizontal tension ties at each principal floor (about 3.5 m to 4.5 m spacing; a part mezzanine need not be included) and vertical ties in principal columns and walls. Minimum design ultimate horizontal tie force 75 kN per beam |
| Deemed robust | A steel frame designed to the five conditions in clause 2.3.4.3 may be assumed not susceptible to disproportionate collapse |
| Local collapse limit | The portion at risk must not exceed 15% of the floor or roof area or 70 m², whichever is less, at that level and at one adjoining floor or roof. If it does, the support is a key element |
| Key element | Design for 34 kPa (also stated as 34 kN/m²) under clause 2.5.9. If the key-element route is chosen, element-by-element removal need not be checked. Higher pressure may be needed for more powerful explosives |
| Lateral system | No substantial part of the building may rely on a single lateral-load element. Each part between expansion joints is a separate structure |
| Accidental deformation | Large permanent deformation is acceptable under accidental or extreme loading of non-key elements |

**SD takeaway:** Provide the tie grid, including 75 kN per beam, or treat any member whose loss exceeds 15% or 70 m² as a key element designed for 34 kPa.

### 5. Minimum lateral load and notional forces (E2.5.3, E2.5.8)

| Load | Where it applies |
|---|---|
| Minimum wind | Unfactored wind not less than 1.0% of unfactored dead load, applied at each floor from that floor and its associated vertical structure, in combinations 2 and 3 |
| Light internal structures | Factored lateral load is the greater of 1% of factored dead plus imposed load, or a factored lateral pressure of 1.0 kN/m² on the enclosing elevation, whether or not it is clad |
| Notional horizontal force | 0.5% of factored dead plus live load: 0.005 × (1.4 DL + 1.6 LL), combination 1 only, as an ultimate load. Not applied to foundations and not combined with other horizontal loads |
| Notional lateral pressure | 0.5 kN/m² on the enclosing envelope in combination 1. Use the greater of this pressure and the notional horizontal force |
| Ultra sway-sensitive structures | Clause 2.5.8 doubles these notional loads |
| Serviceability combination (E2.4.1) | Combined imposed load and wind: only 80% of the full design values. Combined crane and wind: the greater effect only |
| Imposed load | Do not import partial factors from another country's code. The Materials record a Hong Kong car-park imposed load of 4 kN/m² against a UK value of 2.5 kN/m² |

**SD takeaway:** Carry a 1% dead-load lateral cutoff in combinations 2 and 3, and a combination-1 notional force of 0.5% of factored dead plus live, doubled if the frame is ultra sway-sensitive.

### 6. Deflection and tall-building comfort (E5.2, E5.3.4)

| Check | Rule |
|---|---|
| Table 5.1 | Deflection limits for building structures in general. Covered walkways and similar structures need a justified criterion from the designer |
| Approach (a) | Top deflection limited to height/500 and inter-storey drift to storey height/400 under the design wind in the wind code. This usually avoids a dynamic analysis for a typical building |
| Approach (b) | Dynamic serviceability analysis against the tall-building limits, including cladding, partitions, and finishes. Wind-tunnel testing is optional |
| Approach (c) | Performance-based comfort criteria agreed with the client, normally with wind-tunnel testing |
| Frequency estimate | Lowest natural frequency about f0 = 46/H, with H in metres |
| Cross-wind | May dominate at an aspect ratio of about 5:1 or greater |
| Return period in the comfort basis | 10-year, consistent with JGJ 3-2002 and the National Building Code of Canada 1995. Peak acceleration, not root-mean-square. The adopted table does not vary with natural frequency |

**SD takeaway:** Size a typical tower so wind drift stays within H/500 and storey drift within h/400, and start a dynamic comfort check once the aspect ratio is about 5:1.

### 7. Floor vibration (E5.4)

When beam or floor deflection limits are exceeded, a vibration assessment may be required. The Materials name lightweight long spans, dance floors, gymnastics and aerobics rooms, stadia and especially cantilevered terraces, sensitive production equipment, and operating theatres.

Simply supported beam ends, treated as pins for strength, usually act as fixed ends under small vibration movements because the bolts grip by friction. Model that fixity in the vibration analysis.

**SD takeaway:** Flag long-span or rhythmic-use floors for a vibration check, and model the beam ends as fixed for that check even where strength design treats them as pins.

### 8. Composite slab breadth (E10.2.3, E10.2.5)

| Item | Value |
|---|---|
| Effective breadth, internal beam | span/4, split equally each side, and not more than the slab width that acts with the beam |
| Slab spanning the same way as the beam | Effective breadth limited to 80% of the actual breadth |
| Concrete flange resistance | Rc = 0.45 fcu Be (Ds − Dp) |
| Concrete and reinforcement | Normal-weight concrete and reinforcement follow HKCC. Reinforcement modulus 205 kN/mm² |

**SD takeaway:** Take the composite slab's effective breadth as span/4, cut to 80% when the slab spans parallel to the beam.

### 9. Fire-resistant design (E12)

Section 12 covers steel and steel-concrete composite members, to limit collapse and fire spread. Passive protection named in the Materials is spray, board, intumescent coating, and concrete encasement.

| Item | Basis |
|---|---|
| Standard curve | ISO 834 and BS 476: Part 20 |
| Exposure | Standard fire for prescriptive compartment fires. Natural fire for performance-based design of large enclosures |
| Assessment | Standard fire tests, limiting-temperature methods, and simplified calculation from BS 5950: Part 8. Performance-based design from the advanced calculation models in Eurocode 3: Part 1.2 and Eurocode 4: Part 1.2 |
| Test criteria | Load-bearing capacity, integrity, and insulation in clause 12.2.2 of the Code |
| Elevated-temperature properties | Table 12.1, for simplified thermal calculations only |

**SD takeaway:** Set the fire strategy as either a standard ISO 834 test with protection, or a performance-based natural-fire study for a large enclosure, and do not use Table 12.1 outside simplified calculations.

### Source

`EMSUOS2011e.pdf`

Read with the Code of Practice for the Structural Use of Steel 2011 (2023 Edition) and the April 2026 amendment (`SUOS2011e_Amend202604.pdf`). Wind comfort numbers in the wind code are a separate instrument.
