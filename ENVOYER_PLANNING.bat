@echo off
chcp 65001 >nul 2>&1
setlocal EnableExtensions
cd /d "%~dp0"
title Envoyer le planning restant - Madame Portugais

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
echo   Envoyer les publications encore en attente
echo =====================================================
echo.
echo Les publications deja acceptees par Facebook ne seront jamais renvoyees.
echo.
".venv\Scripts\python.exe" -m facebook_bot send-schedule
set "BOT_RESULT=%ERRORLEVEL%"

echo.
if not "%BOT_RESULT%"=="0" (
    echo L'envoi complet n'a pas abouti. Lisez le message ci-dessus.
    echo Si un envoi est indique comme etant a verifier, controlez Meta Business Suite.
    echo Le bot ne le renverra pas afin d'eviter un doublon.
) else (
    echo SUCCES : il ne reste aucune publication locale a envoyer.
    echo Vous pouvez fermer cette fenetre et eteindre le PC.
)
echo.
pause
exit /b %BOT_RESULT%
