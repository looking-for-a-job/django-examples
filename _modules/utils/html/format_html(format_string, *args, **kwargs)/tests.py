#!/usr/bin/env python
from django.utils.html import format_html
from django.utils.safestring import mark_safe


"""
https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.html.format_html

https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.html.format_html
"""

some_html="<p>hello world</p>"
some_text = "<div>not allowed html block</div>"
some_other_text = "<script>alert('you are hacked')</script>"
string = format_html("{} <b>{}</b> {}",
    mark_safe(some_html),
    some_text,
    some_other_text
)
print(string)

