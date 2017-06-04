#!/usr/bin/python3
"""
return an object via json string
"""


def from_json_string(my_str):
    from json import loads
    return(loads(my_str))
