from material import Metal
from properties import MaterialProperties

# Predefined materials database using domain objects
PREDEFINED_MATERIALS = {
    "1": Metal(
        name="Steel",
        properties=MaterialProperties(
            density=7850,
            yield_strength=250_000_000,
            typical_youngs_modulus=200_000_000_000,
        ),
        is_ferrous=True,
    ),
    "2": Metal(
        name="Aluminum",
        properties=MaterialProperties(
            density=2700,
            yield_strength=95_000_000,
            typical_youngs_modulus=69_000_000_000,
        ),
        is_ferrous=False,
    ),
    "3": Metal(
        name="Titanium",
        properties=MaterialProperties(
            density=4500,
            yield_strength=880_000_000,
            typical_youngs_modulus=114_000_000_000,
        ),
        is_ferrous=False,
    ),
}
