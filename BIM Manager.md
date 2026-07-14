# Skill: BIM Manager (Building Information Modeling)

## Purpose
Enables advanced capabilities in digital project delivery, information management, and multi-disciplinary model coordination within architectural and construction workflows. This skill ensures strict compliance with global digital standards, optimal model health, and seamless interoperability between project stakeholders.

## Core Context & Domain Knowledge
* **Standards Frameworks:** ISO 19650 (Parts 1-5), local building authority electronic submission standards (e.g., HK BD/BD-ready BIM guidelines, building control submission parameters), and buildingSMART OpenBIM principles.
* **Information Management Hierarchy:** Organizational Information Requirements (OIR) → Project Information Requirements (PIR) → Exchange Information Requirements (EIR) → BIM Execution Plan (BEP).
* **Data Environments:** Common Data Environments (CDE) like Autodesk Construction Cloud (ACC), BIM 360, Procore, or ProjectWise. Managing access controls, Shared/Published/Archived states.
* **Interoperability Formats:** IFC (Industry Foundation Classes), BCF (BIM Collaboration Format), COBie (Construction Operations Building Information Exchange), and native parametric schemas (Revit `.rvt`, ArchiCAD `.pln`).

---

## Capabilities & Workflows

### 1. BIM Execution Plan (BEP) Authoring & Lifecycle
* **Objective:** Formulate and maintain the project's primary digital contract and playbook.
* **Process:**
    1. Define the project-specific **LOD / LOIN** (Level of Development / Level of Information Need) matrix from LOD 100 through LOD 500.
    2. Establish the **Model Origin Point, Shared Coordinates, and Rotation** to true north across all discipline models (Architectural, Structural, MEP).
    3. Specify the data exchange schedule, software versions (including specific build/hotfix versions), and file naming conventions.

### 2. Clash Detection & Coordination Coordination
* **Objective:** Mitigate site errors by identifying spatial and logical conflicts in the virtual environment.
* **Process:**
    1. Aggregate federated models within coordination engines (e.g., Navisworks, Solibri).
    2. Define targeted clash rule matrices (e.g., *Hard Clash:* Structural Columns vs. MEP Ducts; *Clearance Clash:* Access space around mechanical equipment).
    3. Group raw clash data into actionable items, generate BCF reports, and assign responsibility to specific engineering disciplines.

### 3. Model Health Auditing & Optimization
* **Objective:** Maintain file stability, prevent data corruption, and ensure high performance for production teams.
* **Process:**
    1. Monitor file size thresholds, unplaced rooms/spaces, redundant geometry, and excessive warnings.
    2. Audit family/component libraries to ensure low polygon counts, clean nested parameters, and absence of CAD imports within parametric objects.
    3. Automate periodic maintenance tasks (e.g., purging unused elements, compacting files, auditing central models).

### 4. Regulatory & Submission Validation
* **Objective:** Ensure models comply with local statutory submission pipelines (e.g., automated area calculations, fire safety path computations).
* **Process:**
    1. Validate that model geometry maps precisely to mandatory property sets (Psets) required by local authorities.
    2. Run computational checks for building code parameters (e.g., path of travel lines, room clearance heights, barrier-free access zones).

---

## Execution Strategies (System Prompts / Agent Directives)

When executing tasks under this skill, always apply the following logic:

* **Prioritize Open Standards:** Lean heavily toward OpenBIM and IFC solutions unless specific proprietary vendor environments are explicitly requested.
* **Enforce Data Over Geometry:** Remember that BIM is *Information* modeling. Prioritize correct data structuring, parameter naming, and classification schemas (OmniClass, UniClass) over pure 3D visualization.
* **Proactive Conflict Resolution:** When reviewing project briefs, immediately flag missing coordinate frameworks, ambiguous LOD definitions, or gaps in the Exchange Information Requirements (EIR).
* **Scripted Automation Mindset:** Look for workflows that can be optimized via data automation (e.g., utilizing Python, Dynamo, or Grasshopper for batch parameter editing, schema conversions, or sheet generation).

---

## Technical Tooling Profile
* **Authoring:** Autodesk Revit, Graphisoft ArchiCAD, Rhino/McNeel (Rhino-to-BIM pipelines).
* **Coordination/Review:** Autodesk Navisworks Manage, Solibri Model Checker, Autodesk Docs / CDE Solutions.
* **Computational BIM:** Dynamo, Grasshopper, Python (via `revitpythonshell` or PyRevit).
* **Data Validation:** IFC OpenShell, pandas (for COBie and asset management data extraction).
===================================================================================================================================================

===================================================================================================================================================

Sub-Skill 1: HK Statutory Compliance & Standards Alignment
Domain Context: Navigating the transition from traditional General Building Plan (GBP) submissions to BIM-assisted and BIM-based statutory submissions in HK.

