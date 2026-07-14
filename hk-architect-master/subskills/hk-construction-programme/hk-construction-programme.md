---
name: hk-construction-programme
description: Activate for Hong Kong construction sequencing — main-line milestones, fast-tracking and follow-the-structure (工序穿插), standard floor cycle, MEP embed with structure, facade lead, hold points, procurement parallel lane, and 4-week look-ahead. Use for construction sequence, programme logic, sectional completion, or 主線工序 / 標準層 questions on high-rise RC residential towers.
disable-model-invocation: true
---

# HK Construction Programme

Contractor-side **construction sequencing and fast-tracking** for Hong Kong high-rise projects (archetype: B2/G15 RC residential tower). Distinct from client **programme governance** (`hk-project-management`), **AP/RSE statutory supervision** (`hk-site-supervision`), and **EOT/claims** (`hk-tender-contract-administration`).

**Deep reference** (load via dispatcher `references_available`):
- `../../references/hk-construction-sequence-swimlanes.md` — full 10-lane diagram (Traditional Chinese source) + HK mapping + RIBA Stage 5 bridge

---

## When to Use This Skill

| Question type | Use this skill | Use instead |
|---|---|---|
| Construction sequence, swimlanes, 工序穿插, fast-tracking | `hk-construction-programme` | — |
| Standard floor cycle (7–10 days), follow-the-structure facade | This skill + reference | `hk-building-envelope` (facade detail) |
| MEP embed / first fix with structure | This skill + reference | `hk-building-services` |
| Hold point register vs contract ITP | Reference lane 10 | `hk-site-supervision` (AP/RSE) |
| Master programme governance, client dashboards | — | `hk-project-management` §8 |
| Procurement route selection, typhoon EOT | — | `hk-procurement-strategy` |
| EOT notices, interim certificate, CA duties | — | `hk-tender-contract-administration` §12 |
| RIBA Stage 5 task checklist | Cross-link reference | `hk-plan-of-work` |

## Halt criteria

- Do not infer **statutory compliance** (consent, OP, FSD Fire Certificate) from sequence logic alone — confirm BD consent conditions, AP/RSE inspection regime, and executed contract programme.
- Do not state fixed durations (e.g. 720 days, +8.7% cost) as project truth without user-supplied programme/QS data.
- Taiwan/general-APAC terms in the reference require **HK substitution** (see §4) before applying to a Hong Kong site.

---

## 1. Archetype Defaults (Illustrative Only)

| Parameter | Diagram baseline | HK note |
|---|---|---|
| Structure | RC 鋼筋混凝土 | Dominant private residential — `hk-structural-systems` |
| Storeys | B2 / G15 | Verify lease, OZP BHR, and GBP |
| Use | 集合住宅 | `hk-building-typology` |
| Duration | 720 calendar days | Sensitivity only; programme is contract-specific |
| Management goal | 安全第一、品質優先、如期完工 | Align with SSP + contract KPIs |

---

## 2. Swimlane Index

| Lane | Name | Deep reference section | Primary HK sub-skill |
|---|---|---|---|
| 1 | 主線工序 | §1 Main line | `hk-plan-of-work` Stage 5, `hk-project-management` |
| 2 | 地下工程穿插 | §2 Underground | `hk-structural-systems`, `hk-site-supervision` |
| 3 | 機電預埋同步 | §3 MEP embed | `hk-building-services`, `hk-construction-documentation` |
| 4 | 標準層循環 | §4 Standard floor | `hk-construction-programme`, `hk-mic-dfma` if modular |
| 5 | 外牆工程穿插 | §5 Facade | `hk-building-envelope`, `hk-procurement-strategy` |
| 6 | 機電工程穿插 | §6 MEP phasing | `hk-building-services`, `hk-fsd-licensing-compliance` |
| 7 | 裝修工程穿插 | §7 Fit-out | `hk-practical-completion-snagging` |
| 8 | 驗收管理穿插 | §8 Acceptance | `hk-practical-completion-snagging`, `hk-site-supervision` |
| 9 | 採購發包泳道 | §9 Procurement | `hk-procurement-strategy`, `hk-cost-consultancy` |
| 10 | 品質管理 (Hold Point) | §10 QC | `hk-site-supervision`, `hk-construction-health-safety` |
| AI | 智慧預警 | §11 AI lane | `hk-project-management` §8 (advisory dashboards) |

Load `../../references/hk-construction-sequence-swimlanes.md` for step lists, interface rules, and programme artefacts.

---

