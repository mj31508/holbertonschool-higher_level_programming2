#!/usr/bin/python3
"""
read n lines of txt file
"""
f

def read_lines(filename="", nb_lines=0):
    line_count = 0
    with open("my_file_0.txt", "r", encoding="utf-8") as filename:
        for line in filename:
            line_count += 1
            if nb_lines <= 0 or nb_lines >= line_count:
                print(line.strip())
