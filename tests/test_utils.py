from __future__ import unicode_literals

from tunigo import utils
from tunigo.release import Release


class TestSetInstanceArrayVariables(object):

    def test_sets_variables(self):
        release = Release()
        utils.set_instance_array_variables(
            release,
            ['_author_ids', '_regions'],
            {
                'authorIds': [1, 2],
                'regions': ['no', 'us']
            })

        assert release.author_ids == [1, 2]
        assert release.regions == ['no', 'us']

    def test_sets_missing_variables_to_empty_array(self):
        release = Release(author_ids=None)
        utils.set_instance_array_variables(release, ['_author_ids'], {})

        assert release.author_ids == []


class TestSetInstanceIntVariables(object):

    def test_sets_variables(self):
        release = Release()
        utils.set_instance_int_variables(
            release,
            ['_num_tracks', '_version'],
            {
                'numTracks': 4,
                'version': 6
            })

        assert release.num_tracks == 4
        assert release.version == 6

    def test_sets_missing_variables_to_0(self):
        release = Release(num_tracks=1)
        utils.set_instance_int_variables(release, ['_num_tracks'], {})

        assert release.num_tracks == 0


class TestSetInstanceStringVariables(object):

    def test_sets_variables(self):
        release = Release()
        utils.set_instance_string_variables(
            release,
            ['_album_name', '_artist_name'],
            {
                'albumName': 'Some Album',
                'artistName': 'Some Artist'
            })

        assert release.album_name == 'Some Album'
        assert release.artist_name == 'Some Artist'

    def test_sets_missing_variables_to_empty_string(self):
        release = Release(album_name=None)
        utils.set_instance_string_variables(release, ['_album_name'], {})

        assert release.album_name == ''
