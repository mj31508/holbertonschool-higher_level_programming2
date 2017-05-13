#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        total=a/b
    except (ZeroDivisionError) as error:
        total = None

    finally:
        print("Inside Result: {}".format(total))
    return(total)
