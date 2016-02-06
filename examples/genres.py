from tunigo import Tunigo

tunigo = Tunigo()

# Returns the available genres, including sub genres and a playlist containing
# top tracks for each genre.
genres = tunigo.get_genres()

# Returns playlists for a genre.
genre_playlists = tunigo.get_genre_playlists(genres[0])

# Or use a specific genre key.
genre_playlists = tunigo.get_genre_playlists('rock')

# Returns playlists for a sub genre.
genre_playlists = tunigo.get_genre_playlists(sub_genre=genres[0].sub_genres[0])

# Or use specific genre and sub genre keys.
genre_playlists = tunigo.get_genre_playlists('rock', 'metal')

# Print the name and number of playlists for each genre.
# All the available fields can be seen in tunigo/genre.py
for genre in genres:
    print('{}: {} playlists'.format(genre.name, genre.number_playlists))
