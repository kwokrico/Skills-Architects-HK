# Code of Practice for Structural Use of Concrete 2013 — Amendments (February 2022)
**Architect critical summary for schematic design**
February 2022 amendment sheet | Buildings Department (BD) | Amends the Code of Practice for Structural Use of Concrete 2013 (2020 Edition)

> Scope note: This nine-page appendix is the February 2022 amendment sheet to the 2020 Edition. It adds plain-concrete lining design (clause 6.2.3 and Figure 6.18b), revises concrete-cube size and Table 10.2 compliance numbers, retunes the standard-deviation triggers in clause 10.3.4.2(b), and adds early-age strength monitoring by the maturity method (clause 11.7.5.4, Table 11.2, ASTM C1074-19ε1 in Annex A). It is not a replacement of the 2013 Code, and it does not reprint unamended clauses.

## Regulatory Overview
The sheet inserts clause 6.2.3 for plain concrete linings in tunnels or caverns, with axial-load interaction limits tied to eccentricity, and it points shear checks back to clauses 6.1.2.5(k) and 6.2.2.3(r). It also changes how cube strength is sampled and judged during construction, and it allows a maturity-method proposal to justify striking formwork and falsework earlier than the minimum periods in clause 10.3.8.2, subject to Table 11.2 correction factors and a 24-hour floor.

## Critical main topics and subtopics

### 1. Where plain concrete lining is allowed (new clause 6.2.3.1)
Plain concrete is described as suitable for members with high axial load and relatively low bending moment. For tunnel or cavern linings, the sheet says the following criteria can generally be applied:

| Criterion | Requirement |
|---|---|
| (a) Curvature | Adequate to accommodate axial distribution of external loads |
| (b) Geology and stress | Relatively good rock, and the lining always in compression under all load combinations |
| (c) Imperfection | Effect of lining imperfection considered by rigorous structural analysis |
| (d) Invert | An arch may be plain concrete with a reinforced-concrete invert if the junction meets clause 6.2.3.2 |

**SD takeaway:** Do not draw a plain (unreinforced) tunnel or cavern lining unless the lining stays in compression in good rock and a structural check against clause 6.2.3 is in the schematic structural approach.

### 2. Axial capacity of plain concrete lining (clause 6.2.3.2(a), equations 6.63a and 6.63b, Figure 6.18b)
Ultimate axial capacity per unit length \(n_{LT}\) and ultimate moment per unit length \(m_{LT} = n_{LT} e_x\) are read from the Figure 6.18b interaction curve. \(e_x\) is the resultant eccentricity at right angles to the plan of the lining. \(h\) is the lining thickness used in the eccentricity ratios. \(f_{cu}\) is the concrete cube strength used in the equations as printed.

| Eccentricity | Interaction segment | Ultimate axial capacity |
|---|---|---|
| \(e_x \le 0.1h\) | Point 1 to Point 2; rectangular stress block over the whole section | \(n_{LT} \le 0.32 h f_{cu}\) (equation 6.63a) |
| \(0.1h < e_x \le 0.3h\) | Point 2 to Point 3; stress block over part of the section, reducing as eccentricity increases | \(n_{LT} \le 0.4 (h - 2 e_x) f_{cu}\) (equation 6.63b) |
| Above \(0.3h\) | Point 3 to Point 4 | Cracking restriction stops the strength method. The curve is a straight line down to \(n_{LT} = 0\), \(m_{LT} = 0\) |

**SD takeaway:** Keep thrust eccentricity inside \(0.3h\); beyond that the February 2022 method does not give a cracked-section strength for the plain lining.

### 3. Shear in plain concrete lining (clause 6.2.3.2(b))
Design shear stress under shear plus axial compression, without shear reinforcement, is calculated in accordance with clause 6.1.2.5(k). Design shear resistance is checked in accordance with clause 6.2.2.3(r).

**SD takeaway:** A plain lining has no shear reinforcement in this check; shear capacity has to come from the clauses cited above, not from added stirrups assumed later.

### 4. Cube size and sampling (amended clause 10.3.4.2(a))
Compressive strength is determined 28 days after mixing. Use 100 mm cubes, or 150 mm cubes if the maximum aggregate size exceeds 20 mm. Each sample comes from a single batch of fresh concrete. Sampling is at least the rate in Table 10.1, and at least one sample from each grade produced on any one day.

**SD takeaway:** Specification and method statements should state cube size from aggregate size (150 mm only when maximum aggregate exceeds 20 mm), not a single default cube.

