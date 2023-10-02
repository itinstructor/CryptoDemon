cd c:\temp

python -m nuitka ^
    --lto=no ^
    --mingw64 ^
    --onefile ^
    --windows-disable-console ^
    --enable-plugin=tk-inter ^
    --windows-icon-from-ico=encryption.ico ^
    --output-filename=crypto_demon.exe ^
    crypto_demon_3_AES_DES_CHACHA.py
pause