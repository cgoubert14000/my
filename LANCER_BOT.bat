@echo off
chcp 65001 >nul 2>&1
setlocal EnableExtensions
cd /d "%~dp0"
title Etat du planning Facebook - Madame Portugais

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

echo Verification des publications qui resteraient a envoyer...
".venv\Scripts\python.exe" -m facebook_bot send-schedule
set "SEND_RESULT=%ERRORLEVEL%"
echo.
echo Etat du planning enregistre :
".venv\Scripts\python.exe" -m facebook_bot schedule --days 31

echo.
if not "%SEND_RESULT%"=="0" (
    echo ATTENTION : l'envoi n'est pas entierement confirme.
    echo Lisez les messages ci-dessus et verifiez Meta Business Suite si demande.
) else (
    echo Facebook gere les heures de publication. Ce programme n'a pas besoin
    echo de rester ouvert : vous pouvez fermer cette fenetre et eteindre le PC.
)
echo.
pause
exit /b %SEND_RESULT%
