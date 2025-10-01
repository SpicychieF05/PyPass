#!/usr/bin/env python3
"""
Test script to verify PyPass functionality
"""

from src.password_generator import SecurePasswordGenerator, PersonalInfo, PasswordOptions


def test_password_generation():
    """Test basic password generation functionality"""
    print("Testing PyPass Core Functionality...")

    # Create test personal info
    personal_info = PersonalInfo(
        first_name="John",
        last_name="Doe",
        birth_date="01-01-1990",
        current_date="01-10-2025",
        platform="TestPlatform",
        city="TestCity"
    )

    # Create password options
    options = PasswordOptions()
    options.length = 16

    # Create generator
    generator = SecurePasswordGenerator()
    generator.set_personal_info(personal_info)
    generator.set_options(options)

    # Test password generation
    try:
        password = generator.generate_password()
        print(f"✓ Password generated successfully: {password}")
        print(f"✓ Password length: {len(password)}")

        # Test strength assessment
        strength_label, strength_score = generator.assess_strength(password)
        print(
            f"✓ Strength assessment: {strength_label} ({strength_score:.1f}%)")

        # Test entropy calculation
        entropy = generator.calculate_entropy(password)
        print(f"✓ Shannon entropy: {entropy:.2f}")

        return True

    except Exception as e:
        print(f"✗ Error during password generation: {e}")
        return False


def test_character_sets():
    """Test different character set combinations"""
    print("\nTesting Character Set Combinations...")

    personal_info = PersonalInfo(
        first_name="Test",
        last_name="User",
        birth_date="15-06-1985",
        current_date="01-10-2025",
        platform="TestApp",
        city="TestTown"
    )

    generator = SecurePasswordGenerator()
    generator.set_personal_info(personal_info)

    # Test different combinations
    test_cases = [
        {"uppercase": True, "lowercase": True, "numbers": True, "special": True},
        {"uppercase": True, "lowercase": True, "numbers": True, "special": False},
        {"uppercase": False, "lowercase": True, "numbers": True, "special": False},
        {"uppercase": True, "lowercase": False, "numbers": True, "special": True},
    ]

    for i, case in enumerate(test_cases):
        options = PasswordOptions()
        options.include_uppercase = case["uppercase"]
        options.include_lowercase = case["lowercase"]
        options.include_numbers = case["numbers"]
        options.include_special = case["special"]
        options.length = 12

        generator.set_options(options)

        try:
            password = generator.generate_password()
            print(f"✓ Test case {i+1}: {password}")
        except Exception as e:
            print(f"✗ Test case {i+1} failed: {e}")
            return False

    return True


def test_validation():
    """Test input validation"""
    print("\nTesting Input Validation...")

    # Test incomplete personal info
    incomplete_info = PersonalInfo(first_name="John")  # Missing other fields
    generator = SecurePasswordGenerator()
    generator.set_personal_info(incomplete_info)

    try:
        password = generator.generate_password()
        print("✗ Should have failed with incomplete info")
        return False
    except ValueError as e:
        print(f"✓ Correctly caught incomplete info: {e}")

    # Test no character types selected
    complete_info = PersonalInfo(
        first_name="John",
        last_name="Doe",
        birth_date="01-01-1990",
        current_date="01-10-2025",
        platform="Test",
        city="TestCity"
    )

    options = PasswordOptions()
    options.include_uppercase = False
    options.include_lowercase = False
    options.include_numbers = False
    options.include_special = False

    generator.set_personal_info(complete_info)
    generator.set_options(options)

    try:
        password = generator.generate_password()
        print("✗ Should have failed with no character types")
        return False
    except ValueError as e:
        print(f"✓ Correctly caught no character types: {e}")

    return True


if __name__ == "__main__":
    print("PyPass Verification Test")
    print("=" * 50)

    success = True
    success &= test_password_generation()
    success &= test_character_sets()
    success &= test_validation()

    print("\n" + "=" * 50)
    if success:
        print("✓ All tests passed! PyPass is working correctly.")
    else:
        print("✗ Some tests failed. Please check the issues above.")

    print("=" * 50)
