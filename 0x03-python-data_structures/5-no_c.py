#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        c_list = list(my_string)
        c_list = [i for i in c_list if i != 'c' and i != 'C']
        new_string = ''.join(c_list)
        return (new_string)
