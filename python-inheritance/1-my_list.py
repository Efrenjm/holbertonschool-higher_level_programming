#!/usr/bin/python3
"""define my list"""


class MyList(list):
    """ class MyList """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
