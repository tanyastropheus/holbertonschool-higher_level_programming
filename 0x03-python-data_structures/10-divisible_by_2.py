#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:  # i is a copy of the elements in my_list
        new_list.append(i % 2 == 0)  #  evaluates to boolen (T/F)
    print(new_list)
    return (new_list)
