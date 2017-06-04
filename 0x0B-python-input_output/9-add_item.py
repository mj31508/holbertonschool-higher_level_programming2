#!/usr/bin/python3
"""
Script to add arguments
"""

import json
import sys
import os.path

save_from_json = __import__('7-save_to_json_file').save_to_json_file
load_from_json = __import__('8-load_from_json_file').load_from_json_file

my_list = []

if not os.path.exists("./add_item.json"):
        save_from_json(my_list, "add_item.json")
my_list = load_from_json("add_item.json")

for i in sys.argv[1:]:
    my_list.append(i)
save_from_json(my_list, "add_item.json")
