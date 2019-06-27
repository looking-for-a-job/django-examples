#!/usr/bin/env python
from django.template import Context, Template

out=Template("""
{% load my_filters %}
{{ 42 | my_filter }}""").render(Context())
print(out)
