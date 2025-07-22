@echo off
echo ================================
echo  PERTINAX SECURITY TOOL - BUILD
echo ================================

echo.
echo [1] Installiere PyInstaller (falls notwendig)...
python -m pip install pyinstaller

echo.
echo [2] Starte EXE-Kompilierung...
pyinstaller --noconsole --onefile --name PertinaxSecurityTool main_gui.py

echo.
echo [3] Prüfe, ob EXE erfolgreich erzeugt wurde...

if exist dist\PertinaxSecurityTool.exe (
    echo [OK] EXE erfolgreich erstellt: dist\PertinaxSecurityTool.exe
) else (
    echo [FEHLER] EXE konnte nicht erzeugt werden.
)

echo.
pause