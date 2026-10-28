@echo off
cd /d "%~dp0"
echo Construction de vinted-sniper.exe (2 a 5 minutes)...
where py >nul 2>nul && (set "PY=py -3") || (set "PY=python")
%PY% -m pip install --upgrade pip
%PY% -m pip install -r requirements.txt pyinstaller
if errorlevel 1 goto :erreur
%PY% tools\build_executable.py
if errorlevel 1 goto :erreur
echo.
echo Termine : le fichier dist\vinted-sniper.exe est pret.
pause
exit /b 0
:erreur
echo.
echo Echec de la construction. Verifiez votre connexion Internet.
pause
exit /b 1
