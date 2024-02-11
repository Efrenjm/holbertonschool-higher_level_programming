#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp_dictionary = a_dictionary.copy()

    for key, value in temp_dictionary.items():
        temp_dictionary[key] = value * 2

    return temp_dictionary
