#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        if i > idx:
            return None
        else:
            return("{}".format(my_list[idx]))
