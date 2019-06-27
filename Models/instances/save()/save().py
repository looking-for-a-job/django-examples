#!/usr/bin/env django
from app.models import MyModel

# https://docs.djangoproject.com/en/dev/ref/models/instances/#auto-incrementing-primary-keys

print("test")
instance = Blog(name='Cheddar Talk', tagline='Thoughts on cheese.')
instance.id     # Returns None, because b doesn't have an ID yet.
instance.save()
instance.id     # Returns the ID of your new object.
