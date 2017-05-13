#!/bin/python3
def safe_print_division(a, b):
    try:
        total=a/b
    except (ZeroDivisionError) as error:
        total = 0
        return None

    finally:
        print("Inside Result: {:.1f}".format(total))
        return(total)
