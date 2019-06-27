#!/usr/bin/env python
from django.template import Context, Template

out=Template("""
{% load my_tags %}
<p>The time is {% current_time "%Y-%m-%d %I:%M %p" %}.</p>""").render(Context())
print(out)
