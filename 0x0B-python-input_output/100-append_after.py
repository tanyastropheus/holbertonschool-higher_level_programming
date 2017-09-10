#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r') as f:
        content = f.readlines()  # creating a list of lines

    content_copy = list(content)

    i, j = 1, 0
    for line in content:
        if search_string in line:
            content_copy.insert(i + j, new_string)
            j += 1  # accounting for the offset in the copy after insert
        i += 1

    new_content = "".join(content_copy)

    with open(filename, 'w') as f:
        f.write(new_content)
