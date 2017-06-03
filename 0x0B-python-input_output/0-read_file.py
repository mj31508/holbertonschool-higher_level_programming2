#!/usr/bin/python3
"""
Read a text file
"""


def read_file(filename=""):
    with open(filename, "r", encoding='utf-8') as filename:
            print(filename.read(), end="")
