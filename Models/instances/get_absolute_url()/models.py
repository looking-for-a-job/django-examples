from django.db import models
from django.urls import reverse
from django.utils.text import slugify

"""
https://docs.djangoproject.com/en/dev/ref/models/instances/#get-absolute-url
"""

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])

    def __str__(self):
        return self.title

