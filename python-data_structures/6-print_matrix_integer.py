#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        line = " ".join("{:d}".format(num) for num in row)
        print(line)
