#!/usr/bin/python3
"""
print sorted list using the sort()
"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
