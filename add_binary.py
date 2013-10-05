#!/usr/bin/env python
'''
Leetcode: Add binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''
from __future__ import division
import random

def valid_binary_str(s):
    for bit in list(s):
        if bit != '0' and bit != '1': return False
    return True

# Special cases: negative numbers? not a valid binary string?
def add_binary(a, b):
    if (not valid_binary_str(a)) or (not valid_binary_str(b)): return None
    
    print a,'+',b,'=',
    # make a and b of equal lengths
    l = max(len(a), len(b))
    while len(a) < l: a = '0'+a
    while len(b) < l: b = '0'+b
    
    i = l-1
    results = ""
    prev_carry = 0
    while i >= 0:
        x, y = int(a[i]), int(b[i])
        # add current bits
        z = x ^ y
        cur_carry = x & y
        # add previous carry
        if prev_carry == 1:
            if z == 1: z = 0; cur_carry = 1
            else: z = 1
        
        cur_carry = (z & prev_carry) | cur_carry
        z = z ^ prev_carry
        
        results = str(z) + results
        prev_carry = cur_carry
        i -= 1
    # last carry
    if prev_carry: results = '1'+results
    print results
    return results




if __name__ == '__main__':
    add_binary('11','1')
    add_binary('101011','1111')
    add_binary('101','1111')
    add_binary('0','0')
    add_binary('11','1222')


