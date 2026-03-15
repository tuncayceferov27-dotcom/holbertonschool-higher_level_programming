#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row:  # boş sətir yoxla
            print(" ".join("{:d}".format(i) for i in row))
        else:
            print()
