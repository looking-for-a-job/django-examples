#!/usr/bin/env python
import os

SECRET_KEY = os.getenv('SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER',None),
        'PASSWORD': os.getenv('DB_PASS',None),
        'HOST': os.getenv('DB_HOST',None),
        'PORT': os.getenv('DB_PORT',None)
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': os.getenv('USER'),
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 5432
    }
}
