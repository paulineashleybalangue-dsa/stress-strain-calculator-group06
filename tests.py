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