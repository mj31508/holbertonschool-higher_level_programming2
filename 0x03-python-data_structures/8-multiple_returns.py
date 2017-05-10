#!/usr/bin/python3
def multiple_returns(sentence):
    str_l = len(sentence)
    if str_l is None:
        return
    if sentence == "":
        char = None
    else:
        char = sentence[0]
    return str_l, char
