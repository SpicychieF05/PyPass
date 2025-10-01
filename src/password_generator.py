"""
Password Generator Module
Cryptographically secure password generation with user input integration
"""

import string
import hashlib
import math
from typing import List, Tuple


class PasswordOptions:
    """Configuration class for password generation options"""

    def __init__(self):
        self.length = 12
        self.include_uppercase = True
        self.include_lowercase = True
        self.include_numbers = True
        self.include_special = True
        self.exclude_ambiguous = True  # Exclude 0, O, l, I, 1

    def fingerprint(self) -> str:
        """Return a deterministic fingerprint of the option combination."""
        return "|".join([
            f"len={self.length}",
            f"upper={int(self.include_uppercase)}",
            f"lower={int(self.include_lowercase)}",
            f"digits={int(self.include_numbers)}",
            f"special={int(self.include_special)}",
            f"exclude_ambiguous={int(self.exclude_ambiguous)}",
        ])

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

    class _DeterministicPRNG:
        """Deterministic pseudo-random number generator based on SHA-512."""

        def __init__(self, seed_material: bytes):
            self._seed_material = seed_material
            self._buffer = bytearray()
            self._counter = 0

        def _refill(self):
            counter_bytes = self._counter.to_bytes(8, 'big', signed=False)
            block = hashlib.sha512(
                self._seed_material + counter_bytes).digest()
            self._buffer.extend(block)
            self._counter += 1

        def next_bytes(self, length: int) -> bytes:
            if length <= 0:
                raise ValueError("Length must be positive")
            while len(self._buffer) < length:
                self._refill()
            result = self._buffer[:length]
            del self._buffer[:length]
            return bytes(result)

        def next_int(self, modulo: int) -> int:
            if modulo <= 0:
                raise ValueError("Modulo must be positive")
            value = int.from_bytes(self.next_bytes(4), 'big', signed=False)
            return value % modulo

    def set_personal_info(self, personal_info: PersonalInfo):
        """Set personal information for password generation"""
        self.personal_info = personal_info

    def set_options(self, options: PasswordOptions):
        """Set password generation options"""
        self.options = options

    def _build_prng(self) -> "SecurePasswordGenerator._DeterministicPRNG":
        """Construct a deterministic PRNG based on personal info and options."""
        if not self.personal_info.is_complete():
            raise ValueError("Personal information is incomplete")

        seed_basis = self.personal_info.get_entropy_seed()
        option_fingerprint = self.options.fingerprint()

        seed_material = hashlib.pbkdf2_hmac(
            'sha512',
            seed_basis.encode('utf-8'),
            option_fingerprint.encode('utf-8'),
            200_000,
            dklen=64
        )

        return self._DeterministicPRNG(seed_material)

    def _ensure_character_requirements(self, password: List[str], charset: str,
                                       rng: "SecurePasswordGenerator._DeterministicPRNG") -> List[str]:
        """Ensure password meets character type requirements"""
        # Get required character types
        required_chars = []

        if self.options.include_lowercase:
            lowercase = [c for c in charset if c in string.ascii_lowercase]
            if lowercase and not any(c in lowercase for c in password):
                required_chars.append(lowercase)

        if self.options.include_uppercase:
            uppercase = [c for c in charset if c in string.ascii_uppercase]
            if uppercase and not any(c in uppercase for c in password):
                required_chars.append(uppercase)

        if self.options.include_numbers:
            numbers = [c for c in charset if c in string.digits]
            if numbers and not any(c in numbers for c in password):
                required_chars.append(numbers)

        if self.options.include_special:
            special = [c for c in charset if c in "!@#$%^&*()_+-=[]{}|;:,.<>?"]
            if special and not any(c in special for c in password):
                required_chars.append(special)

        # Replace deterministic positions with required characters
        for char_pool in required_chars:
            if not password:
                break
            position = rng.next_int(len(password))
            replacement = char_pool[rng.next_int(len(char_pool))]
            password[position] = replacement

        return password

    def _avoid_obvious_patterns(self, password: List[str], charset: str,
                                rng: "SecurePasswordGenerator._DeterministicPRNG") -> List[str]:
        """Check and modify password to avoid obvious personal info patterns"""
        # Convert to lowercase for pattern checking
        password_lower = ''.join(password).lower()

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

        # Check for patterns and deterministically adjust if found
        for pattern in patterns_to_avoid:
            while pattern and pattern in password_lower:
                position = rng.next_int(len(password))
                replacement = charset[rng.next_int(len(charset))]
                password[position] = replacement
                password_lower = ''.join(password).lower()

        return password

    def generate_password(self) -> str:
        """Generate a secure password based on personal info and options"""
        charset = self.options.get_character_set()
        if not charset:
            raise ValueError("No character types selected")

        if not 8 <= self.options.length <= 128:
            raise ValueError(
                "Password length must be between 8 and 128 characters")

        rng = self._build_prng()

        # Generate password deterministically using PRNG
        password_chars = [charset[rng.next_int(len(charset))]
                          for _ in range(self.options.length)]

        # Ensure requirements and adjust patterns deterministically
        password_chars = self._ensure_character_requirements(
            password_chars, charset, rng)
        password_chars = self._avoid_obvious_patterns(
            password_chars, charset, rng)

        return ''.join(password_chars)

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
