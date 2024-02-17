#!/usr/bin/python3
""" models/rectangle.py"""
from .base import Base


class Rectangle(Base):
    """
    Rectangle class representing a rectangle with private attributes
    and getters/setters.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's top-left corner.
        y (int): The y-coordinate of the rectangle's top-left corner.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle. Must be greater than 0.
            height (int): The height of the rectangle. Must be greater than 0.
            x (int, optional): The x-coordinate of the rectangle's top-left
                corner.Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's top-left
                corner. Defaults to 0.
            id (int, optional): Optional ID to assign to the object.
                If not provided, a unique ID is generated automatically.

        Raises:
            ValueError: If width or height is not positive.
            TypeError: If width, height, x, or y is not an integer.
        """

        super().__init__(id)
        self._validate_width(width)
        self._validate_height(height)
        self._validate_x(x)
        self._validate_y(y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


    def _validate_width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")

    def _validate_height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")

    def _validate_x(self, value):
        if not isinstance(value, int):
            raise TypeError("x-coordinate must be an integer")
        if value < 0:
            raise ValueError("x-coordinate must be >= 0")

    def _validate_y(self, value):
        if not isinstance(value, int):
            raise TypeError("y-coordinate must be an integer")
        if value < 0:
            raise ValueError("y-coordinate must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self._validate_width(value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self._validate_height(value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self._validate_x(value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self._validate_y(value)
        self.__y = value

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: A formatted string containing the object's ID, width, height,
            x, and y coordinates.
        """

        return f"Rectangle(id={self.id}, width={self.width}" \
            + ", height={self.height}, x={self.x}, y={self.y})"
