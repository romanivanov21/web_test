import os, sys, os.path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_test.settings")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(BASE_DIR)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()