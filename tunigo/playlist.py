from __future__ import unicode_literals


class Playlist(object):

    def __init__(self, uri=None, title=None):
        self._uri = uri
        self._title = title

    def uri(self):
        return self._uri

    def title(self):
        return self._title
