#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    if key in sorted(my_dict):
        del my_dict[key]
    return my_dict
