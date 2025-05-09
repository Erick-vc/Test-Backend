from .base import *

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Cambiado a PostgreSQL
        'NAME': get_secret("DB_NAME"),              # Nombre de la base de datos
        'USER': get_secret('USER'),                 # Usuario de PostgreSQL
        'PASSWORD': get_secret('PASSWORD'),         # Contraseña de PostgreSQL
        'HOST': 'localhost',                        # Host de PostgreSQL
        'PORT': '5433',                             # Puerto de PostgreSQL
    }
}


STATIC_URL = 'static/'
