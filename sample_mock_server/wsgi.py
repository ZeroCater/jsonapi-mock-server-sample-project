import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sample_mock_server.settings")

application = get_wsgi_application()
