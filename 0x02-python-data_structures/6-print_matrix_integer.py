#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        c = 0
        for i in x:
            if c < len(x) - 1:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
            c = c + 1
        print()
