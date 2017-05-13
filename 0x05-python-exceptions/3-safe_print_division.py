#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        total = a / b
    except(ZeroDivisionError):
        total = None
    finally:
        print("{}{}".format("Inside Result: ", total))
        return(total)
