def average(array):
    s = set(array)
    return float('{:,.3f}'.format(sum(s) / len(s)))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)