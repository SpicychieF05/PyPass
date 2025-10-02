@echo off
REM Build PyPass as a directory (ONEDIR mode) for minimal AV detection
REM This creates a folder with PyPass.exe and supporting DLLs
REM Much safer for antivirus detection than onefile mode

echo ========================================
echo   PyPass Safe Build (ONEDIR Mode)
echo ========================================
echo.

REM Clean previous builds
echo Cleaning previous builds...
if exist "dist\PyPass" rmdir /s /q "dist\PyPass"
if exist "build\PyPass" rmdir /s /q "build\PyPass"

REM Build using onedir spec
echo Building PyPass (folder distribution)...
python -m PyInstaller build\pypass_onedir.spec --clean --noconfirm --log-level WARN

if errorlevel 1 (
    echo Build failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Build Complete!
echo ========================================
echo.
echo Output: dist\PyPass\
echo.
echo The PyPass folder contains:
echo   - PyPass.exe (main executable)
echo   - Supporting DLL files
echo   - Python runtime files
echo.
echo To distribute:
echo   1. Compress the entire "dist\PyPass" folder to PyPass-v1.0.0.zip
echo   2. Users extract and run PyPass.exe from the folder
echo.
echo This distribution method has significantly fewer AV false positives!
echo.
pause
