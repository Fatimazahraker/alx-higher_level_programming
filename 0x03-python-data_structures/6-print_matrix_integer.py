#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lin in matrix:
        for col in lin:
            print("{:d}".format(col), end=" " if col != lin[-1] else "")
        print()
