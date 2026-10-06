# Code of Practice for Foundations 2017 — Amendments (September 2025)
**Architect critical summary for schematic design**
September 2025 | Buildings Department
Appendix A to PNAP APP-18

> Scope note: This is the September 2025 amendment sheet to the Code of Practice for Foundations 2017 (2024 Edition). It raises two bearing-capacity caps for buildings with basements on granular soil, and it changes how Young’s modulus may be taken from SPT N. It is **not** the 2024 Edition.

## Regulatory Overview
The sheet applies to shallow foundations and to rafts on granular soil, including saprolite and residual soil, and it revises the tension-load test wording for piles. Plate-load testing and the settlement trigger table are aligned with the same modulus change.

## Critical main topics and subtopics

### 1. Allowable bearing pressure (clause 2.2.4)

The allowable vertical bearing pressure qa is still taken from the bearing-capacity equation in clause 2.2.4. The text layer did not preserve the algebra. The terms and caps that did extract are below.

| Item | 2025 rule |
|---|---|
| qu cap, general granular soil | **3 000 kPa** |
| qu cap, foundations supporting building(s) with basement(s) on granular soil | **4 500 kPa** |
| qo | Effective overburden at the base, qo = γs' Df |
| What qo must exclude | Any overburden removed temporarily or permanently during the design life. Discount voids left for underground utilities |

Note (1) on overburden depth used to derive q:

| Case | Maximum depth of subsoil |
|---|---|
| Shallow foundation | Not greater than **3 m** or **Bf**, whichever is smaller |
| Foundations supporting building(s) with basement(s) on granular soil | Effective depth = minimum overburden depth around the basement perimeter, not greater than **10 m** or **Bf**, whichever is smaller |

**SD takeaway:** A basement on granular soil may use qu up to 4 500 kPa and an overburden depth up to 10 m or Bf; without a basement the caps stay at 3 000 kPa and 3 m or Bf.

### 2. Young’s modulus from SPT N (clause 2.3.1(4), clause 4.2.2(2)(c))

| Case | Es (MPa), if no better data |
|---|---|
| Shallow foundations on granular soil | **1 ×** SPT N |
| Raft on granular soils from in-situ rock weathering (saprolites and residual soils) with SPT N **> 30** | **1.5 ×** SPT N |

The previous shallow-foundation shortcut (Es = 1 × N only when allowable bearing pressure is not greater than 250 kPa) is removed. The 1 × N value now applies to shallow foundations generally, in the absence of more accurate data. Empirical SPT correlations can be unsafe or over-conservative.

Plate-load test clause 4.2.2(2)(c): the Es used for settlement must be greater than **1 ×** SPT N, or **1.5 ×** SPT N for those weathered granular soils with N > 30, as appropriate.

**SD takeaway:** Do not keep the old 250 kPa gate on Es = N; use 1.5 N only for a raft on weathered granular soil with N above 30.

### 3. Settlement triggers and tension tests (Table 7.2, clause 8.10)

| Item | Change |
|---|---|
| Table 7.2 title | Typical values for the three triggering levels now cover nearby buildings, structures, **land** or services that are not sensitive to settlement. The numeric trigger levels did not extract as text |
| Tension test cap | The maximum test load must not stress the test pile or anchor beyond yield |
| When the 1.5 factor applies | Design tension capacity based on bond or friction between rock/soil and concrete/grout, taken as not exceeding **50%** of the corresponding allowable bond stress in compression |
| Test load | May be set at **1.5** times that design tension capacity |

**SD takeaway:** A tension pile test at 1.5 times working tension is available only where the design bond is kept to at most half the allowable compression bond, and the test load must still stay below yield.

### Source

`FoundationCode2017_amendment202509.pdf` (source_reference). Read with the Code of Practice for Foundations 2017 (2024 Edition) and PNAP APP-18.
