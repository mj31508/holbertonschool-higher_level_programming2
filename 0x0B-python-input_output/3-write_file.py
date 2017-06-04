#!/usr/bin/python3
"""
write a string to text file
"""


def write_file(filename="", text=""):
    with open("my_file_0.txt","w", encoding="utf-8") as filename:
        total = filename.write(text)
        return total
