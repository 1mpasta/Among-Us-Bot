# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['src\\main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ("Tesseract-OCR/", "Tesseract-OCR/"),
        ("media/Chart_Course/mask.png", "media/Chart_Course/"),
        ("media/Divert_Power/slider.png", "media/Divert_Power/"),
        ("media/Unlock_Manifolds/1.png", "media/Unlock_Manifolds/"),
        ("media/Unlock_Manifolds/2.png", "media/Unlock_Manifolds/"),
        ("media/Unlock_Manifolds/3.png", "media/Unlock_Manifolds/"),
        ("media/Unlock_Manifolds/4.png", "media/Unlock_Manifolds/"),
        ("media/Unlock_Manifolds/5.png", "media/Unlock_Manifolds/"),
        ("media/Unlock_Manifolds/6.png", "media/Unlock_Manifolds/"),
        ("media/Unlock_Manifolds/7.png", "media/Unlock_Manifolds/"),
        ("media/Unlock_Manifolds/8.png", "media/Unlock_Manifolds/"),
        ("media/Unlock_Manifolds/9.png", "media/Unlock_Manifolds/"),
        ("media/Unlock_Manifolds/10.png", "media/Unlock_Manifolds/")
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
