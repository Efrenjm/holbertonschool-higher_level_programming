#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    dirNames = dir(hidden_4)

    for i in range(len(dirNames)):
        if dirNames[i][:2] != '__':
            print(dirNames[i])
