from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.TextField(max_length=50, blank=True)
    age = models.IntegerField(blank=True)
    profession  = models.CharField(max_length=50, blank=True)

    def get_absolute_url(self):
        return f'/detailinfo/{self.id}'