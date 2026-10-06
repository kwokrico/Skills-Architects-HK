# Code of Practice for Structural Use of Concrete 2013 — Amendments (April 2024)
**Architect critical summary for schematic design**
April 2024 | Buildings Department

> Scope note: This is the April 2024 amendment sheet to the Code of Practice for Structural Use of Concrete 2013 (2020 Edition). It adds coupler-elongation limits, a strut-and-tie method, column-link figures, and a site-mix table for low-strength concrete. It is **not** the 2020 Edition itself.

## Regulatory Overview
The April 2024 sheet is the first place this code sets a strut-and-tie design method and a prescribed mix table for concrete not exceeding 20 N/mm². It also relaxes the 0.1 mm coupler-elongation cap only for couplers longer than 100 mm, and only with crack-width checks.

## Critical main topics and subtopics

### 1. Long type 1 couplers (clause 3.2.8.3, Figure 3.9a)

| Item | Rule |
|---|---|
| Couplers up to the previous rule | Permanent elongation after loading to 0.6fy still must not exceed **0.1 mm** |
| Couplers longer than **100 mm** | Permanent elongation greater than 0.1 mm may be accepted as Figure 3.9a, subject to crack-width control in clauses **7.2.1, 9.4.1 and 12.3.4** |
| Figure 3.9a axes | X = coupler length (mm); Y = permanent elongation after loading to 0.6fy (mm) |

The plotted limit on Figure 3.9a did not survive text extraction. Read the curve from the PDF before using an elongation above 0.1 mm.

**SD takeaway:** Couplers longer than 100 mm may exceed 0.1 mm elongation only inside the Figure 3.9a curve and only if crack width is checked under clauses 7.2.1, 9.4.1 and 12.3.4.

### 2. Strut-and-tie system (clauses 6.1.2.1 and 6.9, Figures 6.21–6.25, equations 6.74–6.81)

Deep beams (clause 5.2.1.1(a)) may now be designed by specialist literature **or** by clause 6.9. A strut-and-tie model is an idealised pin-jointed truss of concrete compression struts, reinforcement tension ties, and concrete nodes.

| Item | Rule |
|---|---|
| Strut-to-tie angle θ | Not less than **25°** and not more than **60°** |
| Node size | From the nodal condition in Figure 6.21, using static equilibrium for shear failure and the plastic stress state (Figure 6.22) |
| Strut strength | fce = **0.32 m fcu** (equation 6.74) |
| Confinement factor m | A2/A1, not greater than **2**. A1 is the loaded area; A2 is the load-distribution area (Figure 6.23) |
| C-C-C node | fce = **0.45 m fcu** (equation 6.75) |
| C-C-T node (one tie) | fce = **0.40 m fcu** (equation 6.76) |
| C-T-T node (two or more ties) | fce = **0.32 m fcu** (equation 6.77) |
| Dry bearing on concrete | fcb = **0.27 m fcu** (equation 6.78) |
| Bedded bearing on concrete | fcb = **0.40 m fcu** (equation 6.79) |
| Steel plate cast into the member | fcb = **0.80 m fcu** if each plate dimension does not exceed **40%** of the corresponding concrete dimension (equation 6.80) |
| Flexible bedding | An intermediate bearing stress between dry and bedded may be used |
| Non-prestressed tie | Ftie = **0.87 fy As** (equation 6.81) |
| Tie layout | Bars evenly distributed across the nodal depth so the centroid coincides with the tie axis |
| Tie anchorage | Clause 8.4. Anchorage starts where the strut edge meets the bearing surface (Figure 6.25). Straight bars extend beyond the node |
| Face reinforcement | Orthogonal grid on each face, minimum **0.25%** |

New symbols in clause 1.5: Ftie, fcb, fce.

**SD takeaway:** A deep-beam or discontinuity region sized by strut-and-tie must keep θ between 25° and 60°, use the node class (C-C-C, C-C-T, C-T-T) for fce, and put at least 0.25% orthogonal steel on each face.

### 3. Column transverse reinforcement (Figure 9.5(g), (h), (i); clause 9.9.2.2(c))

| Detail | Extracted rule |
|---|---|
| (g) | Link passing around the longitudinal bars with an included angle of not more than **135°**; dimension marked **> 150** |
| (h) | Link anchored by hooks with a bend of not less than **135°**; dimension marked **> 150** |
| (i) | Links anchored by hooks bent through not less than **135°**; dimensions marked **≤ 150** |
| Clause 9.9.2.2(c) | Links and ties anchored by hooks of not less than 135° under clause 9.5.2, now including Figures 9.5(g), (h) and (i) as well as (b), (c), (d) and (e) |

**SD takeaway:** Column link detailing now has three extra Figure 9.5 cases; the 150 mm marks and the 135° hooks are part of the accepted arrangement.

### 4. Low-strength and exceptional-project concrete (clause 11.7.1, Table 11.1a)

| Item | Rule |
|---|---|
| Structural concrete | From a supplier certified under the Quality Scheme for the Production and Supply of Concrete (QSPSC), or a similar equivalent |
| Exception | Remote areas (such as outlying islands), or where the volume of concrete **per building project** is less than **50 m³** |
| Even then | The supplier must operate an approved quality system |
| ≤ 20 N/mm² | May use Table 11.1a, batched by weight, for minor structural and non-structural works: on-grade slabs, blinding, U-channels and stepped channels, bedding and haunching for pipes, footings for posts and fences, and mass concrete fill that does not sustain appreciable loading |
| Cement | Ordinary Portland cement |

Table 11.1a (weight of aggregate per bag of cement)

| Strength | Material | 45 kg bag | 50 kg bag | Max free water/cement ratio |
|---|---|---:|---:|---:|
| 10 N/mm² | Fine aggregate | 145 kg | 160 kg | 0.65 |
| 10 N/mm² | 20 mm coarse aggregate | 185 kg | 205 kg | 0.65 |
| 15 N/mm² | Fine aggregate | 120 kg | 130 kg | (blank in the text layer) |
| 15 N/mm² | 20 mm coarse aggregate | 165 kg | 180 kg | (blank in the text layer) |
| 20 N/mm² | Fine aggregate | 95 kg | 105 kg | (blank in the text layer) |
| 20 N/mm² | 20 mm coarse aggregate | 145 kg | 160 kg | (blank in the text layer) |

Only the 10 N/mm² row printed a water/cement ratio (0.65) in the text layer. Confirm the 15 and 20 N/mm² ratios on the PDF table before specifying them.

**SD takeaway:** Do not use Table 11.1a for structural frames; it is limited to the listed minor works at or below 20 N/mm², and the 50 m³ QSPSC exception is per building project.

### 5. Standards and equation 12.2 (Annex A)

| Item | Change |
|---|---|
| Equation 12.2 | Typographical correction. The text layer did not yield a reliable algebraic transcription; use the printed equation |
| BS 8500-1 and BS 8500-2 | Updated from the 2006 editions to the **2015** editions |
| Added | **BS EN 206:2013** Concrete — Specification, performance, production and conformity |

**SD takeaway:** Concrete specifications that cite BS 8500 must use the 2015 parts, with BS EN 206:2013, not the 2006 editions named in the previous annex.

### Source

`CoP_SUC2013e_amendment202404.pdf` (source_reference). Read with the Code of Practice for Structural Use of Concrete 2013 (2020 Edition) and the February 2022 and June 2023 amendment sheets.
