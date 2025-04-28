# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

pat = r"(^[4-6][0-9]{15}$)|(^[4-6][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$)"

def test(s):
    if re.match(pat, s):
        clean_num = re.sub("-", "", s)
        for i in range(len(clean_num)-3):
            if len(set(clean_num[i:i+4])) == 1:  
                return False
        return True
    return False

for i in range(int(input())):
    print("Valid") if test(input()) else print("Invalid")