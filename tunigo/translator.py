from __future__ import unicode_literals


underscore_to_camelcase_cache = {}


def underscore_to_camelcase(word):
    if word in underscore_to_camelcase_cache:
        return underscore_to_camelcase_cache[word]
    else:
        s = ''.join(part.capitalize() for part in word.split('_'))
        s = s[0].lower() + s[1:]
        underscore_to_camelcase_cache[word] = s
        return s
