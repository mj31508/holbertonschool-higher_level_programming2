#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        if i >= len(my_list) or idx < 0:
            return None
        else:
            return("{}".format(my_list[idx]))
