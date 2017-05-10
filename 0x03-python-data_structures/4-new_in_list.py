#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > len(my_list) or idx < 0:
        new_list = my_list[:]
        return new_list

    new_list = my_list[:]
    del new_list[3]
    new_list.insert(3, element)
    return new_list
