#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tempList = []
    for i in my_list:
        if i % 2 == 0:
            tempList.append(True)
        else:
            tempList.append(False)

    return tempList
