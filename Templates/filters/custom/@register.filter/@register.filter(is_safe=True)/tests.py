#!/usr/bin/env python
from django.template import Context, Template

out=Template("""
{% load my_filters %}
{{ "<script>alert('danger!')</script>" | my_not_save_filter }}
{{ "<script>alert('danger!')</script>" | my_save_filter }}""").render(Context())
print(out)
