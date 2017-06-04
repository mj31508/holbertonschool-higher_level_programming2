#!/usr/bin/python3
"""
Script to add arguments
"""

import json
import sys
import os.path

save_from_json = __import__('7-save_to_json_file').save_to_json_file
load_from_json = __import__('8-load_from_json_file').load_from_json_file

MyList = []
if not os.path.exists("./add_item.json"):
    savefromjson(MyList, "add_item.json")
MyList = load_from_json("add_item.json")

for i in sys.argv[1:]:
    MyList.append(i)
savefromjson(MyList, "add_item.json")