Key References:

BD PNAP APP-117: BIM for Building Control (Statutory submissions to Buildings Department).

CIC BIM Standards: General (Version 2/2.1), Architecture, Structural, and MEP streams.

DevB Technical Circulars: Mandates for BIM adoption on public works contracts (exceeding HKD 30M).

Core Workflows:

BIM-assisted GBP Generation: Setting up model views, parameters, and filters to generate standard statutory drawings (e.g., site plans, floor plans, elevations, sections) that strictly comply with BD drafting regulations.

Statutory Area Calculations: Automating and validating Gross Floor Area (GFA) calculations, Usable Floor Area (UFA), and Fire Safety/MOE (Means of Escape) calculations within the model according to the Building (Planning) Regulations.

Data Validation for BD-Ready Models: Ensuring mandatory software property sets (Psets) and object naming parameters are intact before submitting to the Electronic Submission System (ESS).

Sub-Skill 2: Information Management & ISO 19650 (HK Local Annex)
Domain Context: Managing the lifecycle of project data from inception to handover under international frameworks adapted for local Hong Kong practices.

Key References: ISO 19650 Parts 1 & 2, CIC Production of BIM Objects Guide, and the CIC Guidelines for Local Annex requirements.

Core Workflows:

EIR to BEP Translation: Analyzing the client's Exchange Information Requirements (EIR) and authoring both pre-contract and post-contract BIM Execution Plans (BEP).

Common Data Environment (CDE) Administration: Managing standard CDE platforms (Autodesk Construction Cloud/BIM 360, ProjectWise) using the mandatory folder architectures and container naming conventions specified by DevB and ISO 19650 (WIP → Shared → Published → Archived status gates).

Information Delivery Planning: Structuring and tracking the Task Information Delivery Plan (TIDP) and Master Information Delivery Plan (MIDP) across all sub-consultants.

Sub-Skill 3: Federated Coordination & Spatial Interoperability
Domain Context: Handling multi-disciplinary technical coordination across fragmented consultant teams in high-density, complex HK projects.

Key References: Hong Kong 1980 Grid System, Hong Kong Principal Datum (HKPD), buildingSMART OpenBIM standards.

Core Workflows:

Geo-referencing & Shared Coordinates: Establishing the exact spatial orientation of models based on the HK1980 Grid and HKPD, ensuring flawless multi-model alignment across Architecture, Structural (RSE), and MEP fields.

Clash Matrix Formulation: Defining and deploying localized clash rules (e.g., structural elements vs. complex drop-ceiling MEP layouts typical in tight HK spatial designs).

BCF-driven Issue Tracking: Utilizing BIM Collaboration Format (BCF) workflows via platforms like Revizto or BIMtrack to bypass heavy file sharing and directly assign coordination issues to specific engineers.

Sub-Skill 4: Computational BIM & Data Automation
Domain Context: Developing custom computational logic to bridge gaps between design authoring tools and stringent documentation requirements.

Key References: Revit API, open-source IFC frameworks (IFCOpenShell).

Core Workflows:

Model Quality Automation: Writing scripts (Python, Dynamo, Grasshopper) to batch-check element classification codes (e.g., Uniclass 2015 or OmniClass) and file naming compliance.

Geometric Validation Queries: Designing automated scripts to calculate spatial compliance, such as validating barrier-free access travel distances or fire compartment boundary lines.


===================================================================================================================================================

===================================================================================================================================================

Complementary Skill Sets Required for a BIM Manager
A successful BIM Manager cannot survive on technical modeling skills alone. They sit at the intersection of technology, law, project finance, and organizational psychology.

┌────────────────────────────────────────────────────────┐
│                   THE BIM MANAGER                      │
└───────────────────────────┬────────────────────────────┘
                            │
       ┌────────────────────┼────────────────────┐
       ▼                    ▼                    ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Contract &  │     │    Change    │     │Asset & Twin  │
│ Legal Strategy     │  Management  │     │ Integration  │
└──────────────┘     └──────────────┘     └──────────────┘
1. Contractual & Legal Strategy (NEC4 / Hong Kong Context)
BIM changes risk allocation. A BIM Manager must understand how digital models affect standard construction contracts used in Hong Kong.

NEC4 Option X10: Understanding how the NEC4 secondary option for BIM operates on public projects, specifically regarding the "Information Model," "Project Information," and intellectual property rights.

BIM Advisory/Special Conditions of Contract: Navigating who owns the risk of data discrepancies between the BIM model and the physical contract drawings (i.e., which document takes precedence in a legal dispute).

Liability of Shared Data: Managing the legal boundaries of sharing "live" coordination models with main contractors and sub-contractors.

2. Change Management & Organizational Leadership
Implementing BIM is fundamentally about transforming people and corporate culture, not just buying software.

