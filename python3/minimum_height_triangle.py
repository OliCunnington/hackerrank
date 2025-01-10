#!/bin/python3
import math
import sys

def lowestTriangle(base, area):
    # Complete this function
    # base * height/2 = area... (area * 2)/base = height?
    return math.ceil((area*2)/base)

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
