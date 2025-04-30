# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for i in range(int(input())):
    line = input()
    line = re.sub(r"(?<= )\|\|(?= )", "or", line)
    line = re.sub(r"(?<= )&&(?= )", "and", line)
    print(line)