Overcoming Traditional Friction: Designing internal upskilling frameworks to transition senior staff (who may be anchored to traditional 2D CAD workflows) into digital review processes.

Process Redesign: Restructuring office workflows so that coordination happens early in the schematic/detailed design phases, rather than treating BIM as a post-design drafting exercise.

Strategic KPI Alignment: Helping corporate leadership measure the ROI of BIM implementation (e.g., tracking the reduction of on-site RFI/clash modification costs).

3. Asset Management & Digital Twin Integration (FM Handover)
The final frontier of BIM is ensuring the data remains useful long after the construction keys are handed over.

COBie Standard Implementation: Managing the structured collection of non-geometric asset data (warranties, model numbers, maintenance schedules) during design and construction.

GIS-BIM Interoperability: Integrating building models with geographical mapping frameworks (e.g., connecting to the Lands Department’s 3D spatial data infrastructure initiatives in Hong Kong).

Facility Management (FM) Handover: Mapping data schemas from design models into operations platforms (BIM-to-FM) to feed predictive maintenance engines and digital twins.

===================================================================================================================================================

===================================================================================================================================================

# Sub-Skill: Hong Kong Statutory Compliance & BIM Plan Submissions

## Purpose
Enables automated validation, area extraction, and drawing production for statutory submissions to the Hong Kong Buildings Department (BD), Lands Department (LandsD), and Planning Department (PlanD). This sub-skill specifically optimizes the model environment to execute automated Gross Floor Area (GFA) calculations, Fire Safety code compliance checks, and structural/A&A logic boundaries.

## Core Regulatory References
*   **PNAP ADV-34 (BIM for Building Control):** Governs the operational use of BIM for statutory processing, template setting, and the deployment of official BD Automated Checking Tools.
*   **PNAP ADM-19 (General Building Plans):** Defines the centralized plan processing system, 3D spatial data extraction pathways for LandsD/PlanD, and the "plans shall prevail" legal paradigm in case of model-to-drawing discrepancies.
*   **PNAP APP-117 (Structural Requirements for A&A Works):** Governs structural viability assessments for alterations, wind exposure area verifications, and structural adequacy checks on existing building fabrics.
*   **HK DevB BIM Roadmap (Private Sector Mandate):** Adherence to the phased multi-stage mandatory timeline for private sector BIM plan submissions.

---

## Capabilities & Automated Workflows

### 1. BIM-Assisted General Building Plan (GBP) Generation
*   **Objective:** Extract standard 2D statutory drawings (Site Plans, Floor Plans, Elevations, Sections) directly from parametric geometry while maintaining regulatory drafting logic.
*   **Process:**
    1. Initialize the project utilizing standard BD/CIC drawing templates, establishing the mandatory **Hong Kong 1980 Grid System** and **Hong Kong Principal Datum (HKPD)**.
    2. Enforce standard color schemas according to **PNAP ADM-9** (e.g., Pink for new concrete, Blue for demolition/A&A actions under APP-117 context, Yellow for timber).
    3. Configure strict View Templates to hide operational design elements and expose only statutory metadata (e.g., fire barriers, site boundaries, setback clearances).

### 2. Automated GFA & Area Calculation (BD/LandsD Joint Methodology)
*   **Objective:** Deploy the native **BD/LandsD BIM Area Tool** plug-in to compute floor areas under a unified data format, removing traditional discrepancies between Building Ordinance requirements and Lease conditions.
*   **Process:**
    1. Execute the **BD/LandsD Initialisation Routine** to inject localized parameters into the project (parameters prefixed with `BD-GBP-` and `LND-GBP-`).
    2. Map out boundary lines on designated "Area Plans" with absolute zero-gap tolerance. Lines must follow the outer face of external walls or the center line of party walls.
    3. Apply the **Auto-Coloring Tool** view schemes (`LND-GBP-GFA-Base`) to visually isolate and verify area zones before triggering the calculation engine.
    4. Generate the standardized **GFA Calculation Excel Report** directly from the tool for immediate appendix binding.

### 3. GFA Concession Tracking & Validation
*   **Objective:** Parametrically classify and calculate structural/architectural items eligible for GFA exemptions or concessions.
*   **Process:**
    1. Tag specific spatial containers with exact regulatory concession markers matching the 38 designated BD concession categories.
    2. **Mandatory Concession Mapping:**
        *   *Item 1:* Car Parks / Loading & Unloading bays (validation of layout & headrooms).
        *   *Item 2.1:* Telecommunication and Broadcasting Equipment (TBE) & Refuse Storage and Material Recovery Chambers (RSMRC).
        *   *Item 2.3:* Air Handling Unit (AHU) plant rooms.
        *   *Item 5 & 28:* Balconies, Utility Platforms, and AC Platforms (validation of prescribed physical dimensions).
        *   *Item 38:* Modular Integrated Construction (MiC) floor area bonus allocations.

