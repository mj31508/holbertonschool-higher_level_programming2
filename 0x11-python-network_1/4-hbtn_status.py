#!/usr/bin/python3
# takes in a url and dispays the response
import requests

if __name__ == "__main__":
    req_get = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(req_get)))
    print("\t- content: {}".format(req_get))
