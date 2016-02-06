from __future__ import unicode_literals

from tunigo.release import Release


class TestRelease(object):

    def test_creates_instance_from_item_array(self):
        release = Release(item_array={
            'albumName': 'Some Album',
            'artistName': 'Some Artist',
            'artistUri': 'artist:uri',
            'authorIds': [1, 2],
            'created': 3,
            'description': 'Some description',
            'genreId': 'Some genre',
            'id': 'Some id',
            'image': 'Some image',
            'location': 'Some location',
            'numTracks': 4,
            'publicationDate': '2016-02-06',
            'regions': ['no', 'us'],
            'tags': ['Tag 1', 'Tag 2'],
            'updated': 5,
            'uri': 'some:uri',
            'version': 6
        })

        assert release.album_name == 'Some Album'
        assert release.artist_name == 'Some Artist'
        assert release.artist_uri == 'artist:uri'
        assert release.author_ids == [1, 2]
        assert release.created == 3
        assert release.description == 'Some description'
        assert release.genre_id == 'Some genre'
        assert release.id == 'Some id'
        assert release.image == 'Some image'
        assert release.location == 'Some location'
        assert release.num_tracks == 4
        assert release.publication_date == '2016-02-06'
        assert release.regions == ['no', 'us']
        assert release.tags == ['Tag 1', 'Tag 2']
        assert release.updated == 5
        assert release.uri == 'some:uri'
        assert release.version == 6
