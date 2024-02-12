#!/usr/bin/python3
"""define my list"""


class MyList(list):
    """ class MyList """

    def print_sorted(self):
        try:
            sorted_list = sorted(self)
            print(sorted_list)
        except Exception as e:
            pass