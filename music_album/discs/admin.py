from django.contrib import admin

from discs.models import MusicBand, Track, Album


@admin.register(MusicBand)
class MusicBandAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'style')

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'music_album')  # чтобы в админке сразу таблицой показывало 'duration', 'music_album'
    #fields = ['name', ('duration', 'music_album')]  # те что в кортеже при создании нового трека в одминке будут горизонтально
    list_filter = ('music_album', 'music_album__artist__name')
    fieldsets = (                                    #   не получается вместе с fields
        (None, {
            'fields': ('name',)
        }),
        ('Detailed information', {
            'fields': ('duration', 'music_album')
        }),
    )

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'artist')
    list_filter = ('artist', 'artist__age')
