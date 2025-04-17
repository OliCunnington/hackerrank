# Enter your code here. Read input from STDIN. Print output to STDOUT
import re



def check_unique(testcase):
    d = {}
    for c in testcase:
        d[c] = 0
    return len(d) == 10


f = open("output_run.txt", "w")
inp = open("uid_input.txt", "r")
t = open("uid_expected_out.txt")
total = int(inp.readline())
for i in range(total):
    # ^(?=.*[A-Z])(?!.*(\d).*\1)(?!.*([a-zA-Z]).*\2)[a-zA-Z0-9-]{10}$
    # ^(?=.*[A-Z])(?=.*\d)(?!.*(.).*\1)[a-zA-Z0-9-]{10}$
    # ^(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)[A-Za-z\d]{10}$
    testcase = inp.readline()
    match_case = t.readline()
    if re.match(r"^(?=.*[A-Z])(?=.*\d)(?!.*(.).*\1)[a-zA-Z0-9-]{10}$", testcase):
        if match_case != "Valid\n": print("found valid, should be invalid: " + testcase, end="") 
        f.write("Valid\n") 
    else: 
        if match_case != "Invalid\n": print("found invalid, should be valid: " + testcase, end="") 
        f.write("Invalid\n")
f.close()
inp.close()
t.close()


o = open("output_run.txt")
r = open("uid_expected_out.txt")
for i in range(total):
    ol = o.readline()
    rl = r.readline()
    if  ol != rl:
        print("missmatch, o: {}\t\tr: {}\t\t inline: {}\t\toutline: {}".format(ol.strip("\n"), rl.strip("\n"), i+2, i+1))
        # print(in_arr[i])
