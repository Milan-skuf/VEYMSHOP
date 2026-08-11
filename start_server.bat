@echo off
cd /d "%~dp0"

echo ==========================================
echo      VEYM PROJECT STARTUP SCRIPT
echo ==========================================

echo [1/4] Activating Virtual Environment...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo Venv not found! Creating one...
    python -m venv venv
    call venv\Scripts\activate.bat
)

echo [2/4] Installing Dependencies...
pip install -r requirements.txt

echo [3/4] Applying Database Migrations...
echo (This fixes the "no such table" errors)
python manage.py makemigrations
python manage.py migrate

echo [4/4] Creating Media Folders...
if not exist "media\products\gallery" mkdir "media\products\gallery"

echo ==========================================
echo      STARTING SERVER available at:
echo      http://127.0.0.1:8000
echo ==========================================
python manage.py runserver
pause
