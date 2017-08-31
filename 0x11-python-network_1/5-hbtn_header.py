#!/usr/bin/python3
# Taking in a URL and sends a request

import requests
import sys

if __name__ == "__main__":
    url_arg = sys.argv[1]
    req_arg = requests.get(url_arg)

    try:
        store = req_arg.headers["X-Request-Id"]
        print(store)
    except:
        pass
