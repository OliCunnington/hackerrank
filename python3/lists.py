if __name__ == '__main__':
    test = []
    myList = []
    N = int(input())
    for _ in range(N):
        command, *values = input().split(" ")
        values = list(map(int, values))
        test.append([command, values])
    for item in test:
        if item[0] == "print":
            print(myList)
            continue
        program = item[0]+"("
        for value in range(len(item[1])):
            program += str(item[1][value])
            if value != len(item[1])-1:
                program += ", "
        program += ")"
        exec("myList."+program)