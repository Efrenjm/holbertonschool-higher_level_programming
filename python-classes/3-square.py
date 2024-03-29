#!/usr/bin/python3
"""define a class Square"""


class Square:
    """represents a Square"""

    def __init__(self, size=0):
        """Initializes a new Square


        Args:
            size (int): The size of the new square.
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns the current square area

        """
        return self.__size ** 2
