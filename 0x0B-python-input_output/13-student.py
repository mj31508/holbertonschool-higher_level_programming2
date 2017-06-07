#!/usr/bin/python3
"""
Defining a class
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            dict1 = {}
            for attr in attrs:
                if hasattr(self, attr):
                    dict1[attr] = getattr(self, attr)
            return dict1

    def reload_from_json(self, json):
        for item in json:
            self.__dict__[item] = json[item]
