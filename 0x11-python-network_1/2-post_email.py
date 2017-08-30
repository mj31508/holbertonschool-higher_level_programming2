#!/usr/bin/python3
# script that takes in a URL and an email, sends a POST request

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    email_dic = {"email": email}
    print(email_dic)
    data = urllib.parse.urlencode(email_dic)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        read = response.read()
        print(read.decode('utf-8'))
