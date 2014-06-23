from __future__ import unicode_literals


def underscore_to_camelcase(word):
    s = ''.join(part.capitalize() for part in word.split('_'))
    return s[0].lower() + s[1:]
