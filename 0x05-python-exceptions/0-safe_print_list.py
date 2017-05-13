#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    if my_list is None or my_list == [] or x == 0:
        print()
        return None
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except (IndexError):
        pass
    print()
    return(count)
