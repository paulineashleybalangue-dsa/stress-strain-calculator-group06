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