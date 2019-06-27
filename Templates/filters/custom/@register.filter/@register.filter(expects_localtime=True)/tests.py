#!/usr/bin/env python
from datetime import datetime
from django.template import Context, Template

out=Template("""
{% load my_filters %}
{{ value | businesshours }}""").render(Context({"value":datetime.now()}))
print(out)
