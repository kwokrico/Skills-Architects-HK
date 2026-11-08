import math


class EgressCalculator:
    """Rectangular geometry only, not a statutory escape-route assessment."""

    def calculate_remotest_point(self, data):
        if not isinstance(data, dict):
            return {"error": "Supply length and width as positive finite numbers in metres."}
        length, width = data.get("length"), data.get("width")
        limit = data.get("distance_limit")
        for name, value in (("length", length), ("width", width), ("distance_limit", limit)):
            if name == "distance_limit" and value is None:
                continue
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                return {"error": f"{name} must be a positive finite number in metres."}
            try:
                valid = math.isfinite(value) and value > 0
            except OverflowError:
                valid = False
            if not valid:
                return {"error": f"{name} must be a positive finite number in metres."}
        diagonal = math.hypot(length, width)
        if not math.isfinite(diagonal):
            return {"error": "Dimensions exceed the supported numeric range."}
        status = "Not assessed" if limit is None else (
            "Within supplied limit" if diagonal <= limit else "Exceeds supplied limit"
        )
        return {
            "diagonal_distance": round(diagonal, 2),
            "limit": limit,
            "status": status,
            "note": (
                "Rectangular diagonal only, not the actual escape path or compliance. "
                "Any distance_limit is a caller-supplied benchmark whose applicability "
                "requires separate verification; sprinkler status does not select a limit."
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
