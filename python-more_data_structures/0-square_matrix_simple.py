#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    tempMatrix = []

    if len(matrix) > 0:
        for nodo in matrix[:]:
            tempMatrix.append(list(map(lambda x: x ** 2, nodo)))

    return tempMatrix
