# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())): #T
    input() # blocks size
    arr = list(map(int, input().split()))
    ### take the max of arr[0] arr[-1] and pop, pushing it to new arr
    n_arr = []
    n_arr.append(arr.pop(0 if arr[0]>arr[-1] else -1))
    ### keep doing this as long as the popped element is <= than n_arr[-1]
    for i in range(len(arr)):
        if max(arr[0], arr[-1]) <= n_arr[-1]:
            n_arr.append(arr.pop(0 if arr[0]>arr[-1] else -1))
        else:
            break
    print("Yes") if len(arr) == 0 else print("No")
    ### if len(arr[0]) == 0: print yes
    ### if max(arr[0], arr[-1]) > n_arr[-1] : print no