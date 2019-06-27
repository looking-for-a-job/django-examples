#!/usr/bin/env python
from django.utils.html import escape
from django.utils.safestring import mark_safe

"""
https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.safestring.mark_safe

mark_safe(s)
"""

text = "<script>alert('you are hacked')</script>"
print(escape(mark_safe(text)))

