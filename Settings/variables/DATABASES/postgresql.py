#!/usr/bin/env python
from django.conf import settings
settings.configure()

settings.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',                      
        'USER': 'db_user',
        'PASSWORD': 'db_user_password',
        'HOST': ''
    }
}

from pgpass import items

item=items.pypi
settings.DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.postgresql_psycopg2',
        'NAME'      : item.database,                      
        'USER'      : item.user,
        'PASSWORD'  : item.password,
        'HOST'      : item.host
    }
}
