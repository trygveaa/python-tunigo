from __future__ import unicode_literals

import time

import requests

from tunigo.cache import Cache
from tunigo.genre import Genre, SubGenre
from tunigo.playlist import Playlist
from tunigo.release import Release


BASE_URL = 'https://api.tunigo.com/v3/space'


class Tunigo(object):

    def __init__(self, region='all', max_results=1000, cache_time=3600):
        self._region = region
        self._max_results = max_results
        self._cache = Cache(cache_time)

    def __repr__(self):
        return "Tunigo(region='{}', max_results={}, cache_time={})".format(
            self._region,
            self._max_results,
            self._cache._cache_time)

    def _get(self, key, options=''):
        uri = ('{}/{}?region={}&per_page={}'
               .format(BASE_URL, key, self._region, self._max_results))
        if options:
            uri = '{}&{}'.format(uri, options)
        result = requests.get(uri)
        if (result.status_code != 200 or
                result.headers['content-type'] != 'application/json'):
            return []
        return result.json()['items']

    def get_playlists(self, key, options='', cache_key=''):
        if not cache_key:
            cache_key = 'playlists-{}-{}'.format(key, options)
        cache_value = self._cache.get(cache_key)
        if cache_value:
            return cache_value
        else:
            playlists = []
            for item in self._get(key, options):
                playlists.append(Playlist(item_array=item['playlist']))
            self._cache.insert(cache_key, playlists)
            return playlists

    def get_featured_playlists(self):
        return self.get_playlists('featured-playlists',
                                  'dt={}'.format(time.strftime('%FT%H:01:00')),
                                  'featured-playlists')

    def get_top_lists(self):
        return self.get_playlists('toplists')

    def get_genres(self):
        cache_key = 'genres'
        cache_value = self._cache.get(cache_key)
        if cache_value:
            return cache_value
        else:
            genres = []
            for item in self._get('genres'):
                if item['genre']['templateName'] != 'toplists':
                    genres.append(Genre(item_array=item['genre']))
            self._cache.insert(cache_key, genres)
            return genres

    def get_genre_playlists(self, genre=None, sub_genre=None):
        if type(genre) == Genre:
            genre_key = genre.key
        else:
            genre_key = genre
        if type(sub_genre) == SubGenre:
            sub_genre_key = sub_genre.key
            if not genre_key:
                genre_key = sub_genre.main_genre.key
        else:
            sub_genre_key = sub_genre

        if sub_genre_key and sub_genre_key != 'all':
            options = 'filter={}'.format(sub_genre_key)
        else:
            options = ''
        return self.get_playlists(genre_key, options)

    def get_new_releases(self):
        cache_key = 'releases'
        cache_value = self._cache.get(cache_key)
        if cache_value:
            return cache_value
        else:
            releases = []
            for item in self._get('new-releases'):
                releases.append(Release(item_array=item['release']))
            self._cache.insert(cache_key, releases)
            return releases
