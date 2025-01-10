def wrap(string, max_width):
    string = textwrap.wrap(string, max_width)
    new_string = ""
    for s in string:
        new_string += s+"\n"
    return new_string