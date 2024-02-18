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

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A formatted string containing the square's class,
            ID, coordinates, and size.
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

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
            value (int): The new side length for the square.
            Must be greater than 0.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not positive.
        """

        self._validate_width(value)
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A formatted string containing the square's
            class, ID, coordinates, and size.
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Updates the square attributes with given arguments,
        prioritizing kwargs.

        Args:
            *args: Positional arguments (treated as ID, size, x, y).
            **kwargs: Keyword arguments representing attributes to update.

        Raises:
            TypeError: If mixed positional and keyword arguments are provided.
            ValueError: If invalid values are provided for attributes.
        """

        if args:
            try:
                self.id = args[0]
                self._validate_width(args[1])
                self.width = args[1]
                self.height = args[1]
                self._validate_x(args[2])
                self.x = args[2]
                self._validate_y(args[3])
                self.y = args[3]
            except Exception as e:
                pass
        elif kwargs:
            try:
                for key, value in kwargs.items():
                    if key not in ("id", "size", "x", "y"):
                        raise ValueError(f"Invalid attribute name: {key}")
                    if key == "id":
                        self.id = value
                    elif key == "size":
                        self._validate_width(value)
                        self.width = value
                        self.height = value
                    elif key == "x":
                        self._validate_x(value)
                        self.x = value
                    elif key == "y":
                        self._validate_y(value)
                        self.y = value

                setattr(self, f"__{key}", value)
            except Exception as e:
                pass
