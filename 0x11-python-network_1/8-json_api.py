#!/usr/bin/python3
# sends a post request

if __name__ "__main__":
    try:
        post = sys.argv[1]
    except:
        post = ""

    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data={"q": post})

    if req == {}:
        print("No result")
    else:
        print("[{}] {}".format(req["id"], req["name"]))
