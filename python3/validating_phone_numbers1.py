# Enter your code here. Read input from STDIN. Print output to STDOUT

for x in range(int(input())):
    number = input()
    if len(number) == 10 and number[0] in ("7", "8", "9"):
        try:
            number = int(number)
            print("YES")
        except ValueError:
            print("NO")
    else:
        print("NO")
