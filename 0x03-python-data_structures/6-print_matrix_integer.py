#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        if matrix == [[]]:
                print("")
        elif matrix:
                for i in range(len(matrix)):
                        row = matrix[i]
                        for j in row:
                                if j == row[len(row) - 1]:
                                        print("{}".format(j))
                                else:
                                        print("{}".format(j), end=" ")
