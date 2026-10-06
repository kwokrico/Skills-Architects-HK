"""Dump readable text for non-PNAP sources that still need a critical summary."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

ROOT = Path(r"c:\Users\Rico\PycharmProjects\Skills-Architects-HK")
REF = ROOT / "hk_s_reference"
OUT = ROOT / ".tmp_cs_src"
OUT.mkdir(exist_ok=True)

# Relative paths under hk_s_reference that will be summarized.
TARGETS = [
    r"Antiquities and Monuments Office (AMO)/Cap 53 Antiquities and Monuments Ordinance/source_reference/Cap 53 Antiquities and Monuments Ordinance (English).pdf",
    r"Building Department (BD)/Codes of Practice and Design Manuals/Structure/source_reference/EMSUOS2011e.pdf",
    r"Building Department (BD)/Codes of Practice and Design Manuals/Structure/source_reference/ExplanatoryNotesWindEffects2019e.pdf",
    r"Building Department (BD)/Guidelines/source_reference/Ad_Signs_E.pdf",
    r"Building Department (BD)/Guidelines/source_reference/BDG_ENG.pdf",
    r"Building Department (BD)/Guidelines/source_reference/BIMGBPS_e.pdf",
    r"Building Department (BD)/Guidelines/source_reference/BIMSPS_e.pdf",
    r"Building Department (BD)/Guidelines/source_reference/Drainage-System-Guideline-Eng.PDF",
    r"Building Department (BD)/Guidelines/source_reference/GDCBS.pdf",
    r"Building Department (BD)/Guidelines/source_reference/GWS.pdf",
    r"Building Department (BD)/Guidelines/source_reference/Guide_signboards_e.pdf",
    r"Building Department (BD)/Guidelines/source_reference/Guidelines_DCREERB2014e.pdf",
    r"Building Department (BD)/Guidelines/source_reference/Guidelines_DCREERB2014e_AppVI.pdf",
    r"Building Department (BD)/Guidelines/source_reference/IGG_e.pdf",
    r"Building Department (BD)/Guidelines/source_reference/IG_ISDWe.pdf",
    r"Building Department (BD)/Guidelines/source_reference/MWGGe.pdf",
    r"Building Department (BD)/Guidelines/source_reference/MWTGc.pdf",
    r"Building Department (BD)/Guidelines/source_reference/MWTGc_amendment_aug2026.pdf",
    r"Building Department (BD)/Guidelines/source_reference/MWTGc_amendment_oct2025.pdf",
    r"Building Department (BD)/Guidelines/source_reference/VSFUSGGe.pdf",
    r"Building Department (BD)/Guidelines/source_reference/appendix_b_bim_object_presentation_summary.pdf",
    r"Building Department (BD)/Guidelines/source_reference/dev0620cb1-2487-1-AnnexG_e.pdf",
    r"Building Department (BD)/Guidelines/source_reference/heritage_2021.pdf",
    r"Education Bureau (EDB)/Cap 279 Education Ordinance/source_reference/Cap 279 Education Ordinance (English).pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Cap 406 Electricity Ordinance/source_reference/Cap 406 Electricity Ordinance (English).pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Cap 406 Electricity Ordinance/source_reference/Cap 406E Electricity (Wiring) Regulations (English).pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Cap 51 Gas Safety Ordinance/source_reference/Cap 51 Gas Safety Ordinance (English).pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Cap 51 Gas Safety Ordinance/source_reference/Cap 51B Gas Safety (Gas Supply) Regulations (English).pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Cap 51 Gas Safety Ordinance/source_reference/Cap 51C Gas Safety (Installation and Use) Regulations (English).pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Cap 618 Lifts and Escalators Ordinance/source_reference/Works Code_Eng_2021 Edition.pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Codes/source_reference/COP_E_2025.pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Gas Codes/source_reference/COP M1_Issue 3_Eng.pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Gas Codes/source_reference/COP M2_Issue 2_Eng.pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Gas Codes/source_reference/CoP_gas_pipes_2nd_(Eng).pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Gas Codes/source_reference/CoP_gas_pipes_2nd_SI_(Eng).pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Gas Codes/source_reference/GU21 (English) rev.3.pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Gas Codes/source_reference/gu03.pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Gas Codes/source_reference/gu04_eng.pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Gas Codes/source_reference/gu06e.pdf",
    r"Electrical and Mechanical Services Department (EMSD)/Gas Codes/source_reference/gu12_eng.pdf",
    r"Environmental Protection Department (EPD)/Cap 311 Air Pollution Control Ordinance/source_reference/Cap 311A Air Pollution Control (Furnaces, Ovens and Chimneys) (Installation and Alteration) Regulations (English).pdf",
    r"Environmental Protection Department (EPD)/Technical Memoranda/source_reference/GN2014P039-2014c-e.pdf",
    r"Environmental Protection Department (EPD)/Technical Memoranda/source_reference/GN2014P040-2014c-e.pdf",
    r"Environmental Protection Department (EPD)/Technical Memoranda/source_reference/GN2014P041-2014c-e.pdf",
    r"Environmental Protection Department (EPD)/Technical Memoranda/source_reference/GN2014P240-1991c-e.pdf",
    r"Environmental Protection Department (EPD)/Technical Memoranda/source_reference/GN2016P002-2016ah-e.pdf",
    r"Environmental Protection Department (EPD)/Technical Memoranda/source_reference/tm_da_eng.pdf",
    r"Environmental Protection Department (EPD)/Technical Memoranda/source_reference/tm_gw_eng.pdf",
    r"Environmental Protection Department (EPD)/Technical Memoranda/source_reference/tm_ind_eng.pdf",
    r"Environmental Protection Department (EPD)/Technical Memoranda/source_reference/tm_pp_eng.pdf",
    r"Food and Environmental Hygiene Department (FEHD)/Cap 132 Public Health and Municipal Services Ordinance/source_reference/Cap 132 Public Health and Municipal Services Ordinance (English).pdf",
    r"Food and Environmental Hygiene Department (FEHD)/Cap 172 Places of Public Entertainment Ordinance/source_reference/Cap 172 Places of Public Entertainment Ordinance (English).pdf",
    r"HKARB/Cap 408 Architects Registration Ordinance/source_reference/ARB Code of Professional Conduct.pdf",
    r"HKIA/source_reference/code_of_professional_conduct.pdf",
    r"Home Affairs Department (HAD)/Cap 349 Hotel and Guesthouse Accommodation Ordinance/source_reference/Cap 349 Hotel and Guesthouse Accommodation Ordinance (English).pdf",
    r"Labour Department (LD)/Cap 509 Occupational Safety and Health Ordinance/source_reference/Cap 509 Occupational Safety and Health Ordinance (English).pdf",
    r"Labour Department (LD)/Cap 59 Factories and Industrial Undertakings Ordinance/source_reference/Cap 59 Factories and Industrial Undertakings Ordinance (English).pdf",
    r"Labour Department (LD)/Cap 59 Factories and Industrial Undertakings Ordinance/source_reference/Cap 59I Construction Sites (Safety) Regulations (English).pdf",
    r"Land Department (LandD)/LAO Practice Notes/source_reference/PN 3_2026 App I.pdf",
    r"Land Department (LandD)/LAO Practice Notes/source_reference/PN 3_2026 App II.pdf",
    r"Land Department (LandD)/LAO Practice Notes/source_reference/PN 3_2026 App III.pdf",
    r"Land Department (LandD)/LAO Practice Notes/source_reference/PN 3_2026 App IV.pdf",
    r"Land Department (LandD)/LAO Practice Notes/source_reference/PN 3_2026 App V.pdf",
    r"Land Department (LandD)/LAO Practice Notes/source_reference/PN 3_2026 App VI.pdf",
    r"Land Department (LandD)/LAO Practice Notes/source_reference/PN 3_2026.pdf",
    r"Land Department (LandD)/LAO Practice Notes/source_reference/PN 4_2026 App I.pdf",
    r"Land Department (LandD)/LAO Practice Notes/source_reference/PN 4_2026.pdf",
    r"Land Department (LandD)/LAO Practice Notes/source_reference/PN 9_2026.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/TPB_PG-No_34D_eng.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/TPB_PG_13G_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/TPB_PG_29C.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/TPB_PG_30C.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/TPB_PG_31B.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/TPB_PG_32B.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/TPB_PG_33B.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/TPB_PG_36C.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/TPB_PG_38.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/TPB_PG_39.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/TPB_PG_40.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/TPB_PG_41A_Final.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/TPB_PG_42.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/TPB_PG_43A.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg10_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg12c_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg14b_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg15a_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg16a_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg17a_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg18b_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg20a_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg22d_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg23a_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg24d_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg25d_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg26a_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg27_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg35e_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg5a_e.pdf",
    r"Planning Department (PlanD)/Town Planning Board Guidelines/source_reference/pg8_e.pdf",
    r"Social Welfare Department (SWD)/Cap 459 Residential Care Homes (Elderly Persons) Ordinance/source_reference/Cap 459 Residential Care Homes (Elderly Persons) Ordinance (English).pdf",
    r"Social Welfare Department (SWD)/Cap 613 Residential Care Homes (Persons with Disabilities) Ordinance/source_reference/Cap 613 Residential Care Homes (Persons with Disabilities) Ordinance (English).pdf",
]


def slug(rel: str) -> str:
    name = Path(rel).stem
    name = re.sub(r"[^\w.\- ()]+", "_", name)
    return name[:120]


def dump(rel: str) -> None:
    path = REF / rel
    doc = fitz.open(path)
    pages = []
    for page in doc:
        pages.append(page.get_text("text") or "")
    doc.close()
    full = "\n".join(pages)
    # Keep a readable digest: full text if short, else head + numbered/dimension lines.
    if len(full) <= 28000:
        body = full
    else:
        head = full[:12000]
        hits = []
        for line in full.splitlines():
            s = line.strip()
            if not s or len(s) > 220:
                continue
            if re.search(r"\d", s) and re.search(
                r"(m²|m2|mm|metre|meter|storey|section|Section|reg\.|clause|Clause|Table|APPENDIX|Part )",
                s,
                re.I,
            ):
                hits.append(s)
            elif re.match(r"^(\d+(\.\d+)*\s+|[A-Z][A-Z0-9 /-]{8,})", s):
                hits.append(s)
        # de-dupe preserving order
        seen = set()
        uniq = []
        for h in hits:
            if h in seen:
                continue
            seen.add(h)
            uniq.append(h)
            if len(uniq) >= 250:
                break
        body = head + "\n\n===== KEY LINES =====\n" + "\n".join(uniq)
    out = OUT / f"{slug(rel)}.txt"
    out.write_text(f"SOURCE: {rel}\nPAGES: {len(pages)}\nCHARS: {len(full)}\n\n{body}", encoding="utf-8")
    print(f"{out.name}\t{len(body)}")


for rel in TARGETS:
    dump(rel)
