import math


class EgressCalculator:
    """Logic for HK Buildings Ordinance / FS Code Egress Analysis."""

    def calculate_remotest_point(self, data):
        """
        Implements Section 1004.7 logic.
        Expects 'data' with: 'points' (list of coordinates) or 'room_dims'.
        """
        # Example logic for a rectangular room
        length = data.get("length", 0)
        width = data.get("width", 0)

        # Diagonal distance is often the start for remotest point assessment
        diagonal = math.sqrt(length ** 2 + width ** 2)

        # HK FS Code 2011: Max travel distance for residential (sprinklered) is 45m
        limit = 45 if data.get("sprinklered") else 30
        status = "Pass" if diagonal <= limit else "Fail"

        return {
            "diagonal_distance": round(diagonal, 2),
            "limit": limit,
            "status": status,
            "note": "Remotest point starts from the interior-most corner per 1004.7"
        }


class GFACalculator:
    """Logic for PNAP APP-2 GFA and Plot Ratio Aggregation."""

    def aggregate_gfa(self, floor_data):
        """
        Expects floor_data: list of dicts with {'area': float, 'type': string}
        """
        total_gfa = 0
        exempt_gfa = 0

        for item in floor_data:
            area = item.get("area", 0)
            if item.get("is_exempt"):
                # Track aggregate cap logic (PNAP APP-2)
                exempt_gfa += area
            else:
                total_gfa += area

        return {
            "total_gfa": round(total_gfa, 2),
            "exempt_gfa": round(exempt_gfa, 2),
            "accountable_gfa": round(total_gfa - exempt_gfa, 2)
        }


class DataSorter:
    """Logic for the 'Dictionary Sort' for OCR/Layout data."""

    def sort_by_layout(self, items):
        """
        Sorts a list of dictionaries based on 'x' and 'y' coordinates.
        Useful for architectural notes and accounting tables.
        """
        if not items or not isinstance(items, list):
            return []

        # Sort primarily by Y (top to bottom) then by X (left to right)
        # We use a 'tolerance' for Y to group items on the same line
        tolerance = 10

        sorted_items = sorted(
            items,
            key=lambda b: (b.get('y', 0) // tolerance, b.get('x', 0))
        )

        return sorted_items


def run_calculation(calc_type, data):
    """Factory function for the main.py dispatcher."""
    if calc_type == "egress_1004_7":
        return EgressCalculator().calculate_remotest_point(data)
    elif calc_type == "gfa_aggregator":
        return GFACalculator().aggregate_gfa(data)
    elif calc_type == "layout_sort":
        return DataSorter().sort_by_layout(data)
    else:
        return {"error": f"Calculator type {calc_type} not implemented."}