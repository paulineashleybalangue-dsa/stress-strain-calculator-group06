def main():
    """Main function for the stress and strain calculator with enhanced validation and control structures."""

# Material Database 
    materials = {"1": {"name": "Steel", "yield_strength": 250_000_000, "youngs_modulus": 200_000_000_000},
                 "2": {"name": "Aluminum", "yield_strength": 95_000_000, "youngs_modulus": 69_000_000_000},
                 "3": {"name": "Titanium", "yield_strength": 880_000_000, "youngs_modulus": 114_000_000_000}}
    