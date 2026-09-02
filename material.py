# Part 3: Data Structures - Stress and Strain Calculator Template
# TODO: Complete this template by implementing data structures

def main():
    """Main function for the stress and strain calculator with data structures."""

    print("=== Stress and Strain Calculator - Session Manager ===")
    print()

     # TODO: Initialize empty list for calculation history
    calculation_history = []

    # TODO: Initialize empty set for unique materials
    unique_materials = set()

    # TODO: Create tuple for measurement units (N, m², m, Pa)
    units = ("N", "m²", "m", "Pa")

    # TODO: Create materials database dictionary with at least 3 materials
    # Each material should have yield_strength and youngs_modulus

    materials = {
        "1": {
            "name": "Steel", 
            "yield_strength": 250_000_000, 
            "youngs_modulus": 200_000_000_000},
        "2": {
            "name": "Aluminum", 
            "yield_strength": 95_000_000, 
            "youngs_modulus": 69_000_000_000},
        "3": {
            "name": "Titanium", 
            "yield_strength": 880_000_000, 
            "youngs_modulus": 114_000_000_000}}

    # Main calculation loop
    while True:

        # TODO: Display available materials
        print("\n=== Intelligent Stress and Strain Calculator ===")
        print("1. Steel")
        print("2. Aluminum")
        print("3. Titanium")
        print("4. Custom Material")
        print("5. Exit Program")
        print("Type 'q' or 'quit' at any prompt to exit back to menu")

        # TODO: Get material selection from user
        choice = input("Select a material option (1-5): ").strip()

        # TODO: Check if user wants to quit
        if choice.lower() in ["5", "q", "quit"]:
            print("\nExiting program. Goodbye!")
            break

        # TODO: Validate material exists in database
        if choice not in ["1", "2", "3", "4"]:
            print("[Invalid Choice] Please select an option between 1 and 5.")
            continue    

        if choice in materials:
            selected_material = materials[choice]["name"]
            yield_strength = materials[choice]["yield_strength"]
            youngs_modulus = materials[choice]["youngs_modulus"]
            
        else:
            selected_material = input("Enter custom material name: ").strip()
            if  selected_material.lower() in ["q", "quit"]:
                continue
            if not selected_material:
                selected_material = "Custom Material"
            
            # Validate Custom Material Inputs
            exit_to_menu = False
            while True:
                try:
                    ys_raw = input("Enter Custom Yield Strength (MPa): ").strip()
                    if ys_raw.lower() in ["q", "quit"]:
                        exit_to_menu = True
                        break
                    ys_input = float(ys_raw)
                    if ys_input <= 0:
                        print("Yield strength must be positive!")
                        continue
                    yield_strength = ys_input * 1_000_000  # Convert MPa to Pa
                    break
                except ValueError:
                    print("Please enter a valid number for Yield Strength!")

            if exit_to_menu:
                continue
        
        try:
            # TODO: Get input values (force, area, original_length, change_in_length)
            force = float(input(f"Enter applied force ({units[0]}): "))
            area = float(input(f"Enter cross-sectional area ({units[1]}): ")) 
            original_length = float( input(f"Enter original length ({units[2]}): ") ) 
            change_in_length = float( input(f"Enter change in length ({units[2]}): ") )

             # TODO: Validate inputs (positive values, non-zero where needed)
            if force < 0: 
                print("Force cannot be negative!") 
                continue 

            if area <= 0: 
                print( "Cross-sectional area must be greater than zero " "(prevents division error)!" ) 
                continue 

            if original_length <= 0: 
                print( "Original length must be greater than zero!" ) 
                continue 

            if change_in_length < 0: 
                print("Change in length cannot be negative!") 
                continue