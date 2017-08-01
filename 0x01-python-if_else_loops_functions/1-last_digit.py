#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
# Python follows the modulo rule below:
# a % n = b if (a - b) = kn, k = 0, 1, 2, 3,...
last_pos_digit = number % 10
last_neg_digit = ((number * (-1)) % 10) * (-1)

if last_pos_digit == 0:
    print(str, number, "is", last_pos_digit, "and is 0")
elif number > 0 and last_pos_digit > 5:
    print(str, number, "is", last_pos_digit, "and is greater than 5")
elif number > 0 and last_pos_digit < 6:
    print(str, number, "is", last_pos_digit, "and is less than 6 and not 0")
elif number < 0 and last_neg_digit < 6:
    print(str, number, "is", last_neg_digit, "and is less than 6 and not 0")
