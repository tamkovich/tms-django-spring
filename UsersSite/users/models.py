from django.db import models


class CustomUser(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    profession = models.CharField(max_length=50)