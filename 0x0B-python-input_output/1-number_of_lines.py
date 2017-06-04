#!/usr/bin/python3
"""
returning the num of lines
"""


def number_of_lines(filename=""):
    line = 0
    with open(filename, 'rt', encoding="utf-8") as filename:
        for line_count in filename:
            line += 1
        return (line)
