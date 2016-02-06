from __future__ import unicode_literals

import time

import responses

from tunigo.api import BASE_QUERY, BASE_URL, Tunigo
from tunigo.genre import Genre, SubGenre
from tunigo.playlist import Playlist
from tunigo.release import Release


class TestApi(object):

    @responses.activate
    def test_returns_items(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(
            responses.GET,
            BASE_URL + '/key',
            content_type='application/json',
            body='{"items": [{"test": 1}]}')

        result = tunigo._get('key')

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/key?{}&per_page={}'.format(
                BASE_URL, BASE_QUERY, max_results))

        assert len(result) == 1
        assert result[0]['test'] == 1

    @responses.activate
    def test_returns_empty_array_if_status_not_200(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(
            responses.GET,
            BASE_URL + '/key',
            status=404,
            content_type='application/json',
            body='{"items": [{"test": 1}]}')

        result = tunigo._get('key')

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/key?{}&per_page={}'.format(
                BASE_URL, BASE_QUERY, max_results))

        assert result == []

    @responses.activate
    def test_returns_empty_array_if_content_type_not_application_json(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(
            responses.GET,
            BASE_URL + '/key',
            body='{"items": [{"test": 1}]}')

        result = tunigo._get('key')

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/key?{}&per_page={}'.format(
                BASE_URL, BASE_QUERY, max_results))

        assert result == []

    @responses.activate
    def test_set_given_region_query_option(self):
        max_results = 100
        tunigo = Tunigo(region='no', max_results=max_results)

        responses.add(responses.GET, BASE_URL + '/key')

        tunigo._get('key')

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/key?{}&per_page={}&region=no'.format(
                BASE_URL, BASE_QUERY, max_results))

    @responses.activate
    def test_set_given_query_options(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(responses.GET, BASE_URL + '/key')

        tunigo._get('key', 'test=value')

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/key?{}&per_page={}&test=value'.format(
                BASE_URL, BASE_QUERY, max_results))

    @responses.activate
    def test_returns_playlists(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(
            responses.GET,
            BASE_URL + '/key',
            content_type='application/json',
            body="""
                {
                  "items": [
                    {
                      "playlist": {
                        "title": "Title 0",
                        "description": "Description 0",
                        "image": "Image 0",
                        "uri": "uri:0",
                        "numSubscribers": 0
                      }
                    },
                    {
                      "playlist": {
                        "title": "Title 1",
                        "description": "Description 1",
                        "image": "Image 1",
                        "uri": "uri:1",
                        "numSubscribers": 1
                      }
                    }
                  ]
                }""")

        playlists = tunigo.get_playlists('key')

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/key?{}&per_page={}'.format(
                BASE_URL, BASE_QUERY, max_results))

        assert len(playlists) == 2

        assert isinstance(playlists[0], Playlist)
        assert playlists[0].title == 'Title 0'
        assert playlists[0].description == 'Description 0'
        assert playlists[0].image == 'Image 0'
        assert playlists[0].uri == 'uri:0'
        assert playlists[0].num_subscribers == 0

        assert isinstance(playlists[1], Playlist)
        assert playlists[1].title == 'Title 1'
        assert playlists[1].description == 'Description 1'
        assert playlists[1].image == 'Image 1'
        assert playlists[1].uri == 'uri:1'
        assert playlists[1].num_subscribers == 1

    @responses.activate
    def test_sets_playlists_query_options(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(responses.GET, BASE_URL + '/key')

        tunigo.get_playlists('key', 'test=value')

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/key?{}&per_page={}&test=value'.format(
                BASE_URL, BASE_QUERY, max_results))

    @responses.activate
    def test_caches_playlists_result(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(responses.GET, BASE_URL + '/key')

        tunigo.get_playlists('key')
        tunigo.get_playlists('key')

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/key?{}&per_page={}'.format(
                BASE_URL, BASE_QUERY, max_results))

    @responses.activate
    def test_featured_playlist_calls_uri(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(responses.GET, BASE_URL + '/featured-playlists')

        tunigo.get_featured_playlists()

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/featured-playlists?{}&per_page={}&dt={}'.format(
                BASE_URL,
                BASE_QUERY,
                max_results,
                time.strftime('%FT%H:01:00')))

    @responses.activate
    def test_top_lists_calls_uri(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(responses.GET, BASE_URL + '/toplists')

        tunigo.get_top_lists()

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/toplists?{}&per_page={}'.format(
                BASE_URL, BASE_QUERY, max_results))

    @responses.activate
    def test_returns_genres(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(
            responses.GET,
            BASE_URL + '/genres',
            content_type='application/json',
            body="""
                {
                  "items": [
                    {
                      "genre": {
                        "name": "Genre 0",
                        "id": "Id 0",
                        "type": "Type 0",
                        "templateName": "Template name 0",
                        "iconImageUrl": "Icon image url 0",
                        "iconUrl": "Icon url 0",
                        "moodImageUrl": "Mood image url 0",
                        "headerImageUrl": "Header image url 0",
                        "subGenres": [
                          {
                            "name": "Genre 0, subgenre 0",
                            "key": "Key 0, 0"
                          },
                          {
                            "name": "Genre 0, subgenre 1",
                            "key": "Key 0, 1"
                          }
                        ]
                      }
                    },
                    {
                      "genre": {
                        "name": "Genre 1",
                        "id": "Id 1",
                        "type": "Type 1",
                        "templateName": "Template name 1",
                        "iconImageUrl": "Icon image url 1",
                        "iconUrl": "Icon url 1",
                        "moodImageUrl": "Mood image url 1",
                        "headerImageUrl": "Header image url 1",
                        "subGenres": [
                          {
                            "name": "Genre 1, subgenre 0",
                            "key": "Key 1, 0"
                          },
                          {
                            "name": "Genre 1, subgenre 1",
                            "key": "Key 1, 1"
                          }
                        ]
                      }
                    }
                  ]
                }""")

        genres = tunigo.get_genres()

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/genres?{}&per_page={}'.format(
                BASE_URL, BASE_QUERY, max_results))

        assert len(genres) == 2

        assert isinstance(genres[0], Genre)
        assert genres[0].name == 'Genre 0'
        assert genres[0].id == 'Id 0'
        assert genres[0].type == 'Type 0'
        assert genres[0].template_name == 'Template name 0'
        assert genres[0].icon_image_url == 'Icon image url 0'
        assert genres[0].icon_url == 'Icon url 0'
        assert genres[0].mood_image_url == 'Mood image url 0'
        assert genres[0].header_image_url == 'Header image url 0'

        assert len(genres[0].sub_genres) == 2
        assert isinstance(genres[0].sub_genres[0], SubGenre)
        assert genres[0].sub_genres[0].name == 'Genre 0, subgenre 0'
        assert genres[0].sub_genres[0].key == 'Key 0, 0'
        assert isinstance(genres[0].sub_genres[1], SubGenre)
        assert genres[0].sub_genres[1].name == 'Genre 0, subgenre 1'
        assert genres[0].sub_genres[1].key == 'Key 0, 1'

        assert isinstance(genres[0], Genre)
        assert genres[1].name == 'Genre 1'
        assert genres[1].id == 'Id 1'
        assert genres[1].type == 'Type 1'
        assert genres[1].template_name == 'Template name 1'
        assert genres[1].icon_image_url == 'Icon image url 1'
        assert genres[1].icon_url == 'Icon url 1'
        assert genres[1].mood_image_url == 'Mood image url 1'
        assert genres[1].header_image_url == 'Header image url 1'

        assert len(genres[1].sub_genres) == 2
        assert isinstance(genres[1].sub_genres[0], SubGenre)
        assert genres[1].sub_genres[0].name == 'Genre 1, subgenre 0'
        assert genres[1].sub_genres[0].key == 'Key 1, 0'
        assert isinstance(genres[1].sub_genres[1], SubGenre)
        assert genres[1].sub_genres[1].name == 'Genre 1, subgenre 1'
        assert genres[1].sub_genres[1].key == 'Key 1, 1'

    @responses.activate
    def test_caches_genres_result(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(responses.GET, BASE_URL + '/genres')

        tunigo.get_genres()
        tunigo.get_genres()

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/genres?{}&per_page={}'.format(
                BASE_URL, BASE_QUERY, max_results))

    @responses.activate
    def test_genre_playlists_with_genre_string_calls_uri(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(responses.GET, BASE_URL + '/genre')

        tunigo.get_genre_playlists('genre')

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/genre?{}&per_page={}'.format(
                BASE_URL, BASE_QUERY, max_results))

    @responses.activate
    def test_genre_playlists_with_genre_and_subgenre_string_calls_uri(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(responses.GET, BASE_URL + '/genre')

        tunigo.get_genre_playlists('genre', 'subgenre')

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/genre?{}&per_page={}&filter=subgenre'.format(
                BASE_URL, BASE_QUERY, max_results))

    @responses.activate
    def test_genre_playlists_with_genre_instance_calls_uri(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(responses.GET, BASE_URL + '/genre')

        tunigo.get_genre_playlists(Genre(template_name='genre'))

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/genre?{}&per_page={}'.format(
                BASE_URL, BASE_QUERY, max_results))

    @responses.activate
    def test_genre_playlists_with_genre_and_subgenre_instance_calls_uri(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(responses.GET, BASE_URL + '/genre')

        tunigo.get_genre_playlists(
            Genre(template_name='genre'),
            SubGenre(key='subgenre'))

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/genre?{}&per_page={}&filter=subgenre'.format(
                BASE_URL, BASE_QUERY, max_results))

    @responses.activate
    def test_genre_playlists_with_only_subgenre_instance_calls_uri(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(responses.GET, BASE_URL + '/genre')

        tunigo.get_genre_playlists(
            sub_genre=SubGenre(key='subgenre', main_genre='genre'))

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/genre?{}&per_page={}&filter=subgenre'.format(
                BASE_URL, BASE_QUERY, max_results))

    @responses.activate
    def test_returns_releases(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(
            responses.GET,
            BASE_URL + '/new-releases',
            content_type='application/json',
            body="""
                {
                  "items": [
                    {
                      "release": {
                        "albumName": "Album 0",
                        "uri": "uri:0",
                        "artistName": "Artist 0",
                        "image": "Image 0",
                        "artistUri": "artist:uri:0"
                      }
                    },
                    {
                      "release": {
                        "albumName": "Album 1",
                        "uri": "uri:1",
                        "artistName": "Artist 1",
                        "image": "Image 1",
                        "artistUri": "artist:uri:1"
                      }
                    }
                  ]
                }""")

        releases = tunigo.get_new_releases()

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/new-releases?{}&per_page={}'.format(
                BASE_URL, BASE_QUERY, max_results))

        assert len(releases) == 2

        assert isinstance(releases[0], Release)
        assert releases[0].album_name == 'Album 0'
        assert releases[0].uri == 'uri:0'
        assert releases[0].artist_name == 'Artist 0'
        assert releases[0].image == 'Image 0'
        assert releases[0].artist_uri == 'artist:uri:0'

        assert isinstance(releases[1], Release)
        assert releases[1].album_name == 'Album 1'
        assert releases[1].uri == 'uri:1'
        assert releases[1].artist_name == 'Artist 1'
        assert releases[1].image == 'Image 1'
        assert releases[1].artist_uri == 'artist:uri:1'

    @responses.activate
    def test_caches_releases_result(self):
        max_results = 100
        tunigo = Tunigo(max_results=max_results)

        responses.add(responses.GET, BASE_URL + '/new-releases')

        tunigo.get_new_releases()
        tunigo.get_new_releases()

        assert len(responses.calls) == 1
        assert (
            responses.calls[0].request.url ==
            '{}/new-releases?{}&per_page={}'.format(
                BASE_URL, BASE_QUERY, max_results))
