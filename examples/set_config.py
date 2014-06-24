import tunigo

tunigo = tunigo.Tunigo(
    # Region to use in API calls. Should be a two letter country code.
    # Defaults to 'all'.
    region='no',

    # Max number of results for each API call. Defaults to 1000.
    max_results=100,

    # Number of seconds to cache results from the API. Defaults to 3600.
    cache_time=60)
