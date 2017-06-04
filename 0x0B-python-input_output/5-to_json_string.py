#!/usr/bin/python3
"""
JSON representation of an object
"""


def to_json_string(my_obj):
    from json import dumps
    return(dumps(my_obj))
