#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string[:]
    for i in new_string:
        if i == chr(67) or i == chr(99):
            new_string = "" + new_string[1:]
    return new_string
