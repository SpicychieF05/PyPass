# PyPass - Offline Password Generator

## Table of Contents
- [Overview](#overview)
- [Key Features](#-key-features)
- [Security Features](#-security-features)
- [Requirements](#-requirements)
- [Quick Start](#-quick-start)
- [Building from Source](#️-building-from-source)
- [How to Use](#-how-to-use)
- [Security Considerations](#-security-considerations)
- [Project Structure](#-project-structure)
- [Development](#️-development)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [Support](#-support)

## Overview

PyPass is a secure, offline password generator desktop application built with Python and Tkinter. It generates cryptographically strong passwords by combining user personal information with secure random entropy, ensuring both uniqueness and security without requiring internet connectivity.

## ✨ Key Features

- 🔒 **100% Offline** - No internet required, complete privacy
- 🎯 **Personalized Security** - Uses your information to create unique passwords
- 🛡️ **Cryptographically Secure** - Built with Python's `secrets` library
- 📋 **Smart Clipboard** - Auto-clears after 30 seconds for security
- 💾 **Optional File Export** - Save passwords when needed
- 🎨 **User-Friendly GUI** - Simple, intuitive interface
- ⚡ **Lightweight** - Minimal system resources required
- 🔧 **Highly Customizable** - Control length, character types, and complexity

## 🔒 Security Features

- **100% Offline Operation**: No internet connectivity required or used
- **Cryptographically Secure**: Uses Python's `secrets` library for random generation
- **No Data Storage**: Personal information and passwords are never saved unless explicitly downloaded
- **Auto-Clear Clipboard**: Clipboard is automatically cleared after 30 seconds
- **Pattern Avoidance**: Prevents obvious use of personal information in generated passwords
- **Strong Entropy Mixing**: Combines personal data with 1000 rounds of cryptographic hashing

## 📋 Requirements

### System Requirements
- Windows 10 or later (primary platform)
- Linux/macOS (compatible)
- Python 3.11+ (for development) - **Tested with Python 3.13.5**
- 50MB free disk space

### For Development
- Python 3.11+ (recommended: Python 3.13.5)
- tkinter (included with Python standard installation)
- PyInstaller 6.16.0+ (for building executable)
- Virtual environment (recommended for development)

## 🚀 Quick Start

### Option 1: Using Pre-built Executable (Easiest)
1. Download `PyPass.exe` from the [latest release](https://github.com/SpicychieF05/PyPass/releases/latest)
2. Double-click to run the application directly
3. Fill in your personal information in the form
4. Customize password settings as needed
5. Click "Generate Password" to create your secure password

### Option 2: Running from Source (For Developers)
```bash
# Clone the repository
git clone https://github.com/SpicychieF05/PyPass.git
cd PyPass

# Optional: Create virtual environment (recommended)
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install build dependencies (only needed for building executable)
pip install -r requirements.txt

# Run the application directly
python main.py
```

### First Time Setup
1. **Launch PyPass** - Run the executable or `python main.py`
2. **Enter Personal Information** - Fill all required fields for password uniqueness
3. **Configure Options** - Choose password length and character types
4. **Generate** - Click "Generate Password" to create your secure password
5. **Copy & Use** - Copy to clipboard or save to file as needed

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
# Ensure you're in the project directory
cd PyPass

# Install PyInstaller (if not already installed)
pip install pyinstaller>=6.16.0

# Build using spec file (recommended - includes optimized settings)
pyinstaller build/pypass.spec --clean --noconfirm

# Alternative: Build with command line (basic configuration)
pyinstaller --onefile --windowed --name PyPass main.py

# The executable will be created in the dist/ directory
# Test the build:
./dist/PyPass.exe  # Windows
./dist/PyPass      # Linux/macOS
```

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
- Ensure all fields are filled in completely
- Check date format is exactly dd-mm-yyyy (e.g., 25-12-1990)
- Platform/Service field cannot be empty

**"No character types selected"**  
- Select at least one character type checkbox (uppercase, lowercase, numbers, or special characters)
- Default selection includes all character types

**Build fails with PyInstaller**
- Update to Python 3.11+ (recommended: 3.13.5)
- Install latest PyInstaller: `pip install --upgrade pyinstaller`
- Clear any existing build artifacts: `rm -rf build/ dist/`
- Try the build script instead of manual commands: `build_exe.bat` (Windows) or `./build_simple.sh` (Linux/macOS)
- Ensure virtual environment is activated if using one

**Application won't start**
- **From source**: Ensure all dependencies are available and Python version is compatible
- **Executable**: Try running from command prompt to see error messages
- **Windows**: Check if Windows Defender or antivirus is blocking the executable
- **Permissions**: Ensure you have write permissions in the application directory

**Memory or performance issues**
- Close other applications if memory is limited
- First password generation may take 1-2 seconds (normal)
- If application freezes, try restarting

**Clipboard not working**
- Ensure no other applications are accessing clipboard
- Try the "Show/Hide" button to verify password generation is working
- Copy function requires tkinter clipboard support

### Development Issues

**Import errors when running from source**
```bash
# Ensure you're in the correct directory
cd PyPass

# Check Python path includes current directory
python -c "import sys; print(sys.path)"

# Run with explicit module path
python -m main
```

**Virtual environment issues**
```bash
# Recreate virtual environment
rm -rf .venv
python -m venv .venv
# Activate and reinstall dependencies
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Performance Notes
- First password generation may take slightly longer due to entropy pool creation
- Subsequent generations are faster
- Application memory usage is minimal (~10-20MB)

## 📝 License

This project is open source. Feel free to modify and distribute according to your needs.

## 🤝 Contributing

Contributions are welcome! Please ensure any changes maintain the security and offline-only nature of the application.

### Development Setup
1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/PyPass.git`
3. Create a virtual environment: `python -m venv .venv`
4. Activate it and install dependencies: `pip install -r requirements.txt`
5. Make your changes and test thoroughly
6. Submit a pull request

### Code Guidelines
- Maintain compatibility with Python 3.11+
- Preserve security-first design principles
- Keep the application completely offline
- Follow existing code style and structure
- Add appropriate comments for complex logic
- Test all changes before submitting

### Security Considerations for Contributors
- Never add network connectivity or external dependencies
- Avoid storing sensitive data persistently
- Maintain cryptographic security standards
- Test against common attack vectors

## ⚠️ Disclaimer

This software is provided as-is. While designed with security best practices, users should evaluate its suitability for their specific use cases. The developers are not responsible for any security breaches or password compromises.

## 📞 Support

For issues or questions:

### Self-Help Resources
1. **Check this README** - Most common issues are covered in the troubleshooting section
2. **Review the source code** - The application is open source for transparency
3. **Test with development version** - Run from source to get detailed error messages

### Reporting Issues
1. **GitHub Issues** - [Create an issue](https://github.com/SpicychieF05/PyPass/issues) for bugs or feature requests
2. **Include Details** - Provide OS version, Python version, and error messages
3. **Security Issues** - For security vulnerabilities, please create a private issue

### Getting Help
- Check existing GitHub issues for similar problems
- Include your system information and exact error messages
- Describe steps to reproduce the issue
- Mention if you're using the executable or running from source

---

**Remember**: Keep your personal information secure and use strong, unique passwords for all your accounts!