import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

try:
    call_command('migrate', interactive=False)
    from services.seed_data import seed_initial_data
    seed_initial_data()
except Exception as e:
    print(f"Startup initialization error: {e}")

app = application