### 4. Advanced Statutory Vetting (Fire Safety & Sanitary Provisions)
*   **Objective:** Run internal pre-submission checks against the Hong Kong Building (Planning) Regulations and Codes of Practice via the **BIM Fire Safety (FS) Tool** and **Sanitary Fitments (SF) Tool**.
*   **Process:**
    1. **Fire Compartmentation:** Define room occupancy factors, calculate discharge values, and verify travel distances (Direct Distance vs. Actual Travel Distance) directly from spatial boundaries.
    2. **Means of Access (MOA):** Validate the orientation and minimum spatial clearances for Fireman's Lifts and Firefighting & Rescue Stairways (FRS).
    3. **Sanitary Provisions:** Map out the demographic/use occupancy matrix of the building to automate the minimum required count of water closets, urinals, and lavatories.

---

## Technical Parameter Matrix (Data Schema)

To allow automation tools to scan the model successfully, ensure all spatial components contain the following localized parameters:

| Parameter Name | Data Type | Permissible Values / Function |
| :--- | :--- | :--- |
| `BD-GBP-RoomUse` | Text / Dropdown | Matches standard statutory definitions (e.g., Habitable Room, Office, AHU Plant Room, Carpark). |
| `BD-GBP-GFA-Accountability` | Integer / Enum | `0` = Accountable, `1` = Non-Accountable, `2` = Exempted. |
| `BD-GBP-Concession-Item` | Text | Formatted as `Item [X]` matching the BD concession list. |
| `LND-Lease-Req-[Type]` | Length / Area | Global project parameters mapping the baseline restrictions set out in the land lease. |
| `APP117-Structural-Status` | Text / Phase | Used in A&A: `Existing to Remain`, `New Structural Work`, `To Be Demolished`. |

---

## Agent Directives & Execution Logic

When analyzing documents or processing model data under this sub-skill, always execute the following logic:

*   **The "Plans Shall Prevail" Rule:** If reviewing model geometry versus exported PDF/paper drawings for a BD submission package, prioritize visual accuracy and text output on the 2D sheets, as BD processes approvals based on the 2D presentation format (PNAP ADM-19).
*   **Zero-Overlaps Policy:** Ensure that Area Boundary Lines do not overlap or leave unmapped slivers. Any geometric overlap will cause the BD Area Tool to fail or generate skewed GFA reports.
*   **A&A Boundary Isolation:** When processing projects involving **PNAP APP-117**, immediately verify that the existing structural framing properties are locked down and that wind exposure surface area calculation variances are flagged if they increase by greater than or equal to 10%.



===================================================================================================================================================

===================================================================================================================================================

Here is the complete, comprehensive **`SUB_SKILL_ISO19650_INFORMATION_MANAGEMENT.md`** file tailored for your digital repository. It explicitly details the structural workflows, metadata lifecycles, and exact container naming conventions dictated by the **Hong Kong Construction Industry Council (CIC) BIM Standards - General** and the **Development Bureau (DevB) Harmonisation Guidelines**.

---

### `SUB_SKILL_ISO19650_INFORMATION_MANAGEMENT.md`

```markdown
# Sub-Skill: ISO 19650 Information Management & CDE Governance (Hong Kong Local Annex)

## Purpose
Enables comprehensive administration of the Common Data Environment (CDE), information lifecycle orchestration, and strict information container identification tracking. This sub-skill enforces compliance with ISO 19650-1 & 2 frameworks while seamlessly incorporating the localized naming and classification adaptations required by the Hong Kong Construction Industry Council (CIC) and the Development Bureau (DevB).

## Core Standards Framework
* **ISO 19650-1 & 2:** International standards for information management using building information modeling.
* **CIC BIM Standards - General (Latest Edition):** Integrates the official Hong Kong "Local Annex" of ISO 19650-2:2018, clarifying regional terminology, legal realities, and process workflows.
* **DevB BIM Harmonisation Guidelines for Works Departments:** Mandates model federation strategies, maximum filename lengths, and data exchange boundaries across public works and civil departments.

---

## 1. CDE Architecture & Metadata Gateways

The CDE configuration relies on four distinct information states separated by controlled, audited approval gates. In cloud-based CDE architectures (e.g., Autodesk Construction Cloud, ProjectWise), access permissions and metadata attributes govern these states rather than fractured folder directories.


```

[ Work In Progress (WIP) ]
│
▼  (Gate 1: Check / Review / Approve)
[ Shared State ] <───> (Multi-Disciplinary Coordination)
│
▼  (Gate 2: Review / Authorize / Validate)
[ Published State ]
│
▼  (Gate 3: Accept / Sign-off)
[ Archived State ] (Legal Audit Trail)

