#!/usr/bin/env python
'''
Leetcode: pow(x,n)
pow(x,n) = x^n
'''
from __future__ import division
import random

# Divide and Conquer
# remember that n can be < 0
# O(logn)
def pow(x, n):
    if n == 0: return 1
    elif n == 1: return x
    elif n > 1:
        half = pow(x, n//2)
        if n % 2 == 0: return half*half
        else: return half*half*x
    else: # n < 0
        return 1/pow(x, -n)


def pow2(x,n):
    if n == 0: return 1
    if n == 1: return x
    m = -n if n < 0 else n
    ret = 1
    while m > 0:
        if m & 1: ret *= x
        # x^n --> (x^2)^(n/2)
        x *= x
        m >>= 1
    return 1/ret if n < 0 else ret

if __name__ == '__main__':
    print pow2(10,2)
    print pow2(10,0)
    print pow2(5,3)
    print pow2(5,-3)
    print pow2(2,10)


