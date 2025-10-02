@echo off
REM Ultra-safe build script for PyPass - Optimized to minimize AV false positives
REM This script builds PyPass with maximum AV-friendly settings

echo ========================================
echo PyPass Ultra-Safe Build Script
echo ========================================
echo.

REM Check if we're in a virtual environment
python -c "import sys; sys.exit(0 if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix) else 1)"
if %errorlevel% neq 0 (
    echo WARNING: Not running in a virtual environment
    echo It's recommended to use a venv for clean builds
    echo.
)

REM Check if icon file exists
if not exist "assets\pay-pass-logo.ico" (
    echo ERROR: Icon file not found at assets\pay-pass-logo.ico
    exit /b 1
)

echo Cleaning previous builds...
if exist "dist" rmdir /s /q dist
if exist "build\pypass_onedir" rmdir /s /q build\pypass_onedir
echo.

echo Installing/upgrading PyInstaller...
python -m pip install --upgrade pyinstaller
echo.

echo Building PyPass with ultra-safe settings...
echo - No UPX compression
echo - No stripping
echo - Separate directory mode
echo - No admin privileges
echo - Minimal excluded modules
echo.

python -m PyInstaller build\pypass_onedir.spec --clean --noconfirm --log-level=INFO

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo Build completed successfully!
    echo ========================================
    echo.
    echo Output location: dist\PyPass\
    echo Main executable: dist\PyPass\PyPass.exe
    echo.
    echo Next steps:
    echo 1. Test the executable locally
    echo 2. Generate SHA256 checksum
    echo 3. Upload to VirusTotal for verification
    echo 4. Package for distribution
    echo.
    
    REM Generate checksum
    echo Generating SHA256 checksum...
    certutil -hashfile "dist\PyPass\PyPass.exe" SHA256 > "dist\PyPass.exe.sha256.tmp"
    REM Extract just the hash line
    for /f "skip=1 tokens=1" %%i in (dist\PyPass.exe.sha256.tmp) do (
        echo %%i > dist\PyPass.exe.sha256
        goto :done
    )
    :done
    del dist\PyPass.exe.sha256.tmp
    echo SHA256: 
    type dist\PyPass.exe.sha256
    echo.
    
) else (
    echo.
    echo ========================================
    echo Build FAILED!
    echo ========================================
    echo Check the error messages above.
    exit /b 1
)

pause
