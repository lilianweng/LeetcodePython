#!/usr/bin/env python
'''
Bitwise
'''
from __future__ import division
import random


def add(a,b):
    if a == 0 or b == 0:
        return max(a,b)
    sum = a ^ b
    carry = (a & b) << 1
    return add(sum, carry)


def sub(a,b):
    return add(a, ~b+1)


def multiply(a,b):
    import math
    if b == 0: return 0
    elif b == 1: return a
    else:
        if b & 1 == 1:
            # add x + a
            x = multiply((a<<1), (b>>1))
            while a!=0 and x!=0:
                sum = a^b
                carry = (a&b)<<1
                a = sum; x = carry
            return max(a,x)
        else:
            return multiply((a<<1), (b>>1))


def divide(a,b):
    ret = 0
    while a >= b:
        c = b; i = 0
        # double b in each loop
        while a >= c:
            a -= c
            c <<= 1
            ret += (1 << i)
            i += 1
    return ret


if __name__ == '__main__':
    print add(11,4)
    print multiply(12,11)