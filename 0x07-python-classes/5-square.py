#!/usr/bin/python3
class Square():
    def __init__(self, size=0):
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size

        def area(self):
            return (self.__size ** 2)

        @property
        def size(self):
            return self.__size
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif (value < 0):
                raise ValueError("Size must be >= 0")
            self.__size = value
