#!/usr/bin/python3
def remove_char_at(str, n):
    result = str[:n] + str[n + 1:]
    if n == 0:
        result = str[1:]
    elif n < 0:
        result = str
    return (result)
