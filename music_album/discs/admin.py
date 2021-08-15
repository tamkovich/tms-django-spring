from django.contrib import admin

from discs.models import MusicBand, Track, Album


@admin.register(MusicBand)
class MusicBandAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'style')

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'music_album')
    list_filter = ('music_album',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'artist')
    list_filter = ('artist',)
