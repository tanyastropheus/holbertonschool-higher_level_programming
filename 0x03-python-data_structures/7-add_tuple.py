#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum = []
    list_a = list(tuple_a) + [0, 0]
    list_b = list(tuple_b) + [0, 0]
    for i in range(2):
        sum.append(list_a[i] + list_b[i])
    return (sum)
