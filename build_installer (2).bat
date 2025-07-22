@echo off
echo Pertinax Security Tool - Installer
python -m pip install --upgrade pip
pip install pyinstaller
pyinstaller --noconsole --onefile main_gui.py
pause