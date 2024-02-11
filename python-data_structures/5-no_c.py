#!/usr/bin/python3
def no_c(my_string):
    strT = ''
    for i in my_string:
        if i != 'C' and i != 'c':
            strT += i

    return strT
