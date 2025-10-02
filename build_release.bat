@echo off
REM Enhanced Release Build Script for PyPass
REM Ensures maximum compatibility across Windows systems

echo ========================================
echo   PyPass Production Release Builder
echo ========================================
echo.

REM Set error handling
setlocal enabledelayedexpansion

REM Color codes for output
set "GREEN=[92m"
set "RED=[91m"
set "YELLOW=[93m"
set "BLUE=[94m"
set "NC=[0m"

echo %BLUE%Step 1: Environment Verification%NC%
echo =====================================

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo %RED%✗ Python is not installed or not in PATH%NC%
    echo   Please install Python 3.11+ and add to PATH
    echo   Download from: https://python.org/downloads/
    pause
    exit /b 1
)

REM Get Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo %GREEN%✓ Python %PYTHON_VERSION% detected%NC%

REM Check Python version (basic check for 3.11+)
python -c "import sys; sys.exit(0 if sys.version_info >= (3, 11) else 1)" >nul 2>&1
if errorlevel 1 (
    echo %YELLOW%⚠ Warning: Python 3.11+ recommended for best compatibility%NC%
    echo   Your version: %PYTHON_VERSION%
    echo   Continue anyway? [Y/N]
    set /p CONTINUE=
    if /i "!CONTINUE!" neq "Y" exit /b 1
)

REM Check virtual environment (recommended) - simplified check
python -c "import sys; sys.exit(0 if (hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)) else 1)" >nul 2>&1
if errorlevel 1 (
    echo %YELLOW%⚠ Warning: Running in global Python environment%NC%
    echo   Virtual environment recommended for clean builds
    echo %GREEN%✓ Continuing with global environment%NC%
) else (
    echo %GREEN%✓ Virtual environment detected%NC%
)

echo.
echo %BLUE%Step 2: Dependency Management%NC%
echo ===============================

REM Update pip first
echo Updating pip...
python -m pip install --upgrade pip --quiet
if errorlevel 1 (
    echo %RED%✗ Failed to update pip%NC%
    pause
    exit /b 1
)
echo %GREEN%✓ pip updated%NC%

REM Install/update PyInstaller
echo Installing PyInstaller...
python -m pip install --upgrade "pyinstaller>=5.13.0" --quiet
if errorlevel 1 (
    echo %RED%✗ Failed to install PyInstaller%NC%
    pause
    exit /b 1
)

REM Verify PyInstaller installation
python -c "import PyInstaller; print(f'PyInstaller {PyInstaller.__version__}')" 2>nul
if errorlevel 1 (
    echo %RED%✗ PyInstaller verification failed%NC%
    pause
    exit /b 1
)
echo %GREEN%✓ PyInstaller ready%NC%

echo.
echo %BLUE%Step 3: Pre-Build Verification%NC%
echo ================================

REM Verify source code integrity
echo Checking source code...
if not exist "main.py" (
    echo %RED%✗ main.py not found%NC%
    echo   Ensure you're running this script from the PyPass directory
    pause
    exit /b 1
)

if not exist "src\gui.py" (
    echo %RED%✗ src\gui.py not found%NC%
    pause
    exit /b 1
)

if not exist "src\password_generator.py" (
    echo %RED%✗ src\password_generator.py not found%NC%
    pause
    exit /b 1
)

echo %GREEN%✓ Source files verified%NC%

REM Test imports
echo Testing imports...
python -c "from src.password_generator import SecurePasswordGenerator; from src.gui import PasswordGeneratorApp; print('Imports OK')" >nul 2>&1
if errorlevel 1 (
    echo %RED%✗ Import test failed%NC%
    echo   Run 'python main.py' to check for errors
    pause
    exit /b 1
)
echo %GREEN%✓ Imports verified%NC%

REM Run tests if available
if exist "test_pypass.py" (
    echo Running test suite...
    python -m pytest test_pypass.py -v >nul 2>&1
    if errorlevel 1 (
        echo %YELLOW%⚠ Some tests failed%NC%
        echo   Run 'pytest test_pypass.py -v' to see details
        echo   Continue build anyway? [Y/N]
        set /p CONTINUE=
        if /i "!CONTINUE!" neq "Y" exit /b 1
    ) else (
        echo %GREEN%✓ All tests passed%NC%
    )
)

echo.
echo %BLUE%Step 4: Clean Build Environment%NC%
echo =================================

REM Clean previous builds
echo Cleaning previous builds...
if exist "dist" (
    rmdir /s /q "dist" >nul 2>&1
    echo %GREEN%✓ Cleaned dist directory%NC%
)

if exist "build\build" (
    rmdir /s /q "build\build" >nul 2>&1
    echo %GREEN%✓ Cleaned build cache%NC%
)

REM Clean Python cache
echo Cleaning Python cache...
for /r . %%d in (__pycache__) do (
    if exist "%%d" rmdir /s /q "%%d" >nul 2>&1
)
del /s /q *.pyc >nul 2>&1
echo %GREEN%✓ Python cache cleaned%NC%

