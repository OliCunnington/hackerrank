#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import date

minute = 60
hour = minute * 60
day = hour * 24


# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = _split_to_numbers(t1)
    t2 = _split_to_numbers(t2)
    
    t1date = date(int(t1[2]), int(t1[1]), int(t1[0]))
    t2date = date(int(t2[2]), int(t2[1]), int(t2[0]))
    
    date_dif = t1date - t2date
    
    t1time = list(map(int, t1[3].split(":")))
    t2time = list(map(int, t2[3].split(":")))
    
    _t1time = t1time[0] * hour + t1time[1] * minute + t1time[2]
    _t2time = t2time[0] * hour + t2time[1] * minute + t2time[2]
    
    t1tz = _time_zone_to_seconds(t1[4])
    t2tz = _time_zone_to_seconds(t2[4])
    
    _t1time -= int(t1tz)
    _t2time -= int(t2tz)
    
    time_dif = _t1time - _t2time
    
    return str(abs(date_dif.days * day + time_dif))


def _time_zone_to_seconds(t):
    return int(t[0] + str(int(t[1] + t[2]) * hour + int(t[3:]) * minute))


def _split_to_numbers(t):
    ts = t.split()
    match ts[2]:
        case "Jan" | "January":
            ts[2] = 1
        case "Feb" | "Febuary":
            ts[2] = 2
        case "Mar" | "March":
            ts[2] = 3
        case "Apr" | "April":
            ts[2] = 4
        case "May":
            ts[2] = 5
        case "Jun" | "June":
            ts[2] = 6
        case "Jul" | "July":
            ts[2] = 7
        case "Aug" | "August":
            ts[2] = 8
        case "Sep" | "September":
            ts[2] = 9
        case "Oct" | "October":
            ts[2] = 10
        case "Nov" | "November":
            ts[2] = 11
        case "Dec" | "December":
            ts[2] = 12
    
    return ts[1:]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
