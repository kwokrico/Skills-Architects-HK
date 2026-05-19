# HK Procurement Routes — Full Comparison

Reference for `hk-procurement-strategy`. Use with `hk-tender-contract-administration` §4A for contract identification and §10–11 for NEC administration.

---

## 1. Traditional Procurement (Design-Bid-Build)

### Mechanism

The Employer engages the Architect (as **Authorized Person / AP**) and consultants to fully develop the design and construction documentation (General Building Plans, structural calculations, and Bills of Quantities). The package is then competitively tendered to **Registered General Building Contractors (RGBC)**.

### Contract forms used

| Sector | Form |
|---|---|
| Private | HKIA/HKIS Standard Form of Building Contract — **With or Without Quantities** (2005/2006 editions) — codes `SFBC-Private-WQ` / `SFBC-Private-WOQ` |
| Public | Government **General Conditions of Contract (GCC)** for Building Works — code `GCC-Building` |

### Risk allocation

| Risk | Holder |
|---|---|
| Design | Employer and design team |
| Construction (cost and time of execution) | Contractor |
| Statutory submissions | Client's AP and consultant team |

### Hong Kong context and fit

- Benchmark route for **premium private residential**, complex **high-rise commercial** (e.g. Central Grade A offices), and **traditional public works**.
- Excellent where the Architect must retain strict aesthetic control over the building envelope, spatial transitions, and custom detailing (e.g. Mid-Levels residential blocks).
- **Drawback:** No overlap between design and construction. **28-day statutory buffers** for BD plan approvals and consents must be mapped **sequentially** in the master programme (`hk-consent-scheduling`).

### Architect / AP / CA implications

- AP manages BD submissions directly; high control over GBP and consent pathway.
- Architect often acts as **Contract Administrator** under SFBC; certifies EOT and payment per contract.
- Cost certainty is strong at tender if BoQ and design are complete; post-award variation risk remains.

---

## 2. Design and Build (D&B)

### Mechanism

The Employer provides an initial brief, **performance specifications**, and sometimes a preliminary concept plan (often to BD Scheme or preliminary GBP stage). The **D&B Contractor** employs its own design team to complete construction documentation, manage statutory submissions, and execute the works.

### Contract forms used

| Sector | Form |
|---|---|
| Public | Administrative Services Department (**ArchSD**) D&B Conditions of Contract; **Development Bureau (DEVB)** Standard D&B Form — codes `D&B-ArchSD` / `D&B-DEVB` |
| Private | Bespoke or HKIA-aligned D&B — code `D&B-HK` (verify title page) |

### Risk allocation

| Risk | Holder |
|---|---|
| Design coordination and most statutory delivery risk | Contractor (single-point responsibility) |
| Design quality vs brief | Employer if ER is weak; contractor if ER is prescriptive |
| Independent checking | Client typically retains checking engineer / employer's agent |

**Example:** If structural grids do not clear an MTR station box or a transfer slab requires redesign, the contractor absorbs coordination impact.

### Hong Kong context and fit

