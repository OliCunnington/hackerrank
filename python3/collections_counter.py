# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
import os

def get_profit(shoe_sizes, desired_size_and_price):
    # return [shoe_sizes, desired_size_and_price]
    counter = Counter(shoe_sizes)
    profit = 0
    for x, y in desired_size_and_price:
        if counter[x] > 0:
            counter[x] -= 1
            profit += y
    return profit
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    number_of_shoes_input = int(input())

    shoe_sizes_input = [int(x) for x in input().split(" ")] 
    
    desired_size_and_price_input = []
    for c in range(int(input())):
        size_price_str = input().split()
        desired_size_and_price_input.append((int(size_price_str[0]), int(size_price_str[1])))


    result = get_profit(shoe_sizes_input, desired_size_and_price_input)
    
    fptr.write(str(result))
    fptr.write('\n')

    fptr.close()