## 3. HK Substitution Table (Diagram → Hong Kong)

| Diagram term | HK practice | Authority / contract hook |
|---|---|---|
| 假設工程 | Site establishment, hoarding, utilities diversion, survey | Contract programme; LandsD / utility undertakers — detail: `hk-site-establishment` |
| 連續壁工程 | **Pile wall / diaphragm wall / ELS** (site-specific) | RGE + RSE; geotechnical submission |
| 基樁工程 | Bored piles, rock sockets, pile caps | RSE certification |
| 土方開挖 / 支撐 / 降水 | Excavation & lateral support; dewatering where required | AP/RSE hold points; LD site safety |
| 驗收交屋 | **PC** (contract) + **OP** (BD) + FSD Fire Certificate | `hk-practical-completion-snagging`, `hk-op-submission-strategy` |
| 蓄水試驗 (24hr) | Wet-area flood test per contract spec | Architect/CA inspection record |
| 鋁門窗框 | Aluminium window frame — typical HK residential | `hk-building-envelope`; typhoon performance |
| 工序穿插 | Fast-tracking / overlapping trades | Programme logic; not a statutory term |
| 品質管理 Hold Point | Contract **ITP** + AP/RSE critical inspections | SSP — `hk-site-supervision` §2 |
| AI 成本預警 +8.7% | Example dashboard only | QS forecast — never hard-code |

---

## 4. Architect / PM Early-Freezes (Design → Site)

Freeze before superstructure cycle repeats:

1. **Riser and sleeve schedule** — coordinates lane 3 embed with structure (avoid post-pour chasing).
2. **Typical floor structural grid** — lane 4 cycle; transfer slab level fixed at concept (`hk-structural-systems` §3).
3. **Facade panel typology and long-lead procurement** — lane 5 start at structure +5–7 floors.
4. **MEP zoning and shaft sizes** — lanes 3 and 6; separate **FSD submission path** from BD MOE.
5. **Wet-room waterproofing specification** — lane 7; align with PC/snag categories.
6. **Parallel procurement tracker** — lane 9 runs from brief freeze, not from structure completion.

---

## 5. Interface Rules (Summary)

- **Facade follow-structure:** start external envelope when superstructure reaches ~5–7 floors below top — reduces scaffold cycles; confirm wind/watertight strategy (`hk-building-envelope`).
- **MEP first fix before pour:** lane 3 runs inside lane 4 every cycle.
- **Procurement lane 9:** parallel to lanes 1–4 from award; long-lead items (lifts, switchgear, curtain wall) on critical path.
- **Acceptance lane 8 vs statutory:** contract sectional completion ≠ OP; map both on master programme.
- **MiC / D&B:** shorten lane 4 or overlap lane 5 earlier — see reference §12 variants.

---

## 6. Programme Artefacts

| Artefact | Owner | Content |
|---|---|---|
| Master programme | Contractor (accepted by PM/CA) | Lanes 1 + 9 critical path |
| 4-week look-ahead | Site + PM | Lane-level activities, hold points |
| Hold-point register | QA + AP/RSE | Lane 10 aligned to ITP |
| Procurement tracker | QS + PM | Lane 9 milestones |
| Interface log | Lead consultant | MEP/facade/structure clashes |

Optional output template: `../../references/templates/construction-look-ahead.md`

---

## 7. Six Success Keys (Diagram → Suite)

| Key | Diagram focus | HK sub-skill |
|---|---|---|
| 施工管理 | 工序穿插、進度掌控 | This skill + `hk-project-management` |
| 採購發包 | 流程、成本 | `hk-procurement-strategy`, `hk-cost-consultancy` |
| 品質查驗 | 分階段驗收 | `hk-site-supervision`, lane 10 |
| 機電整合 | 提前介入 | `hk-building-services`, `hk-fsd-licensing-compliance` |
| 裝修協調 | 交叉施工 | `hk-practical-completion-snagging` |
| AI 智慧預警 | 數據決策 | `hk-project-management` §8 (advisory) |

---

## 8. Practical Output Checklist

- [ ] Correct archetype and HK substitutions applied
- [ ] Main line mapped to consent, construction, PC, and OP milestones
- [ ] Overlapping lanes identified with interface owners
- [ ] Hold points distinguished from statutory AP/RSE duties
- [ ] Procurement parallel path linked to long-lead items
- [ ] No fabricated cost or duration without user data

---

*Sequencing advice supports programme planning only. AP certification, CA determinations, and authority approvals remain with the appointed professionals and executed contract.*
