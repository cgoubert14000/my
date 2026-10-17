@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
title Bot Facebook - Madame Portugais

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

echo Demarrage du bot Madame Portugais...
echo Cette fenetre doit rester ouverte. Utilisez Ctrl+C pour arreter.
echo.
".venv\Scripts\python.exe" -m facebook_bot run

if errorlevel 1 (
    echo.
    echo Le bot s'est arrete avec une erreur. Lisez le message ci-dessus.
    pause
)
