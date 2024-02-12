#!/usr/bin/python3
""" define base geometry """


def inherits_from(obj, a_class):
    """define my list"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
