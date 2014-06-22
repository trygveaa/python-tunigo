from __future__ import unicode_literals


class Genre(object):

    def __init__(self, key=None, name=None):
        self._key = key
        self._name = name

    def key(self):
        return self._key

    def name(self):
        return self._name
