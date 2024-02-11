#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """
    Prints the argument list passed to the program

    """
    argList = sys.argv
    lenList = len(argList) - 1

    if lenList > 1:
        print(lenList, 'arguments:')
        for i in range(1, lenList + 1):
            print('{:d}: {}'.format(i, argList[i]))
    elif lenList == 1:
        print(lenList, 'argument:')
        for i in range(1, lenList + 1):
            print('{:d}: {}'.format(i, argList[i]))
    elif lenList == 0:
        print(lenList, 'arguments.')
