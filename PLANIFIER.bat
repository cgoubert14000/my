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
echo Le bot va compter les images de images\to_post,
echo demander la date, puis les repartir entre :
echo   Horaire 1 : 07:30, 08:30, 09:30...
echo   Horaire 2 : 07:15, 08:15, 09:15...
echo   Horaire 3 : 07:45, 08:45, 09:45...
echo Maximum : 17 publications par horaire, 51 par date.
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
