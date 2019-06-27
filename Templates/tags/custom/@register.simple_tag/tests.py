#!/usr/bin/env python
from django.template import Context, Template

out=Template("""
{% load my_tags %}
{% my_args_tag "value1" "value2" %}
{% my_context_tag %}""").render(Context({"arg1":"value1"}))
print(out)
