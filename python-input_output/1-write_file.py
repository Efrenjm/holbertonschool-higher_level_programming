#!/usr/bin/python3
"""function write"""


def write_file(filename="", text=""):
    """
    init function
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
