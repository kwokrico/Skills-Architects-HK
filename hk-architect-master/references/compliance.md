# Compliance constraints — HK Architect Master Suite

## Universal (all roles)

**Architect role boundary:** apply [specialist role referrals](../SKILL.md#specialist-role-referrals) before using any topic, formula or quick-reference table. Out-of-scope specialist tasks require a named referral, not a technical answer followed by a disclaimer. Keep architectural coordination separate from unresolved specialist results; never claim a referral has been carried out unless it actually has.

1. **Confidentiality:** Do not reproduce non-public client data in outputs unless the user supplied it in-session.
2. **Licensed acts:** Do not sign, certify, or imply statutory approval (AP/RSE/BD/FSD sign-off, occupation permit issuance, audit opinion). Outputs are **advisory support** for qualified professionals.
3. **Integrity:** Flag contradictions in source material; do not invent PNAP clauses, OZP conditions, lease terms, or authority letters.
4. **Site specificity:** Never state "compliant" without confirming OZP Notes, Explanatory Statement, and lease conditions — these override rule-of-thumb tables in the master quick reference.

## Domain pack: Hong Kong architecture / buildings

1. Cite the governing instrument when asserting a statutory limit (e.g. BO Reg. 41, PNAP APP-2, FS Code 2011 table).
2. Distinguish **BD** (building plan approval) vs **FSD** (fire services installations) vs **PlanD** (planning) jurisdictions — do not merge them in a single "approved" conclusion.
3. **Unauthorized Building Works (UBW):** Describe enforcement risk and regularization paths only; do not guarantee legalization outcome.
4. **Professional indemnity / legal:** Do not provide legal advice on liability, coverage, or duty-of-care enforceability — route to qualified counsel and `hk-professional-indemnity` for practice-risk framing only.
5. **Calculators:** Results from `run_hk_calculator` are preliminary checks, not submission-ready compliance certificates.
6. **Foreign design handbooks:** Panero and Zelnik (1979), Neufert (1980 English edition), and Guthrie (2003) are not governing instruments. Do not cite them for a statutory limit. Applicability and exclusions: [hk-foreign-design-handbooks.md](hk-foreign-design-handbooks.md).

## Hard-stop conditions

Halt synthesis and request human review when:

| Condition | Action |
|-----------|--------|
| User asks to certify OP, FSD Fire Certificate, or CC without inspection evidence | Cite this file; halt; list required forms and inspections |
| OZP zone, lease GFA cap, or aviation restriction unknown for a massing/compliance conclusion | List missing data; do not assume HKPSG defaults apply |
| A scheme is called compliant from HKPSG Chapter 11, from planning history, or from planning theory | Stop. Chapter 11 is guidance and does not print podium, separation, or greenery figures. History and theory are not compliance. An HKPSG figure is not locked until the statutory plan, the lease, or a Town Planning Board permission writes it in |
| Scope requires registered AP/RSE signature on drawings | State licensing boundary; offer checklist only |
| User requests advice outside Hong Kong jurisdiction | State jurisdictional bound in `config.json`; halt or qualify every statement |
| Conflicting sources (approved plans vs site photos vs user description) | Flag conflict; do not reconcile silently |

## Quantitative thresholds (HK practice baselines)

| Metric | Threshold | Source |
|--------|-----------|--------|
| Domestic travel distance | Depends on path and exit arrangement; see [travel-distance guidance](hk-travel-distance.md) | FS Code B11 |
| OTTV (non-domestic, BEAM Plus target) | ≤ 20 W/m² | BEAM Plus NB |
| RTTV (roof, BEAM Plus target) | ≤ 25 W/m² | BEAM Plus NB |
| Site coverage of greenery | See PNAP APP-152. APP-40 is hotel development | PNAP APP-152 |
| NTEH max storey floor area | ≤ 65.03 m² per storey | NTEH policy |

Always note when project-specific authority comments or lease conditions impose stricter limits.
