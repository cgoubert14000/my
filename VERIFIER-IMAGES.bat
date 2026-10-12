@echo off
title Verification des images - fb_auto
cd /d "%~dp0"

rem --- trouver Python (python, sinon py) ---
set "PY=python"
python --version >nul 2>nul
if errorlevel 1 (
  py --version >nul 2>nul
  if errorlevel 1 (
    echo.
    echo   ERREUR : Python n'est pas installe, ou pas reconnu.
    echo.
    echo   Essaie en tapant "py" au lieu de "python" dans le terminal.
    echo.
    pause
    exit /b 1
  )
  set "PY=py"
)

if not exist "verifier_images.py" (
  echo.
  echo   ERREUR : verifier_images.py n'est pas dans CE dossier.
  echo.
  echo   Ce dossier doit etre le dossier fb_auto, celui qui contient
  echo   programmer.py, config.json et planning.txt.
  echo.
  echo   Dossier actuel : %CD%
  echo.
  pause
  exit /b 1
)

echo.
echo ============================================================
echo   VERIFICATION DES IMAGES DU BOT
echo   (ce script ne modifie rien, il regarde seulement)
echo ============================================================

%PY% verifier_images.py

echo.
echo ------------------------------------------------------------
echo Pour REPARER ce qui est signale : double-clique sur
echo   REPARER-IMAGES.bat
echo ------------------------------------------------------------
echo.
pause
