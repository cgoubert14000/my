@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
title Planifier les publications - Madame Portugais

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
echo   Planification des images - Madame Portugais
echo =====================================================
echo.
echo Le bot va lire horraire1.txt, horraire2.txt, horraire3.txt
echo et hashtags.txt, puis compter les images de images\to_post.
echo Il demandera la date et proposera :
echo   1 = horraire1.txt
echo   2 = horraire2.txt
echo   3 = horraire3.txt
echo   4 = les trois plannings avec repartition egale.
echo.
".venv\Scripts\python.exe" -m facebook_bot plan

if errorlevel 1 (
    echo.
    echo La planification n'a pas abouti. Lisez le message ci-dessus.
) else (
    echo.
    echo Vous pouvez maintenant lancer LANCER_BOT.bat.
)
echo.
pause
