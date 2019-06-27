#!/usr/bin/env python
from .models import MyModel

for f in MyModel._meta.fields:
    print(f.name, f, f.__class__)
