#!/usr/bin/python3
import sys

a = ['', 'Hello', 'Holberton', 'School', '98', 'Battery', 'Street']
for i in range(len(sys.argv)):
    if i == 0:
        print("0 argument.")
    elif i > 0:
        print("{}: {} ".format(i, a[i]))
