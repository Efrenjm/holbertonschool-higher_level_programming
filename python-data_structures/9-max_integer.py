#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    numMax = min(my_list)
    for i in my_list:
        if i > numMax:
            numMax = i

    return numMax
