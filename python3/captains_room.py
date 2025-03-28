# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
rooms = {}
for i in list(map(int, input().split())):
    if i in rooms.keys():
        rooms[i] += 1
    else:
        rooms[i] = 1

c = [x for x in rooms.keys() if rooms[x] == 1]
print(c[0])