# Guidelines for using Building Information Modelling in Statutory Plan Submissions 2023
**Architect critical summary for schematic design**
2023. The PDF document title is Guidelines for using Building Information Modelling in Statutory Plan Submissions (other than General Building Plan) 2023 | Buildings Department

> Scope note: Native models for eight types of prescribed plans other than general building plans. The 2019 general building plans guideline remains the route for general building plans. If the model and the prescribed plans differ, the plans prevail. Appendix B, issued as a separate PDF, lists the building information objects used to present those plans. The guidelines are not intended to change the statutory submission requirements.

## Regulatory Overview
Prescribed plans, however they are produced, must still meet the Buildings Ordinance, the codes, the practice notes, and the circular letters, and plans submitted to the Building Authority should be generated from the model. Each native file is limited to 500 MB, is confined to one type of plan, and is lodged through the Electronic Submission Hub with electronic plans or, for a paper submission, on a non-rewritable DVD-ROM.

## Critical main topics and subtopics

### 1. The eight plan types and accepted software (Table 1 and Table 2)
| Type of plan | Software 1 | Software 2 |
| --- | --- | --- |
| Superstructure | Revit 2020 or later | Tekla 2020 or later |
| Foundation | Revit 2020 or later | Tekla 2020 or later |
| Demolition, including hoarding, covered walkway, and gantry | Revit 2020 or later | Tekla 2020 or later |
| Excavation and lateral support | Revit 2020 or later | Tekla 2020 or later |
| Site formation | Revit 2020 or later | Civil 3D 2019 or later |
| Ground investigation | Revit 2020 or later | Civil 3D 2019 or later |
| Drainage | Revit 2020 or later | ArchiCAD 26 or later |
| Curtain wall | Revit 2020 or later | Tekla 2020 or later |

Other structural plans, including cladding, window, window wall, protective barrier, noise barrier, and temporary steel platform, are not included in the superstructure row.

| Software | Native format |
| --- | --- |
| Revit | .rvt |
| Tekla | the Tekla project-name folder |
| Civil 3D | .dwg |
| ArchiCAD | .pla |

Software not in Table 1 needs prior acceptance, with at least one sample project file and the enabling software. Web-based software is not accepted. Add-ins and in-house scripts must not be required for the Department’s standard software to use the file.

**SD takeaway:** Pick the software pair for the plan type before modelling, and keep site formation and ground investigation able to land in Civil 3D as well as Revit.

### 2. Submission lock (section 4)
| Rule | Lock |
| --- | --- |
| Electronic plans | Submit the model with the plans through the Electronic Submission Hub |
| Paper plans | Non-rewritable DVD-ROM, ISO/IEC 13346:1995, submitted with the plans. Other media are not acceptable unless the Building Authority agrees in writing |
| One type per file | Each file not more than 500 MB and confined to one type of plan. Different types may be cross-linked under a clear hierarchy |
| Contents | 3D model, views, schedules, and drawing sheets (plans, sections, area diagrams, calculations) from which the hard copy is printed |
| Hierarchy text | A text file on the hub submission or on the DVD describes the linked-file structure |
| Conflict | If the model and the plans differ, the plans prevail |
| Post-editing | Manual editing of drawings generated from the model should be minimised |
| Samples | The published samples are not a complete approval set |

**SD takeaway:** Generate the statutory sheets from the model, keep each plan type in its own file at or under 500 MB, and treat the signed plans as the document that prevails.

### 3. Appendix B object list
`appendix_b_bim_object_presentation_summary.pdf` is the BIM Objects Presentation Summary. Its text layer is a contents list of object families for the eight plan types, including bored pile, socket H-pile, pile cap, drainage pipe, manhole, grease trap, septic tank, slab, beam, column, wall, staircase, water tank, steelwork, hoarding and covered walkway, propping, and demolition items. It states that it is a presentation summary of major objects because the sample drawings do not cover every object. It does not itself set a dimensional design rule.

**SD takeaway:** Use the Appendix B object names so that piles, drainage, structure, and demolition read the same way on the eight plan types.

### Source
`BIMSPS_e.pdf` and `appendix_b_bim_object_presentation_summary.pdf` (source_reference/).
