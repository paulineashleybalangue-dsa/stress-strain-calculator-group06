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

def validate_non_zero(value: float, name: str) -> float:
    """
    checks if a number is not zero ♡

    arguments:
        value: the number being checked.
        name: the name of the input being checked.

    returns:
        the validated number.

    raises:
        ValueError: if the number is zero.
    """
    if value == 0:
        raise ValueError(f"{name} cannot be zero.")
    return value

def get_validated_input(prompt: str, validator_func, name: str) -> float:
    """
    gets a valid number from the user (｡•ᴗ•｡)

    arguments:
        prompt: the message shown to the user.
        validator_func: the function used to validate the input.
        name: the name of the input being checked.

    returns:
        a validated number.
    """
    while True:
        try:
            value = float(input(prompt))
            return validator_func(value, name)
        except ValueError as error:
            print(f"Invalid input: {error} :(")

def create_calculation_record(material: str, inputs: dict, results: dict) -> dict:
    """
    creates a dictionary for one calculation ♡

    arguments:
        material: the material used in the calculation.
        inputs: the input values used for the calculation.
        results: the calculated results.

    returns:
        a dictionary containing the material, inputs, and results.
    """
    return {
        "material": material,
        "inputs": inputs,
        "results": results
    }

def add_to_history(history_list: list, record: dict) -> None:
    """
    adds a calculation record to the history ♡

    arguments:
        history_list: the list containing calculation records.
        record: the calculation record to add.

    returns:
        None.
    """
    history_list.append(record)

def get_materials_database() -> dict:
    """
    returns the materials properties dictionary ♡

    returns:
        a dictionary containing the available materials
        and their properties.
    """
    return {
        "steel": {
            "yield_strength": 250_000_000
        },
        "aluminum": {
            "yield_strength": 95_000_000
        },
        "concrete": {
            "yield_strength": 880_000_000
        }
    }
