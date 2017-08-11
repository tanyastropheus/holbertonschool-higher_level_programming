#!/usr/bin/python3
def weight_average(my_list=[]):
    weighted = [x * y for (x, y) in my_list]
    dist = [y for (x, y) in my_list]
    w_avg = sum(weighted) / sum(dist)
    return (w_avg)
