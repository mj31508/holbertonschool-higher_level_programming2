#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return my_list

    if idx < 0 or idx >= len(my_list):
        copied_list = my_list[:]
        return copied_list

    new_list = my_list[:]
    new_list[idx] = element
    return new_list