- Extensively used by the Hong Kong Government for **hospitals**, **sports complexes** (e.g. Kai Tak Sports Park), and **government offices**.
- Allows **fast-tracking** (e.g. foundation packages while contractor's architect refines superstructure).
- **Drawback:** Potential loss of architectural control; finishes may skew utilitarian unless **Employer's Requirements (ER)** are exceptionally robust.

### Architect / AP / CA implications

- AP role shifts to contractor's team for submissions; client team reviews and checks.
- Architect may be Employer's Representative or ER author — not contractor's design lead.
- Typhoon EOT: time for **site** stoppage only; design delay during T8 is typically contractor risk (see typhoon reference).

---

## 3. Management Contracting and Construction Management

### Management contracting (MC)

**Mechanism:** Employer appoints a **Management Contractor (MC)** early in design to act as an extension of the project management team. The project is split into **trade packages** (piling, structural core, facade, fitting-out) tendered to **Works Contractors** who contract with the MC.

**Hong Kong fit:** MC paid **fee + actual cost** of works packages. Construction can start (excavation, lateral support) before upper tower floors are detailed.

**Contract:** Bespoke MC agreement + package subcontracts — code `MC-HK`.

### Construction management (CM)

**Mechanism:** Similar package breakdown, but trade contractors contract **directly with the Employer**. The **Construction Manager** acts as agent to manage, coordinate, and programme packages on site.

**Hong Kong fit:** Rarely used for standard private residential due to administrative burden and **direct contractual risk** on the developer. Selective use for **hyper-complex renovations** or specialty **alterations & additions (A&A)** where flexibility is paramount (`hk-alterations-additions`).

**Contract:** Bespoke CM appointment + employer–trade contracts — code `CM-HK`.

### Risk allocation (both)

| Risk | MC | CM |
|---|---|---|
| Design lead | Consultant architect | Consultant architect |
| Package commercial risk | Largely via MC to Works Contractors | **Employer** bears direct trade risk |
| Interface / handover | Critical — typhoon can cascade compensable claims | Same interface risk, employer exposed |

### Architect / AP / CA implications

- Client's AP coordinates design; packages integrated incrementally.
- Architect/PM must maintain **package interfaces**, handover dates, and separate EOT chains per trade.
- QS supports multiple valuations and PC sums (`hk-cost-consultancy`).

---

## 4. Collaborative Procurement — NEC4 and Partnering

### Mechanism

Shift from adversarial contracting (claims, variations, liquidated damages as primary tools) toward **risk-sharing registers**, **early warnings**, and **target-cost** options. Legally driven in public sector by **Development Bureau**.

### Contract forms used

- **NEC4 Engineering and Construction Contract (ECC)** — Options **A to E**.
- Hong Kong public works: commonly **Option C** (Target Cost Contract with Activity Schedule).
- Pain/gain: savings or overruns shared per pre-agreed ratio between Employer and Contractor.

**Mandatory context:** NEC4 is mandatory for major Hong Kong public works under DEVB policy (mid-2020s onward). Also adopted by **MTR Corporation**, **Airport Authority** (e.g. Three-Runway System), and similar statutory clients. **Verify current circular and contract data.**

### Risk allocation

| Element | Treatment |
|---|---|
| Change | Compensation Events (CEs), not only variations |
| Risk | Early Warning (EW) register + risk reduction meetings |
| Cost (Option C) | Target cost, defined cost, pain/gain share |
| Weather (typhoon) | CE only if statistical threshold met — not traditional force majeure wording |

### Hong Kong context and fit

- Reduces litigation volume on unforeseen conditions (e.g. cavernous marble, deep utilities) when pain/gain and EW are operated properly.
- Requires **dedicated resourcing**: PM, Supervisor, programme submissions, CE quotations, communications register (`hk-tender-contract-administration` §10).

### Architect / designer role

- May be separate PSC appointment; design may be employer's or contractor's depending on Works Information.
- Collaborate on EW and interface risks; do not assume SFBC-style certifier role without checking NEC role map.

---

## 5. Master Comparison Table

| Strategy | Design lead | Statutory (AP) | Cost certainty | Speed |
|---|---|---|---|---|
| Traditional | Consultant architect | Client AP | High at tender; variation risk | Slower |
| D&B | Contractor architect | Contractor AP (client checker) | High if ER fixed | Fast |
| Management contracting | Consultant architect | Client AP | Lower; PC sums | Fast |
| Construction management | Consultant architect | Client AP | Lower; employer package risk | Fast |
| NEC4 Option C | Variable | Risk register + collaborative | Shared target | Variable |

---

*Cross-links: `hk-tender-contract-administration` §4A, §10–11; `hk-consent-scheduling`; `hk-plan-of-work` Stages 1–3 procurement tasks.*
