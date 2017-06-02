#!/usr/bin/python3
"""
Define a Rectangle Class
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return(0)
        else:
            return (self.__width + self.__width + self.height + self.height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return("")
        else:
            rectangle = "#"
            for i in range(self.__height):
                for j in range(self.__height - 1):
                    print(rectangle * self.__width)
                return(rectangle * self.width)

    def __repr__(self):
        return("Rectangle({}, {})".format(self.width, self.height))