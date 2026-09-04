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