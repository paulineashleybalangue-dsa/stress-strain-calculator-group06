def main():
    """Main function for the stress and strain calculator with enhanced validation and control structures."""

# Material Database 
    materials = {"1": {"name": "Steel", "yield_strength": 250_000_000, "youngs_modulus": 200_000_000_000},
                 "2": {"name": "Aluminum", "yield_strength": 95_000_000, "youngs_modulus": 69_000_000_000},
                 "3": {"name": "Titanium", "yield_strength": 880_000_000, "youngs_modulus": 114_000_000_000}}

#Repeated Calculation Loop
    while True:
        print("\n=== Intelligent Stress and Strain Calculator ===")
        print("1. Steel")
        print("2. Aluminum")
        print("3. Titanium")
        print("4. Custom Material")
        print("5. Exit Program")
        print("Type 'q' or 'quit' at any prompt to exit back to menu")

        choice = input("Select a material option (1-5): ").strip()

        if choice.lower() in ["5", "q", "quit"]:
            print("\nExiting program. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("[Invalid Choice] Please select an option between 1 and 5.")
            continue

# Material Property Assignment
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
