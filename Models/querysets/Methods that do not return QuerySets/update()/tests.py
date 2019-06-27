#!/usr/bin/env python
from .models import Entry

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#update

update(**kwargs)
"""

Entry.objects.filter(pub_date__year=2010).update(comments_on=False)
