<div align="center">
  <img src="https://res.cloudinary.com/dlxybta5a/image/upload/v1759338153/pay-pass-logo_qekpsy.png" alt="PyPass Logo" width="200">
</div>

# PyPass - Offline Password Generator

🔐 **For End Users**: Looking to use PyPass? Jump to the [User Manual](#-user-manual) for complete installation and usage instructions.

💻 **For Developers**: See [Building from Source](#️-building-from-source) and [Development](#️-development) sections.

## Table of Contents
- [Overview](#overview)
- [Key Features](#-key-features)
- [Security Features](#-security-features)
- [Requirements](#-requirements)
- [Quick Start](#-quick-start)
- [Building from Source](#️-building-from-source)
- [User Manual](#-user-manual)
  - [Installation Guide](#installation-guide)
  - [First Time Setup](#first-time-setup-detailed)
  - [Step-by-Step Usage](#step-by-step-usage)
  - [Advanced Features](#advanced-features)
  - [Security Best Practices](#security-best-practices-for-users)
- [Frequently Asked Questions (FAQ)](#-frequently-asked-questions-faq)
- [How to Use](#-how-to-use)
- [Security Considerations](#-security-considerations)
- [Project Structure](#-project-structure)
- [Development](#️-development)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [Support](#-support)

## Download

Get the latest Windows executable from the GitHub Releases page:
[Download PyPass.zip (v1.0.0)](https://github.com/SpicychieF05/PyPass/releases/download/v1.0.0/PyPass.zip)  
[Download PyPass.exe.sha256 (v1.0.0)](https://github.com/SpicychieF05/PyPass/releases/download/v1.0.0/PyPass.exe.sha256)

**Note:** To use this software, you must download both files.

## Release — v1.0.0

PyPass v1.0.0 is now available as a downloadable Windows executable. You can get the EXE from the Releases page and run it locally (no Python required).

- Release page: https://github.com/SpicychieF05/PyPass/releases/latest
- Direct download (exe): https://github.com/SpicychieF05/PyPass/releases/latest/download/PyPass.exe
- Checksum (SHA256): included on the release page and in the repository as `dist/PyPass.exe.sha256`

How to verify the download (Windows):

PowerShell:

```powershell
Get-FileHash .\PyPass.exe -Algorithm SHA256
```

CMD:

```cmd
certutil -hashfile .\PyPass.exe SHA256
```

Note: This executable is unsigned. Windows SmartScreen or antivirus software may show warnings for new unsigned binaries. If you see a SmartScreen warning, click "More info → Run anyway" after verifying the checksum.

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

### Privacy Guarantees
- **100% Offline Operation**: PyPass never connects to the internet - your information stays on your computer
- **No Data Storage**: Your personal information and passwords are never saved to files or databases
- **No Tracking**: PyPass doesn't collect, store, or transmit any personal data
- **Local Processing**: All password generation happens entirely on your device

### Cryptographic Security
- **Military-Grade Randomness**: Uses Python's `secrets` library for cryptographically secure random generation
- **Strong Encryption**: 1000 rounds of SHA-512 hashing ensures maximum entropy mixing
- **Unique Passwords**: Your personal information creates unique "salt" making your passwords different from everyone else's
- **No Predictable Patterns**: Advanced algorithms prevent obvious use of personal information in passwords

### Built-in Safety Features
- **Auto-Clear Clipboard**: Copied passwords are automatically removed from clipboard after 30 seconds
- **Memory Protection**: Sensitive data is cleared from computer memory when not needed
- **No Password Storage**: Generated passwords exist only while the application is running
- **Secure File Deletion**: Any saved password files can be safely deleted without traces

### What This Means for You
✅ **Your passwords are truly private** - nobody else can access them, not even the developers
✅ **Works anywhere** - no internet required, use on any computer safely  
✅ **Reproducible security** - same inputs always create the same secure password
✅ **No vendor lock-in** - your password generation method is completely independent

⚠️ **Important**: Keep your personal information secure and consistent - it's the key to regenerating your passwords

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

### For End Users (Easiest Method)

**Download and Run:**
1. **Get PyPass**: Go to [Latest Release](https://github.com/SpicychieF05/PyPass/releases/latest) and download `PyPass.exe`
2. **Save Safely**: Save to a permanent location like `C:\Programs\PyPass\` or your Desktop
3. **Launch**: Double-click `PyPass.exe` to start the application
4. **Handle Security Warning**: If Windows shows a warning, click "More info" → "Run anyway" (PyPass is safe)

**First Use:**
1. **Fill Personal Info**: Enter your name, birth date, current city, and the service you're creating a password for
2. **Choose Settings**: Select password length (12+ recommended) and character types
3. **Generate**: Click "Generate Password" to create your secure password
4. **Copy & Use**: Click "Copy to Clipboard" and paste into your account

**That's it!** PyPass will remember your settings for next time, and you can generate the same password again by using the same information.

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

# Install build/runtime dependencies (includes pytest for testing)
pip install -r requirements.txt

# Run the application directly
python main.py
```

### System Compatibility
- **Windows**: Windows 10 or later (primary platform)
- **Storage**: 50MB free space required
- **Internet**: Not required - works completely offline
- **Dependencies**: None - everything included in the .exe file

## 🏗️ Building from Source

### Using Build Scripts (Recommended)
```bash
# Ultra-safe build (5/72 AV detections - RECOMMENDED)
build_ultra_safe.bat

# Safe build (onedir mode)
build_safe.bat

# Standard single-file build
build_release.bat
```

See [BUILD_GUIDE.md](BUILD_GUIDE.md) for detailed build instructions and antivirus optimization.

### Manual PyInstaller
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
  - Run the build script: `build_ultra_safe.bat` (recommended) or `build_release.bat`.
  - Verify the executable launches correctly on a clean machine or Windows sandbox.
  - See [BUILD_GUIDE.md](BUILD_GUIDE.md) for antivirus optimization details.

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
  - Select the tag, add a title (e.g. `PyPass v1.0.0`), vand paste the release notes.
  - Attach `PyPass.exe` (and the optional `.zip` plus checksum file).
  - Mark the release as pre-release if you want early testers first.

4. **Post-release checklist**
  - Update the download link in this README if needed (point to `https://github.com/<user>/<repo>/releases/latest`).
  - Smoke-test the downloadable asset directly from GitHub to confirm SmartScreen/AV prompts are acceptable.
  - Optionally notarize/sign the executable for fewer security prompts (requires Authenticode certificate).
  - Encourage users to verify the checksum before allowing execution.

## 📖 User Manual

### Installation Guide

#### For End Users (Recommended)

**System Requirements:**
- Windows 10 or later (64-bit recommended)
- 50 MB free disk space
- No Python installation required

**Download and Installation:**

You may see two download options on the Releases page. Choose either one:

Option A — Safe folder version (recommended on some antivirus setups)
1. Download the ZIP package, typically named like `PyPass-<version>-Safe.zip`
2. Right‑click the ZIP → Extract All… (or use your unzip tool)
3. Open the extracted `PyPass` folder and run `PyPass.exe`
  - Important: Keep `PyPass.exe` inside the extracted folder; the nearby files are required

Option B — Portable single EXE
1. Download `PyPass.exe`
2. Place it in a convenient location (e.g., `C:\Programs\PyPass\` or Desktop)
3. Double‑click `PyPass.exe` to start

First launch on Windows
- Windows may show a SmartScreen warning for new/unsigned apps
- Click "More info" → "Run anyway" after you verify the file came from the official release
- You may see a Windows Defender popup stating: "Microsoft Defender SmartScreen prevented an unrecognized app from starting. Running this app might put your PC at risk." This is expected for new unsigned apps—tap "More info" and then "Run anyway" to continue
- PyPass will not harm your PC/Laptop. It is a fully offline application and does not access the internet

Recommendation (optional)
- For extra peace of mind, unzip/extract and run `PyPass.exe` after turning off your Wi‑Fi—PyPass works entirely offline

Create a desktop shortcut (optional)
- Right‑click `PyPass.exe` → Create shortcut
- Move the shortcut to your Desktop or Start Menu
- For the ZIP/folder version, create the shortcut to the `PyPass.exe` inside the extracted folder

Verify checksum (optional but recommended)
- If a `.sha256` file is provided, compare it with your download:
  - Open Command Prompt and run: `certutil -hashfile <path-to>\PyPass.exe SHA256`
  - Confirm the printed hash matches the contents of the `.sha256` file

**Antivirus Considerations:**
- Some antivirus software may flag new executables as suspicious
- PyPass is completely safe and contains no malware
- You can add `PyPass.exe` to your antivirus whitelist if needed
- The application works entirely offline with no network access

### First Time Setup (Detailed)

When you first launch PyPass, you'll see the main interface with several sections:

1. **Personal Information Section (Top)**
   - Fill in all required fields for secure password generation
   - Your information creates unique "salt" for each password
   - This information is never saved or transmitted anywhere

2. **Password Options Section (Middle)**
   - Configure your password requirements
   - Choose length and character types
   - Preview your settings before generating

3. **Generated Password Section (Bottom)**
   - View your generated password
   - Copy to clipboard or save to file
   - See password strength assessment

### Step-by-Step Usage

#### Creating Your First Password

**Step 1: Enter Personal Information**
```
┌─ Personal Information ────────────────────────┐
│ First Name: [John                    ]        │
│ Last Name:  [Smith                   ]        │
│ Birth Date: [25-12-1990              ]        │
│ Today's Date: [02-10-2025            ]        │
│ Platform:   [Gmail                   ]        │
│ City:       [New York                ]        │
└───────────────────────────────────────────────┘
```
- **First Name**: Your actual first name
- **Last Name**: Your actual last name  
- **Birth Date**: Format: DD-MM-YYYY (day-month-year)
- **Today's Date**: Auto-filled, but you can change it
- **Platform**: Where you'll use this password (Gmail, Facebook, etc.)
- **City**: Your current city name

**Step 2: Configure Password Options**
```
┌─ Password Options ────────────────────────────┐
│ Length: [12        ] (8-20 characters)        │
│ ☑ Uppercase Letters (A-Z)                    │
│ ☑ Lowercase Letters (a-z)                    │
│ ☑ Numbers (0-9)                              │
│ ☑ Special Characters (!@#$%...)              │
│ ☐ Exclude Ambiguous Characters               │
└───────────────────────────────────────────────┘
```
- **Length**: Use slider or type desired length (8-20 characters)
- **Character Types**: Check at least one box (all recommended)
- **Exclude Ambiguous**: Removes confusing characters like 0/O, 1/I/l

**Step 3: Generate and Use Your Password**
```
┌─ Generated Password ──────────────────────────┐
│ Password: [●●●●●●●●●●●●] [Show] [Hide]        │
│ Strength: ████████░░ Very Strong (85%)        │
│                                               │
│ [Generate Password] [Copy to Clipboard]       │
│ [Save to File]     [Clear All]                │
└───────────────────────────────────────────────┘
```
- Click **"Generate Password"** to create your password
- Use **"Show"** to reveal the password or **"Hide"** to conceal it
- **"Copy to Clipboard"** copies the password (auto-clears in 30 seconds)
- **"Save to File"** downloads as `[Platform]_password.txt`

#### Creating Passwords for Different Services

**For Multiple Accounts:**
1. Change the **Platform** field for each service:
   - "Gmail" → generates one unique password
   - "Facebook" → generates a completely different password
   - "Banking" → generates another unique password

2. Keep all other personal information the same
3. This ensures each service gets a unique password while being reproducible

**Example for Different Services:**
```
Gmail Account:     Platform = "Gmail"     → Password: K9@mX2pL4#vN
Facebook Account:  Platform = "Facebook"  → Password: R7$nY9qW8!eM
Banking Account:   Platform = "Banking"   → Password: T4&bN6kS2@xP
```

### Advanced Features

#### Password Strength Indicator
The strength bar shows password security level:
- **Very Weak (0-20%)**: Red - Too simple, easily cracked
- **Weak (20-40%)**: Orange - Basic security, vulnerable
- **Medium (40-60%)**: Yellow - Adequate for low-risk accounts
- **Strong (60-80%)**: Light Green - Good for most accounts
- **Very Strong (80-100%)**: Dark Green - Excellent for sensitive accounts

**Improving Password Strength:**
- Increase length (longer = stronger)
- Include all character types
- Avoid excluding character types unless necessary

#### Clipboard Auto-Clear Feature
For security, PyPass automatically clears your clipboard after 30 seconds:
- Copy your password when ready to use it
- Paste it into the password field immediately
- After 30 seconds, clipboard is automatically cleared
- This prevents accidental password exposure

#### File Export Feature
You can save passwords to files for secure storage:
- Click **"Save to File"** after generating a password
- Files are saved as `[Platform]_password.txt` (e.g., `Gmail_password.txt`)
- Choose your save location (Desktop, Documents, etc.)
- **Important**: Delete these files after use or store them securely

#### Regenerating the Same Password
To get the same password again:
1. Enter the **exact same** personal information
2. Use the **exact same** password options
3. The generated password will be identical every time
4. This allows you to "remember" passwords without storing them

### Security Best Practices for Users

#### Information Management
**✅ Do:**
- Use your real personal information for maximum uniqueness
- Keep your personal information consistent across password generations
- Use descriptive, specific platform names ("Gmail-Work", "Gmail-Personal")
- Clear the application completely when finished

**❌ Don't:**
- Use fake or random personal information
- Share your personal information used in the app
- Use the same platform name for different types of accounts
- Leave the application open and unattended

#### Password Usage
**✅ Do:**
- Generate unique passwords for every account/service
- Use the strongest settings your account allows
- Copy passwords directly from the app when logging in
- Delete any saved password files after transferring them

**❌ Don't:**
- Reuse the same platform name for multiple accounts
- Save passwords in plain text files long-term
- Share generated passwords
- Use the app on untrusted computers

#### Account Security
**✅ Do:**
- Enable two-factor authentication where available
- Use different platform names for work vs. personal accounts
- Regenerate passwords periodically for sensitive accounts
- Keep a secure backup of your personal information template

**❌ Don't:**
- Rely solely on password strength for critical accounts
- Use obvious platform names that others could guess
- Forget your personal information details
- Use the same password generation parameters for everything

## ❓ Frequently Asked Questions (FAQ)

### General Usage

**Q: How do I install PyPass?**
A: Simply download `PyPass.exe` from the GitHub releases page and double-click to run. No installation required. If Windows shows a security warning, click "More info" then "Run anyway" - PyPass is completely safe.

**Q: Do I need Python installed to use PyPass?**
A: No. The `.exe` file is completely self-contained and includes everything needed to run the application.

**Q: Why does Windows Defender flag PyPass as suspicious?**
A: This is normal for new or unsigned executables. PyPass is completely safe - it works entirely offline with no network access. You can safely click "Run anyway" or add it to your antivirus whitelist.

**Q: Can I use PyPass on Mac or Linux?**
A: The `.exe` file is Windows-only, but you can run PyPass from source code on Mac/Linux with Python installed. See the "Building from Source" section.

### Password Generation

**Q: How does PyPass create passwords without storing anything?**
A: PyPass uses your personal information combined with cryptographic algorithms to generate passwords. The same input always produces the same output, but your information is never stored anywhere.

**Q: If I lose my personal information, can I recover my passwords?**
A: No. PyPass doesn't store anything, so you must remember your personal information exactly as entered. We recommend keeping a secure note of your information template (without any generated passwords).

**Q: Why do I need to enter personal information?**
A: Your personal information acts as a unique "seed" that ensures your passwords are different from everyone else's, even if you use the same platform names and settings.

**Q: Can I generate the same password again later?**
A: Yes! As long as you enter the exact same personal information and use the same password settings, PyPass will generate the identical password every time.

**Q: What happens if I change my personal information?**
A: Changing any personal information will generate completely different passwords. Only change your information if you want entirely new passwords for all your accounts.

### Security Concerns

**Q: Is PyPass really secure?**
A: Yes. PyPass uses cryptographically secure random number generation, works completely offline, and never stores your information. However, no password manager is 100% foolproof - always use good security practices.

**Q: Does PyPass connect to the internet?**
A: No. PyPass works completely offline and never makes any network connections. Your personal information and passwords never leave your computer.

**Q: Where does PyPass store my information?**
A: Nowhere. PyPass doesn't save any personal information or generated passwords. Everything is cleared when you close the application.

**Q: How strong are PyPass passwords?**
A: PyPass generates cryptographically strong passwords with high entropy. A 12-character password with all character types enabled typically rates as "Very Strong" and would take millions of years to crack with current technology.

**Q: Should I use the same personal information for all my passwords?**
A: Yes. Using consistent personal information ensures you can regenerate the same passwords. Only change the "Platform" field to create different passwords for different services.

### Technical Issues

**Q: PyPass won't start - what should I do?**
A: Try these steps:
1. Right-click and "Run as administrator"
2. Temporarily disable antivirus and try again
3. Download a fresh copy of `PyPass.exe`
4. Check if you have sufficient disk space (50MB required)

**Q: I get "Personal information is incomplete" error**
A: Ensure all fields are filled in completely:
- First name and last name cannot be empty
- Date format must be exactly DD-MM-YYYY (e.g., 25-12-1990)
- Platform field cannot be empty
- City name cannot be empty

**Q: The clipboard copy function doesn't work**
A: Try these solutions:
1. Close other applications that might be using the clipboard
2. Try the "Show" button to verify the password generated correctly
3. Manually select and copy the password text
4. Restart PyPass if the issue persists

**Q: My password strength shows as "Weak" even with all options enabled**
A: Password strength depends mainly on length. Try:
- Increasing the password length to 12+ characters
- Ensuring all character types are enabled
- Making sure "Exclude Ambiguous Characters" is unchecked

### Best Practices

**Q: How often should I change my passwords?**
A: For sensitive accounts (banking, email), consider regenerating passwords every 3-6 months. For low-risk accounts, yearly changes are usually sufficient. Always change passwords immediately if you suspect a security breach.

**Q: Should I use PyPass for all my passwords?**
A: PyPass is excellent for most accounts, but consider:
- Use PyPass for most online accounts
- Use a traditional password manager for frequently changing passwords
- Some high-security systems may require different password policies
- Always enable two-factor authentication where available

**Q: Can I share my PyPass settings with family members?**
A: Each person should use their own personal information for maximum security. However, family members can use the same application and similar settings - just with their own personal details.

**Q: What should I do if I forget my personal information?**
A: Unfortunately, there's no way to recover your passwords without the exact personal information. We recommend:
- Writing down your personal information template (securely)
- Using information you're unlikely to forget
- Testing password regeneration before relying on it for important accounts

**Q: Is it safe to save passwords to files?**
A: The file save feature is provided for convenience, but saved files should be:
- Stored in a secure location
- Encrypted if stored long-term
- Deleted after transferring passwords to your accounts
- Never shared or stored in cloud services

### Troubleshooting

**Q: PyPass is running slowly**
A: First-time password generation may take 1-2 seconds due to cryptographic operations. This is normal. If consistently slow:
- Close other memory-intensive applications
- Restart PyPass
- Ensure you have adequate system resources

**Q: I can't remember what platform name I used**
A: Try common variations:
- "Gmail" vs "Google" vs "Gmail-Work"
- "Facebook" vs "FB" vs "Meta"
- Check for spaces, capitalization, or special characters
- Consider keeping a (secure) list of your platform naming conventions

**Q: The application crashed or froze**
A: Try these steps:
1. Close and restart PyPass
2. Run PyPass as administrator
3. Check if your antivirus is interfering
4. Download a fresh copy of the application
5. Report persistent issues on GitHub

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
├── main.py                    # Application entry point
├── version.py                 # Version information
├── requirements.txt           # Python dependencies (PyInstaller, pytest)
├── test_pypass.py            # Test suite
├── README.md                  # Main documentation
├── BUILD_GUIDE.md            # Build and distribution guide
├── ANTIVIRUS_README.md       # AV detection explanation
├── SECURITY.md               # Security considerations
├── AV_OPTIMIZATION_RESULTS.md # Latest AV test results
├── build_ultra_safe.bat      # Ultra-safe build script (RECOMMENDED)
├── build_safe.bat            # Safe onedir build script
├── build_release.bat         # Standard single-file build script
├── src/
│   ├── __init__.py           # Package initialization
│   ├── gui.py                # Tkinter GUI implementation
│   └── password_generator.py # Core password generation logic
├── assets/
│   └── pay-pass-logo.ico     # Application icon
├── build/
│   ├── pypass.spec           # PyInstaller spec (single-file)
│   ├── pypass_onedir.spec    # PyInstaller spec (directory mode)
│   └── version_info.txt      # Windows version metadata
├── RELEASE_NOTES/
│   └── v1.0.0.md            # Release notes
└── dist/                     # Built executables (created during build)
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
- Clear any existing build artifacts: `rm -rf build/pypass_onedir/ dist/`
- Use the provided build scripts: `build_ultra_safe.bat` (recommended), `build_safe.bat`, or `build_release.bat`
- Ensure virtual environment is activated if using one
- See [BUILD_GUIDE.md](BUILD_GUIDE.md) for detailed troubleshooting

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
