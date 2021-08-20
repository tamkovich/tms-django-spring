from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class MusicBand(models.Model):
    name = models.CharField(max_length=30)
    album = models.ManyToManyField('Album', null=True, blank=True, related_name='albums')
    year_of_foundation = models.IntegerField(validators=[
                                    MinValueValidator(1900),
                                    MaxValueValidator(2021)], help_text='год основания от 1900 до 2021')
    music_style = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Album(models.Model):
    help_text = 'Заполните следующие графы'
    name = models.CharField(max_length=20)
    year = models.IntegerField(validators=[
                                    MinValueValidator(1900),
                                    MaxValueValidator(2021)], help_text='год выпуска от 1900 до 2021')
    tracks = models.ManyToManyField('Track', null=True, blank=True, related_name='tracks')

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=30)
    duration = models.DurationField(blank=True, help_text='указывается формат hh:mm:ss')

    def __str__(self):
        return self.name
