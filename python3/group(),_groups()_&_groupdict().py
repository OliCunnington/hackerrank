# Enter your code here. Read input from STDIN. Print output to STDOUT

string = input()

for c in string:
    if c.isalpha:
        if c+c in string:
            print(c)
            break
        print(-1)

