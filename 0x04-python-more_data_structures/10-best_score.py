#!/usr/bin/python3
def best_score(my_dict):
    if not my_dict:
        return (None)
    flip_dict = {v: k for (k, v) in my_dict.items()}
    max_value = flip_dict[max(flip_dict.keys())]
    return (max_value)
