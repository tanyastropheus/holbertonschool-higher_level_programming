#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mul_2 = list(my_list)
    if my_list == []:
        return (mul_2)
    else:
        for i in range(len(mul_2)):
            if mul_2[i] % 2 == 0:
                mul_2[i] = True
            else:
                mul_2[i] = False
    return (mul_2)
