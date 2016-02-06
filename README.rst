*************
Python-Tunigo
*************

Python-Tunigo is a python package that allows for simple access to `Tunigo
<http://tunigo.com/>`_'s API. This is an API for fetching featured playlists and
new releases for `Spotify <https://www.spotify.com/>`_. It supports featured
playlists, top playlists, new album releases and playlists for a range of
different genres.

Tunigo's API is what the Spotify client uses to provide its Browse-feature.

Note that the API is not documented or officially released, so it may change at
any time.


Installation
============

Debian/Ubuntu/Raspbian: Install the ``python-tunigo`` or the ``python3-tunigo``
package from `apt.mopidy.com <http://apt.mopidy.com/>`_::

    sudo apt-get install python-tunigo
    sudo apt-get install python3-tunigo

Arch Linux: Install the ``python2-tunigo`` or the ``python-tunigo`` package
from `AUR <https://aur.archlinux.org/packages/mopidy-spotify/>`_, e.g.::

    yaourt -S python2-tunigo
    yaourt -S python-tunigo

Else: Install the ``tunigo`` package from PyPI::

    pip install tunigo


Examples
========

.. code-block:: python

    import tunigo
    tunigo = tunigo.Tunigo()
    for playlist in tunigo.get_featured_playlists():
        print(playlist.title)

See the ``examples/`` directory for further examples.


License
=======

Python-Tunigo is copyright 2014 Trygve Aaberge and contributors.
Python-Tunigo is licensed under the `Apache License, Version 2.0
<http://www.apache.org/licenses/LICENSE-2.0>`_.


Project resources
=================

- `Source code <https://github.com/trygveaa/python-tunigo>`_
- `Issue tracker <https://github.com/trygveaa/python-tunigo/issues>`_
- `Download development snapshot <https://github.com/trygveaa/python-tunigo/archive/master.tar.gz#egg=python-tunigo-dev>`_

.. image:: https://img.shields.io/pypi/v/tunigo.svg?style=flat
    :target: https://pypi.python.org/pypi/tunigo/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/tunigo.svg?style=flat
    :target: https://pypi.python.org/pypi/tunigo/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/travis/trygveaa/python-tunigo/master.png?style=flat
    :target: https://travis-ci.org/trygveaa/python-tunigo
    :alt: Travis CI build status

.. image:: https://img.shields.io/coveralls/trygveaa/python-tunigo/master.svg?style=flat
   :target: https://coveralls.io/r/trygveaa/python-tunigo?branch=master
   :alt: Test coverage


Changelog
=========

v1.0.0 (UNRELEASED)
-------------------

- Add the new field Release.artist_uri.
- Fix type of Release.created to be int all places.

v0.1.3 (2014-11-29)
-------------------

- Fix check for content-type so it doesn't fail after a change in the API.

v0.1.2 (2014-08-03)
-------------------

- Fix that some genres were not listed by using the same query options as
  play.spotify.com.

v0.1.1 (2014-07-21)
-------------------

- Allow Genre- and SubGenre-objects as arguments to get_genre_playlists.
- Allow a SubGenre to be created with main_genre as a string.
- Add __repr__ and __str__ methods to classes.

v0.1.0 (2014-06-24)
-------------------

- Initial release.
