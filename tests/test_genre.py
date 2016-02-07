from __future__ import unicode_literals

from tunigo.genre import Genre, SubGenre
from tunigo.playlist import Playlist


class TestGenre(object):

    def test_repr(self):
        genre = Genre(template_name='genre')

        assert genre.__repr__() == "Genre(template_name='genre')"

    def test_str(self):
        genre = Genre(template_name='genre')

        assert genre.__str__() == 'genre'

    def test_creates_instance_from_item_array(self):
        genre = Genre(item_array={
            'created': 1,
            'headerImageUrl': 'http://some.header.image',
            'iconImageUrl': 'http://some.icon.image',
            'iconUrl': 'http://some.icon',
            'id': 'Some id',
            'location': 'Some location',
            'moodImageUrl': 'http://some.mood.image',
            'name': 'Some name',
            'numberPlaylists': 2,
            'templateName': 'Some template name',
            'type': 'Some type',
            'updated': 3,
            'version': 4
        })

        assert genre.created == 1
        assert genre.header_image_url == 'http://some.header.image'
        assert genre.icon_image_url == 'http://some.icon.image'
        assert genre.icon_url == 'http://some.icon'
        assert genre.id == 'Some id'
        assert genre.location == 'Some location'
        assert genre.mood_image_url == 'http://some.mood.image'
        assert genre.name == 'Some name'
        assert genre.number_playlists == 2
        assert isinstance(genre.playlist, Playlist)
        assert genre.playlist.main_genre == genre
        assert genre.sub_genres == []
        assert genre.template_name == 'Some template name'
        assert genre.type == 'Some type'
        assert genre.updated == 3
        assert genre.version == 4

    def test_creates_playlist_from_playlist_uri_in_item_array(self):
        genre = Genre(item_array={
            'playlistUri': 'some:playlist:uri'
        })

        assert isinstance(genre.playlist, Playlist)
        assert genre.playlist.main_genre == genre
        assert genre.playlist.uri == 'some:playlist:uri'
        assert genre.playlist_uri == 'some:playlist:uri'

    def test_creates_playlist_from_playlist_uri_in_arguments(self):
        genre = Genre(playlist_uri='some:playlist:uri')

        assert isinstance(genre.playlist, Playlist)
        assert genre.playlist.main_genre == genre
        assert genre.playlist.uri == 'some:playlist:uri'
        assert genre.playlist_uri == 'some:playlist:uri'

    def test_sets_playlist_to_given_playlist_instance_in_arguments(self):
        playlist = Playlist(uri='some:playlist:uri')
        genre = Genre(playlist=playlist)

        assert isinstance(genre.playlist, Playlist)
        assert genre.playlist.main_genre == genre
        assert genre.playlist == playlist
        assert genre.playlist_uri == 'some:playlist:uri'

    def test_creates_empty_playlist_if_not_given(self):
        genre = Genre()

        assert isinstance(genre.playlist, Playlist)
        assert genre.playlist.main_genre == genre

    def test_creates_sub_genres_from_sub_genres_in_item_array(self):
        genre = Genre(item_array={
            'subGenres': [{
                'key': 'Key 0',
                'name': 'Name 0'
            }, {
                'key': 'Key 1',
                'name': 'Name 1'
            }]
        })

        assert len(genre.sub_genres) == 2

        assert isinstance(genre.sub_genres[0], SubGenre)
        assert genre.sub_genres[0].main_genre == genre
        assert genre.sub_genres[0].key == 'Key 0'
        assert genre.sub_genres[0].name == 'Name 0'

        assert isinstance(genre.sub_genres[1], SubGenre)
        assert genre.sub_genres[1].main_genre == genre
        assert genre.sub_genres[1].key == 'Key 1'
        assert genre.sub_genres[1].name == 'Name 1'


class TestSubGenre(object):

    def test_repr(self):
        sub_genre = SubGenre(key='sub_genre', main_genre='genre')

        assert (
            sub_genre.__repr__() ==
            "SubGenre(main_genre='genre', key='sub_genre')")

    def test_str(self):
        sub_genre = SubGenre(key='sub_genre', main_genre='genre')

        assert sub_genre.__str__() == 'genre/sub_genre'

    def test_creates_empty_main_genre_if_not_given(self):
        sub_genre = SubGenre()

        assert isinstance(sub_genre.main_genre, Genre)

    def test_sets_main_genre_to_given_genre_instance(self):
        genre = Genre(template_name='Some genre')
        sub_genre = SubGenre(main_genre=genre)

        assert sub_genre.main_genre == genre

    def test_creates_main_genre_from_given_name(self):
        sub_genre = SubGenre(main_genre='Some genre')

        assert isinstance(sub_genre.main_genre, Genre)
        assert sub_genre.main_genre.template_name == 'Some genre'
