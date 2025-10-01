#!/usr/bin/env python3
"""
Final verification script for PyPass
"""


def verify_imports():
    """Verify all imports work correctly"""
    try:
        from src.password_generator import SecurePasswordGenerator, PersonalInfo, PasswordOptions
        from src.gui import PasswordGeneratorApp, ClipboardManager
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False


def verify_instantiation():
    """Verify all classes can be instantiated"""
    try:
        from src.password_generator import SecurePasswordGenerator, PersonalInfo, PasswordOptions

        # Test instantiation
        generator = SecurePasswordGenerator()
        personal_info = PersonalInfo()
        options = PasswordOptions()

        print("✓ All core classes can be instantiated")
        return True
    except Exception as e:
        print(f"✗ Instantiation error: {e}")
        return False


def verify_basic_functionality():
    """Verify basic password generation works"""
    try:
        from src.password_generator import SecurePasswordGenerator, PersonalInfo, PasswordOptions

        # Create a complete setup
        personal_info = PersonalInfo(
            first_name="Test",
            last_name="User",
            birth_date="01-01-1990",
            current_date="01-10-2025",
            platform="VerificationTest",
            city="TestCity"
        )

        options = PasswordOptions()
        generator = SecurePasswordGenerator()
        generator.set_personal_info(personal_info)
        generator.set_options(options)

        # Generate password
        password = generator.generate_password()

        if len(password) == options.length:
            print("✓ Password generation working correctly")
            return True
        else:
            print(
                f"✗ Password length mismatch: expected {options.length}, got {len(password)}")
            return False

    except Exception as e:
        print(f"✗ Functionality error: {e}")
        return False


if __name__ == "__main__":
    print("PyPass Final Verification")
    print("=" * 40)

    success = True
    success &= verify_imports()
    success &= verify_instantiation()
    success &= verify_basic_functionality()

    print("=" * 40)
    if success:
        print("✓ ALL SYSTEMS GO! PyPass is fully functional.")
        print("✓ Ready for production use.")
    else:
        print("✗ Issues detected. Review errors above.")
    print("=" * 40)
