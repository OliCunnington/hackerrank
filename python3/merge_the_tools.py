def merge_the_tools(string, k):
    # your code goes here
    temp = []

    i = 0
    while i<len(string):
        temp.append(string[i:i+3:1])
        i += 3


    for t in temp:
        u = ""
        for c in t:
            if c not in u:
                u = u + c
        print(u)

