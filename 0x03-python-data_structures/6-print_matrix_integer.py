#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for number in range(len(arr)):
            print("{:d}".format(arr[number]), end="")

            if number != len(arr) - 1:
                print(" ", end="")
        print("")
