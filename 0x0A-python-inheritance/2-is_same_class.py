#!/usr/bin/python3
"""
using isinstance to fnd same type
"""


def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
