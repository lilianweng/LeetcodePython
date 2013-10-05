#!/usr/bin/env python
'''
Leetcode: Divide Two Integers
Divide two integers without using multiplication, division and mod operator.
'''
from __future__ import division
import random

def divide_two_nums(x, y): # x/y
    if y == 0: return None
    q = 0
    a = long(x); b = long(y)
    if y < 0: b = ~b + 1
    while a > b:
        a -= b
        q += 1
    if y < 0: q = ~q + 1
    return q

##############################################


def bit_add(x, y):
    carry = x & y
    result = x ^ y
    while carry != 0:
        shifted_carry = carry << 1
        # try to add shifted carry and result
        carry = result & shifted_carry
        result = result ^ shifted_carry
    return result

def bit_add2(x, y):
    while True:
        carry = x & y
        result = x ^ y
        x = carry << 1
        y = result
        if carry == 0: break
    return y

def bit_sub(x, y):
    print x, bin(x)
    print ~y+1, bin(~y+1)
    return bit_add2(x, ~y+1)

def bit_multi(x, y):
    result = 0
    for i in range(y):
        result = bit_add(result, x)
    return result

''' Divide two integers using only bitwise operations '''
def bit_divide(x, y):
    pass

if __name__ == '__main__':
    print 234, 11
    print divide_two_nums(234,11)
    print divide_two_nums(234,-11)
    print bit_add(234,11)
    #print bit_sub(234,11)
    print bit_multi(234,11)


