#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return (0)
    else:
        new_list = sorted(my_list)
        sum = new_list[0]
        num = new_list[0]
        for i in new_list:
            if i != num:
                sum = sum + i
                num = i
                return (sum)
