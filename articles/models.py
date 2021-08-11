from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    editions = models.ManyToManyField('Edition')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Article(models.Model):
    DoesNotExist = None
    title = models.CharField(max_length=50)
    content = models.TextField()
    author_name = models.CharField(max_length=50)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField()
    topic = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 null=True, blank=True, related_name='articles')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    author = models.OneToOneField('Author', on_delete=models.CASCADE, related_name='contact_info')
    phone = models.CharField(max_length=50, null=True, default=None)
    address = models.CharField(max_length=50, null=True, default=None)


class Edition(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
