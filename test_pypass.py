#!/usr/bin/env python3
"""Test suite validating PyPass password generation."""

import pytest

from src.password_generator import SecurePasswordGenerator, PersonalInfo, PasswordOptions


def _build_generator(personal_info: PersonalInfo, options: PasswordOptions) -> SecurePasswordGenerator:
    generator = SecurePasswordGenerator()
    generator.set_personal_info(personal_info)
    generator.set_options(options)
    return generator


def test_password_generation():
    personal_info = PersonalInfo(
        first_name="John",
        last_name="Doe",
        birth_date="01-01-1990",
        current_date="01-10-2025",
        platform="TestPlatform",
        city="TestCity",
    )

    options = PasswordOptions()
    options.length = 16

    generator = _build_generator(personal_info, options)
    password = generator.generate_password()

    assert len(password) == options.length

    strength_label, strength_score = generator.assess_strength(password)
    assert strength_label in {"Very Strong", "Strong", "Medium"}
    assert 0 <= strength_score <= 100

    entropy = generator.calculate_entropy(password)
    assert entropy > 0


@pytest.mark.parametrize(
    "options_kwargs",
    [
        {"include_uppercase": True, "include_lowercase": True,
            "include_numbers": True, "include_special": True},
        {"include_uppercase": True, "include_lowercase": True,
            "include_numbers": True, "include_special": False},
        {"include_uppercase": False, "include_lowercase": True,
            "include_numbers": True, "include_special": False},
        {"include_uppercase": True, "include_lowercase": False,
            "include_numbers": True, "include_special": True},
    ],
)
def test_character_sets(options_kwargs):
    personal_info = PersonalInfo(
        first_name="Test",
        last_name="User",
        birth_date="15-06-1985",
        current_date="01-10-2025",
        platform="TestApp",
        city="TestTown",
    )

    options = PasswordOptions()
    options.length = 12
    options.include_uppercase = options_kwargs["include_uppercase"]
    options.include_lowercase = options_kwargs["include_lowercase"]
    options.include_numbers = options_kwargs["include_numbers"]
    options.include_special = options_kwargs["include_special"]

    generator = _build_generator(personal_info, options)
    password = generator.generate_password()

    assert len(password) == options.length
    if options.include_uppercase:
        assert any(c.isupper() for c in password)
    if options.include_lowercase:
        assert any(c.islower() for c in password)
    if options.include_numbers:
        assert any(c.isdigit() for c in password)
    if options.include_special:
        assert any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)


def test_validation():
    incomplete_info = PersonalInfo(first_name="John")
    generator = SecurePasswordGenerator()
    generator.set_personal_info(incomplete_info)

    with pytest.raises(ValueError):
        generator.generate_password()

    complete_info = PersonalInfo(
        first_name="John",
        last_name="Doe",
        birth_date="01-01-1990",
        current_date="01-10-2025",
        platform="Test",
        city="TestCity",
    )

    options = PasswordOptions()
    options.include_uppercase = False
    options.include_lowercase = False
    options.include_numbers = False
    options.include_special = False

    generator.set_personal_info(complete_info)
    generator.set_options(options)

    with pytest.raises(ValueError):
        generator.generate_password()


def test_deterministic_generation():
    personal_info = PersonalInfo(
        first_name="Alice",
        last_name="Smith",
        birth_date="12-08-1992",
        current_date="02-10-2025",
        platform="Email",
        city="London",
    )

    options = PasswordOptions()
    options.length = 14

    generator = _build_generator(personal_info, options)
    password_first = generator.generate_password()
    password_second = generator.generate_password()

    assert password_first == password_second

    new_options = PasswordOptions()
    new_options.length = 14
    new_options.include_special = False
    generator.set_options(new_options)
    password_third = generator.generate_password()

    assert password_third != password_first
