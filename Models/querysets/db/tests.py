#!/usr/bin/env python
from .models import MyModel


qs = MyModel.objects.all()
print(q.db)
print(q.query)
