@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
title Envoyer le planning restant - Madame Portugais

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
echo   Envoyer les publications encore en attente
echo =====================================================
echo.
echo Les publications déjà acceptées par Facebook ne seront jamais renvoyées.
echo.
".venv\Scripts\python.exe" -m facebook_bot send-schedule

if errorlevel 1 (
    echo.
    echo L'envoi complet n'a pas abouti. Lisez le message ci-dessus.
    echo Si un envoi est « à vérifier », contrôlez Meta Business Suite :
    echo le bot ne le renverra pas afin d'éviter un doublon.
) else (
    echo.
    echo SUCCÈS : il ne reste aucune publication locale à envoyer.
    echo Vous pouvez fermer cette fenêtre et éteindre le PC.
)
echo.
pause
