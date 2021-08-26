from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author_name = models.CharField(max_length=50)
    rating = models.IntegerField()
    topic = models.CharField(max_length=50, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='articles')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name='authors')


class Category(models.Model):
    name = models.CharField(max_length=50)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class ContactInfo(models.Model):
    author = models.OneToOneField('Author', on_delete=models.CASCADE, related_name='contact_info')
    phone = models.CharField(max_length=50, null=True, default=None)
    address = models.CharField(max_length=50, null=True, default=None)
