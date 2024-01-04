import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_submodules

path = Path(sys.argv[0]).resolve().parent

block_cipher = None

a = Analysis(
    [path / 'main.py'],
    pathex=[str(path)],
    binaries=[],
    datas=[(path / 'app/templates', 'app/templates'), (path / 'app/assets', 'app/assets')],
    hiddenimports=collect_submodules('flask') + collect_submodules('webview'),
    hookspath=[],
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
    name='nome_do_seu_executavel',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='nome_do_seu_executavel',
)
