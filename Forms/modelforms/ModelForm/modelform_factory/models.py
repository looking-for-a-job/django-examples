from django.db import models

class Article(models.Model):
    headline = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
