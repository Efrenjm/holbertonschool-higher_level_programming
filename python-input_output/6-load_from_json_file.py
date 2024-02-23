#!/usr/bin/python3
"""load json file"""


from json import loads


def load_from_json_file(filename):
    """
    init function
    """

    with open(filename, encoding='utf-8') as f:
        return loads(f.read())
