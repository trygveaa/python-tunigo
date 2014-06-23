from __future__ import unicode_literals

from tunigo import translator


def set_instance_variables(instance, keys, values, convert):
    for key_underscore in keys:
        key_camelcase = translator.underscore_to_camelcase(key_underscore)
        if key_camelcase in values:
            setattr(instance, key_underscore, convert(values[key_camelcase]))
        else:
            setattr(instance, key_underscore, convert(None))


def set_instance_array_variables(instance, keys, values):
    set_instance_variables(instance, keys, values, lambda x: x or [])


def set_instance_int_variables(instance, keys, values):
    set_instance_variables(instance, keys, values,
                           lambda x: int(x) if x else 0)


def set_instance_string_variables(instance, keys, values):
    set_instance_variables(instance, keys, values, lambda x: x or '')
