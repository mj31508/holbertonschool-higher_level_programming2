#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    if my_list is None or x == 0 or my_list == []:
        print()
        return None
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
        return(i + 1)
    except IndexError:
        print()
        return(i)
    return(i+1)
