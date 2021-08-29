from django.db import models


class InputLetters(models.Model):
    letters1 = models.TextField()
    letters2 = models.TextField()
    letters3 = models.TextField()

