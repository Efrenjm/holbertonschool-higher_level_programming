#!/usr/bin/python3
"""defines a square with size as integer with setter"""


class Square:
    """represents a square"""


    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
