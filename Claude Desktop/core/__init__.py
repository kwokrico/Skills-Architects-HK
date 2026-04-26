"""
HK Architect Core Logic Package
Contains mathematical engines for Egress, GFA, and Data Sorting.
"""

from .calculators import (
    EgressCalculator,
    GFACalculator,
    DataSorter,
    run_calculation
)

# You can also define package-wide constants here
VERSION = "1.0.0"
AUTHOR = "Rico Kwok"

# This defines what is exported when someone runs 'from core import *'
__all__ = [
    "EgressCalculator",
    "GFACalculator",
    "DataSorter",
    "run_calculation"
]