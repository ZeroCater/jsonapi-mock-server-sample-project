import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '9+vof!4so7tc!hs+503203$l89-9=lpdmuq9r9d331xhr7)3vc'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth'
]
MIDDLEWARE_CLASSES = []
ROOT_URLCONF = 'sample_mock_server.urls'
WSGI_APPLICATION = 'sample_mock_server.wsgi.application'
DATABASES = {}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
TEST_RUNNER = 'jsonapi_mock_server.base_tests.DatabaselessTestRunner'
MS_DEFAULT_LIST_LENGTH = 10
