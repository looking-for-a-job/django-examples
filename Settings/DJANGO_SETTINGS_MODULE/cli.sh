#!/usr/bin/env bash

export DJANGO_SETTINGS_MODULE='mysite.settings'
python manage.py "$@"
django-admin "$@"

unset DJANGO_SETTINGS_MODULE
python manage.py "$@" --settings='mysite.settings'
django-admin "$@" --settings='mysite.settings'

