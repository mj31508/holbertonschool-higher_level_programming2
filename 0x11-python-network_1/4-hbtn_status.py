#!/usr/bin/python3
# takes in a url and dispays the response
import requests

if __name__ == "__main__":
    print("Body Response")
    response = requests.get("https://intranet.hbtn.io/status")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
