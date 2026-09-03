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

def calculate_strain(original_length, change_in_length):
    """
    calculates strain based on original length and change in length.

    arguments:
        original_length: the original length in meters.
        change_in_length: the change in length in meters.

    returns:
        the calculated strain.

    raises:
        ValueError: if the original length is zero or negative.
    """
    if original_length <= 0:
        raise ValueError("Original length must be greater than zero.")
    return change_in_length / original_length