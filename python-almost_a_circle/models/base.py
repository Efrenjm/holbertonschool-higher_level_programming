#!/usr/bin/python3
""" models/base.py """


class Base:
    """
    Base class for managing unique IDs and providing additional
    utilities for model classes.
    """

    __nb_objects = 0  # Private class attribute for generating unique IDs

    def __init__(self, id=None):
        """
        Initializes the Base object.

        Args:
            id (int, optional): Optional ID to assign to the object.
            If not provided, a unique ID is generated automatically.

        Raises:
            TypeError: If the provided `id` is not an integer.
        """

        if id is not None:
            if not isinstance(id, int):
                raise TypeError("Provided ID must be an integer.")
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def __str__(self):
        """
        Returns a string representation of the Base object.

        Returns:
            str: A formatted string containing the object's class name and ID.
        """

        return f"{self.__class__.__name__}(id={self.id})"

    # @staticmethod
    # def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries to convert
            to JSON.

        Returns:
            str: The JSON string representation of the list, or "[]" if empty.
        """

        # if not list_dictionaries:
        #     return "[]"

        # return json.dumps(list_dictionaries, indent=4)
