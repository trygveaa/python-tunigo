from __future__ import unicode_literals


from tunigo.api import Tunigo
from tunigo.genre import Genre, SubGenre
from tunigo.playlist import Playlist
from tunigo.release import Release


__version__ = '1.0.0'


__all__ = [
    'Genre',
    'Playlist',
    'Release',
    'SubGenre',
    'Tunigo',
]
