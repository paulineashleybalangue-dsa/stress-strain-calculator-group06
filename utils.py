def calculate_stress(force: float, area: float) -> float:
    """Calculates stress in Pascals (Pa)."""
    if area <= 0:
        raise ValueError("Area must be greater than zero.")
    return force / area

def calculate_strain(original_length: float, change_in_length: float) -> float:
    """Calculates engineering strain (dimensionless)."""
    if original_length <= 0:
        raise ValueError("Original length must be greater than zero.")
    return change_in_length / original_length

def calculate_factor_of_safety(yield_strength: float, stress: float) -> float:
    """Calculates the factor of safety (Yield Strength / Stress)."""
    if yield_strength <= 0:
        raise ValueError("Yield strength must be greater than zero.")
    if stress <= 0:
        return float("inf")
    return yield_strength / stress

# --- VALIDATION HELPERS ---

def validate_positive_number(value: float, name: str) -> float:
    """Ensures a number is strictly greater than zero."""
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero.")
    return value

