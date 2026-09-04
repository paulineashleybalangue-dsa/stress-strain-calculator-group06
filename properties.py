from dataclasses import dataclass

@dataclass
class MaterialProperties:
    density: float  # kg/m^3
    yield_strength: float  # Pa
    typical_youngs_modulus: float  # Pa

    def __post_init__(self):
        """Validate that all physical properties are positive numbers."""
        if (
            self.density <= 0
            or self.yield_strength <= 0
            or self.typical_youngs_modulus <= 0
        ):
            raise ValueError("All material properties must be positive values.")
