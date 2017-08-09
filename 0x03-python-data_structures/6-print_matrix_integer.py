#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
        if matrix == [[]]:
                print("")
        elif matrix:
                for row in matrix:
                        for j in row:
                                if j == row[len(row) - 1]:
                                        print("{}".format(j))
                                else:
                                        print("{}".format(j), end=" ")
