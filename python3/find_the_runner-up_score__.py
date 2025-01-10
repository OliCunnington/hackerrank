if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max = 0
    secnd = 0
    for i in arr:
        if i>max:
            max = i
        elif i>secnd and i<max:
            secnd = i
    print(secnd)