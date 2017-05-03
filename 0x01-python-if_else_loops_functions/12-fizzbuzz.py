#!/usr/bin/python3
def fizzbuzz():
    for x in range(1,100):
        if x % 3 != 0 and x % 5 != 0:
            print(x, "", end="")
        if x % 3 == 0:
            print("Fizz ", end="")
        if x % 5 == 0:
            print("Buzz ", end="")
        elif x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
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
