import csv
import json
from datetime import datetime
from pathlib import Path
from material import Material
from utils import (
    calculate_factor_of_safety,
    calculate_strain,
    calculate_stress,
)

class StressStrainTest:

    def __init__(
        self,
        material: Material,
        force: float,
        area: float,
        original_length: float,
        change_in_length: float,
    ):
        self.material = material
        self.force = force
        self.area = area
        self.original_length = original_length
        self.change_in_length = change_in_length
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# automatically run calculations using utility functions
        self.stress = calculate_stress(force, area)
        self.strain = calculate_strain(original_length, change_in_length)
        self.factor_of_safety = calculate_factor_of_safety(
            material.properties.yield_strength, self.stress
        )

    @property
    def stress_mpa(self) -> float:
        return self.stress / 1_000_000

    def will_fail(self) -> bool:
        return not self.material.can_withstand_stress(self.stress)

    def to_dict(self) -> dict:
        """Converts test instance into a dictionary for serialization."""
        return {
            "timestamp": self.timestamp,
            "material": self.material.name,
            "force_N": self.force,
            "area_m2": self.area,
            "original_length_m": self.original_length,
            "change_in_length_m": self.change_in_length,
            "stress_Pa": self.stress,
            "stress_MPa": self.stress_mpa,
            "strain": self.strain,
            "factor_of_safety": self.factor_of_safety,
            "failed": self.will_fail(),
        }