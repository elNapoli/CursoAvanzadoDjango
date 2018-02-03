from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'sistema_discusiones',
        'USER':'postgres',
        'PASSWORD':'123123',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

STATIC_URL = '/static/'