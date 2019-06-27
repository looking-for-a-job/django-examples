#!/usr/bin/env python
from django.template import Context, Template

out=Template("""
{% load my_filters %}
{{ "value" | filter_name }}""").render(Context())
print(out)
