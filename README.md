# PyPass - Offline Password Generator

## Overview

PyPass is a secure, offline password generator desktop application built with Python and Tkinter. It generates cryptographically strong passwords by combining user personal information with secure random entropy, ensuring both uniqueness and security.

## 🔒 Security Features

- **100% Offline Operation**: No internet connectivity required or used
- **Cryptographically Secure**: Uses Python's `secrets` library for random generation
- **No Data Storage**: Personal information and passwords are never saved unless explicitly downloaded
- **Auto-Clear Clipboard**: Clipboard is automatically cleared after 30 seconds
- **Pattern Avoidance**: Prevents obvious use of personal information in generated passwords
- **Strong Entropy Mixing**: Combines personal data with 1000 rounds of cryptographic hashing

## 📋 Requirements

### System Requirements
- Windows 10 or later
- Python 3.11+ (for development)
- 50MB free disk space

### For Development
- Python 3.11+
- tkinter (usually included with Python)
- PyInstaller 5.13.0+ (for building executable)

## 🚀 Quick Start

### Using Pre-built Executable
1. Download `PyPass.exe` from releases
2. Run the executable directly
3. Fill in your personal information
4. Customize password options
5. Click "Generate Password"

### Running from Source
```bash
# Clone or download the project
cd PyPass

# Install dependencies (optional, for building only)
pip install -r requirements.txt

# Run the application
python main.py
```

## 🏗️ Building from Source

### Method 1: Using Build Script (Recommended)
```bash
# Windows
build_exe.bat

# Linux/macOS
chmod +x build_simple.sh
./build_simple.sh
```

### Method 2: Manual PyInstaller
```bash
# Install PyInstaller
pip install pyinstaller>=5.13.0

# Build using spec file
pyinstaller build/pypass.spec --clean --noconfirm

# Or build with command line
pyinstaller --onefile --windowed --name PyPass main.py
```

The executable will be created in the `dist/` directory.

### 📦 Publishing a Release on GitHub

1. **Create a clean build**
  - Activate your virtual environment (if any).
  - Install build deps: `pip install -r requirements.txt`.
  - Run the Windows build script: `build_exe.bat` (or `python -m PyInstaller build/pypass.spec --clean --noconfirm`).
  - Verify `dist/PyPass.exe` launches correctly on a clean machine or Windows sandbox.

2. **Prepare release artifacts**
  - Optionally compress the executable: `zip -j PyPass-windows-x64.zip dist/PyPass.exe`.
  - Generate a checksum for verification:
    ```bash
    certutil -hashfile dist/PyPass.exe SHA256
    ```
  - Capture release notes (new features, fixes, known issues) in Markdown.

3. **Publish the release on GitHub**
  - Push your latest changes and tag the commit, e.g. `git tag v1.0.0` followed by `git push --tags`.
  - Open *GitHub → Releases → Draft a new release*.
  - Select the tag, add a title (e.g. `PyPass v1.0.0`), and paste the release notes.
  - Attach `PyPass.exe` (and the optional `.zip` plus checksum file).
  - Mark the release as pre-release if you want early testers first.

4. **Post-release checklist**
  - Update the download link in this README if needed (point to `https://github.com/<user>/<repo>/releases/latest`).
  - Smoke-test the downloadable asset directly from GitHub to confirm SmartScreen/AV prompts are acceptable.
  - Optionally notarize/sign the executable for fewer security prompts (requires Authenticode certificate).
  - Encourage users to verify the checksum before allowing execution.

## 📱 How to Use

### 1. Personal Information
Fill in all required fields:
- **First Name**: Your first name
- **Last Name**: Your last name  
- **Date of Birth**: Format dd-mm-yyyy (e.g., 25-12-1990)
- **Current Date**: Auto-filled, but editable
- **Platform/Service**: Where you'll use this password (e.g., Gmail, Facebook)
- **Current City**: Your current city

### 2. Password Options
Customize your password:
- **Length**: 8-20 characters (slider)
- **Character Types**: Choose which to include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*...)
- **Exclude Ambiguous**: Remove confusing characters (0, O, l, I, 1)

