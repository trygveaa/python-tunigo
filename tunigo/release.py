from __future__ import unicode_literals


class Release(object):

    def __init__(self,
                 album_name='',
                 artist_name='',
                 author_ids=[],
                 created=0,
                 description='',
                 genre_id='',
                 id='',
                 image='',
                 location='',
                 num_tracks=0,
                 publication_date='',
                 regions=[],
                 tags=[],
                 updated=0,
                 uri='',
                 version=0,
                 item_array=None):

        if item_array:
            self._album_name = item_array['albumName']
            self._artist_name = item_array['artistName']
            self._author_ids = item_array['authorIds']
            self._created = item_array['created']
            self._description = item_array['description']
            self._genre_id = item_array['genreId']
            self._id = item_array['id']
            self._image = item_array['image']
            self._location = item_array['location']
            self._num_tracks = int(item_array['numTracks'])
            self._publication_date = item_array['publicationDate']
            self._regions = item_array['regions']
            self._tags = item_array['tags']
            self._updated = int(item_array['updated'])
            self._uri = item_array['uri']
            self._version = int(item_array['version'])

        else:
            self._album_name = album_name
            self._artist_name = artist_name
            self._author_ids = author_ids
            self._created = created
            self._description = description
            self._genre_id = genre_id
            self._id = id
            self._image = image
            self._location = location
            self._num_tracks = int(num_tracks)
            self._publication_date = publication_date
            self._regions = regions
            self._tags = tags
            self._updated = int(updated)
            self._uri = uri
            self._version = int(version)

    @property
    def uri(self):
        return self._uri

    @property
    def artist_name(self):
        return self._artist_name

    @property
    def album_name(self):
        return self._album_name

    @property
    def album_name(self):
        return self._album_name

    @property
    def artist_name(self):
        return self._artist_name

    @property
    def author_ids(self):
        return self._author_ids

    @property
    def created(self):
        return self._created

    @property
    def description(self):
        return self._description

    @property
    def genre_id(self):
        return self._genre_id

    @property
    def id(self):
        return self._id

    @property
    def image(self):
        return self._image

    @property
    def location(self):
        return self._location

    @property
    def num_tracks(self):
        return self._num_tracks

    @property
    def publication_date(self):
        return self._publication_date

    @property
    def regions(self):
        return self._regions

    @property
    def tags(self):
        return self._tags

    @property
    def updated(self):
        return self._updated

    @property
    def uri(self):
        return self._uri

    @property
    def version(self):
        return self._version
