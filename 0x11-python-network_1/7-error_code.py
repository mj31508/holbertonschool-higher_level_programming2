#!/usr/bin/python3
# print a 200 error response
import requests
import sys

if __name__ == "__main__":
    rep_get = requests.get(sys.argv[1])
    if rep_get.status_code >= 400:
        print("Error code: {}".format(rep_get.status_code))
    else:
        print(rep_get.text)
