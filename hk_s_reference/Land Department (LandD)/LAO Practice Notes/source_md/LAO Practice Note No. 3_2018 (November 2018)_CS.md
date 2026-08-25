# LAO Practice Note No. 3/2018 — Computer calculation of areas / coloured building plans
**Architect critical summary for schematic design**  
26 November 2018 | Lands Administration Office — Lands Department  
Issue No. 3/2018 | Supersedes **LAO PN 8/2006** | Applies to new GBP (incl. subsequent amendments/major revisions/re-submissions) received via Centralized Processing System **on or after 1 February 2019**

> Scope note: Electronic **CAD** format and **Coloured Building Plans** so LandsD can check **lease** GFA/SC. Approval/disapproval under lease is still given on **hard copies** — DVD-ROM does not replace paper GBP. **Not** applicable as a DVD/CBP requirement to ordinary A&A (annotations/dimensions on hard copy suffice). Relates to **PNAP ADM-19** para 16 and Appendix F.

---

## Regulatory Overview

AP should follow Annex 1 for CAD on **non-rewritable DVD-ROM**, and Annex 3 for a full set of hard-copy floor plans identical to GBP layouts, coloured for SC, transfer plate, and GFA accountable/non-accountable **under lease**. Soft and hard copies **must be identical**. Practice to be reviewed **6 months** after implementation (including possible BIM for GFA).

---

## Critical main topics and subtopics

### 1. When DVD-ROM / CBP are required — and reject clocks (paras 3–8)

| Item | Rule |
|---|---|
| Approval medium | Hard-copy GBP only |
| CBP vs GBP diagrams | Coloured extents must **match** GFA/SC calculations and diagrams in GBP; mismatch → reject without further checking |
| DVD not conforming (Annex 1 §§3.1–3.4) | LandsD requires replacement; **performance-pledge clock frozen**; replacement **within 7 calendar days** → clock resumes; **after 7 days** → clock **re-set** as new start; no replacement before pledge expiry → reject for insufficient information |
| Pre-1 Feb 2019 receipts | Continue under previous practice |
| A&A / addition / alteration | **No** new DVD-ROM or CBP required; if submitted, **not considered**; put annotations and dimensions on hard-copy GBP |

**SD takeaway:** Budget **hard-copy coloured plans + identical .dwg DVD** for first/major GBP from **1 February 2019**; do not treat A&A as a DVD job.

---

### 2. CAD minimums — reject without further checking (Annex 1)

| Topic | Hard rule |
|---|---|
| Media | Non-rewritable **DVD-ROM** only (unless Director agrees otherwise) |
| Format | **.dwg** only; AutoCAD **R14 or later** (or software accepted by Director); no zip/compress |
| Files | **One** hard-copy drawing per CAD file; default zoom full extent; all approval info in **same** file (cross-ref only if software layer limits; then path trial in hard copy; all files in **one folder**) |
| Covering letter | List drawing file name(s) used for lease area checking; **certify** GFA/SC computations and deductions are **directly from CAD with no manual input** — missing this → reject |
| Layers | Names per **Annex 2** (CSWP); non-conforming layer names → reject; extra layers allowed if legend + covering letter |
| Model space | True size, **1 drawing unit = 1 mm or metre**, precision nearest **mm**; LandsD default checker is **millimetre** |
| Polylines | **Closed** polylines; one closed polyline = one area diagram; open / self-intersecting / duplicated → reject |
| Dimensions | Software-generated true dimensions in Dimension Layer; **typed-in** dimensions → reject |
| Areas | **m²** to **3 decimal places** |
| Content | No lighting/appliances etc. not requiring Director’s approval under lease |
| If minima met | Diagrammatic GFA/SC/green-feature **breakdowns not required** on plans; **annotations and dimensions still required** on each floor plan |

**SD takeaway:** Draw lease GFA/SC as **closed mm polylines on Annex 2 layers** with auto dimensions and a covering-letter CAD-no-manual-input certificate — any typed dimension or open polyline is an automatic reject.

---

### 3. Layer families and coloured-plan colours (Annexes 2–3)

| Calculation family | Layer stem (ARC prefix ignored by LandsD checker) |
|---|---|
| Non-domestic SC | ADA08610 / 08615 + 0861A–Z deductions (JPN 1&2, curtain wall, E&M/refuse/APP-89 lifts, private parking/L/UL, misc.; skip I and O) |
| Domestic SC | ADA08620 / 08625 + 0862A–H then J–Z (adds caretaker office/quarters, rec facilities, OC office) |
| Non-domestic GFA | ADA08640 / 08645 + 0864A–K then L–Z (adds covered walkways, mail rooms/nests for **C/I** only, RCHE, GA, PTT, hotel BOH) |
| Domestic GFA | ADA08650 / 08655 + 0865A–M, P, then N–Z (adds bay windows, rec facilities under **PN 4/2000(B)**, logistic service room for **residential** only, rec-facility deduction layer) |
| NOFA | ADA08670 / 08675 |
| UFA / greenery | ADA08690 / 08695; 0869A–B obsolete rec under PN 4/2000; 0869C–H greenery / 50% green / green roof |
| Open space | ADA08600 / 08605 |
| Dimension | ADA086_8 |

**Standard CBP colours (RGB):** transfer plate = red thick dash (227,100,102); SC line = blue thick dash (73,167,209); building line above = black thick dash; residential = orange (255,164,25); balcony/UP edged orange; caretaker office = light brown hatched black; caretaker quarters = light brown; OC office = light brown cross-hatched; rec = pink (255,167,255); office = red hatched black; retail/commercial = red; hotel = light blue (144,214,236); GFA non-accountable **inside** accountable = blue; **outside** = yellow (255,237,61). Extra colours allowed (e.g. industrial, GA) if declared to LandsD. One hard copy, **same scale/size** as GBP floors.

**SD takeaway:** Colour **residential orange / rec pink / hotel light blue / deducted-in-GFA blue / deducted-outside yellow** on a full floor set that matches the CAD layers — LandsD checks colour vs numbers.

---

### Source

- `PN 3_2018.pdf` (LAO PN Issue No. 3/2018, 26 November 2018)
- Read with: **PNAP ADM-19** Appendix F; **LAO PN 2/2018** and **4/2018** (note 4/2018 Stage 1 says DVD-ROM **not** required at Stage 1); **LAO PN 4/2000(B)**; **PNAP APP-89**; **JPN Nos. 1 & 2**
