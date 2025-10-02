# PyInstaller spec file for PyPass - ONEDIR MODE
# This creates a directory with PyPass.exe and supporting files
# Much less likely to trigger antivirus false positives

block_cipher = None

a = Analysis(
    ['../main.py'],
    pathex=['..'],
    binaries=[],
    datas=[],
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
        'tkinter.filedialog',
        'secrets',
        'hashlib',
        'datetime',
        'threading',
        'time',
        're'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Exclude unnecessary modules that won't break the app
        'matplotlib', 'numpy', 'pandas', 'PIL', 'cv2',
        'PyQt5', 'PyQt6', 'PySide2', 'PySide6',
        'jupyter', 'IPython', 'notebook',
        'scipy', 'sklearn', 'tensorflow', 'torch',
        'pytest', 'doctest',
        'pydoc', 'pdb', 'bdb', 'profile',
        'distutils', 'setuptools', 'pip'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,  # KEY CHANGE: Don't bundle everything into one file
    name='PyPass',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,  # Don't strip symbols (can trigger AV)
    upx=False,  # UPX disabled - reduces AV false positives
    console=False,  # Windowed application
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='..\\assets\\pay-pass-logo.ico',
    version_file='version_info.txt',
    uac_admin=False,  # Don't request admin privileges
    uac_uiaccess=False,  # Don't request UI access
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,  # Don't strip binaries
    upx=False,  # Never compress with UPX
    upx_exclude=[],
    name='PyPass',
)
