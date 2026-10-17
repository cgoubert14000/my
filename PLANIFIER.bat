@echo off
chcp 65001 >nul 2>&1
setlocal EnableExtensions
cd /d "%~dp0"
title Planifier sur Facebook - Madame Portugais

if not exist ".venv\Scripts\python.exe" (
    echo Le bot n'est pas encore configure.
    echo Double-cliquez d'abord sur CONFIGURER.bat.
    echo.
    pause
    exit /b 1
)

if not exist ".env" (
    echo Le fichier secret .env est absent.
    echo Double-cliquez d'abord sur CONFIGURER.bat.
    echo.
    pause
    exit /b 1
)

echo =====================================================
echo   Planifier les images - Madame Portugais
echo =====================================================
echo.
echo Le bot va lire horraire1.txt, horraire2.txt, horraire3.txt
echo et hashtags.txt, puis compter les images de images\to_post.
echo Il demandera la date et proposera :
echo   1 = horraire1.txt
echo   2 = horraire2.txt
echo   3 = horraire3.txt
echo   4 = les trois plannings avec repartition egale.
echo       45 images = 15 par planning, 48 = 16, 51 = 17.
echo.
echo Apres votre confirmation, tout le planning sera envoye immediatement
echo a Facebook. Vous n'aurez pas a laisser ce PC allume.
echo.
".venv\Scripts\python.exe" -m facebook_bot plan
set "BOT_RESULT=%ERRORLEVEL%"

echo.
if not "%BOT_RESULT%"=="0" (
    echo Le planning complet n'a pas ete confirme par Facebook.
    echo Lisez le message ci-dessus. S'il reste des envois en attente,
    echo utilisez ENVOYER_PLANNING.bat apres avoir corrige le probleme.
) else (
    echo SUCCES : Facebook possede le planning complet.
    echo Vous pouvez fermer cette fenetre et eteindre le PC.
)
echo.
pause
exit /b %BOT_RESULT%
