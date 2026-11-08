"""Regression checks for misleading egress results; no statutory compliance test."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    "calculators", Path(__file__).resolve().parents[1] / "scripts" / "calculators.py"
)
calculators = importlib.util.module_from_spec(spec)
spec.loader.exec_module(calculators)


class CalculatorBoundaries(unittest.TestCase):
    def test_missing_geometry_cannot_pass(self):
        for data in ({}, {"area": 500}, {"length": 10}):
            with self.subTest(data=data):
                self.assertIn("error", calculators.run_calculation("egress_1004_7", data))

    def test_invalid_geometry_is_rejected(self):
        for value in (0, -1, float("nan"), float("inf"), True, "10"):
            with self.subTest(value=value):
                self.assertIn("error", calculators.run_calculation(
                    "egress_1004_7", {"length": value, "width": 4}))

    def test_sprinklers_do_not_supply_statutory_limit(self):
        for sprinklered in (False, True):
            result = calculators.run_calculation(
                "egress_1004_7", {"length": 3, "width": 4, "sprinklered": sprinklered})
            self.assertEqual(result["diagonal_distance"], 5)
            self.assertIsNone(result["limit"])
            self.assertEqual(result["status"], "Not assessed")

    def test_explicit_benchmark_is_only_geometric_comparison(self):
        for limit, status in ((5, "Within supplied limit"), (4, "Exceeds supplied limit")):
            result = calculators.run_calculation(
                "egress_1004_7", {"length": 3, "width": 4, "distance_limit": limit})
            self.assertEqual(result["status"], status)
            self.assertEqual(result["limit"], limit)

    def test_invalid_benchmark_is_rejected(self):
        for limit in (0, -1, True, float("nan")):
            self.assertIn("error", calculators.run_calculation(
                "egress_1004_7", {"length": 3, "width": 4, "distance_limit": limit}))

    def test_gfa_preserves_supplied_classification(self):
        result = calculators.run_calculation("gfa_aggregator", {"floors": [
            {"area": 500, "is_exempt": False}, {"area": 30, "is_exempt": True}]})
        self.assertEqual(result, {"total_gfa": 530, "exempt_gfa": 30, "accountable_gfa": 500})


if __name__ == "__main__":
    unittest.main()
