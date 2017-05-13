#!/usr/bin/python3
def safe_print_division(a, b):
    print("Inside Result: ", end="")
    try:
        total=a/b
    except (ZeroDivisionError):
        total = None

    finally:
        print("{}".format(total))
    return(total)
