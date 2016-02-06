from tunigo import Tunigo

tunigo = Tunigo()

# Returns the currently featured playlists.
featured_playlists = tunigo.get_featured_playlists()

# Returns playlists of top tracks in various categories, as well as other
# popular playlists.
top_lists = tunigo.get_top_lists()

# Print the title and URI for each playlist.
# All the available fields can be seen in tunigo/playlist.py
for playlist in top_lists:
    print('{} ({})'.format(playlist.title, playlist.uri))
