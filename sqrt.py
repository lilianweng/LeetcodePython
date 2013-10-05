#!/usr/bin/env python
'''
Leetcode: Sqrt(x)
Implement int sqrt(int x).
Compute and return the square root of x.
'''
from __future__ import division
import random

DIFF = 10**-10

# Binary search
def sqrt(x):
    from math import fabs
    if x == 0: return 0
    elif x < 0: return None
    elif x == 1: return 1
    elif x > 1:
        a = 1; b = x
    else: # x < 1
        a = 0; b = 1
    
    while a < b:
        mid = (a+b)/2
        if fabs(mid*mid-x) < DIFF: return mid
        elif x > mid*mid: a = mid
        else: b = mid
    return a


if __name__ == '__main__':
    print sqrt(100)
    print sqrt(5)
    print sqrt(2)
    print sqrt(0.1)
    print sqrt(0.03435435)
    print sqrt(0.0001)


