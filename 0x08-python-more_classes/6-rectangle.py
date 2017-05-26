#!/usr/bin/python3
"""
Define a Rectangle Class
"""


class Rectangle:
    """
   Rectangle  Class
    """
    """initiaize
    """
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1
        """width method getter
        """
    @property
    def width(self):
        return self.__width

    """sets width"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

        """height getter"""
    @property
    def height(self):
        return self.__height

    """setting te height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

        """returning the area of the rectangle"""
    def area(self):
        return (self.__width * self.__height)

    """returning the perimeter of the rectangle"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return(0)
        else:
            return (self.__width + self.__width + self.height + self.height)

        """string method to print #"""
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return("")
        else:
            rectangle = "#"
            for i in range(self.__height):
                for j in range(self.height - 1):
                    print(rectangle * self.__width)
                return(rectangle * self.width)

            """ repr method to return decreasing instances"""
    def __repr__(self):
        return("Rectangle{}, {}".format(self.width, self.height))

    """ prints a message when a instance gets deleted"""
    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
