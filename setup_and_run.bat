@echo off
echo ==========================================
echo   SETUP DJANGO SITE WITH T-SHIRTS
echo ==========================================

cd /d "%~dp0"

echo.
echo [Step 1/5] Installing Dependencies...
pip install -r requirements.txt

echo.
echo [Step 2/5] Creating Database Tables...
python manage.py makemigrations catalog cart
python manage.py migrate

echo.
echo [Step 3/5] Adding T-Shirts to Database...
python add_tshirts.py

echo.
echo [Step 4/5] Creating Superuser (for admin panel)...
echo.
echo Username: admin
echo Password: admin123
echo.
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')"

echo.
echo [Step 5/5] Starting Server...
echo.
echo ==========================================
echo   SITE IS READY!
echo   - Main site: http://127.0.0.1:8000/
echo   - Admin: http://127.0.0.1:8000/admin/
echo   - Username: admin
echo   - Password: admin123
echo ==========================================
echo.
python manage.py runserver
