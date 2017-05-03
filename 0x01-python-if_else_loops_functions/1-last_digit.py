#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = ("Last digit of")
s2 = ("and is greater than 5")
s3 = ("and is 0")
s4 = ("and is less than 6 and not 0")
if number >= 0:
    last = number % 10
if number < 0:
    last = number % -10
if last > 5:
    print("{} {} is {} ".format(s, number, last) + "{}".format(s2))
elif last == 0:
    print("{} {} is {} ".format(s, number, last) + "{}".format(s3))
else:
    print("{} {} is {} ".format(s, number, last) + "{}".format(s4))
