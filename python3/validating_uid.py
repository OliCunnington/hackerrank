# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


for i in range(int(input())):
    print("Valid") if re.match(r"^(?=.*[A-Z])(?=.*\d)(?!.*(.).*\1)[a-zA-Z0-9-]{10}$", input()) else print("Invalid")