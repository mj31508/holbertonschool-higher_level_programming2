#!/usr/bin/python3
"""
write a string to text file
"""


def write_file(filename="", text=""):
    with open(filename,"w", encoding="utf-8") as filename:
        total = filename.write(text)
        return total
