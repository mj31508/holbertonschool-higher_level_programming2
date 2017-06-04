#!/usr/bin/python3
"""
write an object to Json
"""


def save_to_json_file(my_obj, filename):
    import json
    with open(filename, 'w') as filename:
        json.dump(my_obj, filename)
