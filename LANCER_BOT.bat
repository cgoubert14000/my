@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
title État du planning Facebook - Madame Portugais

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

echo Vérification des publications qui resteraient à envoyer...
".venv\Scripts\python.exe" -m facebook_bot send-schedule
set "SEND_RESULT=%ERRORLEVEL%"
echo.
echo État du planning enregistré :
".venv\Scripts\python.exe" -m facebook_bot schedule --days 31

echo.
if not "%SEND_RESULT%"=="0" (
    echo ATTENTION : l'envoi n'est pas entièrement confirmé.
    echo Lisez les messages ci-dessus et vérifiez Meta Business Suite si demandé.
) else (
    echo Facebook gère les heures de publication. Ce programme n'a pas besoin
    echo de rester ouvert : vous pouvez fermer cette fenêtre et éteindre le PC.
)
echo.
pause
exit /b %SEND_RESULT%
