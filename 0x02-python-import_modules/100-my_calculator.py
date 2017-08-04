#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    ops = {'+': add, '-': sub, '*': mul, '/': div}
    if len(argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    num_1 = int(argv[1])
    num_2 = int(argv[3])
    op = argv[2]
    if op in ops:
        print("{} {} {} = {}".format(num_1, op, num_2, ops[op](num_1, num_2)))
        exit(0)
    elif op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
