#!/usr/bin/env python
from django.utils.html import conditional_escape, escape

"""
https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.html.escape

escape(text)
"""

text = "<script>alert('test')</script>"
print(conditional_escape(text))
assert conditional_escape(escape(text)) == escape(text)

