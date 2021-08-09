from django.db import models


class Article(models.Model):
    DoesNotExist = None
    title = models.CharField(max_length=50)
    content = models.TextField()
    author_name = models.CharField(max_length=50)
    rating = models.IntegerField()
    topic = models.CharField(max_length=50)
