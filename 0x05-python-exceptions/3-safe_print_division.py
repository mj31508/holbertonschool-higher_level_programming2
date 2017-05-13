#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        total = a / b
    except(ZeroDivisionError)
        total = None
    finally:
        print("Inside Result: ", end="")
        print("{}".format(total))
    return(total)
