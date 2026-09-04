from database import PREDEFINED_MATERIALS
from material import Material
from properties import MaterialProperties
from tests import StressStrainTest, TestHistoryManager
from utils import get_validated_input, validate_positive_number

def run_automated_verification_tests(history_manager: TestHistoryManager):
    """Runs Test 1 and Test 2 automatically to verify results against requirements."""
    print("\n" + "=" * 15 + " RUNNING AUTOMATED VERIFICATION " + "=" * 15)

    # Test 1 — Steel
    steel = PREDEFINED_MATERIALS["1"]
    test1 = StressStrainTest(
        material=steel,
        force=50000.0,
        area=0.01,
        original_length=10.0,
        change_in_length=0.005,
    )
    history_manager.add_test(test1)

    print("\n--- Test 1 Results (Steel) ---")
    print(
        f"Calculated Stress : {test1.stress:,.2f} Pa (Expected: 5,000,000 Pa) -> {'PASS' if test1.stress == 5000000 else 'FAIL'}"
    )
    print(
        f"Calculated Strain : {test1.strain} (Expected: 0.0005) -> {'PASS' if test1.strain == 0.0005 else 'FAIL'}"
    )

    # Test 2 — Aluminum
    aluminum = PREDEFINED_MATERIALS["2"]
    test2 = StressStrainTest(
        material=aluminum,
        force=10000.0,
        area=0.002,
        original_length=1.0,
        change_in_length=0.0015,
    )
    history_manager.add_test(test2)

    print("\n--- Test 2 Results (Aluminum) ---")
    print(
        f"Calculated Stress : {test2.stress:,.2f} Pa (Expected: 5,000,000 Pa) -> {'PASS' if test2.stress == 5000000 else 'FAIL'}"
    )
    print(
        f"Calculated Strain : {test2.strain} (Expected: 0.0015) -> {'PASS' if test2.strain == 0.0015 else 'FAIL'}"
    )
    print("=" * 62)


def main():
    history_manager = TestHistoryManager()

    while True:
        print("\n=== Stress & Strain Calculator ===")
        print("1. Steel Test")
        print("2. Aluminum Test")
        print("3. Titanium Test")
        print("4. Custom Material Test")
        print("5. Load Test History from JSON")
        print("6. Run Automated Verification Suite (Test 1 & 2)")
        print("7. Export History & Exit")

        choice = input("\nSelect an option (1-7): ").strip()

        if choice == "7" or choice.lower() in ["q", "quit"]:
            if history_manager.history:
                json_path = history_manager.export_to_json()
                csv_path = history_manager.export_to_csv()
                print(f"\n[Saved] Exported {len(history_manager.history)} records to:")
                print(f" - JSON: {json_path}")
                print(f" - CSV:  {csv_path}")
            print("Exiting application. Goodbye!")
            break

        elif choice == "5":
            history_manager.load_from_json()
            continue

        elif choice == "6":
            run_automated_verification_tests(history_manager)
            continue

        elif choice not in ["1", "2", "3", "4"]:
            print("[Invalid Choice] Please enter a number between 1 and 7.")
            continue

