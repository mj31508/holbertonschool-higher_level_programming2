#!/usr/bin/python3
# print 2 digits numbers from 00 to 99
a = 0
while a <= 98:
    print("{:02d}, ".format(a), end="")
    a += 1
print("99")
