@echo off
REM Build script for PyPass - Windows Executable
REM This script builds the application using PyInstaller

echo Building PyPass Windows Executable...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.11+ and try again
    pause
    exit /b 1
)

REM Check if PyInstaller is installed
python -c "import PyInstaller" >nul 2>&1
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    python -m pip install pyinstaller>=5.13.0
    if errorlevel 1 (
        echo Error: Failed to install PyInstaller
        pause
        exit /b 1
    )
)

REM Clean previous builds
echo Cleaning previous builds...
if exist "dist" rmdir /s /q "dist"
if exist "build\build" rmdir /s /q "build\build"

REM Create output directory
if not exist "dist" mkdir "dist"

REM Build the executable
echo Building executable...
python -m PyInstaller build\pypass.spec --clean --noconfirm

REM Check if build was successful
if exist "dist\PyPass.exe" (
    echo.
    echo ✓ Build successful!
    echo ✓ Executable created: dist\PyPass.exe
    echo.
    echo File size:
    for %%F in ("dist\PyPass.exe") do echo   %%~zF bytes
    echo.
    echo You can now distribute the PyPass.exe file.
    echo It contains all dependencies and runs offline.
) else (
    echo.
    echo ✗ Build failed!
    echo Check the error messages above for details.
)

echo.
pause