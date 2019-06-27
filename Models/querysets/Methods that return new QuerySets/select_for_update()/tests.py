#!/usr/bin/env python
from django.db import transaction
from .models import Entry

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#select-for-update

select_for_update(nowait=False, skip_locked=False, of=())
"""

entries = Entry.objects.select_for_update()
with transaction.atomic():
    for entry in entries:
        entry.save(title="new title")
