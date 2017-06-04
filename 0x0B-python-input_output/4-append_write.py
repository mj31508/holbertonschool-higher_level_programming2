#!/usr/bin/python3
"""
appending a string to text file
"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as filename:
        filename.write(text)
        return(len(text))
