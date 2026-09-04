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


