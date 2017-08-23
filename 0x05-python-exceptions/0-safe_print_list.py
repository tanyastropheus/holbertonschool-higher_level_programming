#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list[0:x]:  # slicing the list
            print("{}".format(i), end="")
            count = count + 1
        print()
    except IndexError:
        pass  # code after pass will still get executed
    return count
