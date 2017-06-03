#!/usr/bin/python3
"""
Read a text file
"""


def read_file(filename=""):
    with open("my_file_0.txt", "r", encoding="utf-8") as filename:
        for line in filename:
            print(line.strip('\n'))
