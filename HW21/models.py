from django.db import models


class Users(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    age = models.IntegerField()
    profession = models.CharField(max_length=50)
