def count_substring(string, sub_string):
    count = 0
    sub = len(sub_string)
    for i in range(len(string)):
        if string[i:i+sub] == sub_string:
            count += 1
    return count