```

### State Workflows & Access Controls:
1.  **Work In Progress (WIP):** * *Access:* Restricted strictly to the creating Task Team (e.g., Architectural design team only).
    * *Function:* Unshared development work. Models undergo internal QA checks prior to progression.
2.  **Shared State:** * *Access:* Read-only for all project consultants; edit permissions restricted to the originating author.
    * *Function:* The unified center for multi-disciplinary coordination, clash detection, and design development interface reviews.
3.  **Published State:** * *Access:* Read-only for the entire delivery team; authorized access for clients and contractors.
    * *Function:* Holds approved information containers used for statutory submissions (BD/LandsD), tendering, procurement, and construction.
4.  **Archived State:** * *Access:* Read-only historical record.
    * *Function:* Full audit trail of all transaction histories, transaction logs, and previous revisions.

---

## 2. Information Container Naming Convention (HK Local Annex)

To facilitate error-free electronic processing across the HK Buildings Department and local works departments, every information container (model file, drawing sheet, document) must conform to a strict, delimited naming convention.

### The HK Naming Standard Schema
The filename consists of exactly seven core fields separated by a hyphen delimiter (`-`). 
* **Max Character Limit:** 43 characters total (excluding the file extension).
* **Case Sensitivity:** Absolute Uppercase only. No spaces allowed.


```

[Project]-[Originator]-[Volume/System]-[Level/Location]-[Type]-[Discipline]-[Number]

```

### Detailed Field Breakdowns:

| Field | Description | Character Rule | Examples |
| :--- | :--- | :--- | :--- |
| **Project** | Unique project identifier code assigned by the client. | 3 to 5 Alphanumeric | `12345`, `HKX01` |
| **Originator** | Abbreviation representing the organization creating the file. | 3 to 4 Alphanumeric | `ARCH` (Architect), `RSE1` (Structural Engineer) |
| **Volume / System** | Physical block, sector, zone, or distinct system of the asset. | 2 Alphanumeric | `T1` (Tower 1), `B1` (Podium B), `ZZ` (All Volumes) |
| **Level / Location** | Precise floor level or vertical height identifier. | 2 Alphanumeric | `GF` (Ground), `01` (1st Floor), `RF` (Roof), `ZZ` (Multi-level) |
| **Type** | The functional delivery format of the information container. | 2 Characters | `M3` (3D Model File), `DR` (2D Drawing), `RP` (Report) |
| **Discipline** | The localized domain stream (modified from UK Annex "Role"). | 1 Character | `A` (Arch), `S` (Struct), `M` (Mech), `B` (Building Services) |
| **Number** | A sequential code ensuring file name uniqueness. | 4 Digits | `0001` through `9999` |

*Filename Example:* **`HKX01-ARCH-T1-01-M3-A-0002.rvt`**
*(Interpreted as: Project HKX01, authored by ARCH, targeting Tower 1, 1st Floor, 3D Model file, Architectural discipline, sequence number 0002)*

---

## 3. Metadata Attributes: Status & Revision Codes

Status and Revision values **must never** be written directly into the filename string. They must be mapped as separate CDE system metadata fields attached to the container to prevent broken link paths during file updates.

### Suitability/Status Codes (ISO 19650 / CIC Aligned)
Status codes declare what the information container can legally be used for at its current lifecycle point.

* **WIP State:**
    * `S0` = Work in Progress (Internal use only)
* **Shared State (Coordination Phase):**
    * `S1` = Suitable for Coordination (Cross-discipline referencing)
    * `S2` = Suitable for Information (Review only, not for design modifications)
    * `S3` = Suitable for Internal Review & Comment
    * `S4` = Suitable for Stage Approval
* **Published State (Contractual/Execution Phase):**
    * `A1` = Suitable for Buildings Department (BD) Statutory Submission
    * `A2` = Suitable for Tender Procurement
    * `A3` = Suitable for Construction Execution
    * `A4` = Suitable for Stage Completion / As-Built Record

### Revision Coding System
Revisions follow a dual-digit classification loop to clearly isolate preliminary drafting modifications from formal contractual issues.

* **Preliminary Revisions (WIP & Shared States):** Prefixed with a **`P`** followed by a two-digit integer, tracking minor iterations as decimals.
    * *Example:* `P01.01` (First draft, first internal update) $\rightarrow$ `P01.02` $\rightarrow$ `P01` (Shared with coordination team).
* **Contractual Revisions (Published State):** Prefixed with a **`C`** followed by a two-digit integer once authorized.
    * *Example:* `C01` (First formal construction issue), `C02` (Revised construction issue).

---

## 4. Agent Directives & Validation Logic

When evaluating CDE directories or checking uploaded document packages under this skill, apply the following strict execution directives:

1.  **Enforce Naming Compliance Before Ingestion:** Reject any information container that deviates from the 7-field structure or exceeds 43 characters. Immediately flag lower-case text or illegal delimiters (e.g., underscores `_`).
2.  **Cross-Verify Status vs. Location:** Flag an error if a file located within a "Published" CDE directory carries an `S1` or `S2` coordination status code. Published directories must only host containers stamped with authorized `A` or `C` codes.
3.  **Ensure Spatial Cohesion via Volume/Level Fields:** Cross-reference the model's inner bounding geometry with its filename parameters. If a model file is named with `Level 01` (`01`), but contains structural slabs assigned to `Level 05`, mark the container as non-compliant due to physical/data mismatch.

```

