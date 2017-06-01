#!/usr/bin/python3
"""
using isinstance to fnd same type
"""


def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return isinstance(obj, a_class)
    else:
        return False
