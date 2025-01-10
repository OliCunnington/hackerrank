n = int(input())

for _ in range (n):
    value = input().split()
    try:
        value = [int(i) for i in value]
        print (value[0]//value[1])
    except (ZeroDivisionError, ValueError) as e:
        print ("Error Code:",e)