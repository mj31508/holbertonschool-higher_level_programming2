#!/usr/bin/python3
"""
raising an exception
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        name = "width"
        super().integer_validator(name, width)
        super().integer_validator(name, height)
        self.__height = height
        self.__width = width
