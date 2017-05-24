#!/usr/bin/python3
"""
Defining a Square class
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

        @property
        def width(self):
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")

            @property
            def height(self):
                return self.__height

            @height.setter
            def height(self, value):
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
