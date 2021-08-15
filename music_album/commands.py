Album.objects.filter(artist__name='Rammstein')
Track.objects.filter(music_album__name='Reise Reise')
Track.objects.filter(music_album__artist__name='Rammstein')
Album.objects.filter(artist__age=1994)