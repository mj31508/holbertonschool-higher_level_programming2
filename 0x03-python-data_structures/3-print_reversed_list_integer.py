#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    index = 0
    for i in range(len(my_list)):
        my_list.reverse()
        print("{}".format(my_list[index]))
        index += 1
