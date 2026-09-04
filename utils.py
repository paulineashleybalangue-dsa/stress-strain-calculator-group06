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