### 3. Generate & Use
- Click **"Generate Password"** to create your password
- Use **"Show/Hide"** to toggle password visibility
- **"Copy to Clipboard"** copies password (auto-clears in 30 seconds)
- **"Save to File"** downloads as `[platform]_password.txt`
- **"Clear All"** resets all fields

### 4. Password Strength
The strength indicator shows:
- **Very Weak** (0-20%): Not secure
- **Weak** (20-40%): Basic security
- **Medium** (40-60%): Adequate security
- **Strong** (60-80%): Good security
- **Very Strong** (80-100%): Excellent security

## 🔐 Security Considerations

### Cryptographic Security
- Uses `secrets` module for cryptographically secure random number generation
- Implements Shannon entropy calculation for strength assessment
- Performs 1000 rounds of SHA-512 hashing for entropy mixing
- Prevents predictable patterns from personal information

### Privacy Protection
- **No Network Access**: Application works completely offline
- **No Data Persistence**: Information is cleared when application closes
- **Memory Clearing**: Sensitive data is not retained in memory longer than necessary
- **Clipboard Security**: Auto-clears clipboard after 30 seconds

### Best Practices
1. **Use Unique Information**: Provide accurate personal details for uniqueness
2. **Different Platforms**: Use different platform names for different passwords
3. **Regular Updates**: Regenerate passwords periodically for sensitive accounts
4. **Secure Storage**: If saving passwords to file, store files securely
5. **Delete Files**: Remove saved password files when no longer needed

### Threat Model
**Protects Against:**
- Rainbow table attacks (unique salt from personal info)
- Brute force attacks (high entropy)
- Pattern-based attacks (avoids obvious personal info patterns)

**Does NOT Protect Against:**
- Keyloggers or malware on compromised systems
- Physical access to saved password files
- Social engineering attacks
- Compromise of the platforms where passwords are used

## 📁 Project Structure

```
PyPass/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── build_exe.bat          # Windows build script
├── build_simple.sh        # Linux/macOS build script
├── README.md              # This documentation
├── src/
│   ├── gui.py             # Tkinter GUI implementation
│   └── password_generator.py  # Core password generation logic
├── build/
│   └── pypass.spec        # PyInstaller configuration
└── dist/                  # Built executables (created during build)
```

## 🛠️ Development

### Code Structure
- `main.py`: Entry point and path setup
- `src/gui.py`: Complete Tkinter GUI implementation
- `src/password_generator.py`: Core password generation and security logic

### Key Classes
- `SecurePasswordGenerator`: Main password generation engine
- `PersonalInfo`: Container for user personal data
- `PasswordOptions`: Configuration for password generation
- `PasswordGeneratorApp`: Main GUI application
- `ClipboardManager`: Handles clipboard operations with auto-clear

### Extending the Application
The modular design allows easy extension:
- Add new character sets in `PasswordOptions`
- Implement additional entropy sources in `SecurePasswordGenerator`
- Extend GUI with new features in `PasswordGeneratorApp`

## 🔍 Troubleshooting

### Common Issues

**"Personal information is incomplete"**
- Ensure all fields are filled in
- Check date format is dd-mm-yyyy

**"No character types selected"**  
- Select at least one character type checkbox

**Build fails with PyInstaller**
- Update to Python 3.11+
- Install latest PyInstaller: `pip install --upgrade pyinstaller`
- Try the simple build script instead of spec file

**Application won't start**
- Ensure all dependencies are available
- Check Python version compatibility
- Run from command line to see error messages

### Performance Notes
- First password generation may take slightly longer due to entropy pool creation
- Subsequent generations are faster
- Application memory usage is minimal (~10-20MB)

## 📝 License

This project is open source. Feel free to modify and distribute according to your needs.

## 🤝 Contributing

Contributions are welcome! Please ensure any changes maintain the security and offline-only nature of the application.

## ⚠️ Disclaimer

This software is provided as-is. While designed with security best practices, users should evaluate its suitability for their specific use cases. The developers are not responsible for any security breaches or password compromises.

## 📞 Support

For issues or questions:
1. Check this README for common solutions
2. Review the source code for understanding
3. Test with the development version before building

---

**Remember**: Keep your personal information secure and use strong, unique passwords for all your accounts!