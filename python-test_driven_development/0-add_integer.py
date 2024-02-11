#!/usr/bin/python3
"""A module to add two numbers"""


def add_integer(a, b=98):
    """Adds two numbers

    Performs the addition between two numbers.

    Args:
        a (:obj:`int, float`): The first number.
        b (:obj:`int, float`, optional): The second number.

    Returns:
        int: The result of the addition.

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
