#!/usr/bin/python3
add = __import__('add_0').add
a, b = 1, 2
print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
