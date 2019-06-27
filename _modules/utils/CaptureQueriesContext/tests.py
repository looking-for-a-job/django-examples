#!/usr/bin/env python
from django.db import connection
from django.test.utils import CaptureQueriesContext
from .models import MyModel


with CaptureQueriesContext(connection) as queries:
    MyModel.objects.all()
    print("\n".join(map(lambda q:q['sql'],connection.queries)))

