if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    if arr[0]>arr[1]:
        m, m2 = arr[0],arr[1]
    elif arr[0]==arr[1]:
        m, m2 = arr[0], float('-inf')
    else:
        m, m2 = arr[1],arr[0]
        
    for i in arr[2:n]:
        if i > m2:
            if i == m:
                continue
            elif i > m:
                m, m2 = i, m
            else:
                m2 = i
                
    print(m2)