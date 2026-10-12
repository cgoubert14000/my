@echo off
title Reparation des images - fb_auto
cd /d "%~dp0"

set "PY=python"
python --version >nul 2>nul
if errorlevel 1 (
  py --version >nul 2>nul
  if errorlevel 1 (
    echo.
    echo   ERREUR : Python n'est pas installe, ou pas reconnu.
    echo.
    pause
    exit /b 1
  )
  set "PY=py"
)

if not exist "verifier_images.py" (
  echo.
  echo   ERREUR : verifier_images.py n'est pas dans CE dossier.
  echo   Il doit etre dans le dossier fb_auto, a cote de programmer.py.
  echo.
  echo   Dossier actuel : %CD%
  echo.
  pause
  exit /b 1
)

echo.
echo ============================================================
echo   REPARATION DES IMAGES
echo   deplace / renomme / convertit ce qui doit l'etre
echo   ne supprime AUCUNE image, n'ecrase AUCUN fichier
echo ============================================================

%PY% verifier_images.py --corriger

echo.
echo ------------------------------------------------------------
echo Si tout est en place, relance ton bot :
echo   python programmer.py "demain" --par-jour 5 --limite 20 --test
echo ------------------------------------------------------------
echo.
pause
