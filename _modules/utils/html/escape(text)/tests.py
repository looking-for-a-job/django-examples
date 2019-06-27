#!/usr/bin/env python
from django.utils.html import escape

"""
https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.html.escape

escape(text)
"""

text = "<script>alert('test')</script>"
print(escape(text))

