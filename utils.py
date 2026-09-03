def calculate_stress(force, area):
    """
    calculates stress based on force and area.

    arguments:
        force: the applied force in newtons.
        area: the cross-sectional area in square meters.

    returns:
        the calculated stress in pascals.

    raises:
        ValueError: if the area is zero or negative.
    """
    if area <= 0:
        raise ValueError("Area must be greater than zero.")
    return force / area