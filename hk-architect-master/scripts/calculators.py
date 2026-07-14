import math


class EgressCalculator:
    """Logic for HK Buildings Ordinance / FS Code Egress Analysis."""

    def calculate_remotest_point(self, data):
        length = data.get("length", 0)
        width = data.get("width", 0)
        diagonal = math.sqrt(length ** 2 + width ** 2)
        limit = 45 if data.get("sprinklered") else 30
        status = "Pass" if diagonal <= limit else "Fail"
        return {
            "diagonal_distance": round(diagonal, 2),
            "limit": limit,
            "status": status,
            "note": (
                "Simplified rectangular-room check only; full FS Code remotest-point "
                "path analysis requires manual/AP review — not statutory sign-off."
            ),
        }


class GFACalculator:
    """Logic for PNAP APP-2 GFA and Plot Ratio Aggregation."""

    def aggregate_gfa(self, floor_data):
        total_gfa = 0
        exempt_gfa = 0
        for item in floor_data:
            area = item.get("area", 0)
            if item.get("is_exempt"):
                exempt_gfa += area
            else:
                total_gfa += area
        return {
            "total_gfa": round(total_gfa + exempt_gfa, 2),
            "exempt_gfa": round(exempt_gfa, 2),
            "accountable_gfa": round(total_gfa, 2),
        }


class DataSorter:
    """Sort OCR/layout items by Y then X."""

    def sort_by_layout(self, items):
        if not items or not isinstance(items, list):
            return []
        tolerance = 10
        return sorted(
            items,
            key=lambda b: (b.get("y", 0) // tolerance, b.get("x", 0)),
        )


def run_calculation(calc_type, data):
    data = data or {}
    if calc_type == "egress_1004_7":
        return EgressCalculator().calculate_remotest_point(data)
    if calc_type == "gfa_aggregator":
        floor_data = data if isinstance(data, list) else data.get("floors", [])
        return GFACalculator().aggregate_gfa(floor_data)
    if calc_type == "layout_sort":
        items = data if isinstance(data, list) else data.get("items", [])
        return DataSorter().sort_by_layout(items)
    return {"error": f"Calculator type {calc_type} not implemented."}
