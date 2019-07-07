#!/usr/bin/env python
from .models import Article


article = Article(headline="article title",content="content")
article.save()

assert article.slug == "article title"
