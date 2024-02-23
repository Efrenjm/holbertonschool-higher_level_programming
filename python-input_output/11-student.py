#!/usr/bin/python3
"""class student"""


class Student:
    """
    init class
    """

    def __init__(self, first_name, last_name, age):
        """
        init fucntion
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

    def reload_from_json(self, json):
        """
        reload function
        """

        for i in json:
            if i in self.__dict__.keys():
                self.__dict__[i] = json[i]
