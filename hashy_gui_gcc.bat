cd c:\temp

python -m nuitka ^
    --lto=no ^
    --mingw64 ^
    --onefile ^
    --windows-disable-console ^
    --enable-plugin=tk-inter ^
    --windows-icon-from-ico=encryption.ico ^
    --output-filename=hashy_gui.exe ^
    hashy_gui_2.py
pause