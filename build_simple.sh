#!/bin/bash
# Alternative build script for PyPass using command line PyInstaller
# Use this if the .spec file approach doesn't work

echo "Building PyPass Windows Executable..."

# Check Python
if ! command -v python &> /dev/null; then
    echo "Error: Python is not installed or not in PATH"
    exit 1
fi

# Check PyInstaller
if ! python -c "import PyInstaller" &> /dev/null; then
    echo "Installing PyInstaller..."
    python -m pip install pyinstaller>=5.13.0
fi

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf dist build/__pycache__ src/__pycache__

# Build with PyInstaller
echo "Building executable..."
python -m PyInstaller \
    --onefile \
    --windowed \
    --name PyPass \
    --clean \
    --noconfirm \
    --exclude-module matplotlib \
    --exclude-module numpy \
    --exclude-module pandas \
    --exclude-module PIL \
    --distpath dist \
    --workpath build/temp \
    main.py

# Check result
if [ -f "dist/PyPass.exe" ]; then
    echo "✓ Build successful!"
    echo "✓ Executable created: dist/PyPass.exe"
    ls -lh dist/PyPass.exe
else
    echo "✗ Build failed!"
    exit 1
fi