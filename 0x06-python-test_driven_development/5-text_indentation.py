#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines

    Args:
    text -- String

    Return: None

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text_r = text.replace(".", ".\n\n")
    text_r = text_r.replace("?", "?\n\n")
    text_r = text_r.replace(":", ":\n\n")
    text_r1 = text_r.split("\n")
    for line in range(len(text_r1)):
        print("{}".format(text_r1[line].strip()),
              end=("" if (line == (len(text_r1) - 1)) else "\n"))
