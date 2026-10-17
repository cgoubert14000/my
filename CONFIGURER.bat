@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
title Configuration du bot Madame Portugais

echo =====================================================
echo   Configuration securisee du bot Madame Portugais
echo =====================================================
echo.
echo Le jeton sera lu automatiquement depuis le presse-papiers.
echo Il sera conserve uniquement dans le fichier local .env.
echo Il ne sera jamais affiche dans cette fenetre.
echo.

set "PYTHON_CMD="
where py >nul 2>&1
if not errorlevel 1 set "PYTHON_CMD=py"
if not defined PYTHON_CMD (
    where python >nul 2>&1
    if not errorlevel 1 set "PYTHON_CMD=python"
)

if not defined PYTHON_CMD (
    echo ERREUR : Python est introuvable.
    echo Installez Python 3.10 ou plus recent depuis https://www.python.org/downloads/
    echo Pendant l'installation, cochez "Add Python to PATH".
    goto :failure
)

if not exist ".venv\Scripts\python.exe" (
    echo Creation de l'environnement Python...
    %PYTHON_CMD% -m venv .venv
    if errorlevel 1 goto :failure
)

echo Installation ou mise a jour du bot...
".venv\Scripts\python.exe" -m pip install --disable-pip-version-check -e .
if errorlevel 1 goto :failure

echo.
echo Dans Meta, creez un NOUVEAU jeton pour Madame Portugais.
echo Cliquez sur la petite icone Copier a droite du jeton.
echo Ne collez pas le jeton ici : laissez-le simplement dans le presse-papiers.
echo.
pause
".venv\Scripts\python.exe" -m facebook_bot setup --clipboard
if errorlevel 1 goto :failure

echo.
echo Verification finale...
".venv\Scripts\python.exe" -m facebook_bot doctor
if errorlevel 1 goto :failure

echo.
echo =====================================================
echo   Configuration terminee avec succes.
echo   Utilisez maintenant LANCER_BOT.bat
echo =====================================================
echo.
pause
exit /b 0

:failure
echo.
echo La configuration n'a pas abouti. Lisez le message d'erreur ci-dessus.
echo Aucun jeton invalide n'a ete ajoute au programme.
echo.
pause
exit /b 1
