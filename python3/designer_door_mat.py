height, width = map(int, input().split())
design = ".|."
for i in range (1, height, 2):
    print((design*i).center(width, "-"))
print("WELCOME".center(width, "-"))
for i in range (height-2, -1, -2):
    print((design*i).center(width, "-"))