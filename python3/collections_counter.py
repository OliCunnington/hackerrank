# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
import os

def get_profit(number_of_shoes, shoe_sizes, number_of_customers, desired_size_and_price):
    return [number_of_shoes, shoe_sizes, number_of_customers, desired_size_and_price]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    number_of_shoes_input = int(input())

    shoe_sizes_input = [int(x) for x in input().split(" ")] 
    
    number_of_customers_input = int(input()) 
    
    desired_size_and_price_input = []
    for c in range(number_of_customers_input):
        size_price_str = input().split()
        desired_size_and_price_input.append((int(size_price_str[0]), int(size_price_str[1])))


    result = get_profit(number_of_shoes_input, shoe_sizes_input, number_of_customers_input, desired_size_and_price_input)
    
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()