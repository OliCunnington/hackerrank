cube = lambda x: x * x * x # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = [0, 1, 1]
    if n <= 3:
        return fib[0:n]
    for i in range (n - 3):
        fib.append(fib[-1] + fib[-2])
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))