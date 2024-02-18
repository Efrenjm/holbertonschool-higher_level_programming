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
        """
        Validate width

        Args:
            value (int): The width of the rectangle. Must be greater than 0.

        Raises:
            ValueError: If value is not positive.
            TypeError: If value is not an integer.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    def _validate_height(self, value):
        """
        Validate height

        Args:
            value (int): The height of the rectangle. Must be greater than 0.

        Raises:
            ValueError: If value is not positive.
            TypeError: If value is not an integer.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    def _validate_x(self, value):
        """
        Validate x

        Args:
            value (int): The x-coordinate of the rectangle's top-left

        Raises:
            ValueError: If value is not positive.
            TypeError: If value is not an integer.
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    def _validate_y(self, value):
        """
        Validate y

        Args:
            y (int, optional): The y-coordinate of the rectangle's top-left
                corner. Defaults to 0.

        Raises:
            ValueError: If value is not positive.
            TypeError: If value is not an integer.
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """

        return self.width * self.height

    def display(self):
        """
        Prints the rectangle to standard output using '#' characters.
        """

        for i in range(self.height + self.y):
            if i < self.y:
                print()
                continue
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """
        Updates the rectangle attributes with given arguments in
        specific order.

        Args:
            *args: Positional arguments representing the new values
                for ID, width, height, x, and y (in that order).
            **kwargs: Keyword arguments representing attributes to update.

        Raises:
            TypeError: If the number of arguments is not 5 or any
                argument is not an integer.
            ValueError: If width or height is not positive, or x
                or y is negative.
        """

        if args:
            try:
                self.id = args[0]
                self._validate_width(args[1])
                self.__width = args[1]
                self._validate_height(args[2])
                self.__height = args[2]
                self._validate_x(args[3])
                self.__x = args[3]
                self._validate_y(args[4])
                self.__y = args[4]
            except Exception as e:
                pass
        elif kwargs:
            try:
                for key, value in kwargs.items():
                    if key not in ("id", "width", "height", "x", "y"):
                        raise ValueError(f"Invalid attribute name: {key}")
                    if key == "id":
                        self.id = value
                    elif key == "height":
                        self._validate_height(value)
                        self.__height = value
                    elif key == "width":
                        self._validate_width(value)
                        self.__width = value
                    elif key == "x":
                        self._validate_x(value)
                        self.__x = value
                    elif key == "y":
                        self._validate_y(value)
                        self.__y = value

                setattr(self, f"__{key}", value)
            except Exception as e:
                pass

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle object.

        Returns:
            dict: A dictionary containing the rectangle's ID, width, height, x, and y attributes.
        """

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
    
    def __str__(self):
        """
        Returns a string representation of the Rectangle object
        in the specified format.

        Returns:
            str: A formatted string containing the rectangle's
                class, ID, coordinates, and dimensions.
        """

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} -" \
            + f" {self.width}/{self.height}"

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
