"""
Password Generator Module
Cryptographically secure password generation with user input integration
"""

import secrets
import string
import hashlib
import math
from datetime import datetime
from typing import Dict, List, Tuple


class PasswordOptions:
    """Configuration class for password generation options"""

    def __init__(self):
        self.length = 12
        self.include_uppercase = True
        self.include_lowercase = True
        self.include_numbers = True
        self.include_special = True
        self.exclude_ambiguous = True  # Exclude 0, O, l, I, 1

    def get_character_set(self) -> str:
        """Build character set based on options"""
        charset = ""

        if self.include_lowercase:
            charset += string.ascii_lowercase
        if self.include_uppercase:
            charset += string.ascii_uppercase
        if self.include_numbers:
            charset += string.digits
        if self.include_special:
            charset += "!@#$%^&*()_+-=[]{}|;:,.<>?"

        # Remove ambiguous characters if requested
        if self.exclude_ambiguous:
            ambiguous = "0Ol1I"
            charset = ''.join(c for c in charset if c not in ambiguous)

        return charset


class PersonalInfo:
    """Container for user personal information"""

    def __init__(self, first_name: str = "", last_name: str = "",
                 birth_date: str = "", current_date: str = "",
                 platform: str = "", city: str = ""):
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.birth_date = birth_date.strip()
        self.current_date = current_date.strip()
        self.platform = platform.strip()
        self.city = city.strip()

    def is_complete(self) -> bool:
        """Check if all required fields are filled"""
        return all([self.first_name, self.last_name, self.birth_date,
                   self.current_date, self.platform, self.city])

    def get_entropy_seed(self) -> str:
        """Create a deterministic seed from personal info for entropy mixing"""
        combined = f"{self.first_name}{self.last_name}{self.birth_date}{self.current_date}{self.platform}{self.city}"
        return hashlib.sha256(combined.encode('utf-8')).hexdigest()


