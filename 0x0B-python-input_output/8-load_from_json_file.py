#!/usr/bin/python3
"""
Create a Object from a JSON
"""


def load_from_json_file(filename):
    import json
    with open(filename, 'r') as filename:
        return json.load(filename)
