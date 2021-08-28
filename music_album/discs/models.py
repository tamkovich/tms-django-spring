from django.db import models

# Создать три модели MusicBand, Album и Track.
# Каждая музыкальная группа может иметь несколько альбомов.
# В каждом альбоме может содержаться несколько треков.
# Каждая группа имеет название, год основания, стиль музыки.
# Каждый Альбом содержит название, год выпуска.
# Каждый трек имеет длительность и название.


class MusicBand(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    artist = models.ForeignKey(MusicBand, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=50)
    duration = models.FloatField()
    music_album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


