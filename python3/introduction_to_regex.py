# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


for i in range(int(input())):
    val = input()
    # val[0] == - + . [0-9]
    # res = bool(re.search("^[.-+\d]"))
    res = bool(re.match(r"^[.\-+\d]", val))
    # val.count(".") == 1
    # res = res and bool(re.match(r"^(?:[^.]*\.){1}[^.]*$", val))
    #                               ^(?:[^.]*\.){1}[^.]*$
    # res = res and bool(re.match(r"^[^.]*\.(?!\.)[^.]*$", val))
    res = res and val.count(".") == 1
    # index after . is [0-9]
    res = res and bool(re.match(r"^[^.]*\.(?!\.)\d+[^.]*$", val))
    # val[1:] has no + -  
    res = res and bool(re.match(r"^[-+]?[^\+\-]+$", val))
    # val contains no letters
    res = res and bool(re.match(r"^[^a-zA-Z]*$", val))
    
    print(res)