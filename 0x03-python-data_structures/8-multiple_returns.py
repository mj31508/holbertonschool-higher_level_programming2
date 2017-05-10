#!/usr/bin/python3
def multiple_returns(sentence):
    str_l = len(sentence)
    if str_l is None:
        return
    if sentence == "":
        sentence[0] = None
    return str_l, sentence[0]
