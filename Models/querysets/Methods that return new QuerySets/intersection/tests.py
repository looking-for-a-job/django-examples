#!/usr/bin/env python
from .models import MyModel1, MyModel2, MyModel3

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#intersection

intersection(*other_qs)
"""

qs1=MyModel1.objects.all()
qs2=MyModel2.objects.all()
qs3=MyModel3.objects.all()
qs=qs1.intersection(qs2,qs3)
for r in qs:
    print(r.value)
