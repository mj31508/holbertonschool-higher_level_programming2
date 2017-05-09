#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        if idx < 1 and idx > 5:
            return None
        else:
            return("{}".format(my_list[idx]))
