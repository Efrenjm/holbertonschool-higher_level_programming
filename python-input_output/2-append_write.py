#!/usr/bin/python3
"""Append function"""


def append_write(filename="", text=""):
    """
    init function
    """

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
