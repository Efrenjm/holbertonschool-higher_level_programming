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

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
