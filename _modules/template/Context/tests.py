#!/usr/bin/env python
from django.template import Context, Template

"""
https://docs.djangoproject.com/en/dev/ref/templates/api/#loading-a-template
"""

context = Context({"list": [1, 2, 3]})

template_string = """
{% for l in list %}
    {{ l }}
{% endfor %}
"""

out = Template(template_string).render(context)
print(out)
