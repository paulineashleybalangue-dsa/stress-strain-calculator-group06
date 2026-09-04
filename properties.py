from dataclasses import dataclass

@dataclass
class MaterialProperties:
    density: float  # kg/m^3
    yield_strength: float  # Pa
    typical_youngs_modulus: float  # Pa
