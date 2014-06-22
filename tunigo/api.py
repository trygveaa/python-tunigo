from __future__ import unicode_literals

import time

import requests

from tunigo.genre import Genre
from tunigo.playlist import Playlist
from tunigo.release import Release


BASE_URL = 'https://api.tunigo.com/v3/space'


class Tunigo(object):

    def __init__(self, region='all', max_results='1000'):
        self._region = region
        self._max_results = max_results

    def _get(self, key, options=''):
        uri = ('{}/{}?region={}&per_page={}'
               .format(BASE_URL, key, self._region, self._max_results))
        if options:
            uri = '{}&{}'.format(uri, options)
        return requests.get(uri).json()['items']

    def get_playlists(self, key, options=''):
        playlists = []
        for item in self._get(key, options):
            playlists.append(Playlist(item_array=item['playlist']))
        return playlists

    def get_featured_playlists(self):
        return self.get_playlists('featured-playlists',
                                  'dt={}'.format(time.strftime('%FT%H:01:00')))

    def get_top_lists(self):
        return self.get_playlists('toplists')

    def get_genres(self):
        genres = []
        for item in self._get('genres'):
            if item['genre']['templateName'] != 'toplists':
                genres.append(Genre(item_array=item['genre']))
        return genres

    def get_new_releases(self):
        releases = []
        for item in self._get('new-releases'):
            releases.append(Release(item_array=item['release']))
        return releases