### 5. Amended Table 10.2 compliance margins
Column A is the amount by which the average of 4 consecutive results must exceed the specified grade strength. Column B is the amount the specified grade strength may exceed any individual result (the result must not be less than grade strength minus this value). Figures in parentheses are for 150 mm cubes; the leading figure is for 100 mm cubes.

| Specified grade | Compliance criteria | Column A | Column B |
|---|---|---|---|
| C20 and above | C1 | 7 MPa (5 MPa) | 2 MPa (3 MPa) |
| C20 and above | C2 | 5 MPa (3 MPa) | 2 MPa (3 MPa) |
| Below C20 | C1 or C2 | 3 MPa (2 MPa) | 2 MPa (2 MPa) |

**SD takeaway:** Compliance margins now depend on cube size; a 100 mm cube set is judged on the larger Column A margins (7 MPa / 5 MPa for C20 and above).

### 6. When C1 or C2 applies (amended clause 10.3.4.2(b)(i)–(iii))
The amendment replaces the paired 150 mm / 100 mm standard-deviation tests with one threshold stated for the 100 mm basis and a parenthesis for 150 mm cubes.

| Situation | Amended trigger | Result |
|---|---|---|
| Before 40 results, and previous production data from the same plant, similar materials and supervision, show the standard deviation of 40 results is below the threshold | Less than 5.5 MPa (5 MPa for 150 mm cubes) | C2 may be adopted; otherwise C1 |
| A set of 40 consecutive results already judged by C2 exceeds the threshold | Exceeds 5.5 MPa (5 MPa for 150 mm cubes) | Change C2 to C1 on the 35th day after making the last pair in that set |
| Standard deviation of 40 previous consecutive results is below the threshold | Less than 5.5 MPa (5 MPa for 150 mm cubes) | Change C1 to C2 on the 35th day after making the last pair in that set |

**SD takeaway:** Early works without a qualifying production history stay on the stricter C1 margins until 40 results support C2.

### 7. Further numerical triggers in clause 10.3.4.2(b)(iv) and (vi)
The sheet replaces only the figures in these subparagraphs. It does not reprint the lead-in of clause 10.3.4.2(b), so the surrounding test remains the 2020 Edition text.

| Subparagraph | Amended figures |
|---|---|
| (iv), concrete grade not exceeding C60 | Calculated standard deviation exceeds 8.5 MPa (8 MPa for 150 mm cubes) |
| (vi) | Average of the latest 40 results exceeds grade strength by at least 12 MPa (10 MPa for 150 mm cubes), and every individual result exceeds grade strength by at least 5 MPa (4 MPa for 150 mm cubes) |

**SD takeaway:** Over-strong or high-scatter cube runs are judged on these cube-size pairs; do not keep the pre-2022 100 mm figures of 8.5 MPa standard deviation as if they applied to 150 mm cubes.

### 8. Maturity method for early striking (new clause 11.7.5.4, Table 11.2, Annex A)
After casting, in-situ compressive strength at early age may be estimated from the temperature-time history for ages up to 14 days, to decide strength for striking formwork and falsework instead of the minimum periods in clause 10.3.8.2. Because strength gain is rapid within 24 hours, the method is not suitable for justifying a minimum period of less than 24 hours before striking.

A proposal must refer to the acceptable standard in Annex A (ASTM C1074-19ε1, Standard Practice for Estimating Concrete Strength by the Maturity Method, is added) and cover: maturity function and constants; apparatuses and calibration; strength-maturity relationship; estimating in-situ strength; validation; re-calibration and re-validation; quality assurance and supervision. The mix in the structure must be the mix used to derive the relationship.

Table 11.2 correction factors apply to the estimated in-situ compressive strength:

| Mix | ≤ 48 hours after casting | > 48 hours after casting |
|---|---|---|
| Concrete containing pfa (pulverized fuel ash) or ggbs (ground granulated blastfurnace slag) | 0.7 | 0.8 |
| Other concrete mix | 0.8 | 0.8 |

**SD takeaway:** Programme a minimum 24 hours before striking even if maturity readings look high, and apply the 0.7 factor to pfa or ggbs mixes in the first 48 hours.

### Source
`CoP_SUC2013e_amendment202202.pdf` (Amendments to the Code of Practice for Structural Use of Concrete 2013 (2020 Edition), February 2022). Read with the 2020 Edition for every clause this sheet does not replace, including Table 10.1 sampling rates, clause 10.3.8.2 striking periods, clause 6.1.2.5(k) and clause 6.2.2.3(r). Later amendment sheets (June 2023, April 2024) are separate documents and are not incorporated here.
