#!/usr/bin/python3
offset = ord('a') - ord('A')
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 != 0:
        i = i - offset
    print("{}".format(chr(i)), end="")
