def calculate_stress(force: float, area: float) -> float:
    """Calculates stress in Pascals (Pa)."""
    if area <= 0:
        raise ValueError("Area must be greater than zero.")
    return force / area
