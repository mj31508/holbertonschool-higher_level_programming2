#!/usr/bin/python3
"""
print sorted list using the sort()
"""


class MyList(list):
    def print_sorted(self):
        for i in self:
            if isinstance(i, int) is False:
        print(sorted(self))
