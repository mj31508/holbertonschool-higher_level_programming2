#!/usr/bin/python3
"""
Showing the url body or error code message
"""

import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as answer:
            if answer.status == 200:
                print(answer.read().decode("utf-8"))
            else:
                error = urllib.error.HTTPError
                print("Error code: {}".format(error))
