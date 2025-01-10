*Enter your code here. Read input from STDIN. Print output to STDOUT
for x in range(int(STDIN())):
    number = STDIN()
    if 1<len(number)<16 and number[0] in (7, 8, 9):
        print("YES")
    else:
        print("NO")
