@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
title Programmer sur Facebook - Madame Portugais

if not exist ".venv\Scripts\python.exe" (
    echo Le bot n'est pas encore configuré.
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
echo   Programmer les images - Madame Portugais
echo =====================================================
echo.
echo Le bot va lire horraire1.txt, horraire2.txt, horraire3.txt
echo et hashtags.txt, puis compter les images de images\to_post.
echo Il demandera la date et proposera :
echo   1 = horraire1.txt
echo   2 = horraire2.txt
echo   3 = horraire3.txt
echo   4 = les trois plannings avec répartition égale.
echo.
echo Après votre confirmation, tout le planning sera envoyé immédiatement
echo à Facebook. Vous n'aurez pas à laisser ce PC allumé.
echo.
".venv\Scripts\python.exe" -m facebook_bot plan

if errorlevel 1 (
    echo.
    echo Le planning complet n'a pas été confirmé par Facebook.
    echo Lisez le message ci-dessus. S'il reste des envois en attente,
    echo utilisez ENVOYER_PLANNING.bat après avoir corrigé le problème.
) else (
    echo.
    echo SUCCÈS : Facebook possède le planning complet.
    echo Vous pouvez fermer cette fenêtre et éteindre le PC.
)
echo.
pause
