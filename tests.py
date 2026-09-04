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

class TestHistoryManager:

    def __init__(self, output_dir: str = "output"):
        self.history = []
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def add_test(self, test: StressStrainTest) -> None:
        self.history.append(test)

    def export_to_json(self, filename: str = "test_history.json") -> Path:
        filepath = self.output_dir / filename
        data = [test.to_dict() for test in self.history]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return filepath

    def export_to_csv(self, filename: str = "test_history.csv") -> Path:
        filepath = self.output_dir / filename
        if not self.history:
            return filepath

        fieldnames = list(self.history[0].to_dict().keys())
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for test in self.history:
                writer.writerow(test.to_dict())
        return filepath