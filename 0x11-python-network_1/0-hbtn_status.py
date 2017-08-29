#!/usr/bin/python3
# Python script that fetches a url
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        url = response.read()
        print("Body Response:")
        print("\t- type: {}".format(type(url)))
        print("\t- content: {}".format(url))
        print("\t- utf8 content: {}".format(url.decode("utf-8")))
