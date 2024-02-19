#!/usr/bin/python3
""" models/base.py """
import json


class Base:
    """
    Base class for managing unique IDs and providing additional
    utilities for model classes.
    """

    __nb_objects = 0

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries to convert
            to JSON.

        Returns:
            str: The JSON string representation of the list, or "[]" if empty.
        """

        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        else:
            json_string = "["
            for dict in list_dictionaries:
                if dict == {}:
                    json_string += "{}"
                else:
                    json_string += "{"
                    for key, val in dict.items():
                        json_string += f'"{key}": {val}, '
                    json_string = json_string[:-2] + "}, "
            json_string = json_string[:-2] + "]"

        return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves the JSON string representation of a list of objects to a file.

        Args:
            cls (class): The class of the objects in the list.
            list_objs (list): A list of objects inheriting from Base.

        Raises:
            TypeError: If any object in the list is not an instance
            of the calling class.
        """

        if not list_objs:
            list_objs = []

        json_string = cls.to_json_string([obj.to_dictionary()
                                          for obj in list_objs])

        filename = f"{cls.__name__}.json"

        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of objects represented by a JSON string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: A list of objects, or an empty list if json_string is
            None or empty.
        """

        if not json_string:
            return []

        try:
            list_dictionaries = json.loads(json_string)
            return list_dictionaries
        except json.JSONDecodeError:
            print("Invalid JSON string.")
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        Returns the list of objects represented by a JSON string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: A list of objects, or an empty list if json_string is
            None or empty.
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class for create method.")

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns the list of objects represented by a JSON string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: A list of objects, or an empty list if json_string is
            None or empty.
        """

        filename = f"{cls.__name__}.json"

        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**dict) for dict in list_dicts]
        except FileNotFoundError:
            return []
