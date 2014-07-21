from __future__ import unicode_literals


__version__ = '0.1.1'


from tunigo.api import Tunigo
from tunigo.genre import Genre, SubGenre
from tunigo.playlist import Playlist
from tunigo.release import Release


__all__ = [
    'Genre',
    'Playlist',
    'Release',
    'SubGenre',
    'Tunigo',
]
