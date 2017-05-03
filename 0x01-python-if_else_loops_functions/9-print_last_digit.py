#!/usr/bin/python3
def print_last_digit(number):
    x = number
    if number < 0:
        x =  number * -1
    print(x % 10, end="")
    return(x % 10)
