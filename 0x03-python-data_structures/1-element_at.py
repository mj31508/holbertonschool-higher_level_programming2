#!/usr/bin/python3
def element_at(my_list, idx):
    if my_list is None:
        return my_list
    
    for i in range(len(my_list)):
        if idx >= len(my_list)-1 or idx <= 0:
            return None
        else:
            return("{}".format(my_list[idx]))