===================================================================================================================================================

===================================================================================================================================================

import numpy as np
import pandas as pd


def load_and_clean_bim_data(file_path):
    """Loads the exported BIM schedule and cleans up trailing whitespace

    and case mismatches common in multi-disciplinary model merges.
    """
    # Supports both Excel reports or CSV raw dumps
    if file_path.endswith(".xlsx") or file_path.endswith(".xls"):
        df = pd.read_excel(file_path)
    else:
        df = pd.read_csv(file_path)

    # Clean parameter string inputs to ensure deterministic matching
    string_cols = df.select_dtypes(include=["object"]).columns
    for col in string_cols:
        df[col] = df[col].astype(str).str.strip().str.upper()

    return df


def audit_hk_statutory_areas(df):
    """Executes compliance audits matching BD (PNAP ADV-34/ADM-19) constraints

    against LandsD Lease parameters.
    """
    mismatches = []

    # -------------------------------------------------------------------------
    # RULE 1: Detect Missing Critical Parameter Data (Zero-Tolerance Boundaries)
    # -------------------------------------------------------------------------
    critical_params = [
        "COMPARTMENT_ID",
        "BD-GBP-ROOMUSE",
        "BD-GBP-GFA-ACCOUNTABILITY",
        "LND-GBP-GFA-ACCOUNTABILITY",
        "CALCULATED_AREA_M2",
    ]

    missing_data_mask = df[critical_params].isna().any(axis=1) | (
        df[critical_params] == "NAN"
    )
    df_missing = df[missing_data_mask]

    # -------------------------------------------------------------------------
    # RULE 2: GFA Accountability Conflicts (BD Concession vs LandsD Lease)
    # -------------------------------------------------------------------------
    # Example: A green feature or plant room might be exempted/non-accountable
    # by BD under PNAP APP-2 profit rules, but strictly accountable under Lease.
    # Unintended identical tags or completely conflicting tags must be verified.
    gfa_mismatch_mask = (
        df["BD-GBP-GFA-ACCOUNTABILITY"] != df["LND-GBP-GFA-ACCOUNTABILITY"]
    )

    # Define common logical edge cases where they ARE allowed to differ.
    # Adjust this exclusion list according to your project's specific Land Lease terms.
    allowed_variance_uses = ["CARPARK", "PLANT ROOM", "AHU"]
    is_not_exempt_exception = ~df["BD-GBP-ROOMUSE"].str.contains(
        "|".join(allowed_variance_uses), na=False
    )

    df_gfa_conflicts = df[gfa_mismatch_mask & is_not_exempt_exception]

    # -------------------------------------------------------------------------
    # RULE 3: Room Use / Typology Classification Mismatches
    # -------------------------------------------------------------------------
    # Ensures that text values don't cause processing loops in automated checking tools.
    use_mismatch_mask = (
        (df["BD-GBP-ROOMUSE"] == "HABITABLE ROOM")
        & (df["LND-LEASE-USE"] == "INDUSTRIAL")
    ) | (
        (df["BD-GBP-ROOMUSE"] == "PLANT ROOM")
        & (df["LND-LEASE-USE"].isin(["DOMESTIC", "RETAIL"]))
    )
    df_use_conflicts = df[use_mismatch_mask]

    return df_missing, df_gfa_conflicts, df_use_conflicts


def generate_validation_summary(df_missing, df_gfa_conflicts, df_use_conflicts):
    """Compiles the analytical flags into an actionable project management console log."""
    print("=" * 80)
    print("          HONG KONG STATUTORY BIM AREA COMPLIANCE REPORT (2026)          ")
    print("=" * 80)

    print(f"\n[FLAG 1] Missing Critical Parameters: {len(df_missing)} items found")
    if not df_missing.empty:
        print(
            df_missing[
                [
                    "COMPARTMENT_ID",
                    "BD-GBP-ROOMUSE",
                    "BD-GBP-GFA-ACCOUNTABILITY",
                ]
            ].to_string()
        )

    print(
        f"\n[FLAG 2] Potential BD vs LandsD GFA Policy Mismatches: {len(df_gfa_conflicts)} items found"
    )
    print("👉 (Review required to confirm Lease conditions match PNAP allowances)")
    if not df_gfa_conflicts.empty:
        print(
            df_gfa_conflicts[
                [
                    "COMPARTMENT_ID",
                    "BD-GBP-ROOMUSE",
                    "BD-GBP-GFA-ACCOUNTABILITY",
                    "LND-GBP-GFA-ACCOUNTABILITY",
                ]
            ].to_string()
        )

    print(
        f"\n[FLAG 3] High-Risk Room Use Classification Conflicts: {len(df_use_conflicts)} items found"
    )
    if not df_use_conflicts.empty:
        print(
            df_use_conflicts[
                ["COMPARTMENT_ID", "BD-GBP-ROOMUSE", "LND-LEASE-USE"]
            ].to_string()
        )

    print("\n" + "=" * 80)


