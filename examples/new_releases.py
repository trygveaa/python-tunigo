import tunigo

tunigo = tunigo.Tunigo()

# Returns new album releases.
releases = tunigo.get_new_releases()

# Print the artist and album name, as well as the URI for each release.
# All the available fields can be seen in tunigo/release.py.
for release in releases:
    print('{} - {} ({})'.format(release.artist_name,
                                release.album_name,
                                release.uri))
