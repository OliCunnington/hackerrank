# Enter your code here. Read input from STDIN. Print output to STDOUT
func = []
input()
for i in (input().split()):
    func.append(int(i))
for i in func:
    print(func[i-1])
