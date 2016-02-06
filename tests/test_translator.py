from __future__ import unicode_literals

from tunigo import translator


class TestUndescoreToCamelCase(object):

    def test_returns_converted_to_camel_case(self):
        word = translator.underscore_to_camelcase('some_word_with_underscore')

        assert word == 'someWordWithUnderscore'
