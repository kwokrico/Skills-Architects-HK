# Code of Practice for the Structural Use of Steel 2011 — Amendments (April 2026)
**Architect critical summary for schematic design**
April 2026 | Buildings Department

> Scope note: This is the April 2026 amendment sheet to the Code of Practice for the Structural Use of Steel 2011 (2023 Edition). It changes tall-building acceleration, composite-column grades, dissimilar-steel welding, and footbridge vibration. It is **not** the 2023 Edition.

## Regulatory Overview
The sheet is a structural-design amendment, not a loading code. Comfort acceleration is no longer a fixed milli-g table in this clause; composite filled columns may use higher steel and concrete grades than encased columns.

## Critical main topics and subtopics

### 1. Tall-building acceleration (clause 5.3.4)

| Item | Amended rule |
|---|---|
| Analysis | A dynamic analysis of building motion, frequency and acceleration is still required |
| Acceptance | Occupant comfort is acceptable if the **1-year** and the **10-year** peak accelerations are less than the limits in the **HKWC** |
| Removed from this clause | The previous fixed caps (residential **15** milli-g and office/hotel **25** milli-g) for the worst 10 consecutive minutes of a 10-year wind |

**SD takeaway:** Do not lock residential acceleration at 15 milli-g from this clause; both the 1-year and 10-year peaks must meet the HKWC limits.

### 2. Welding dissimilar grades (clause 3.4)

| Item | Rule |
|---|---|
| Steels with design strength not exceeding **690 N/mm²** | Yield strength, ultimate tensile strength, elongation and Charpy value of the consumable must be equal to or better than the grade being welded |
| Different grades welded together | Consumable requirements follow the **lower** grade. The previous rule (the most onerous grade governs) is deleted |
| Ultra-high-strength steel | A lower-strength consumable may be used if needed to make a suitable joint. Elongation and Charpy value should still match the parent material. Design strength of the weld is then based on the weld material |
| Ys and Us (clause 3.1.3) | For design strength above 690 N/mm², py may be taken as Ys/γm1 but not greater than Us/γm2. Ys and Us are determined according to clause 3.1.2 |

**SD takeaway:** A joint between two steel grades is specified to the lower grade, not the higher one.

### 3. Concrete in composite construction (clauses 10.1.2 and 10.5, Figure 10.17, Tables 10.1, 10.11 and 10.13)

| Item | Rule |
|---|---|
| Aggregate | Nominal maximum size not exceeding **20 mm** |
| Density, if no other information | Wet **2450 kg/m³**, dry **2350 kg/m³** |
| Grade window in clause 10.1.2 | **C25 to C80**, then follow clause 10.2.1(2), 10.4.1(2) or 10.5.1(3) for composite beams, composite slabs with profiled steel sheet, or composite columns. Otherwise justify by test and analysis |
| Short-term modulus | Equation (10.1) and Table 10.1 give Ecm (kN/mm²) from fcu (N/mm²). The text layer shows the tokens 3.46, fcu and + 3.21 in equation (10.1). Use the printed equation and table; do not reconstruct the algebra from this summary |
| Concrete-encased steel section | Yield strength **235 to 460 N/mm²**, concrete **C25 to C60** |
| Concrete-filled hollow section | Yield strength **235 to 690 N/mm²**, concrete **C25 to C80** |
| Filled hollow section above C60 | Special attention to quality assurance, temperature control and curing (clause 10.5.2(5)) |
| Creep and shrinkage | Still considered if they reduce stability significantly. May be ignored if the increase in first-order moments from creep and from permanent-load axial force is not greater than **10%** |
| Partial factor | gf reduced to **80%** for internal forces from independent actions that increase resistance |
| Tables 10.11 and 10.13 | Maximum geometric ratios, and buckling curves and member imperfections, are updated. The replacement numbers did not extract as text |

**SD takeaway:** A filled hollow composite column can use steel up to 690 N/mm² and concrete up to C80; an encased section stays at 460 N/mm² and C60, and concrete above C60 in a filled section needs a curing and temperature-control method.

### 4. Footbridges and lap-joint notation (clause 13.6.4, equations 9.9 and 9.10)

| Item | Rule |
|---|---|
| Vertical frequency | Not less than **3 Hz** |
| If vertical frequency is below 3 Hz | Limit maximum vertical acceleration av to the value in the recognised guidelines in **Annex A2.5** |
| Lateral crowd response | Need not be considered if there are no significant lateral modes with frequencies below **1.5 Hz** |
| Equation 9.9 | Typographical correction to the lap-joint length factor. The printed equation governs |
| Equation 9.10 | an is the net cross-sectional area with reduction for openings. Ke remains 1.2 (S275), 1.1 (S355), 1.0 (S460), 0.84 (S550), 0.80 (S690) |
| Mechanised and automatic welding | Added in clauses 14.3.2 and 14.3.3, Table 14.2b (carbon equivalent value) and Annex A1.4.2.2. The acceptance criteria did not extract as a numeric table |

**SD takeaway:** A footbridge needs a vertical natural frequency of at least 3 Hz, or an Annex A2.5 acceleration check, and lateral crowd loading is in play once a significant lateral mode sits below 1.5 Hz.

### Source

`SUOS2011e_Amend202604.pdf` (source_reference). Read with the Code of Practice for the Structural Use of Steel 2011 (2023 Edition). The HKWC limits cited in clause 5.3.4 are not printed in this sheet.
