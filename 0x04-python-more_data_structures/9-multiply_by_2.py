#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {x: y*2 for (x, y) in my_dict.items()}
    return (new_dict)
