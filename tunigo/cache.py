from __future__ import unicode_literals

import time


class Cache(object):

    def __init__(self, cache_time):
        self._cache = {}
        self._cache_time = cache_time

    def _cache_valid(self, key):
        return (key in self._cache and
                self._cache[key]['access_time'] >
                time.time() - self._cache_time)

    def get(self, key):
        if self._cache_valid(key):
            return self._cache[key]['obj']
        else:
            return False

    def insert(self, key, obj):
        if self._cache_time:
            self._cache[key] = {
                'access_time': time.time(),
                'obj': obj
            }
