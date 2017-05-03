#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 3 != 0 and x % 5 != 0:
            print(x, "", end="")
        if x % 5 == 0 and x % 3 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz ", end="")
        elif x % 5 == 0:
            print("Buzz ", end="")
            '''if x % 3 != 0 and x % 5 != 0:
            print(x, "", end="")'''

    ''' i = 0
    while i <= 100:
        if i % 3 == 0:
            print("Fizz ", end="")
        if i % 5 == 0:
            print("Buzz ", end="")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
'''
