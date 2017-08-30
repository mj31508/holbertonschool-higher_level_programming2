#!/usr/bin/python3
"""
Showing the url body or error code message
"""

import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as req:
            print(req.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
