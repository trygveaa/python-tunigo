from __future__ import unicode_literals

import time

import mock

from tunigo.cache import Cache


class TestCache(object):

    def test_returns_none_for_unknown_key(self):
        cache = Cache(100)

        assert cache.get('key') is None

    def test_returns_value_for_known_key(self):
        cache = Cache(100)
        cache.insert('key', 'value')

        assert cache.get('key') == 'value'

    def test_returns_value_for_non_expired_key(self):
        cache = Cache(100)
        cache.insert('key', 'value')
        expire_time = time.time() + 99

        with mock.patch('time.time') as time_mock:
            time_mock.return_value = expire_time
            assert cache.get('key') == 'value'

    def test_returns_none_for_expired_key(self):
        cache = Cache(100)
        cache.insert('key', 'value')
        expire_time = time.time() + 100

        with mock.patch('time.time') as time_mock:
            time_mock.return_value = expire_time
            assert cache.get('key') is None
