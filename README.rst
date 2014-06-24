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

To install Python-Tunigo, you can use pip::

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

v0.1.0 (2014-06-24)
-------------------

- Initial release.
