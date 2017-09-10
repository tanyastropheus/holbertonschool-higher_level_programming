#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r') as f:
        content = f.readlines()  # creating a list of lines

    # inset lines in the copy since we cannot modify while iterating
    content_copy = list(content)

    insert_index = 1
    for line in content:
        if search_string in line:
            content_copy.insert(insert_index, new_string)
            insert_index += 1  # account for the offset in the copy after insert
        insert_index += 1

    # join lines back into text
    new_content = "".join(content_copy)

    # rewrite new content into the file
    with open(filename, 'w') as f:
        f.write(new_content)
