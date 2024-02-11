#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            j = 1
            leng = len(i)

            for m in i:
                if j == leng:
                    print('{:d}'.format(m), end='')
                else:
                    print('{:d}'.format(m), end=' ')
                j += 1

            print()