# -------------------------------------------------------------------------
# Execution / Mock Data Demonstration
# -------------------------------------------------------------------------
if __name__ == "__main__":
    # Simulating a typical dirty schedule export from a federated model
    mock_data = {
        "COMPARTMENT_ID": ["RM-101", "RM-102", "RM-103", "RM-104"],
        "BD-GBP-ROOMUSE": [
            "Habitable Room ",
            "AHU Plant Room",
            "Plant Room",
            None,
        ],
        "LND-LEASE-USE": ["Industrial", "Plant Room", "Domestic", "Retail"],
        "BD-GBP-GFA-ACCOUNTABILITY": [
            "Accountable",
            "Exempted",
            "Exempted",
            "Accountable",
        ],
        "LND-GBP-GFA-ACCOUNTABILITY": [
            "Accountable",
            "Exempted",
            "Accountable",
            "Accountable",
        ],
        "CALCULATED_AREA_M2": [45.2, 12.5, 34.0, 18.2],
    }

    # Convert to DataFrame
    raw_bim_df = pd.DataFrame(mock_data)

    # Temporarily save to simulate a local system file path loading routine
    raw_bim_df.to_csv("BIM_Area_Export.csv", index=False)

    # Process and analyze data
    cleaned_df = load_and_clean_bim_data("BIM_Area_Export.csv")
    missing, gfa_err, use_err = audit_hk_statutory_areas(cleaned_df)

    # Output visual diagnostic results
    generate_validation_summary(missing, gfa_err, use_err)

===================================================================================================================================================

===================================================================================================================================================


https://gemini.google.com/app/b07972d498d4efd4

===================================================================================================================================================

===================================================================================================================================================

This comprehensive **pyRevit script blueprint** acts as an automated audit tool for a BIM Manager's toolbox. It hooks directly into the Autodesk Revit API to evaluate the active model's data health and filename syntax against the **Hong Kong CIC BIM Standards - General** parameters.

Deploying this inside an office extension tab allows production teams to self-audit before syncing or triggering a Common Data Environment (CDE) submission.

---

## 1. pyRevit Automation Script (`script.py`)

This script executes three automated audits: checks the active file name against the HK CIC 7-field regex, counts active model warnings, and flags performance-killing DWG/CAD imports.

