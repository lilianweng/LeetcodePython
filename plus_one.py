#!/usr/bin/env python
'''
Leetcode: Plus one
Given a number represented as an array of digits, plus one to the number.
'''
from __future__ import division
import random

def plus_one(digits):
    print digits, '+ 1 =',
    carry = 1
    for i in reversed(xrange(len(digits))):
        x = digits[i]
        carry, x = divmod(x+carry, 10)
        digits[i] = x
    if carry > 0: digits.insert(0,carry)
    print digits
    return digits

if __name__ == '__main__':
    plus_one([1,2,3,4])
    plus_one([1,9,9])
    plus_one([9,9,9])
    plus_one([0])


