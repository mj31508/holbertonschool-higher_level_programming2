#!/usr/bin/python3
# Python script that fetches a url
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        url = response.read()
        print("Body Response:\n"
              t- type: {}\n"
              "\t- content: {}\n"
              "\t- utf content: {} "
              .format(type(url), url, url.decode("utf-8")))