class SecurePasswordGenerator:
    """Cryptographically secure password generator"""

    def __init__(self):
        self.personal_info = PersonalInfo()
        self.options = PasswordOptions()

    def set_personal_info(self, personal_info: PersonalInfo):
        """Set personal information for password generation"""
        self.personal_info = personal_info

    def set_options(self, options: PasswordOptions):
        """Set password generation options"""
        self.options = options

    def _create_entropy_pool(self) -> str:
        """Create a large entropy pool mixing personal info and secure randomness"""
        # Start with cryptographically secure random bytes
        secure_random = secrets.token_bytes(64)

        # Mix with personal info hash for uniqueness
        personal_seed = self.personal_info.get_entropy_seed()

        # Combine and hash multiple times for good mixing
        combined = secure_random + personal_seed.encode('utf-8')

        # Multiple rounds of hashing to increase entropy mixing
        for _ in range(1000):  # 1000 rounds of mixing
            combined = hashlib.sha512(combined).digest()

        return combined.hex()

    def _ensure_character_requirements(self, password: str, charset: str) -> str:
        """Ensure password meets character type requirements"""
        # Get required character types
        required_chars = []

        if self.options.include_lowercase:
            lowercase = [c for c in charset if c in string.ascii_lowercase]
            if lowercase and not any(c in password for c in lowercase):
                required_chars.append(secrets.choice(lowercase))

        if self.options.include_uppercase:
            uppercase = [c for c in charset if c in string.ascii_uppercase]
            if uppercase and not any(c in password for c in uppercase):
                required_chars.append(secrets.choice(uppercase))

        if self.options.include_numbers:
            numbers = [c for c in charset if c in string.digits]
            if numbers and not any(c in password for c in numbers):
                required_chars.append(secrets.choice(numbers))

        if self.options.include_special:
            special = [c for c in charset if c in "!@#$%^&*()_+-=[]{}|;:,.<>?"]
            if special and not any(c in password for c in special):
                required_chars.append(secrets.choice(special))

        # Replace random positions with required characters
        password_list = list(password)
        for req_char in required_chars:
            if len(password_list) > 0:
                pos = secrets.randbelow(len(password_list))
                password_list[pos] = req_char

        return ''.join(password_list)

    def _avoid_obvious_patterns(self, password: str) -> str:
        """Check and modify password to avoid obvious personal info patterns"""
        # Convert to lowercase for pattern checking
        password_lower = password.lower()

        # Patterns to avoid
        patterns_to_avoid = [
            self.personal_info.first_name.lower()[:4] if len(
                self.personal_info.first_name) >= 4 else "",
            self.personal_info.last_name.lower()[:4] if len(
                self.personal_info.last_name) >= 4 else "",
            self.personal_info.birth_date.replace("-", ""),
            self.personal_info.city.lower()[:4] if len(
                self.personal_info.city) >= 4 else "",
        ]

        # Remove empty patterns
        patterns_to_avoid = [p for p in patterns_to_avoid if len(p) >= 3]

        # Check for patterns and regenerate if found
        for pattern in patterns_to_avoid:
            if pattern in password_lower:
                # Regenerate with different entropy if pattern found
                charset = self.options.get_character_set()
                new_password = ""
                entropy_pool = self._create_entropy_pool()

                for i in range(self.options.length):
                    # Use different position in entropy pool
                    entropy_index = (
                        hash(entropy_pool + str(i + 100)) % len(charset))
                    new_password += charset[entropy_index % len(charset)]

                # Recursive check
                return self._avoid_obvious_patterns(new_password)

        return password

    def generate_password(self) -> str:
        """Generate a secure password based on personal info and options"""
        if not self.personal_info.is_complete():
            raise ValueError("Personal information is incomplete")

        charset = self.options.get_character_set()
        if not charset:
            raise ValueError("No character types selected")

        # Create entropy pool
        entropy_pool = self._create_entropy_pool()

        # Generate password using entropy pool
        password = ""
        for i in range(self.options.length):
            # Use different parts of entropy pool for each character
            entropy_segment = entropy_pool[i * 4:(i + 1) * 4]
            if len(entropy_segment) < 4:
                entropy_segment = entropy_pool[i % (
                    len(entropy_pool) - 4):i % (len(entropy_pool) - 4) + 4]

            # Convert to integer and use for character selection
            char_index = int(entropy_segment, 16) % len(charset)
            password += charset[char_index]

        # Ensure character requirements are met
        password = self._ensure_character_requirements(password, charset)

        # Avoid obvious patterns
        password = self._avoid_obvious_patterns(password)

        return password

    def calculate_entropy(self, password: str) -> float:
        """Calculate Shannon entropy of password"""
        if not password:
            return 0.0

        # Count frequency of each character
        frequency = {}
        for char in password:
            frequency[char] = frequency.get(char, 0) + 1

        # Calculate Shannon entropy
        entropy = 0.0
        length = len(password)

        for count in frequency.values():
            probability = count / length
            if probability > 0:
                entropy -= probability * math.log2(probability)

        return entropy

    def assess_strength(self, password: str) -> Tuple[str, float]:
        """Assess password strength and return (label, score)"""
        if not password:
            return "Very Weak", 0.0

        score = 0.0

        # Length scoring (0-30 points)
        length_score = min(30, len(password) * 2)
        score += length_score

        # Character variety scoring (0-40 points)
        variety_score = 0
        if any(c.islower() for c in password):
            variety_score += 10
        if any(c.isupper() for c in password):
            variety_score += 10
        if any(c.isdigit() for c in password):
            variety_score += 10
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            variety_score += 10
        score += variety_score

        # Entropy scoring (0-30 points)
        entropy = self.calculate_entropy(password)
        entropy_score = min(30, entropy * 6)
        score += entropy_score

        # Normalize to 0-100
        final_score = min(100, score)

        # Categorize strength
        if final_score >= 80:
            return "Very Strong", final_score
        elif final_score >= 60:
            return "Strong", final_score
        elif final_score >= 40:
            return "Medium", final_score
        elif final_score >= 20:
            return "Weak", final_score
        else:
            return "Very Weak", final_score
