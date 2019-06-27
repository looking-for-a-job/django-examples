#!/usr/bin/env python
from django.template import Context, Template

out=Template("""
{% load my_filters %}
{{ "value" | my_filter }}""").render(Context())
print(out)