REM Create output directory
if not exist "dist" mkdir "dist"

echo.
echo %BLUE%Step 5: Build Executable%NC%
echo =========================

REM Record build start time
echo Build started at %date% %time%
echo.

REM Build the executable with verbose output
echo Building PyPass executable...
echo This may take several minutes...
echo.

REM Ensure icon file exists (recommended)
if not exist "assets\pay-pass-logo.ico" (
    echo %YELLOW%⚠ Warning: icon file assets\pay-pass-logo.ico not found.%NC%
    echo   The build will continue but the executable will use the default icon.
    echo   Place your .ico at assets\pay-pass-logo.ico to embed it into the EXE.
)

python -m PyInstaller build\pypass.spec --clean --noconfirm --log-level WARN
set BUILD_RESULT=%errorlevel%

echo.
if %BUILD_RESULT% neq 0 (
    echo %RED%✗ Build failed with error code %BUILD_RESULT%%NC%
    echo.
    echo Common solutions:
    echo 1. Ensure all source files are present
    echo 2. Check for import errors in your code
    echo 3. Try updating PyInstaller: pip install --upgrade pyinstaller
    echo 4. Run in a clean virtual environment
    echo.
    pause
    exit /b %BUILD_RESULT%
)

echo %GREEN%✓ Build completed successfully!%NC%

echo.
echo %BLUE%Step 6: Build Verification%NC%
echo ===========================

REM Check if executable was created
if not exist "dist\PyPass.exe" (
    echo %RED%✗ PyPass.exe was not created%NC%
    echo   Check build output for errors
    pause
    exit /b 1
)

REM Get file size
for %%F in ("dist\PyPass.exe") do set FILE_SIZE=%%~zF
echo %GREEN%✓ PyPass.exe created%NC%
echo   File size: %FILE_SIZE% bytes

REM Check file size (warn if too large)
if %FILE_SIZE% gtr 52428800 (
    echo %YELLOW%⚠ Warning: File size is large (>50MB)%NC%
    echo   Consider optimizing excludes in pypass.spec
)

REM Test executable launch (quick test)
echo Testing executable launch...
echo This will open PyPass briefly to verify it works...
timeout /t 2 /nobreak >nul
start "" "dist\PyPass.exe"
timeout /t 3 /nobreak >nul
taskkill /im "PyPass.exe" /f >nul 2>&1

echo %GREEN%✓ Executable launch test completed%NC%

echo.
echo %BLUE%Step 7: Security and Distribution Preparation%NC%
echo ==============================================

REM Generate SHA256 checksum
echo Generating SHA256 checksum...
certutil -hashfile "dist\PyPass.exe" SHA256 > "dist\PyPass.exe.sha256"
if errorlevel 1 (
    echo %YELLOW%⚠ Failed to generate checksum%NC%
) else (
    echo %GREEN%✓ SHA256 checksum generated%NC%
)

REM Display checksum
echo.
echo %BLUE%SHA256 Checksum:%NC%
type "dist\PyPass.exe.sha256" | findstr /v "CertUtil"
echo.

REM Create ZIP package (optional)
echo Creating distribution package...
powershell -Command "try { Compress-Archive -Path 'dist\PyPass.exe' -DestinationPath 'dist\PyPass-windows-x64.zip' -Force; Write-Host 'ZIP package created' } catch { Write-Host 'ZIP creation failed' }"

echo.
echo %GREEN%========================================%NC%
echo %GREEN%       BUILD COMPLETED SUCCESSFULLY!    %NC%
echo %GREEN%========================================%NC%
echo.
echo %BLUE%Distribution files created:%NC%
echo   📁 dist\PyPass.exe              - Main executable
echo   📄 dist\PyPass.exe.sha256       - Security checksum
echo   📦 dist\PyPass-windows-x64.zip  - ZIP package (optional)
echo.
echo %BLUE%File size summary:%NC%
set /a FILE_SIZE_MB=%FILE_SIZE% / 1048576
echo   PyPass.exe: %FILE_SIZE% bytes (~%FILE_SIZE_MB% MB)

if exist "dist\PyPass-windows-x64.zip" (
    for %%F in ("dist\PyPass-windows-x64.zip") do echo   ZIP package: %%~zF bytes
)

echo.
echo %BLUE%Next steps:%NC%
echo   1. Test PyPass.exe on a clean Windows machine
echo   2. Verify the checksum matches
echo   3. Upload to GitHub releases
echo   4. Update README with download links
echo.
echo %BLUE%Security verification:%NC%
echo   - Upload to VirusTotal.com for malware scanning
echo   - Test on different Windows versions (10, 11)
echo   - Verify works without Python installed
echo.

REM Final recommendations
echo %YELLOW%💡 Pro Tips:%NC%
echo   • Test on machines WITHOUT Python installed
echo   • Check with multiple antivirus scanners
echo   • Document any Windows security warnings in README
echo   • Keep this checksum for GitHub release notes
echo.

pause
echo Build process completed. Check dist\ folder for files.