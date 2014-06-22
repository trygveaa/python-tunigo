from __future__ import unicode_literals


class Release(object):

    def __init__(self, uri=None, artist_name=None, album_name=None):
        self._uri = uri
        self._artist_name = artist_name
        self._album_name = album_name

    def uri(self):
        return self._uri

    def artist_name(self):
        return self._artist_name

    def album_name(self):
        return self._album_name
