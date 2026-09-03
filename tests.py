def validate_positive_number(value: float, name: str) -> float:
    """
    checks if a number is greater than zero ♡

    arguments:
        value: the number being checked.
        name: the name of the input being checked.

    returns:
        the validated number.

    raises:
        ValueError: if the number is zero or negative.
    """
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero.")
    return value