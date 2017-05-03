#!/usr/bin/python3
def fizzbuzz():
    for x in range(1,99):
        i = ""
        if x % 3 == 0:
            print("Fizz ", end="")
        if x % 5 == 0:
            print("Buzz ", end="")
        if i  == "":
            i = x
            print(i , end="")

    ''' i = 0
    while i <= 100:
        if i % 3 == 0:
            print("Fizz ", end="")
        if i % 5 == 0:
            print("Buzz ", end="")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
'''
