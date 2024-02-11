#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dicionary_s = sorted(a_dictionary.items())

    for key, value in dicionary_s:
        print('{0}: {1}'.format(key, value))
