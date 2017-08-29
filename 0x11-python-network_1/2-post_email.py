#!/usr/bin/python3
# script that takes in a URL and an email, sends a POST request

import urlib.request
import sys

if __name__ == '__main__':
    email_parse = urllib.parse.urlencode({"email": sys.argv[2]}).encode("utf-8")
    url_request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url_request) as answer:
        print (response.read())
