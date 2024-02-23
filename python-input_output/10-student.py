#!/usr/bin/python3
"""class student"""


class Student:
    """
    init class
    """

    def __init__(self, first_name, last_name, age):
        """
        init function
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        function to json
        """

        class_d = self.__dict__
        sel_d = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return class_d

                if attr in class_d:
                    sel_d[attr] = class_d[attr]

            return sel_d

        return class_d
