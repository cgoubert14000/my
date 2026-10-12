@echo off
title Associer les images - fb_auto
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

if not exist "associer_images.py" (
  echo.
  echo   ERREUR : associer_images.py n'est pas dans CE dossier.
  echo   Il doit etre dans le dossier fb_auto, a cote de programmer.py.
  echo.
  echo   Dossier actuel : %CD%
  echo.
  pause
  exit /b 1
)

echo.
echo ============================================================
echo   ASSOCIER TES IMAGES AU PLANNING
echo   prend toutes les images du dossier (quel que soit leur nom)
echo   et en fait des copies 01.jpg, 02.jpg, 03.jpg...
echo.
echo   Il ne SUPPRIME rien et ne renomme rien : il ajoute.
echo.
echo   Il va te demander de taper  oui  pour confirmer.
echo ============================================================

%PY% associer_images.py --preparer

echo.
echo ------------------------------------------------------------
echo ET MAINTENANT, regarde ce qui sera publie (rien n'est envoye) :
echo.
echo   %PY% programmer.py "demain" --planning planning_auto.txt --par-jour 5 --limite 20 --test
echo.
echo Si l'apercu te plait, relance la MEME commande sans --test.
echo ------------------------------------------------------------
echo.
pause
