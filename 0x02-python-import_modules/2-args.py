#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sin = "argument"
    plu = "arguments"

    if len(sys.argv) == 1:
        print("{:d} {}.".format(0, sin))

    elif len(sys.argv) == 2:
        print("{:d} {}:".format(1, sin))
        print("{:d}: {}".format(1, sys.argv[1]))

    else:
        print("{:d} {}:".format(len(sys.argv) - 1, plu))
        for i in range(1, len(sys.argv) + 1):
              print("{:d}: {}".format(i, sys.argv[i - 1]))
