#!/usr/bin/env python
from django.db.models.functions import Greatest
from .models import Comment

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#greatest

class Greatest(*expressions, **extra)

Accepts a list of at least two field names or expressions and returns the greatest value. Each argument must be of a similar type, so mixing text and numbers will result in a database error
"""

qs = Comment.objects.annotate(last_updated=Greatest('modified', 'blog__modified'))
for comment in qs.all():
    print(comment.last_updated)