```python
# -*- coding: utf-8 -*-
"""HK CIC Standard & Model Health Auditor.

Authorized for enterprise-level deployment within local design pipelines.
"""

import re
from Autodesk.Revit.DB import (
    BuiltInCategory,
    FilteredElementCollector,
    ImportInstance,
)
from pyrevit import forms, script

# Initialize pyRevit output console formatting
output = script.get_output()
output.set_title("HK CIC Compliance & Model Health Audit")
output.print_header()

# Establish link to active Revit Document
uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

# -------------------------------------------------------------------------
# AUDIT 1: HK CIC 7-Field Filename Syntax Verification
# -------------------------------------------------------------------------
# Regex breaks down: Proj(3-5) - Orig(3-4) - Vol(2) - Lvl(2) - Type(2) - Disc(1) - Num(4)
HK_CIC_REGEX = (
    r"^[A-Z0-9]{3,5}-[A-Z0-9]{3,4}-[A-Z0-9]{2}-[A-Z0-9]{2}-"
    r"[A-Z0-9]{2}-[A-Z0-9]{1}-[0-9]{4}$"
)


def verify_file_naming(doc_name):
    # Strip out the ".rvt" extension if present
    clean_name = doc_name.replace(".rvt", "").split("_detached")[0]

    output.print_subtitle("1. Filename Classification Audit")
    if re.match(HK_CIC_REGEX, clean_name):
        output.print_md(
            "**[PASS]** Filename matches HK CIC Local Annex standard pattern."
        )
        print("Active Filename: {}".format(doc_name))
    else:
        output.print_md(
            "🔴 **[FAIL] Filename violates HK CIC standard structure!**"
        )
        print("Active Filename: {}".format(doc_name))
        print("Expected Syntax: [Proj]-[Orig]-[Vol/Sys]-[Lvl]-[Type]-[Disc]-[Num]")
        print("Ensure zero spaces, uppercase letters, and correct delimiters.")


# -------------------------------------------------------------------------
# AUDIT 2: Revit Warnings Assessment
# -------------------------------------------------------------------------
def check_model_warnings(document):
    warnings = document.GetWarnings()
    warning_count = len(warnings)

    output.print_subtitle("2. Central File Memory & Warning Thresholds")

    # Define warning threshold boundaries based on project scale
    if warning_count < 200:
        output.print_md(
            "**[PASS]** Warning density is stable. Total Warnings: `{}`".format(
                warning_count
            )
        )
    elif 200 <= warning_count < 500:
        output.print_md(
            "⚠️ **[WARNING]** Model performance optimization required. Total Warnings: `{}`".format(
                warning_count
            )
        )
    else:
        output.print_md(
            "🔴 **[CRITICAL CRASH RISK]** Exceeds maximum allowance. Total Warnings: `{}`".format(
                warning_count
            )
        )


# -------------------------------------------------------------------------
# AUDIT 3: High-Risk CAD / DWG Import Tracking
# -------------------------------------------------------------------------
def check_imported_cad_files(document):
    output.print_subtitle("3. Exploded or Imported CAD Vectors")

    # Collect all CAD Import Instances inside the database
    cad_collector = (
        FilteredElementCollector(document)
        .OfClass(ImportInstance)
        .ToElements()
    )

    imported_dwgs = []
    for element in cad_collector:
        # Filter out linked files, leaving only performance-degrading imports
        if not element.IsLinked:
            # Safely fetch the type name or geometry link name
            param = element.Category.Name if element.Category else "Unknown CAD"
            imported_dwgs.append(param)

    if not imported_dwgs:
        output.print_md(
            "**[PASS]** Zero imported CAD files found. (All external DWGs correctly linked)."
        )
    else:
        output.print_md(
            "🔴 **[FAIL] Exploded/Imported DWG instances detected.** Elements must be purged:"
        )
        for dwg in imported_dwgs:
            print("- Object Name/Category Reference: {}".format(dwg))


# -------------------------------------------------------------------------
# Execution Routines
# -------------------------------------------------------------------------
if __name__ == "__main__":
    verify_file_naming(doc.Title)
    print("-" * 70)
    check_model_warnings(doc)
    print("-" * 70)
    check_imported_cad_files(doc)

```

---

## 2. Dynamo Alternative: Visual Logic Node Graph Outline

If deploying within a visual programming framework rather than pyRevit, structure your **Dynamo Canvas** routing sequentially using the following layout logic:

```
[Document.Current] ──► [Document.Title] ──► [String.ToUpperCase] ──► [String.RegexMatch]
                                                                            │
   ┌────────────────────────────────────────────────────────────────────────┘
   ▼
[List.FilterByBoolMask] ──► True  ──► "Filename Compliant" Message Box
                        ──► False ──► "Naming Violation" Warning Alert

```

### Node Sequence Configuration:

1. **Filename Extraction:** * `Document.Current` $\rightarrow$ `Document.Title` $\rightarrow$ `String.Replace` (strip out `.rvt` text elements).
2. **Regex Enforcement:** * Insert a `String` node containing the regular expression rule: `^([A-Z0-9]{3,5})-([A-Z0-9]{3,4})-([A-Z0-9]{2})-([A-Z0-9]{2})-([A-Z0-9]{2})-([A-Z0-9]{1})-([0-9]{4})$`
* Pipe both string inputs directly into a `String.RegexMatch` node.


3. **Warnings Extraction:** * Deploy the native `Document.Warnings` node $\rightarrow$ connect to a `List.Count` node to tally warnings. Connect a `Formula` block or conditional operator (`x > 400`) to flag severe conditions.
4. **CAD Audit Pipeline:**
* `Categories` (set to `OST_ImportBlocks` or use an `Element Types` node targeting `ImportInstance`) $\rightarrow$ `All Elements of Type`.
* Filter the elements by querying their parameters to isolate linked vs. embedded status.



---

## 3. Deployment Parameters

To execute these checks smoothly across production teams, maintain these environment variables:

| Audit Type | Threshold / Success Rule | System Failure Penalty |
| --- | --- | --- |
| **Naming String Match** | Exact match with HK CIC regex blueprint | File blocked from advancing from WIP to Shared CDE state. |
| **Model Warnings Count** | $<200$ warnings = Pass; $>500$ warnings = Fail | Model audit report auto-escalated to BIM Manager for manual purge. |
| **CAD Ingestion Logic** | `IsLinked == False` count must equal `0` | Automated script runs background delete or isolation sweep. |



===================================================================================================================================================

===================================================================================================================================================





===================================================================================================================================================

===================================================================================================================================================

