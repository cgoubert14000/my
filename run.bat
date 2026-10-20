@echo off
REM Vinted Sniper - installation + lancement en une commande (Windows).
REM Usage : run.bat --port 9000 --host 0.0.0.0
setlocal
cd /d "%~dp0"

if not exist .venv (
  echo Creation de l'environnement virtuel...
  where py >nul 2>nul
  if errorlevel 1 (
    python -m venv .venv
  ) else (
    py -3 -m venv .venv
  )
  if errorlevel 1 (
    echo Python 3.10+ est requis : https://www.python.org/downloads/
    pause
    exit /b 1
  )
)

call .venv\Scripts\activate.bat
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements.txt

python main.py %*
if errorlevel 1 pause
endlocal
