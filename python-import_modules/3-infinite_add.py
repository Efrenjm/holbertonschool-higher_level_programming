#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argList = sys.argv
    lenList = len(argList)
    sum = 0

    if lenList > 1:
        for i in range(1, lenList):
            sum += int(argList[i])
    print(sum)
