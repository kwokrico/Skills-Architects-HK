# Explanatory Notes to the Code of Practice on Wind Effects in Hong Kong 2019 — Amendments (December 2023)
**Architect critical summary for schematic design**
December 2023 | Buildings Department

> Scope note: This amends the explanatory notes to the 2019 wind code. It adds a way to take the fundamental frequency of towers on a podium, and a net-pressure table for site hoardings and covered walkways. It is **not** the wind code itself (see the separate December 2023 code amendment).

## Regulatory Overview
Two design additions matter at schematic stage: how to estimate across-wind frequency for several towers on one podium, and an all-inclusive net pressure for construction hoarding and covered walkways. The rest of the sheet is wording, a damping example, and a torsion-procedure figure renumbering.

## Critical main topics and subtopics

### 1. Across-wind frequency for towers on a podium (clause 2.2.3)

The existing exemption is unchanged: with natural periods of H/46 in both directions, across-wind base moment need not be checked when **H / min(B, D) < 5**, **H < 100 m** and **N > 0.5 Hz**.

For multiple towers over a common podium, the fundamental frequency for across-wind effects may be taken by any one of these:

| Assumption | Limit |
|---|---|
| (a) Tower alone | Tower extended to the building base, not connected to the podium |
| (b) Tower plus a slice of podium | From the structural wall or column edge of the modelled tower, not exceeding the least of **20 m**, **three bays** of the podium structure, and the middle line to the nearby tower. No substantial openings in the floor slabs of that integrated portion; openings may be considered separately |
| (c) Engineering model | The integrated podium portion in conformity with recognised engineering principles and practice |
| Computer model | If an integrated model of towers and podium exists, the dominant fundamental frequency of the mode mainly aligned with the across-wind direction of that tower may be used, with engineering justification |
| Unclear tributary | If (b) cannot define the tributary, use an integrated model of all towers and the podium |

**SD takeaway:** Towers sharing a podium do not automatically use the standalone H/46 period; lock frequency by (a), (b) within 20 m / three bays / the mid-line, (c), or an integrated model.

### 2. Hoarding and covered walkway net pressure (clause 2.5, Table 2-1)

The 37% rule remains for hoarding and covered walkway associated with a construction site, contractor shed, bamboo shed, tent or marquee that is not for residential use: wind pressures not less than **37%** of the pressures in the Code.

For hoarding and covered walkway associated with a construction site, Table 2-1 may be used instead. The text layer returned these rows. Cp and Ss are included. Linear interpolation is permitted for intermediate heights.

| Height above ground Z | Design net pressure (kPa), all-inclusive |
|---|---:|
| ≤ 2.5 m | 0.63 |
| 5 m | 0.70 |
| 10 m | 0.77 |

Notes on the table: beneficial self-weight of steel members may be considered; a topography factor is required where local topography may adversely affect wind. Further rows, if printed below 10 m, were not in the text layer — confirm the PDF table before using a taller hoarding.

**SD takeaway:** Site hoarding and covered walkway can be sized from Table 2-1 (0.63 / 0.70 / 0.77 kPa at 2.5 / 5 / 10 m) instead of applying 37% by hand, and the value already includes Cp and Ss.

### 3. Shelter, accidental opening, and torsion bookkeeping (clauses 4.3.1 and 6.4, Appendices C2 and E3.1)

| Item | Amended rule |
|---|---|
| Accidental dominant opening (clause 4.3.1) | Not a compulsory requirement of this Code (Appendix B1.3). The previous wording said it was out of scope |
| No building-removal investigation (clause 6.4) | Shelter benefit limited to **80%** of the loads of the Standard Method. Compare **total base moments**. The previous cap was 80% of the along-wind value |
| Appendix C2 example | The replacement paragraph records an outlying high damping value for a cubic building. The text layer prints the height as **1250m**. Confirm that digit string on the PDF before relying on it; it is an example, not a design limit |
| Appendix E3.1 | Torsion procedure now refers to Figure E-7(a), (b), (c) and (d), and the example resultant uses F1-1, F2-1, F3-1 and F4-1 |

The torsion procedure is bookkeeping. The cubic-building sentence in Appendix C2 is an example only.

**SD takeaway:** If a building-removal study is not done, cap the shelter benefit at 80% of the Standard Method loads and compare total base moments, not the along-wind component alone.

### Source

`ExplanatoryNotesWindEffects2019e_Amend2023e.pdf` (source_reference). Read with the Explanatory Notes to the Code of Practice on Wind Effects in Hong Kong 2019 and the December 2023 wind-code amendment (WindEffects2019e_Amend2023e.pdf).
