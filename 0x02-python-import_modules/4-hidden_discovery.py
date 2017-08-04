#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    s_alpha = sorted(dir(hidden_4))
    for i in s_alpha:
        if i[0] != "_" and i[1] != "_":
            print("{}".format(i), end="\n")
