@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"
title Vinted Sniper 1.2.0

if exist "vinted-sniper.exe" (
  echo.
  echo   Vinted Sniper demarre...
  echo   Dashboard : http://127.0.0.1:8000
  echo   Pour arreter : fermez cette fenetre ou Ctrl+C
  echo.
  "vinted-sniper.exe"
  goto :fin
)

echo Executable absent : demarrage via Python.
set "PY="
where py >nul 2>nul && set "PY=py -3"
if not defined PY (
  where python >nul 2>nul && set "PY=python"
)
if not defined PY goto :nopython

if not exist ".venv\Scripts\python.exe" (
  echo Premiere utilisation : installation ^(1 a 2 minutes^)...
  %PY% -m venv .venv || goto :erreur
  ".venv\Scripts\python.exe" -m pip install --upgrade pip
  ".venv\Scripts\python.exe" -m pip install -r requirements.txt || goto :erreur
)
".venv\Scripts\python.exe" main.py
goto :fin

:nopython
echo.
echo Python 3.10+ est requis : https://www.python.org/downloads/
echo Cochez "Add python.exe to PATH" pendant l'installation, puis relancez.
echo.
pause
exit /b 1

:erreur
echo.
echo L'installation a echoue. Verifiez votre connexion Internet puis relancez.
echo.
pause
exit /b 1

:fin
echo.
echo Vinted Sniper arrete.
pause
