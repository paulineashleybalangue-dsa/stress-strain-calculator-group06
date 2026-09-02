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
