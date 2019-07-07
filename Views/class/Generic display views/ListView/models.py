from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    headline = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique = True, default='' )
    content = models.SlugField(max_length=200, unique=True)
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.headline, allow_unicode=True)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.headline
