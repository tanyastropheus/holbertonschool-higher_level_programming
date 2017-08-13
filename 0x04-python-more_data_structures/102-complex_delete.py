#!/usr/bin/python3
def complex_delete(my_dict, value):
    if not my_dict:
        return (None)
    for (k, v) in list(my_dict.items()):
        if v == value:
            del my_dict[k]
    return (my_dict)
