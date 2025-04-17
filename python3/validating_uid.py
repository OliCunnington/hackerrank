# Enter your code here. Read input from STDIN. Print output to STDOUT
# import re

def unique_and_len(in_string):
    d = {}
    for ch in in_string:
        d[str(ch)] = 0
    return len(d) == 10

def capitals(in_string):
    return sum([1 for x in in_string if x.isupper()]) >= 2

def digits(in_string):
    return sum([1 for x in in_string if x.isnumeric()]) >= 3

def alphanum(in_string):
    return all([x.isalnum for x in in_string])
    
def validate(in_string):
    return unique_and_len(in_string) and capitals(in_string) and digits(in_string) and alphanum(in_string)

for i in range(int(input())):
    print("Valid") if validate(input()) else print("Invalid")
    
    
    # print("Valid") if re.match(r"^(?=.*[A-Z])(?=.*\d)(?!.*(.).*\1)[a-zA-Z0-9-]{10}$", input()) else print("Invalid")