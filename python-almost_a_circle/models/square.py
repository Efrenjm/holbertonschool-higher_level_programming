#!/usr/bin/python3
"""models/square.py"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Square class representing a square with inherited attributes and methods
    from Rectangle.

    Attributes:
        size (int): The side length of the square. Must be greater than 0.
        x (int): The x-coordinate of the square's top-left corner. Must be
            non-negative.
        y (int): The y-coordinate of the square's top-left corner. Must be
            non-negative.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The side length of the square. Must be greater
                than 0.
            x (int, optional): The x-coordinate of the square's top-left
                corner. Defaults to 0.
            y (int, optional): The y-coordinate of the square's top-left
                corner. Defaults to 0.
            id (int, optional): Optional ID to assign to the object. If
            not provided, a unique ID is generated automatically.

        Raises:
            TypeError: If size, x, or y is not an integer.
            ValueError: If size is not positive, or x or y is negative.
        """

        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A formatted string containing the square's class,
            ID, coordinates, and size.
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__size}"

    @property
    def size(self):
        """
        Gets the current side length of the square.

        Returns:
            int: The square's side length.
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the side length of the square, updating both width and height.

        Args:
            value (int): The new side length for the square. Must be greater than 0.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not positive.
        """

        # if not isinstance(value, int):
        #     raise TypeError("Size must be an integer.")
        self._validate_width(value)
        self.__size = value
        self.__width = value
        self.__height = value

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A formatted string containing the square's class, ID, coordinates,
                 and size.
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__size}"
