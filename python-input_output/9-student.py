#!/usr/bin/python3
""" class student"""


class Student:
    """
    init class
    """

    def __init__(self, first_name, last_name, age):
        """
        function init
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        function to json
        """

        return self.__dict__
